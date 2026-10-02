# -*- coding: utf-8 -*-
import csv, re, json, collections, math
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EXP,AUT,TJ,EST,SENT,DEP,ABO,PREST,NOTAS=10,1,8,0,12,17,9,2,5
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)
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
PROV=re.compile(r"suspensi[oó]n provisional",re.I)
CONC=re.compile(r"(se concede|concede la|otorga|se decreta|concedi[oó]|se otorga)",re.I)
NEG=re.compile(r"(niega|neg[oó]|no ha lugar|improceden|no se concede)",re.I)
REINST=re.compile(r"reinstalaci[oó]n|indemnizaci[oó]n|salarios ca[ií]dos",re.I)
def nivel(r):
    blob=" ".join(r);mo=maxmonto(r);y=yr(r[EXP]);est=r[EST].strip();sent=r[SENT].strip();s=0
    m=PROV.search(blob);sc=None
    if m:
        w=blob[max(0,m.start()-45):m.end()+45]
        sc="negada" if NEG.search(w) else "concedida" if CONC.search(w) else "indet"
    if mo>0:s+=(50 if mo>500000 else 42 if mo>200000 else 32 if mo>100000 else 22 if mo>50000 else 12 if mo>10000 else 6)
    if est in("Laudo","Sentencia"):s+=20
    elif est=="Amparo":s+=12
    if sent=="Desfavorable":s+=25
    if sent=="Ampara y protege":s+=18
    if REINST.search(r[PREST]):s+=12
    if sc=="concedida":s+=15
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO":s+=10
    s=min(100,round(s));return ("Crítico" if s>75 else "Alto" if s>=55 else "Medio" if s>=30 else "Bajo"),s,mo
EXITO={"Favorable","Sobresee","Desechó","Niega","Caducidad","Desistimiento","Infundada"}
ADV={"Desfavorable","Ampara y protege","Fundado"}
ag={}
for r in U:
    a=r[ABO].strip()
    if not a:continue
    niv,sc,mo=nivel(r);act=r[EST].strip().upper()!="CONCLUIDO";s=r[SENT].strip()
    d=ag.setdefault(a,{"abogado":a,"total":0,"vigentes":0,"critico":0,"alto":0,"medio":0,"bajo":0,
                       "score_sum":0,"pasivo":0.0,"exito":0,"adv":0})
    d["total"]+=1
    if act:d["vigentes"]+=1
    d[niv.lower().replace("í","i")]+=1
    d["score_sum"]+=sc; d["pasivo"]+=mo
    if s in EXITO:d["exito"]+=1
    elif s in ADV:d["adv"]+=1
out=[]
for a,d in ag.items():
    d["alto_riesgo"]=d["critico"]+d["alto"]
    d["dens_riesgo"]=round(100*d["alto_riesgo"]/d["vigentes"],1) if d["vigentes"] else 0
    d["score_prom"]=round(d["score_sum"]/d["total"],1) if d["total"] else 0
    ba=d["exito"]+d["adv"]; d["tasa_ampliada"]=round(100*d["exito"]/ba,1) if ba else None
    d["base"]=ba; d["pasivo"]=round(d["pasivo"],0)
    out.append(d)
out.sort(key=lambda x:-x["vigentes"])
# Gini de la carga
def gini(v):
    v=sorted(v);n=len(v);c=sum((i+1)*x for i,x in enumerate(v));s=sum(v)
    return round((2*c)/(n*s)-(n+1)/n,3) if s else 0
gv=gini([d["vigentes"] for d in out]); gr=gini([d["alto_riesgo"] for d in out])
# correlación carga vs alto_riesgo
import statistics as st
xs=[d["vigentes"] for d in out]; ys=[d["alto_riesgo"] for d in out]
mx=st.mean(xs);my=st.mean(ys)
cov=sum((x-mx)*(y-my) for x,y in zip(xs,ys));dx=math.sqrt(sum((x-mx)**2 for x in xs));dy=math.sqrt(sum((y-my)**2 for y in ys))
corr=round(cov/(dx*dy),2) if dx*dy else 0
json.dump({"abogados":out,"gini_carga":gv,"gini_riesgo":gr,"corr_carga_riesgo":corr,
           "total_alto":sum(d["alto_riesgo"] for d in out)},
          open(OUT+"equidad_data.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(f"{'Abogado':34}{'Vig':>4}{'AltoR':>6}{'Crit':>5}{'Dens%':>6}{'ScPr':>5}{'TasaA':>6}{'Pasivo':>12}")
for d in out:
    print(f"{d['abogado'][:34]:34}{d['vigentes']:>4}{d['alto_riesgo']:>6}{d['critico']:>5}{d['dens_riesgo']:>6}{d['score_prom']:>5}{(str(d['tasa_ampliada']) if d['tasa_ampliada'] is not None else 's/d'):>6}{('$'+format(int(d['pasivo']),',')):>12}")
print(f"\nGini carga={gv} | Gini alto-riesgo={gr} | Correlación carga↔riesgo={corr}")
print("(Gini 0=equitativo, 1=concentrado; corr>0.7 = los de más carga llevan más riesgo)")
