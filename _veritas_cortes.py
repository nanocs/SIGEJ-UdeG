# -*- coding: utf-8 -*-
import csv, re, json, collections, math
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
def act(r): return r[EST].strip().upper()!="CONCLUIDO"

# ---------- 1) ASUNTOS POR ABOGADO (vigentes) ----------
tot=collections.Counter(r[ABO].strip() or "(sin asignar)" for r in U)
act_c=collections.Counter(r[ABO].strip() or "(sin asignar)" for r in U if act(r))
print("="*64);print("1) ASUNTOS POR ABOGADO — VIGENTES (activos)");print("="*64)
print(f"{'#':>2}  {'Abogado':38} {'Vigentes':>9} {'Total':>6} {'Concl.':>6}")
with open(OUT+"ABOGADOS_vigentes.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f);w.writerow(["abogado","vigentes","total","concluidos"])
    for i,(a,t) in enumerate(tot.most_common(),1):
        v=act_c.get(a,0)
        print(f"{i:>2}  {a:38} {v:>9} {t:>6} {t-v:>6}")
        w.writerow([a,v,t,t-v])
print(f"\nTOTAL vigentes: {sum(act_c.values())} | TOTAL asignados: {sum(tot.values())}")

# ---------- 2) ALTO RIESGO (proxy) con expediente ----------
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
def susp(r):
    blob=" ".join(r);m=PROV.search(blob)
    if not m:return None
    w=blob[max(0,m.start()-45):m.end()+45]
    return "negada" if NEG.search(w) else "concedida" if CONC.search(w) else "indet"
risk=[]
for r in U:
    mo=maxmonto(r);y=yr(r[EXP]);est=r[EST].strip();sent=r[SENT].strip();sc=susp(r);s=0;dv=[]
    if mo>0:c=max(15,min(30,15+(math.log10(mo)-4)*8));s+=c;dv.append(f"monto ${mo:,.0f}")
    if est in("Laudo","Sentencia"):s+=20;dv.append(f"etapa {est}")
    elif est=="Amparo":s+=12;dv.append("amparo")
    if sent=="Desfavorable":s+=25;dv.append("desfavorable")
    if sent=="Ampara y protege":s+=18;dv.append("amparo a contraparte")
    if REINST.search(r[PREST]):s+=12;dv.append("reinstalación/indemniz.")
    if sc=="concedida":s+=15;dv.append("susp. concedida")
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO":s+=10;dv.append(f"{2026-y}a antig.")
    s=min(100,round(s));niv="Crítico" if s>75 else "Alto" if s>=55 else "Medio" if s>=30 else "Bajo"
    if niv in("Alto","Crítico"):
        risk.append({"exp":r[EXP].strip(),"nivel":niv,"score":s,"materia":r[MAT].strip(),
                     "dependencia":r[DEP].strip(),"abogado":r[ABO].strip(),"estado":est,
                     "vigente":"Sí" if act(r) else "No","factores":", ".join(dv)})
risk.sort(key=lambda x:-x["score"])
print("\n"+"="*64);print(f"2) ASUNTOS DE ALTO RIESGO (proxy) — {len(risk)} casos");print("="*64)
print(f"{'Expediente':12} {'Niv':8} {'Sc':>3} {'Vig':3} {'Materia':8} {'Dependencia':22} Factores")
with open(OUT+"ALTO_RIESGO.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["exp","nivel","score","vigente","materia","dependencia","abogado","estado","factores"]);w.writeheader()
    for e in risk:
        print(f"{e['exp']:12} {e['nivel']:8} {e['score']:>3} {e['vigente']:3} {e['materia']:8} {e['dependencia'][:22]:22} {e['factores'][:48]}")
        w.writerow(e)

# ---------- 3) DEPENDENCIAS (todas) ----------
dep=collections.Counter(r[DEP].strip() for r in U if r[DEP].strip())
depA=collections.Counter(r[DEP].strip() for r in U if r[DEP].strip() and act(r))
print("\n"+"="*64);print(f"3) DEPENDENCIAS QUE GENERAN MÁS CONFLICTOS — {len(dep)} dependencias");print("="*64)
print(f"{'#':>3}  {'Dependencia':46} {'Total':>6} {'Vigentes':>9}")
with open(OUT+"DEPENDENCIAS.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f);w.writerow(["dependencia","total","vigentes"])
    for i,(dnm,n) in enumerate(dep.most_common(),1):
        w.writerow([dnm,n,depA.get(dnm,0)])
        if n>=2: print(f"{i:>3}  {dnm[:46]:46} {n:>6} {depA.get(dnm,0):>9}")
    sing=sum(1 for _,n in dep.items() if n==1)
    print(f"\n(+{sing} dependencias con 1 solo expediente — ver DEPENDENCIAS.csv)")
print("sin dependencia registrada:",sum(1 for r in U if not r[DEP].strip()))
