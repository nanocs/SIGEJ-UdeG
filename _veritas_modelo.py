# -*- coding: utf-8 -*-
import csv, re, json, collections, math, random
random.seed(42)
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
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
try: NLP=json.load(open(OUT+"nlp_expedientes.json",encoding="utf-8"))
except Exception: NLP={}
EXITO={"Favorable","Sobresee","Desechó","Niega","Caducidad","Desistimiento","Infundada"}
ADV={"Desfavorable","Ampara y protege","Fundado"}
def organo(a):
    a=a.lower()
    if "junta" in a:return "Junta C.A."
    if "tribunal colegiado" in a:return "T.Colegiado"
    if "juzgado" in a and "distrito" in a:return "Jdo.Distrito"
    if "materia laboral" in a or "tribunal laboral" in a:return "Trib.Laboral"
    if "sala" in a:return "Sala"
    return "Otro"
def materia_fina(r):
    a=r[AUT].lower();tj=r[TJ].strip();base=r[MAT].strip()
    if re.search(r"junta .*conciliaci|tribunal laboral|materia de trabajo|de trabajo",a):return "Laboral"
    if re.search(r"agrario",a) or tj=="Agrario":return "Agraria"
    if re.search(r"administrativ|justicia administrativa",a) or tj=="Administrativo":return "Administrativa"
    if re.search(r"mercantil",a) or tj=="Mercantil":return "Mercantil"
    if base=="Laboral":return "Laboral"
    return "Civil/Otra"
def via(r):
    tj=r[TJ].strip()
    return "Amparo" if "Amparo" in tj else "Recurso" if tj in("Recurso de Revisión","Queja") else "Ordinario"
REINST=re.compile(r"reinstalaci[oó]n|indemnizaci[oó]n|salarios ca[ií]dos",re.I)
def montob(r):
    nl=NLP.get(r[EXP].strip(),{});mo=nl.get("monto_max",0)
    return ">200k" if mo>200000 else "50-200k" if mo>50000 else "<50k" if mo>0 else "s/d"
def feats(r):
    return {"materia":materia_fina(r),"organo":organo(r[AUT]),"via":via(r),
            "reinst":"sí" if REINST.search(r[PREST]) else "no","monto":montob(r),"tipo":r[TJ].strip()}
# Dataset etiquetado (resueltos)
DS=[]
for r in U:
    s=r[SENT].strip()
    if s in EXITO:DS.append((feats(r),"Éxito",r[EXP].strip()))
    elif s in ADV:DS.append((feats(r),"Adverso",r[EXP].strip()))
print(f"Casos etiquetados: {len(DS)} (Éxito {sum(1 for x in DS if x[1]=='Éxito')}, Adverso {sum(1 for x in DS if x[1]=='Adverso')})")
FEATS=["materia","organo","via","reinst","monto","tipo"]
def train(tr):
    pri=collections.Counter(c for _,c,_ in tr)
    cnt={f:{c:collections.Counter() for c in pri} for f in FEATS}
    for x,c,_ in tr:
        for f in FEATS:cnt[f][c][x[f]]+=1
    vocab={f:set(x[f] for x,_,_ in tr) for f in FEATS}
    return pri,cnt,vocab,len(tr)
def predict(m,x):
    pri,cnt,vocab,N=m;sc={}
    for c in pri:
        lp=math.log(pri[c]/N)
        for f in FEATS:
            tot=sum(cnt[f][c].values());V=len(vocab[f])
            lp+=math.log((cnt[f][c].get(x[f],0)+1)/(tot+V))
        sc[c]=lp
    mx=max(sc.values());ex={c:math.exp(sc[c]-mx) for c in sc};Z=sum(ex.values())
    return {c:ex[c]/Z for c in ex}
# Validación cruzada 5-fold
random.shuffle(DS)
K=5;folds=[DS[i::K] for i in range(K)]
acc=[];cm=collections.Counter()
for i in range(K):
    te=folds[i];tr=[x for j in range(K) if j!=i for x in folds[j]]
    m=train(tr);ok=0
    for x,c,_ in te:
        p=predict(m,x);pred=max(p,key=p.get)
        if pred==c:ok+=1
        cm[(c,pred)]+=1
    acc.append(ok/len(te))
base=max(collections.Counter(c for _,c,_ in DS).values())/len(DS)
print(f"\nAccuracy CV 5-fold: {sum(acc)/K:.1%} (baseline mayoría: {base:.1%})")
print("Matriz de confusión (real→pred):")
for real in ["Éxito","Adverso"]:
    print(f"   {real:8} -> Éxito {cm[(real,'Éxito')]:>3} | Adverso {cm[(real,'Adverso')]:>3}")
# Modelo final con todo + factores explicativos
M=train(DS)
print("\nFACTORES MÁS PREDICTIVOS (log-odds hacia Éxito):")
pri,cnt,vocab,N=M;lo=[]
for f in FEATS:
    for v in vocab[f]:
        te=sum(cnt[f]['Éxito'].values());ta=sum(cnt[f]['Adverso'].values())
        pe=(cnt[f]['Éxito'].get(v,0)+1)/(te+len(vocab[f]));pa=(cnt[f]['Adverso'].get(v,0)+1)/(ta+len(vocab[f]))
        n=cnt[f]['Éxito'].get(v,0)+cnt[f]['Adverso'].get(v,0)
        if n>=8:lo.append((math.log(pe/pa),f,v,n))
lo.sort(reverse=True)
for x in lo[:5]:print(f"   +{x[0]:+.2f}  {x[1]}={x[2]} (n={x[3]})  → favorece ÉXITO")
for x in lo[-5:]:print(f"   {x[0]:+.2f}  {x[1]}={x[2]} (n={x[3]})  → favorece ADVERSO")
# Predicción sobre activos no resueltos
pred=[]
for r in U:
    if r[SENT].strip() in EXITO or r[SENT].strip() in ADV:continue
    if r[EST].strip().upper()=="CONCLUIDO":continue
    p=predict(M,feats(r));pred.append({"num":r[EXP].strip(),"materia":materia_fina(r),"p_exito":round(p['Éxito'],3)})
pred.sort(key=lambda x:x['p_exito'])
json.dump({"accuracy":round(sum(acc)/K,3),"baseline":round(base,3),"n":len(DS),
  "pred_activos":pred},open(OUT+"modelo_data.json","w",encoding="utf-8"),ensure_ascii=False)
print(f"\nPredicción sobre {len(pred)} activos no resueltos:")
print(f"   prob. éxito mediana: {sorted(p['p_exito'] for p in pred)[len(pred)//2]:.0%}")
print(f"   en riesgo (p_éxito<40%): {sum(1 for p in pred if p['p_exito']<0.4)} | favorables (>60%): {sum(1 for p in pred if p['p_exito']>0.6)}")
print("   5 de mayor riesgo de perder:")
for p in pred[:5]:print(f"      {p['num']:12} {p['materia']:12} p.éxito {p['p_exito']:.0%}")
