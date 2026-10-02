# -*- coding: utf-8 -*-
import csv, re, collections, math
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EST,AUT,PREST,SENT,TJ,EXP,MAT,DEP=0,1,2,12,8,10,24,17
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)
money=re.compile(r"\$\s?([\d]{1,3}(?:[, ]\d{3})*(?:\.\d{1,2})?)")
def maxmonto(r):
    v=[]
    for c in [PREST,5,14,15,18,22,25,26,28]:
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
def nivel(s):return "Crítico" if s>75 else "Alto" if s>=55 else "Medio" if s>=30 else "Bajo"

def score_old(r):
    mo=maxmonto(r);y=yr(r[EXP]);est=r[EST].strip();sent=r[SENT].strip();blob=" ".join(r);s=0;sc=None
    m=PROV.search(blob)
    if m:
        w=blob[max(0,m.start()-45):m.end()+45];sc="concedida" if CONC.search(w) and not NEG.search(w) else None
    if mo>0:s+=max(15,min(30,15+(math.log10(mo)-4)*8))
    if est in("Laudo","Sentencia"):s+=20
    elif est=="Amparo":s+=12
    if sent=="Desfavorable":s+=25
    if sent=="Ampara y protege":s+=18
    if REINST.search(r[PREST]):s+=12
    if sc=="concedida":s+=15
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO":s+=10
    return min(100,round(s))

def monto_comp(mo):           # IMPACTO ECONÓMICO (peso reforzado, hasta 50)
    if mo>500000:return 50
    if mo>200000:return 42
    if mo>100000:return 32
    if mo>50000:return 22
    if mo>10000:return 12
    if mo>0:return 6
    return 0                  # $0 = monto NO capturado: el caso se sostiene por sus factores procesales
def score_new(r):
    mo=maxmonto(r);y=yr(r[EXP]);est=r[EST].strip();sent=r[SENT].strip();blob=" ".join(r);s=0;sc=None
    m=PROV.search(blob)
    if m:
        w=blob[max(0,m.start()-45):m.end()+45];sc="concedida" if CONC.search(w) and not NEG.search(w) else None
    s+=monto_comp(mo)                          # impacto
    # PROBABILIDAD DE MATERIALIZACIÓN (factores procesales, conservados)
    if est in("Laudo","Sentencia"):s+=20
    elif est=="Amparo":s+=12
    if sent=="Desfavorable":s+=25
    if sent=="Ampara y protege":s+=18
    if REINST.search(r[PREST]):s+=12
    if sc=="concedida":s+=15
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO":s+=10
    return min(100,round(s))

res=[]
for r in U:
    so=score_old(r);sn=score_new(r)
    res.append({"num":r[EXP].strip(),"mat":r[MAT].strip(),"dep":r[DEP].strip(),"mo":round(maxmonto(r)),
                "est":r[EST].strip(),"old":so,"no":nivel(so),"new":sn,"nn":nivel(sn)})
do=collections.Counter(x["no"] for x in res);dn=collections.Counter(x["nn"] for x in res)
print("DISTRIBUCIÓN  | viejo -> nuevo")
for niv in ["Crítico","Alto","Medio","Bajo"]:
    print(f"  {niv:8}: {do[niv]:4d} -> {dn[niv]:4d}")
altoO=sum(do[k] for k in("Alto","Crítico"));altoN=sum(dn[k] for k in("Alto","Crítico"))
print(f"  ALTO+CRÍTICO: {altoO} -> {altoN}")
print("\nNUEVO TOP-15 ALTO RIESGO (ordenado por score nuevo):")
res.sort(key=lambda x:-x["new"])
print("{:11}{:14}{:>11}{:11}{:>5}{:>5}  Nivel".format('Exped','Mat','Monto','Estado','old','new'))
for x in res[:15]:
    print("{:11}{:14}{:>11}{:11}{:>5}{:>5}  {}".format(x['num'],x['mat'][:14],'$'+format(x['mo'],','),x['est'][:11],x['old'],x['new'],x['nn']))
print("\nMOVIMIENTOS CLAVE (subieron de nivel):")
order=["Bajo","Medio","Alto","Crítico"]
ups=[x for x in res if order.index(x['nn'])>order.index(x['no'])]
ups.sort(key=lambda x:-x['mo'])
for x in ups[:12]:
    print("  {:11} {:12} ${:>10,}  {} -> {}  ({})".format(x['num'],x['mat'][:12],x['mo'],x['no'],x['nn'],x['dep'][:22]))
print("\nTotal que SUBIERON de nivel:",len(ups),"| 137/2022 ->",[x for x in res if x['num']=='137/2022'][0])
