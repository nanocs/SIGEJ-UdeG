# -*- coding: utf-8 -*-
import csv, re, json, collections, datetime, statistics
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
CORTE=datetime.date(2026,6,18)
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EXP,HIST,GEST,PREST=10,6,7,2
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
    try:return datetime.date(y,mm,int(d))
    except:return None
MONEY=re.compile(r"\$\s?([\d]{1,3}(?:[, ]\d{3})*(?:\.\d{1,2})?)")
def montos_txt(s):
    out=[]
    for m in MONEY.finditer(s):
        try:
            v=float(m.group(1).replace(",","").replace(" ",""))
            if v>=100:out.append(v)
        except:pass
    return out
RES={'Laudo':re.compile(r'\blaudo\b',re.I),'Sentencia definitiva':re.compile(r'sentencia definitiva',re.I),
     'Interlocutoria':re.compile(r'interlocutoria',re.I),'Sobreseimiento':re.compile(r'sobresee|sobreseimiento',re.I),
     'Ampara':re.compile(r'\bampara\b|concede el amparo',re.I),'Niega amparo':re.compile(r'niega el amparo|se niega el amparo',re.I)}
SENAL=re.compile(r'se[ñn]ala(?:n)?\s+(?:nueva\s+)?fecha|para que tenga verificativo|cit[aó] a las partes',re.I)
AUD=re.compile(r'audiencia',re.I)

def eventos(txt):
    # parte el relato por las fechas que actúan como marcadores de evento
    idxs=[(m.start(),pdate(m)) for m in DRE.finditer(txt)]
    idxs=[(i,d) for i,d in idxs if d]
    ev=[]
    for k,(i,d) in enumerate(idxs):
        j=idxs[k+1][0] if k+1<len(idxs) else len(txt)
        ev.append((d,txt[i:j]))
    return ev

recov={'monto':0,'monto_solo_texto':0,'tipo_res':0,'fecha_res':0,'prox':0,'eventos':0}
out={}
montos_field_re=lambda r:[v for c in [PREST,5,14,15,18,22,25,26,28] if c<len(r) for v in montos_txt(r[c])]
for r in U:
    num=r[EXP].strip();blob=(r[HIST] or "")+" \n "+(r[GEST] or "")
    ev=eventos(r[HIST] or "")
    fechas=[d for d,_ in ev]
    ult=max(fechas) if fechas else None
    fut=[d for d in fechas if d>CORTE]
    prox=min(fut) if fut else None
    # tipo y fecha de la ÚLTIMA resolución mencionada
    tipo_res=None;fecha_res=None
    for d,seg in sorted(ev,key=lambda x:x[0]):
        for nom,rx in RES.items():
            if rx.search(seg):tipo_res=nom;fecha_res=d
    # montos: campos estructurados + texto del historial/gestiones
    CEIL=100_000_000  # techo de sanidad: >$100M se trata como anómalo (verificar)
    m_field=[v for v in montos_field_re(r)]
    m_text=[v for v in montos_txt(blob)]
    todos=m_field+m_text
    monto_bruto=max(todos) if todos else 0
    anomalo=monto_bruto>CEIL
    monto=0 if anomalo else monto_bruto
    n_ev=len(ev)
    rec={'num':num,'ult_actuacion':ult.isoformat() if ult else None,'n_eventos':n_ev,
         'prox_fecha':prox.isoformat() if prox else None,'monto_max':round(monto),
         'monto_anomalo':round(monto_bruto) if anomalo else 0,
         'monto_de_texto':bool(m_text and (not m_field or (max(m_text)>max(m_field)))),
         'tipo_resolucion':tipo_res,'fecha_resolucion':fecha_res.isoformat() if fecha_res else None}
    out[num]=rec
    if monto>0:recov['monto']+=1
    if m_text and not m_field:recov['monto_solo_texto']+=1
    if tipo_res:recov['tipo_res']+=1
    if fecha_res:recov['fecha_res']+=1
    if prox:recov['prox']+=1
    if n_ev:recov['eventos']+=1
json.dump(out,open(OUT+"nlp_expedientes.json","w",encoding="utf-8"),ensure_ascii=False)
N=len(U)
print("="*60);print(f"RECUPERACIÓN NLP sobre {N} expedientes");print("="*60)
print(f"  con MONTO (estructurado o texto):   {recov['monto']:>4}  (antes ~38 con $ estructurado)")
print(f"   …monto recuperado SOLO del texto:  {recov['monto_solo_texto']:>4}")
print(f"  con TIPO de resolución detectado:   {recov['tipo_res']:>4}")
print(f"  con FECHA de resolución:            {recov['fecha_res']:>4}")
print(f"  con próxima fecha (futura):         {recov['prox']:>4}")
print(f"  con eventos procesales fechados:    {recov['eventos']:>4}")
nev=[out[k]['n_eventos'] for k in out if out[k]['n_eventos']]
print(f"\n  eventos por expediente -> mediana {int(statistics.median(nev))}, máx {max(nev)}, total {sum(nev):,}")
tr=collections.Counter(out[k]['tipo_resolucion'] for k in out if out[k]['tipo_resolucion'])
print("  tipos de resolución detectados:",dict(tr))
mm=[out[k]['monto_max'] for k in out if out[k]['monto_max']>0]
anom=[(k,out[k]['monto_anomalo']) for k in out if out[k]['monto_anomalo']>0]
print(f"  pasivo recuperable SANITIZADO (≤$100M): ${sum(mm):,} en {len(mm)} expedientes")
print(f"  ANÓMALOS excluidos (>$100M, verificar): {len(anom)} -> {anom}")
print(f"  >$5M (revisar): {sum(1 for v in mm if v>5_000_000)} | >$1M: {sum(1 for v in mm if v>1_000_000)}")
