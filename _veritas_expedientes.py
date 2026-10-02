# -*- coding: utf-8 -*-
import csv, re, json, collections, math, datetime
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
CORTE=datetime.date(2026,6,18)
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EST,AUT,PREST,ACTOR,DEMA,NOTAS,HIST,GEST,TJ,ABO,EXP,FPRES,SENT,DEP,SIS,MAT=0,1,2,3,4,5,6,7,8,9,10,11,12,17,23,24
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)
try: NLP=json.load(open(OUT+"nlp_expedientes.json",encoding="utf-8"))
except Exception: NLP={}
try: PREDM={p["num"]:p["p_exito"] for p in json.load(open(OUT+"modelo_data.json",encoding="utf-8"))["pred_activos"]}
except Exception: PREDM={}
MES={'ene':1,'feb':2,'mar':3,'abr':4,'may':5,'jun':6,'jul':7,'ago':8,'sep':9,'oct':10,'nov':11,'dic':12}
dre=re.compile(r'(\d{1,2})[/\- ]([A-Za-zÁ-úñ]{3,4}|\d{1,2})[/\- ](\d{2,4})')
def parse(t):
    d,mo,y=t.groups();mm=MES.get(mo[:3].lower(), int(mo) if mo.isdigit() else 0)
    if not(1<=mm<=12):return None
    y=int(('20'+y if int(y)<50 else '19'+y) if len(y)==2 else y)
    try:return datetime.date(y,mm,int(d))
    except:return None
money=re.compile(r"\$\s?([\d]{1,3}(?:[, ]\d{3})*(?:\.\d{1,2})?)")
def maxmonto(r):
    v=[]
    for c in [PREST,NOTAS,14,15,18,22,25,26,28]:
        if c<len(r):
            for m in money.finditer(r[c]):
                try:v.append(float(m.group(1).replace(",","").replace(" ","")))
                except:pass
    return max(v) if v else 0.0
def yr(v):
    m=re.search(r"/\s*(\d{2,4})",v or "")
    if not m:return None
    y=m.group(1);y=("20"+y if int(y)<50 else "19"+y) if len(y)==2 else y
    return int(y) if y.isdigit() and 1990<=int(y)<=2026 else None
PROV=re.compile(r"suspensi[oó]n provisional",re.I);CONC=re.compile(r"(se concede|otorga|se decreta|concedi[oó])",re.I)
NEG=re.compile(r"(niega|neg[oó]|no ha lugar|improceden)",re.I);REINST=re.compile(r"reinstalaci[oó]n|indemnizaci[oó]n|salarios ca[ií]dos",re.I)
EXITO={"Favorable","Sobresee","Desechó","Niega","Caducidad","Desistimiento","Infundada"};ADV={"Desfavorable","Ampara y protege","Fundado"}
def materia_fina(r):
    a=r[AUT].lower(); tj=r[TJ].strip(); base=r[MAT].strip()
    if re.search(r"junta .*conciliaci|tribunal laboral|materia de trabajo|materia laboral|de trabajo|arbitraje del estado",a):rama="Laboral"
    elif re.search(r"agrario|agraria",a) or tj=="Agrario":rama="Agraria"
    elif re.search(r"administrativ|justicia administrativa|fiscal",a) or tj=="Administrativo":rama="Administrativa"
    elif re.search(r"materia penal|\bpenal\b",a):rama="Penal"
    elif re.search(r"materia civil|familiar|juzgado .*civil",a) or tj=="Civil":rama="Civil"
    elif re.search(r"mercantil",a) or tj=="Mercantil":rama="Mercantil"
    else:rama=None
    if rama is None:
        if tj=="Mercantil":rama="Mercantil"
        elif tj=="Agrario":rama="Agraria"
        elif tj=="Administrativo":rama="Administrativa"
        elif tj=="Civil":rama="Civil"
        elif base=="Laboral":rama="Laboral"
        elif base=="Penal":rama="Penal"
        elif base=="Civil":rama="Civil (no especificada)"
        else:rama="No identificada"
    return rama
def via(r):
    tj=r[TJ].strip()
    if tj in("Amparo Directo","Amparo Indirecto"):return tj
    if tj in("Recurso de Revisión","Queja","Recurso de Reclamación","Incidente de Inejecución"):return "Recurso/Incidente (amparo)"
    return "Jurisdicción ordinaria"
def centro(dep):
    d=dep.upper()
    if d.startswith("CUC") or d.startswith("CUA") or d in("CUCEA","CUCS","CUCSH","CUCEI","CUCBA","CUAAD"):return "Centro Universitario Temático"
    if d.startswith("CU"):return "Centro Universitario Regional"
    if "PREPARATORIA" in d or "POLITÉCNICA" in d or "VOCACIONAL" in d or d=="SEMS":return "SEMS (Educación Media Superior)"
    if "RECTOR" in d:return "Rectoría / Administración General"
    if "COORDINACI" in d or "OPERADORA" in d or "DIRECCIÓN" in d or "SISTEMA" in d or "SECRETAR" in d:return "Dependencia Administrativa / Red"
    return "Otra dependencia"
def actuaciones(r):
    txt=(r[HIST] or "").replace("\r"," ").replace("\n"," ")
    return txt[:600]+("…" if len(txt)>600 else "")
