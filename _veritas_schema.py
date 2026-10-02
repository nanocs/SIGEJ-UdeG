# -*- coding: utf-8 -*-
import csv, collections, re

PATH = "/Users/edithroque/Documents/CLAUDE/juicios.tab"
rows = []
with open(PATH, encoding="latin-1", newline="") as f:
    cleaned = (line.replace("\x00", "") for line in f)
    for row in csv.reader(cleaned, delimiter="\t"):
        rows.append(row)

clean = [r for r in rows if len(r) == 25]
print("Filas canónicas (25 col):", len(clean), "de", len(rows))
print("="*80)

def dist(col, top=40, label=""):
    c = collections.Counter(r[col].strip() for r in clean if r[col].strip())
    print(f"\n### COLUMNA {col}  {label}  (no_vacíos={sum(c.values())}, únicos={len(c)})")
    for v, n in c.most_common(top):
        print(f"   {n:4d}  {v[:75]}")

# Categóricas candidatas
for col in [0, 1, 8, 9, 12, 17, 23, 24]:
    dist(col)

# Detección de patrones: expediente y fechas/años
print("\n", "="*80)
exp_re = re.compile(r"\b\d{1,4}\s*/\s*\d{4}")
year_re = re.compile(r"(20\d{2}|19\d{2}|/\d{2}\b)")
for col in [10, 11]:
    vals = [r[col].strip() for r in clean if r[col].strip()]
    nexp = sum(1 for v in vals if exp_re.search(v))
    print(f"col {col}: {len(vals)} no vacíos; con patrón nº/año: {nexp}; muestra: {vals[:6]}")

# Años en columna 11 (fecha de presentación candidata)
print("\nAÑOS detectados en col 11 (fecha presentación?):")
yr = collections.Counter()
for r in clean:
    v = r[11].strip()
    m = re.search(r"(\d{1,2})[/\-](\d{1,2})[/\-](\d{2,4})", v)
    if m:
        y = m.group(3)
        if len(y) == 2: y = "20"+y if int(y) < 50 else "19"+y
        yr[y]+=1
for y, n in sorted(yr.items()):
    print(f"   {y}: {n}")
