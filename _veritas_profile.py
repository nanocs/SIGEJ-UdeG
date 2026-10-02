# -*- coding: utf-8 -*-
import csv, sys, collections

PATH = "/Users/edithroque/Documents/CLAUDE/juicios.tab"

rows = []
with open(PATH, encoding="latin-1", newline="") as f:
    cleaned = (line.replace("\x00", "") for line in f)
    r = csv.reader(cleaned, delimiter="\t")
    for row in r:
        rows.append(row)

print("TOTAL DE FILAS LEÍDAS:", len(rows))
ncols = collections.Counter(len(r) for r in rows)
print("DISTRIBUCIÓN DE Nº DE COLUMNAS POR FILA:", dict(ncols))
MAXC = max(len(r) for r in rows)
print("MÁX COLUMNAS:", MAXC)
print("=" * 90)

def trunc(s, n=70):
    s = s.replace("\r"," ").replace("\n"," ").strip()
    return (s[:n] + "…") if len(s) > n else s

for c in range(MAXC):
    vals = [r[c] for r in rows if len(r) > c]
    nonempty = [v for v in vals if v.strip()]
    uniq = set(v.strip() for v in nonempty)
    print(f"\n--- COLUMNA {c} ---  no_vacíos={len(nonempty)}/{len(rows)}  únicos={len(uniq)}")
    # muestra hasta 4 valores no vacíos distintos
    seen = []
    for v in nonempty:
        t = trunc(v)
        if t not in seen:
            seen.append(t)
        if len(seen) >= 4:
            break
    for s in seen:
        print("    •", s)
