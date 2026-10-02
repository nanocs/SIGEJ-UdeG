# -*- coding: utf-8 -*-
import csv, re, json, collections

PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EXP,MAT,AUT,TJ,EST,SENT,DEP,ABO,PREST,NOTAS=10,24,1,8,0,12,17,9,2,5
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)

money=re.compile(r"\$\s?([\d]{1,3}(?:[, ]\d{3})*(?:\.\d{1,2})?)")
def maxmonto(r):
    vals=[]
    for c in [PREST,NOTAS,14,15,18,22,25,26,28]:
        if c<len(r):
            for m in money.finditer(r[c]):
                try:vals.append(float(m.group(1).replace(",","").replace(" ","")))
                except:pass
    return max(vals) if vals else 0.0
def yr(v):
    m=re.search(r"/\s*(\d{2,4})",v or "")
    if not m:return None
    y=m.group(1);y=("20"+y if int(y)<50 else "19"+y) if len(y)==2 else y
    return int(y) if y.isdigit() and 1990<=int(y)<=2026 else None
PROV=re.compile(r"suspensi[oó]n provisional",re.I)
CONC=re.compile(r"(se concede|concede la|otorga|se decreta|concedi[oó]|se otorga)",re.I)
NEG=re.compile(r"(niega|neg[oó]|no ha lugar|improceden|no se concede)",re.I)
REINST=re.compile(r"reinstalaci[oó]n|indemnizaci[oó]n|salarios ca[ií]dos",re.I)

import math
def susp_conc(r):
    blob=" ".join(r);m=PROV.search(blob)
    if not m:return None
    w=blob[max(0,m.start()-45):m.end()+45]
    return "negada" if NEG.search(w) else "concedida" if CONC.search(w) else "indeterminada"

enr=[]
for r in U:
    monto=maxmonto(r); y=yr(r[EXP]); est=r[EST].strip(); sent=r[SENT].strip()
    sc=susp_conc(r)
    score=0; drv=[]
    if monto>0:
        c=min(30,15+ (math.log10(monto)-4)*8); c=max(15,c); score+=c; drv.append(f"monto ${monto:,.0f}")
    if est in("Laudo","Sentencia"): score+=20; drv.append(f"etapa {est}")
    elif est=="Amparo": score+=12; drv.append("en amparo")
    if sent=="Desfavorable": score+=25; drv.append("resolución desfavorable")
    if sent=="Ampara y protege": score+=18; drv.append("amparo concedido a la contraparte")
    if REINST.search(r[PREST]): score+=12; drv.append("reinstalación/indemnización")
    if sc=="concedida": score+=15; drv.append("suspensión concedida")
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO": score+=10; drv.append(f"antigüedad {2026-y} años")
    score=min(100,round(score))
    nivel="Crítico" if score>75 else "Alto" if score>=55 else "Medio" if score>=30 else "Bajo"
    enr.append({"exp":r[EXP].strip(),"materia":r[MAT].strip(),"dependencia":r[DEP].strip(),
                "abogado":r[ABO].strip(),"estado":est,"sentido":sent,"monto":monto,"anio":y,
                "susp":sc,"score":score,"nivel":nivel,"drivers":", ".join(drv) or "sin factores"})

activos=[e for e in enr if e["estado"].upper()!="CONCLUIDO"]
# Atención inmediata: activo y (etapa laudo/sent O susp concedida O crítico)
urg=[e for e in activos if e["estado"] in("Laudo","Sentencia") or e["susp"]=="concedida" or e["nivel"]=="Crítico"]
urg.sort(key=lambda x:-x["score"])
altorisk=sorted([e for e in enr if e["nivel"] in("Alto","Crítico")],key=lambda x:-x["score"])

def topn(counter,n=8): return dict(counter.most_common(n))
mat=collections.Counter(e["materia"] or "(s/d)" for e in enr)
dep=collections.Counter(e["dependencia"] for e in enr if e["dependencia"])
abo=collections.Counter(e["abogado"] for e in enr if e["abogado"])
fav=sum(1 for e in enr if e["sentido"]=="Favorable"); desf=sum(1 for e in enr if e["sentido"]=="Desfavorable")
pasivo=sum(e["monto"] for e in enr); con_monto=sum(1 for e in enr if e["monto"]>0)
niveles=collections.Counter(e["nivel"] for e in enr)

ans={
 "q1_activos":{"valor":len(activos),"total":len(enr),"pct":round(100*len(activos)/len(enr),1)},
 "q2_materias":topn(mat),
 "q3_dependencias":topn(dep,10),
 "q4_alto_riesgo":{"conteo":len(altorisk),"niveles":dict(niveles),
    "top":[{k:e[k] for k in("exp","materia","dependencia","nivel","score","drivers")} for e in altorisk[:15]]},
 "q5_pasivo":{"piso_parcial":round(pasivo,2),"exp_con_monto":con_monto,"total":len(enr)},
 "q6_abogados":topn(abo,16),
 "q7_tasa_exito":{"pct":round(100*fav/(fav+desf),1) if fav+desf else None,"fav":fav,"desf":desf},
 "q8_atencion":{"conteo":len(urg),
    "top":[{k:e[k] for k in("exp","materia","dependencia","abogado","estado","nivel","score")} for e in urg[:20]]},
 "meta":{"universo":821,"base":len(enr),"corte":"2026-06-18"}
}
json.dump(ans,open(OUT+"alta_direccion_data.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("activos",len(activos),"| alto+crítico",len(altorisk),"| urgentes",len(urg))
print("niveles",dict(niveles))
print("pasivo piso $%.0f en %d exp"%(pasivo,con_monto))
print("top urgentes:",[(e["exp"],e["nivel"],e["score"]) for e in urg[:6]])
