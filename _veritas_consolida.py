# -*- coding: utf-8 -*-
import csv, collections, re

PATH = "/Users/edithroque/Documents/CLAUDE/juicios.tab"
rows = []
with open(PATH, encoding="latin-1", newline="") as f:
    cleaned = (line.replace("\x00", "") for line in f)
    for row in csv.reader(cleaned, delimiter="\t"):
        rows.append(row)

TOTAL = len(rows)
clean = [r for r in rows if len(r) == 25]
misaligned = [r for r in rows if len(r) != 25]

# --- Esquema canónico (índices) ---
ESTADO, AUTORIDAD, PRESTACIONES, ACTOR, DEMANDADO = 0,1,2,3,4
TIPO_JUICIO, ABOG_INTERNO, EXPEDIENTE, FECHA_PRES = 8,9,10,11
SENTIDO_RES, DEPENDENCIA, SISTEMA, MATERIA = 12,17,23,24

exp_year = re.compile(r"/\s*(\d{2,4})")
def year_from_exp(v):
    m = exp_year.search(v)
    if not m: return None
    y = m.group(1)
    if len(y) == 2: y = "20"+y if int(y) < 50 else "19"+y
    return y if 1990 <= int(y) <= 2026 else None

# --- DEDUP por expediente (col 10) ---
print("="*70); print("CALIDAD Y CONSOLIDACIÓN"); print("="*70)
print(f"Filas totales en archivo:        {TOTAL}")
print(f"  canónicas (25 col):            {len(clean)}")
print(f"  desalineadas (≠25 col):        {len(misaligned)}  -> EXCLUIDAS de conteo posicional")
exp_counts = collections.Counter(r[EXPEDIENTE].strip() for r in clean if r[EXPEDIENTE].strip())
dups = {e:n for e,n in exp_counts.items() if n>1}
vacios_exp = sum(1 for r in clean if not r[EXPEDIENTE].strip())
print(f"Expedientes sin número (col 10): {vacios_exp}")
print(f"Expedientes duplicados:          {len(dups)} (filas extra: {sum(n-1 for n in dups.values())})")
for e,n in list(dups.items())[:12]:
    print(f"    dup x{n}: {e}")

# base única: una fila por expediente (primera aparición); filas sin exp se conservan como registro propio
seen=set(); unica=[]
for r in clean:
    e=r[EXPEDIENTE].strip()
    key = e if e else f"__sinexp__{len(unica)}"
    if key in seen: continue
    seen.add(key); unica.append(r)
print(f"\nBASE ÚNICA CONSOLIDADA:           {len(unica)} registros")

def tabla(col, label, base=None, top=50):
    base = base or unica
    c = collections.Counter(r[col].strip() or "(vacío)" for r in base)
    print(f"\n--- {label} (col {col}) ---  base={len(base)}")
    for v,n in c.most_common(top):
        print(f"   {n:4d}  {v[:70]}")

tabla(MATERIA, "MATERIA")
tabla(TIPO_JUICIO, "TIPO DE JUICIO")
tabla(ESTADO, "ESTADO / ETAPA PROCESAL")
tabla(SENTIDO_RES, "SENTIDO DE LA RESOLUCIÓN")
tabla(SISTEMA, "SISTEMA (régimen)")

# AÑO por expediente
print("\n--- AÑO DE LA DEMANDA (derivado del nº de expediente) ---")
yc = collections.Counter()
sinyear=0
for r in unica:
    y=year_from_exp(r[EXPEDIENTE])
    if y: yc[y]+=1
    else: sinyear+=1
for y in sorted(yc): print(f"   {y}: {yc[y]}")
print(f"   sin año determinable: {sinyear}")
desde2020 = sum(n for y,n in yc.items() if int(y)>=2020)
print(f"   >> registros con expediente 2020-2026: {desde2020}")

# CRITERIO 'ACTIVA' propuesto: estado != CONCLUIDO
activos = [r for r in unica if r[ESTADO].strip().upper()!="CONCLUIDO"]
print(f"\n--- CRITERIO PROPUESTO 'ACTIVA' = estado(col0) != 'CONCLUIDO' ---")
print(f"   activas: {len(activos)} / {len(unica)}   (concluidas: {len(unica)-len(activos)})")

# ETAPA DE SENTENCIA: estado in {Laudo, Sentencia} OR sentido de resolución no vacío
def es_sentencia(r):
    st=r[ESTADO].strip().lower()
    return st in ("laudo","sentencia") or bool(r[SENTIDO_RES].strip())
sent=[r for r in unica if es_sentencia(r)]
print(f"\n--- 'LLEGÓ A SENTENCIA/LAUDO' = estado∈{{Laudo,Sentencia}} o sentido_resolución≠vacío ---")
print(f"   con sentencia/laudo/resolución: {len(sent)}")

# SUSPENSIÓN PROVISIONAL: búsqueda conservadora de texto literal
def cell_join(r): return " ".join(r).lower()
susp_prov = [r for r in clean if "suspensión provisional" in cell_join(r) or "suspension provisional" in cell_join(r)]
susp_any = [r for r in clean if "suspensión" in cell_join(r) or "suspension" in cell_join(r)]
print(f"\n--- SUSPENSIÓN (búsqueda literal en texto, base 767 canónicas) ---")
print(f"   mencionan 'suspensión provisional': {len(susp_prov)} expedientes")
print(f"   mencionan 'suspensión' (cualquiera): {len(susp_any)} expedientes")

# CONCILIACIÓN / CONVENIO
concil = [r for r in clean if any(k in cell_join(r) for k in ["conciliación","conciliacion","convenio"])]
convenio_estado = [r for r in unica if r[ESTADO].strip().lower()=="convenio" or r[SENTIDO_RES].strip().lower()=="por convenio"]
print(f"\n--- CONCILIACIÓN / CONVENIO ---")
print(f"   mencionan 'conciliación/convenio' en texto: {len(concil)} expedientes")
print(f"   estado='Convenio' o sentido='Por Convenio' (estructurado): {len(convenio_estado)}")

# Cruce materia x tipo de juicio
print("\n--- CRUCE MATERIA x TIPO DE JUICIO ---")
cx=collections.Counter((r[MATERIA].strip() or "(vacío)", r[TIPO_JUICIO].strip() or "(vacío)") for r in unica)
for (m,t),n in cx.most_common(25):
    print(f"   {n:4d}  {m:10s} | {t}")