recs=[];susp_c=0
for i,r in enumerate(U):
    mo=maxmonto(r);y=yr(r[EXP]);est=r[EST].strip();sent=r[SENT].strip();blob=" ".join(r);s=0;dv=[]
    sc=None;m=PROV.search(blob)
    if m:
        w=blob[max(0,m.start()-45):m.end()+45];sc="negada" if NEG.search(w) else "concedida" if CONC.search(w) else "indet"
        if sc=="concedida":susp_c+=1
    if mo>0:s+=(50 if mo>500000 else 42 if mo>200000 else 32 if mo>100000 else 22 if mo>50000 else 12 if mo>10000 else 6);dv.append("monto")
    if est in("Laudo","Sentencia"):s+=20;dv.append("etapa "+est)
    elif est=="Amparo":s+=12;dv.append("amparo")
    if sent=="Desfavorable":s+=25;dv.append("desfavorable")
    if sent=="Ampara y protege":s+=18;dv.append("amparo a contraparte")
    if REINST.search(r[PREST]):s+=12;dv.append("reinstalación")
    if sc=="concedida":s+=15;dv.append("susp. concedida")
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO":s+=10;dv.append("antigüedad")
    s=min(100,round(s));niv="Crítico" if s>75 else "Alto" if s>=55 else "Medio" if s>=30 else "Bajo"
    fs=[parse(mm) for mm in dre.finditer(blob)];fs=[d for d in fs if d];ult=max(fs) if fs else None
    activo=est.upper()!="CONCLUIDO"
    prob=("Resuelto a favor" if sent in EXITO else "Resuelto en contra" if sent in ADV else ("Baja" if s>=55 else "Media" if s>=30 else "Alta")+" (proxy)")
    pri="Urgente" if (activo and (est in("Laudo","Sentencia") or sc=="concedida" or niv=="Crítico")) else "Alta" if niv=="Alto" else "Normal"
    nl=NLP.get(r[EXP].strip(),{})
    recs.append({"id":f"EXP-{i+1:04d}","num":r[EXP].strip() or "(s/n)","materia":r[MAT].strip() or "(s/d)",
      "materia_fina":materia_fina(r),"via":via(r),"tipo_juicio":r[TJ].strip(),
      "nlp_tipo_res":nl.get("tipo_resolucion"),"nlp_fecha_res":nl.get("fecha_resolucion"),
      "nlp_eventos":nl.get("n_eventos",0),"nlp_monto_texto":nl.get("monto_max",0),"nlp_monto_anomalo":nl.get("monto_anomalo",0),
      "pred_exito":PREDM.get(r[EXP].strip()),
      "dependencia":r[DEP].strip() or "(s/d)","centro":centro(r[DEP]),"actor":r[ACTOR].strip(),"demandado":r[DEMA].strip(),
      "autoridad":r[AUT].strip(),"responsable":r[ABO].strip() or "(sin asignar)","estado":est,"nivel_riesgo":niv,"score":s,
      "prob_exito":prob,"monto":round(mo),"pasivo":round(mo) if activo else 0,"anio":y,
      "fecha_inicio":(r[FPRES].strip() or (str(y) if y else "")),"fecha_cierre":("" if activo else (ult.isoformat() if ult else "")),
      "ult_mov":ult.isoformat() if ult else "","semaforo":niv,"prioridad":pri,"sentido":sent,"sistema":r[SIS].strip(),
      "observaciones":(r[PREST] or "").replace("\r"," ").replace("\n"," ")[:220],"actuaciones":actuaciones(r),"activo":activo})
def cat(key):return sorted({x[key] for x in recs if x[key] and x[key]!="(s/d)"})
catalogos={"materia":cat("materia"),"materia_fina":cat("materia_fina"),"via":cat("via"),"estado":cat("estado"),"tipo_juicio":cat("tipo_juicio"),
  "nivel_riesgo":["Crítico","Alto","Medio","Bajo"],"anio":sorted({str(x["anio"]) for x in recs if x["anio"]}),
  "responsable":cat("responsable"),"centro":cat("centro"),
  "dependencia":[d for d,_ in collections.Counter(x["dependencia"] for x in recs).most_common(40)]}
kpi={"activos":sum(1 for x in recs if x["activo"]),"concluidos":sum(1 for x in recs if not x["activo"]),
  "total":len(recs),"con_sentencia":sum(1 for x in recs if x["estado"] in("Laudo","Sentencia") or x["sentido"]),
  "susp":susp_c,"alto_riesgo":sum(1 for x in recs if x["nivel_riesgo"] in("Alto","Crítico")),
  "urgentes":sum(1 for x in recs if x["prioridad"]=="Urgente"),"pasivo":round(sum(x["pasivo"] for x in recs)),
  "responsables":len(set(x["responsable"] for x in recs))}
json.dump({"corte":CORTE.isoformat(),"expedientes":recs,"catalogos":catalogos,"kpi":kpi},
          open(OUT+"expedientes_data.json","w",encoding="utf-8"),ensure_ascii=False)
print("expedientes:",len(recs),"| activos:",kpi["activos"],"| alto riesgo:",kpi["alto_riesgo"],"| urgentes:",kpi["urgentes"])
print("catálogos -> materias:",len(catalogos["materia"]),"resp:",len(catalogos["responsable"]),"dep:",len(catalogos["dependencia"]),"centros:",catalogos["centro"])
import os;print("tamaño JSON: %.0f KB"%(os.path.getsize(OUT+"expedientes_data.json")/1024))
