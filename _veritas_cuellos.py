# -*- coding: utf-8 -*-
import csv, re, json, collections, datetime, statistics
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
CORTE=datetime.date(2026,6,18)
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EXP,HIST,EST,AUT,MAT,TJ=10,6,0,1,24,8
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)
MES={'ene':1,'feb':2,'mar':3,'abr':4,'may':5,'jun':6,'jul':7,'ago':8,'sep':9,'oct':10,'nov':11,'dic':12}
DRE=re.compile(r'(\d{1,2})[/\- ]([A-Za-zÁ-úñ]{3,4}|\d{1,2})[/\- ](\d{2,4})')
def pdate(t):
    d,mo,y=t.groups();mm=MES.get(mo[:3].lower(), int(mo) if mo.isdigit() else 0)
    if not(1<=mm<=12):return None
    y=int(('20'+y if int(y)<50 else '19'+y) if len(y)==2 else y)
    try:
        dt=datetime.date(y,mm,int(d))
        return dt if datetime.date(1990,1,1)<=dt<=datetime.date(2027,1,1) else None
    except:return None
def eventos(txt):
    idx=[(m.start(),pdate(m)) for m in DRE.finditer(txt)]
    idx=[(i,d) for i,d in idx if d]
    out=[]
    for k,(i,d) in enumerate(idx):
        j=idx[k+1][0] if k+1<len(idx) else len(txt)
        out.append((d,txt[i:j].lower()))
    return sorted(out,key=lambda x:x[0])
STAGES=[('Inicio',re.compile(r'avocamiento|admite la demanda|radicaci[oó]n|auto inicial|presentaci[oó]n de demanda')),
        ('Emplazamiento',re.compile(r'emplaz')),
        ('Audiencia',re.compile(r'audiencia')),
        ('Pruebas',re.compile(r'prueba')),
        ('Alegatos',re.compile(r'alegatos')),
        ('Resolución',re.compile(r'laudo|sentencia|interlocutoria|se resuelve|resoluci[oó]n'))]
def first_stage(ev):
    fs={}
    for d,seg in ev:
        for nom,rx in STAGES:
            if nom not in fs and rx.search(seg):fs[nom]=d
    return fs
def mdays(a,b):return (b-a).days
data=[];trans=collections.defaultdict(list);dur_mat=collections.defaultdict(list)
idle=[];lifespans=[]
for r in U:
    ev=eventos(r[HIST] or "")
    if not ev:continue
    first,last=ev[0][0],ev[-1][0]
    activo=r[EST].strip().upper()!="CONCLUIDO"
    gaps=[mdays(ev[k][0],ev[k+1][0]) for k in range(len(ev)-1)]
    maxgap=max(gaps) if gaps else 0
    life=mdays(first,last)
    fs=first_stage(ev)
    idl=mdays(last,CORTE) if activo else None
    rec={'num':r[EXP].strip(),'materia':r[MAT].strip(),'autoridad':r[AUT].strip(),'estado':r[EST].strip(),
         'n_ev':len(ev),'inicio':first.isoformat(),'ultimo':last.isoformat(),'vida_dias':life,
         'max_gap_dias':maxgap,'idle_dias':idl,'activo':activo}
    data.append(rec)
    if life>0:lifespans.append(life);dur_mat[r[MAT].strip()].append(life)
    if idl is not None:idle.append((idl,r[EXP].strip(),r[MAT].strip(),last.isoformat()))
    # transiciones entre etapas consecutivas presentes
    seq=['Inicio','Emplazamiento','Audiencia','Pruebas','Alegatos','Resolución']
    pres=[(s,fs[s]) for s in seq if s in fs]
    for k in range(len(pres)-1):
        dd=mdays(pres[k][1],pres[k+1][1])
        if 0<=dd<6000:trans[pres[k][0]+' → '+pres[k+1][0]].append(dd)
def med(x):return int(statistics.median(x)) if x else 0
print("="*64);print(f"CUELLOS DE BOTELLA — {len(data)} expedientes con eventos");print("="*64)
print(f"Duración total del juicio (primer→último evento): mediana {med(lifespans)} días ({med(lifespans)/365:.1f} años)")
print("\nDuración por materia (mediana, días):")
for m,v in sorted(dur_mat.items(),key=lambda x:-med(x[1])):
    if len(v)>=5:print(f"   {m:14} {med(v):>6} d  ({med(v)/365:.1f} a)  n={len(v)}")
print("\nTRANSICIONES ENTRE ETAPAS (mediana de días) — los cuellos de botella:")
for t,v in sorted(trans.items(),key=lambda x:-med(x[1])):
    if len(v)>=10:print(f"   {t:28} {med(v):>5} d   n={len(v)}")
print("\nBrecha máxima sin movimiento (mediana entre todos): %d días"%med([d['max_gap_dias'] for d in data if d['max_gap_dias']]))
act_idle=sorted([x for x in idle],reverse=True)
print(f"\nEXPEDIENTES ACTIVOS MÁS ATORADOS (sin movimiento, top 10):")
for idl,num,mat,last in act_idle[:10]:
    print(f"   {num:12} {mat:10} sin mov. {idl} d ({idl/30:.0f} meses) — último {last}")
print(f"\nActivos sin movimiento > 12 meses: {sum(1 for x in idle if x[0]>365)} | > 24 meses: {sum(1 for x in idle if x[0]>730)}")
_act=[x for x in data if x['activo'] and x['idle_dias'] is not None]
idle_counts={'total_activos':len(_act),'a12':sum(1 for x in _act if x['idle_dias']>365),'a24':sum(1 for x in _act if x['idle_dias']>730)}
json.dump({'data':data,'idle_counts':idle_counts,'lifespan_med':med(lifespans),
  'dur_materia':{m:med(v) for m,v in dur_mat.items() if len(v)>=5},
  'transiciones':{t:{'mediana':med(v),'n':len(v)} for t,v in trans.items() if len(v)>=10},
  'atorados':[{'num':n,'materia':m,'idle_dias':i,'ultimo':l} for i,n,m,l in act_idle[:30]]},
  open(OUT+"cuellos_data.json","w",encoding="utf-8"),ensure_ascii=False)
print("\ncuellos_data.json exportado")
