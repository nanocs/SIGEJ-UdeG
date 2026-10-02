# -*- coding: utf-8 -*-
import csv, re

PATH = "/Users/edithroque/Documents/CLAUDE/juicios.tab"
OUT  = "/Users/edithroque/Documents/CLAUDE/"
rows=[]
with open(PATH, encoding="latin-1", newline="") as f:
    cleaned=(l.replace("\x00","") for l in f)
    for r in csv.reader(cleaned, delimiter="\t"):
        rows.append(r)
clean=[r for r in rows if len(r)==25]

HEAD = ["estado_procesal","autoridad","prestaciones","actor","demandado",
        "notas_acumulados","historial_procesal","gestiones_abogado_general","tipo_juicio",
        "abogado_interno","expediente","fecha_presentacion","sentido_resolucion","col13","col14",
        "col15","col16","dependencia_centro","col18","col19","col20","col21","col22","sistema","materia"]
EXP, MAT, AUT, TJ, EST, SENT, HIST, GEST = 10,24,1,8,0,12,6,7

# Base única (dedup por expediente)
seen=set(); unica=[]
for r in clean:
    e=r[EXP].strip(); key=e or f"__sinexp__{len(unica)}"
    if key in seen: continue
    seen.add(key); unica.append(r)

with open(OUT+"BASE_UNICA_consolidada.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(HEAD)
    for r in unica: w.writerow(r)
print("BASE_UNICA_consolidada.csv:", len(unica),"registros")

# Suspensión provisional (literal) con contexto
def ctx(text, term):
    i=text.lower().find(term)
    return text[max(0,i-40):i+80].replace("\n"," ").replace("\r"," ") if i>=0 else ""
with open(OUT+"SUSPENSION_PROVISIONAL_candidatos.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["expediente","materia","tipo_juicio","autoridad","contexto_literal"])
    n=0
    for r in unica:
        blob=" ".join(r)
        if re.search(r"suspensi[oó]n provisional", blob, re.I):
            w.writerow([r[EXP],r[MAT],r[TJ],r[AUT], ctx(blob,"suspensi")]); n+=1
print("SUSPENSION_PROVISIONAL_candidatos.csv:", n)

# Conciliación/convenio ESTRUCTURADO (no audiencias)
with open(OUT+"CONCILIACION_estructurada.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["expediente","materia","tipo_juicio","autoridad","estado","sentido_resolucion"])
    n=0
    for r in unica:
        if r[EST].strip().lower()=="convenio" or r[SENT].strip().lower()=="por convenio":
            w.writerow([r[EXP],r[MAT],r[TJ],r[AUT],r[EST],r[SENT]]); n+=1
print("CONCILIACION_estructurada.csv:", n)

# Tabla materia x año (determinable) -> export
import collections
exp_year=re.compile(r"/\s*(\d{2,4})")
def yr(v):
    m=exp_year.search(v)
    if not m: return "s/d"
    y=m.group(1)
    if len(y)==2: y="20"+y if int(y)<50 else "19"+y
    return y if 1990<=int(y)<=2026 else "s/d"
mat_year=collections.Counter((yr(r[EXP]), r[MAT].strip() or "(s/materia)") for r in unica)
with open(OUT+"MATERIA_POR_ANIO.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["anio","materia","n_demandas"])
    for (y,m),n in sorted(mat_year.items()):
        w.writerow([y,m,n])
print("MATERIA_POR_ANIO.csv exportado")
