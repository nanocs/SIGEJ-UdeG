# -*- coding: utf-8 -*-
import csv, re, collections
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EST,AUT,TJ,MAT=0,1,8,24
seen=set();U=[]
for r in clean:
    e=r[10].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)

def materia_fina(r):
    a=r[AUT].lower(); tj=r[TJ].strip(); base=r[MAT].strip()
    # 1) Señal por AUTORIDAD (la más confiable de la rama sustantiva)
    if re.search(r"junta .*conciliaci|tribunal laboral|materia de trabajo|materia laboral|de trabajo|arbitraje del estado",a):
        rama="Laboral"
    elif re.search(r"agrario|agraria",a) or tj=="Agrario":
        rama="Agraria"
    elif re.search(r"administrativ|justicia administrativa|fiscal",a) or tj=="Administrativo":
        rama="Administrativa"
    elif re.search(r"materia penal|penal",a):
        rama="Penal"
    elif re.search(r"materia civil|\bcivil\b|familiar|juzgado .*civil",a) or tj=="Civil":
        rama="Civil"
    elif re.search(r"mercantil",a) or tj=="Mercantil":
        rama="Mercantil"
    else:
        rama=None
    # 2) Si la autoridad no resolvió (p.ej. juzgado de distrito genérico en amparo), usar tipo de juicio
    if rama is None:
        if tj=="Mercantil": rama="Mercantil"
        elif tj=="Agrario": rama="Agraria"
        elif tj=="Administrativo": rama="Administrativa"
        elif tj=="Civil": rama="Civil"
        else:
            # 3) Fallback a la materia base (col24), reinterpretando "Civil" genérico
            if base=="Laboral": rama="Laboral"
            elif base=="Penal": rama="Penal"
            elif base=="Civil": rama="Civil (no especificada)"
            else: rama="No identificada"
    return rama

def via(r):
    tj=r[TJ].strip()
    if tj in("Amparo Directo","Amparo Indirecto"): return tj
    if tj in("Recurso de Revisión","Queja","Recurso de Reclamación","Incidente de Inejecución"): return "Recurso/Incidente (amparo)"
    return "Jurisdicción ordinaria"

fina=collections.Counter(materia_fina(r) for r in U)
vias=collections.Counter(via(r) for r in U)
print("=== MATERIA FINA (rama sustantiva) ===")
for k,n in fina.most_common(): print(f"   {n:4d}  {k}")
print("\n=== VÍA ===")
for k,n in vias.most_common(): print(f"   {n:4d}  {k}")
print("\n=== CRUCE base(col24) -> fina ===")
cx=collections.Counter((r[MAT].strip() or '(s/d)', materia_fina(r)) for r in U)
for (b,f),n in cx.most_common(): print(f"   {n:4d}  {b:8} -> {f}")
