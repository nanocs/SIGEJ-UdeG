# -*- coding: utf-8 -*-
import csv, re, collections

PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
misaligned=[r for r in rows if len(r)!=25]

EXP,MAT,AUT,TJ,EST,SENT,HIST,GEST=10,24,1,8,0,12,6,7
MATERIAS={"laboral","civil","penal","administrativa","mercantil","agraria"}
TIPOS={"ordinario","amparo directo","amparo indirecto","administrativo","especial",
       "recurso de revisión","queja","civil","agrario","mercantil"}
exp_re=re.compile(r"\b(\d{1,4}\s*/\s*\d{2,4}(?:-?[A-Z])?)\b")
def yr(v):
    m=re.search(r"/\s*(\d{2,4})",v or "");
    if not m: return "s/d"
    y=m.group(1); y=("20"+y if int(y)<50 else "19"+y) if len(y)==2 else y
    return y if y.isdigit() and 1990<=int(y)<=2026 else "s/d"

# ---------- 1) RECUPERAR 74 FILAS DESALINEADAS ----------
rec=[]
for r in misaligned:
    blob=" ".join(r)
    exp=""
    for cell in r:
        m=exp_re.search(cell.strip())
        if m and len(cell.strip())<=14: exp=m.group(1).replace(" ",""); break
    if not exp:
        m=exp_re.search(blob); exp=m.group(1).replace(" ","") if m else ""
    mat=next((c.strip() for c in r if c.strip().lower() in MATERIAS),"")
    tj =next((c.strip() for c in r if c.strip().lower() in TIPOS),"")
    aut=next((c.strip() for c in r if re.search(r"junta|tribunal|juzgado|sala",c,re.I)),"")
    rec.append({"expediente":exp,"anio":yr(exp),"materia":mat or "(no identificada)",
                "tipo_juicio":tj,"autoridad":aut,"ncols":len(r)})
with open(OUT+"RECUPERADAS_74.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["expediente","anio","materia","tipo_juicio","autoridad","ncols"]);w.writeheader()
    for d in rec: w.writerow(d)
rec_exp=sum(1 for d in rec if d["expediente"]); rec_mat=sum(1 for d in rec if d["materia"]!="(no identificada)")
print(f"[1] 74 desalineadas -> expediente recuperado: {rec_exp}/74 | materia: {rec_mat}/74")

# base única (dedup) de canónicas
seen=set();unica=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(unica)}"
    if k in seen:continue
    seen.add(k);unica.append(r)

# ---------- 2) SUSPENSIÓN PROVISIONAL: concedida vs negada ----------
NEG=re.compile(r"(niega|neg[oó]|no ha lugar|improceden|no se concede|sin conceder)",re.I)
CONC=re.compile(r"(se concede|concede la|otorga|se decreta|concedi[oó]|se otorga)",re.I)
PROV=re.compile(r"suspensi[oó]n provisional",re.I)
susp=[]
for r in unica:
    blob=" ".join(r)
    for m in PROV.finditer(blob):
        win=blob[max(0,m.start()-45):m.end()+45]
        estado=("negada" if NEG.search(win) else "concedida" if CONC.search(win) else "indeterminada")
        susp.append({"expediente":r[EXP],"materia":r[MAT],"tipo_juicio":r[TJ],"autoridad":r[AUT],
                     "clasificacion":estado,"contexto":win.replace("\n"," ").replace("\r"," ")})
        break
cls=collections.Counter(s["clasificacion"] for s in susp)
with open(OUT+"SUSPENSION_clasificada.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["expediente","materia","tipo_juicio","autoridad","clasificacion","contexto"]);w.writeheader()
    for s in susp:w.writerow(s)
print(f"[2] suspensión provisional (mencionan): {len(susp)} -> {dict(cls)}")

# ---------- 3) SENTENCIA / LAUDO: tipo + fecha ----------
MES={"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,"jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}
date_txt=re.compile(r"(\d{1,2})[/\- ]([A-Za-zÁ-úñ]{3,4}|\d{1,2})[/\- ](\d{2,4})")
def norm_date(t):
    d,mo,y=t.groups();
    if not mo[:3].lower() in MES and not mo.isdigit(): return None
    mm=MES.get(mo[:3].lower(),int(mo) if mo.isdigit() else 0)
    if not(1<=mm<=12):return None
    y=("20"+y if int(y)<50 else "19"+y) if len(y)==2 else y
    try:return (int(y),mm,int(d))
    except:return None
def tipo_sentencia(blob):
    b=blob.lower();t=[]
    if "laudo" in b:t.append("Laudo")
    if "sentencia definitiva" in b or re.search(r"sentencia(?!\s+interlocutoria)",b):t.append("Sentencia definitiva")
    if "interlocutoria" in b:t.append("Interlocutoria")
    return "/".join(dict.fromkeys(t)) or "(otra/no clasif.)"
def es_sent(r): return r[EST].strip().lower() in ("laudo","sentencia") or bool(r[SENT].strip())
sents=[]
for r in unica:
    if not es_sent(r):continue
    blob=r[HIST]+" "+r[GEST]
    ds=[norm_date(m) for m in date_txt.finditer(blob)];ds=[d for d in ds if d]
    fecha=max(ds) if ds else None
    sents.append({"expediente":r[EXP],"anio_exp":yr(r[EXP]),"materia":r[MAT],"estado":r[EST],
                  "sentido":r[SENT],"tipo_resolucion":tipo_sentencia(blob),
                  "fecha_ult_movto":f"{fecha[0]}-{fecha[1]:02d}-{fecha[2]:02d}" if fecha else "no extraíble"})
with open(OUT+"SENTENCIAS_tipo_fecha.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["expediente","anio_exp","materia","estado","sentido","tipo_resolucion","fecha_ult_movto"]);w.writeheader()
    for s in sents:w.writerow(s)
tc=collections.Counter(s["tipo_resolucion"] for s in sents)
con_fecha=sum(1 for s in sents if s["fecha_ult_movto"]!="no extraíble")
print(f"[3] etapa sentencia/laudo: {len(sents)} | con fecha extraída: {con_fecha} | tipos: {dict(tc)}")

# ---------- CRITERIOS 'ACTIVA' (ambas lecturas) ----------
print("\n--- DEMANDAS ACTIVAS bajo criterios alternos (base 749 únicas) ---")
a1=[r for r in unica if r[EST].strip().upper()!="CONCLUIDO"]
a2=[r for r in unica if not r[SENT].strip() and r[EST].strip().upper()!="CONCLUIDO"]
a3=[r for r in unica if r[EST].strip().upper()!="CONCLUIDO" and yr(r[EXP])!="s/d" and int(yr(r[EXP]))>=2020]
print(f"  C1 estado!=CONCLUIDO:                      {len(a1)}")
print(f"  C2 sin resolución firme y !=CONCLUIDO:     {len(a2)}")
print(f"  C3 (C1) y expediente 2020-2026:            {len(a3)}")
print(f"\nUniverso ampliado (749 únicas + {rec_exp} recuperadas con clave) = {749+rec_exp}")
