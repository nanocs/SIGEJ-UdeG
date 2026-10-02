# -*- coding: utf-8 -*-
import csv, re, json, collections

PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
mis=[r for r in rows if len(r)!=25]
EXP,MAT,AUT,TJ,EST,SENT,DEP,ABO,SIS,PREST,NOTAS=10,24,1,8,0,12,17,9,23,2,5

seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)

def yr(v):
    m=re.search(r"/\s*(\d{2,4})",v or "")
    if not m:return None
    y=m.group(1);y=("20"+y if int(y)<50 else "19"+y) if len(y)==2 else y
    return int(y) if y.isdigit() and 1990<=int(y)<=2026 else None

def cnt(col,base=None):
    base=base or U
    return dict(collections.Counter((r[col].strip() or "(s/d)") for r in base).most_common())

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
        elif base=="Civil":rama="Civil (n/e)"
        else:rama="No identificada"
    return rama
materia_fina_dist=dict(collections.Counter(materia_fina(r) for r in U).most_common())

# Normalizar autoridad (typo Concilición) y agrupar por tipo de órgano
def tipo_organo(a):
    a=a.lower()
    if "junta" in a and "federal" in a:return "Junta Federal C. y A."
    if "junta" in a:return "Junta Local C. y A."
    if "tribunal colegiado" in a:return "Tribunal Colegiado"
    if "juzgado" in a and "distrito" in a:return "Juzgado de Distrito"
    if "tribunal laboral" in a or "materia laboral" in a:return "Tribunal/Juzgado Laboral"
    if "sala" in a and ("administrativ" in a or "justicia administrativa" in a):return "Sala Admva."
    if "agrario" in a:return "Tribunal Agrario"
    return "Otro"
organo=collections.Counter(tipo_organo(r[AUT]) for r in U if r[AUT].strip())

# Montos -> pasivo contingente (aprox)
money=re.compile(r"\$\s?([\d]{1,3}(?:[, ]\d{3})*(?:\.\d{1,2})?)")
def montos(r):
    tot=0.0
    for c in [PREST,NOTAS,14,15,18,22,25,26,28]:
        if c<len(r):
            for m in money.finditer(r[c]):
                try:tot+=float(m.group(1).replace(",","").replace(" ",""))
                except:pass
    return tot
mont=[montos(r) for r in U]
con_monto=sum(1 for x in mont if x>0)
pasivo=sum(mont)

# Año
anio=collections.Counter()
for r in U:
    y=yr(r[EXP]);  anio[y if y else "s/d"]+=1
anio_ord={str(k):anio[k] for k in sorted([x for x in anio if x!="s/d"])}
anio_ord["s/d"]=anio.get("s/d",0)

# Litigios
estado=cnt(EST); sentido=cnt(SENT)
activos=sum(1 for r in U if r[EST].strip().upper()!="CONCLUIDO")
concluidos=len(U)-activos
laudo=estado.get("Laudo",0); sent_etapa=estado.get("Sentencia",0)
con_res=sum(1 for r in U if r[SENT].strip())
favorable=sentido.get("Favorable",0); desfavorable=sentido.get("Desfavorable",0)
ampara=sentido.get("Ampara y protege",0); sobresee=sentido.get("Sobresee",0)
conc=sum(1 for r in U if r[EST].strip().lower()=="convenio" or r[SENT].strip().lower()=="por convenio")

# Suspensión provisional concedida (reusar lógica fase2)
PROV=re.compile(r"suspensi[oó]n provisional",re.I)
NEG=re.compile(r"(niega|neg[oó]|no ha lugar|improceden|no se concede)",re.I)
CONC=re.compile(r"(se concede|concede la|otorga|se decreta|concedi[oó]|se otorga)",re.I)
sp=collections.Counter()
for r in U:
    blob=" ".join(r)
    m=PROV.search(blob)
    if m:
        w=blob[max(0,m.start()-45):m.end()+45]
        sp["negada" if NEG.search(w) else "concedida" if CONC.search(w) else "indeterminada"]+=1

# Productividad por abogado
abogado=dict(collections.Counter(r[ABO].strip() for r in U if r[ABO].strip()).most_common())

# Desempeño por abogado: carga + tasa estricta + tasa ampliada
EXITO={"Favorable","Sobresee","Desechó","Niega","Caducidad","Desistimiento","Infundada"}
ADV={"Desfavorable","Ampara y protege","Fundado"}
desemp={}
for r in U:
    a=r[ABO].strip()
    if not a:continue
    s=r[SENT].strip()
    d=desemp.setdefault(a,{"abogado":a,"total":0,"vigentes":0,"fav":0,"desf":0,"exito":0,"adv":0})
    d["total"]+=1
    if r[EST].strip().upper()!="CONCLUIDO":d["vigentes"]+=1
    if s=="Favorable":d["fav"]+=1
    elif s=="Desfavorable":d["desf"]+=1
    if s in EXITO:d["exito"]+=1
    elif s in ADV:d["adv"]+=1
desempeno=[]
for a,d in desemp.items():
    be=d["fav"]+d["desf"]; ba=d["exito"]+d["adv"]
    d["tasa_estricta"]=round(100*d["fav"]/be,1) if be else None
    d["tasa_ampliada"]=round(100*d["exito"]/ba,1) if ba else None
    d["base_estricta"]=be; d["base_ampliada"]=ba
    desempeno.append(d)
desempeno.sort(key=lambda x:-x["vigentes"])
# Dependencia (col17) top
dep=dict(collections.Counter(r[DEP].strip() for r in U if r[DEP].strip()).most_common(15))
# Heatmap dependencia(top8) x materia
topdep=list(dep)[:8]
heat=[]
for d in topdep:
    row={"dependencia":d}
    for m in ["Laboral","Civil","Penal"]:
        row[m]=sum(1 for r in U if r[DEP].strip()==d and r[MAT].strip()==m)
    heat.append(row)

data={
 "meta":{"universo":len(U)+72,"base_estructurada":len(U),"recuperados":72,
         "corruptas":len(mis),"fuente":"juicios.tab","fecha_corte":"2026-06-18"},
 "kpis":{"activos":activos,"concluidos":concluidos,"total":len(U),
         "pct_activos":round(100*activos/len(U),1),
         "tasa_exito":round(100*favorable/(favorable+desfavorable),1) if favorable+desfavorable else None,
         "pasivo_contingente":round(pasivo,2),"exp_con_monto":con_monto,
         "susp_concedidas":sp.get("concedida",0),"conciliaciones":conc,
         "abogados":len(abogado)},
 "materia":cnt(MAT),"materia_fina":materia_fina_dist,"tipo_juicio":cnt(TJ),"estado":estado,"sentido":sentido,
 "anio":anio_ord,"organo":dict(organo.most_common()),"abogado":abogado,
 "dependencia":dep,"heatmap":heat,"desempeno":desempeno,
 "litigios":{"laudo":laudo,"sentencia_etapa":sent_etapa,"con_resolucion":con_res,
             "favorable":favorable,"desfavorable":desfavorable,"ampara":ampara,
             "sobresee":sobresee,"susp":dict(sp),"conciliacion":conc},
}
with open(OUT+"dashboard_data.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=1)
print("dashboard_data.json OK")
print("Universo:",data["meta"]["universo"],"| activos:",activos,"| pasivo aprox: ${:,.2f}".format(pasivo),"en",con_monto,"exp")
print("tasa_exito:",data["kpis"]["tasa_exito"],"% | susp concedidas:",sp.get("concedida",0),"| concil:",conc)
print("abogados:",len(abogado),"| top dep:",list(dep)[:5])
