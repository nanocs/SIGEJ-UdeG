# -*- coding: utf-8 -*-
import csv, re, json, collections, math, datetime
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
CORTE=datetime.date(2026,6,18)
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EXP,AUT,TJ,EST,SENT,DEP,ABO,ACTOR,DEMA,PREST,NOTAS,HIST=10,1,8,0,12,17,9,3,4,2,5,6
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)
MES={'ene':1,'feb':2,'mar':3,'abr':4,'may':5,'jun':6,'jul':7,'ago':8,'sep':9,'oct':10,'nov':11,'dic':12}
dre=re.compile(r'(\d{1,2})[/\- ]([A-Za-zÁ-úñ]{3,4}|\d{1,2})[/\- ](\d{2,4})')
def parse(t):
    d,mo,y=t.groups();mm=MES.get(mo[:3].lower(), int(mo) if mo.isdigit() else 0)
    if not(1<=mm<=12):return None
    y=int(('20'+y if int(y)<50 else '19'+y) if len(y)==2 else y)
    try:return datetime.date(y,mm,int(d))
    except:return None
def fechas(r):
    return [d for d in (parse(m) for m in dre.finditer(" ".join(r))) if d]
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
PROV=re.compile(r"suspensi[oó]n provisional",re.I);CONC=re.compile(r"(se concede|otorga|se decreta|concedi[oó])",re.I)
NEG=re.compile(r"(niega|neg[oó]|no ha lugar|improceden)",re.I);REINST=re.compile(r"reinstalaci[oó]n|indemnizaci[oó]n|salarios ca[ií]dos",re.I)
def enrich(r):
    blob=" ".join(r);mo=maxmonto(r);y=yr(r[EXP]);est=r[EST].strip();sent=r[SENT].strip();s=0;dv=[]
    sc=None;m=PROV.search(blob)
    if m:
        w=blob[max(0,m.start()-45):m.end()+45];sc="negada" if NEG.search(w) else "concedida" if CONC.search(w) else "indet"
    if mo>0:s+=(50 if mo>500000 else 42 if mo>200000 else 32 if mo>100000 else 22 if mo>50000 else 12 if mo>10000 else 6);dv.append(f"monto ${mo:,.0f}")
    if est in("Laudo","Sentencia"):s+=20;dv.append(f"etapa {est}")
    elif est=="Amparo":s+=12;dv.append("en amparo")
    if sent=="Desfavorable":s+=25;dv.append("resolución desfavorable")
    if sent=="Ampara y protege":s+=18;dv.append("amparo a la contraparte")
    if REINST.search(r[PREST]):s+=12;dv.append("reinstalación/indemnización")
    if sc=="concedida":s+=15;dv.append("suspensión concedida")
    if y and (2026-y)>=5 and est.upper()!="CONCLUIDO":s+=10;dv.append(f"{2026-y} años de antigüedad")
    s=min(100,round(s));niv="Crítico" if s>75 else "Alto" if s>=55 else "Medio" if s>=30 else "Bajo"
    fs=fechas(r);ult=max(fs) if fs else None;fut=[d for d in fs if d>CORTE]
    return dict(exp=r[EXP].strip(),materia=r[24].strip(),tj=r[TJ].strip(),estado=est,sent=sent,
                dep=r[DEP].strip(),abogado=r[ABO].strip(),actor=r[ACTOR].strip(),demandado=r[DEMA].strip(),
                prestaciones=r[PREST].strip()[:160],monto=round(mo),anio=y,susp=sc,score=s,nivel=niv,
                drivers=dv,activo=est.upper()!="CONCLUIDO",ult=ult.isoformat() if ult else None,
                prox=min(fut).isoformat() if fut else None)
E=[enrich(r) for r in U]

# ---- ESTRATEGIAS (motor de reglas, orientativo) ----
def estrategias(e):
    L=[];adverso=e["sent"] in("Desfavorable","Ampara y protege");lab=e["materia"]=="Laboral"
    if adverso:
        L.append(("Impugnación / medio de defensa","Valorar amparo directo o recurso de revisión contra la resolución adversa. VERIFICAR plazo (≈15 días hábiles, Ley de Amparo arts. 17-18 — verificar vigencia).","Alta"))
        L.append(("Contención del daño","Negociar convenio en ejecución para acotar condena"+(" (salarios caídos topados, LFT art. 48 — verificar)" if lab else "")+". Cuantificar exposición real.","Media"))
        L.append(("Provisión y causa raíz","Registrar provisión contable del contingente e identificar la causa que originó el resultado para prevención.","Media"))
    elif e["estado"] in("Laudo","Sentencia"):
        L.append(("Fortalecer probanza/alegatos","Robustecer pruebas y alegatos antes de la resolución; revisar carga probatoria.","Alta"))
        L.append(("Salida negociada (MASC)","Evaluar conciliación/convenio temprano dado el riesgo, para evitar condena mayor.","Media"))
        L.append(("Amparo de cobertura","Preparar proyecto de amparo por si la resolución resulta adversa.","Media"))
    elif e["tj"] in("Amparo Indirecto","Amparo Directo"):
        L.append(("Informe justificado sólido","Rendir informe con constancias completas; sostener la constitucionalidad del acto.","Alta"))
        L.append(("Gestión de la suspensión","Combatir o cumplir la suspensión según convenga; evitar incidente de incumplimiento.","Media"))
        L.append(("Preparación de revisión","Anticipar recurso de revisión contra la interlocutoria/sentencia.","Media"))
    else:
        L.append(("Depuración procesal","Verificar procedencia, competencia y plazos para evitar improcedencia.","Alta"))
        L.append(("Impulso procesal","Promover periódicamente para evitar caducidad por inactividad.","Media"))
        L.append(("Evaluación de salida","Analizar viabilidad de convenio o desistimiento estratégico.","Baja"))
    return [{"estrategia":a,"accion":b,"prioridad":c} for a,b,c in L]
def matriz(e):
    p="Muy alta" if e["score"]>75 else "Alta" if e["score"]>=55 else "Media" if e["score"]>=30 else "Baja"
    im="Crítico" if e["monto"]>500000 else "Alto" if e["monto"]>100000 else "Medio" if e["monto"]>0 else "Indeterminado"
    return {"probabilidad":p,"impacto":im}
def ficha(e):
    return {"exp":e["exp"],"nivel":e["nivel"],"score":e["score"],
            "resumen":f"{e['materia']} ({e['tj']}) · {e['actor']} vs {e['demandado']} · {e['dep']} · etapa {e['estado']}"+(f" · sentido {e['sent']}" if e['sent'] else "")+f". Responsable: {e['abogado']}. Monto detectado: ${e['monto']:,}.",
            "matriz":matriz(e),"estrategias":estrategias(e),
            "trazabilidad":[f"Expediente (col10): {e['exp']}",f"Estado (col0): {e['estado']}",f"Sentido (col12): {e['sent'] or '—'}",
                            f"Materia (col24): {e['materia']}",f"Monto (texto): ${e['monto']:,}",f"Factores de riesgo: {', '.join(e['drivers']) or '—'}"]}
altos=[e for e in E if e["nivel"] in("Alto","Crítico")]
altos.sort(key=lambda x:-x["score"])
fichas=[ficha(e) for e in altos]

# ---- ALERTAS ----
venc=[{"exp":e["exp"],"materia":e["materia"],"abogado":e["abogado"],"prox":e["prox"],
       "dias":(datetime.date.fromisoformat(e["prox"])-CORTE).days,"nivel":e["nivel"]} for e in E if e["prox"]]
venc.sort(key=lambda x:x["dias"])
def meses(iso):
    if not iso:return None
    return round((CORTE-datetime.date.fromisoformat(iso)).days/30.4)
inact=[{"exp":e["exp"],"materia":e["materia"],"abogado":e["abogado"],"ult":e["ult"],
        "meses_sin_mov":meses(e["ult"]),"nivel":e["nivel"]} for e in E if e["activo"] and e["ult"] and meses(e["ult"])>=18]
inact.sort(key=lambda x:-x["meses_sin_mov"])
conting=[{"exp":e["exp"],"materia":e["materia"],"abogado":e["abogado"],"dep":e["dep"],
          "monto":e["monto"],"nivel":e["nivel"],"score":e["score"]} for e in E if e["activo"] and e["monto"]>0 and e["nivel"] in("Alto","Crítico")]
conting.sort(key=lambda x:-x["monto"])

# ---- LECCIONES APRENDIDAS (marco normativo curado, VERIFICAR) ----
LEC={
 "Sobresee":{"causa":"Se actualizó una causal de improcedencia o cesaron los efectos del acto reclamado; el juicio termina sin resolver el fondo.","evitar":"Depurar la procedencia antes de promover y vigilar el cumplimiento para evitar que el acto quede sin materia.","marco":"Ley de Amparo art. 63 (causales de sobreseimiento; p.ej. fr. IV, inexistencia del acto reclamado). Improcedencia: art. 61.","verif":"verificado"},
 "Desechó":{"causa":"Demanda desechada de plano por motivo manifiesto e indudable de improcedencia (o presentada fuera de plazo).","evitar":"Revisar requisitos de procedencia y cómputo de plazos antes de presentar; la improcedencia debe ser evidente desde la demanda.","marco":"Ley de Amparo art. 113 (desechamiento de plano por motivo manifiesto e indudable de improcedencia); plazos arts. 17-18.","verif":"verificado"},
 "Niega":{"causa":"Los conceptos de violación/agravios se declararon infundados; el acto se estimó constitucional/legal.","evitar":"Reforzar agravios, ofrecer y desahogar pruebas idóneas, cuidar la técnica del amparo.","marco":"Ley de Amparo art. 74 (requisitos de la sentencia que concede, niega o sobresee; fr. IV, fundamentos legales) y art. 77 (efectos de la concesión).","verif":"verificado"},
 "Caducidad":{"causa":"Inactividad procesal del actor: en el juicio laboral ante Juntas, falta de promoción por el plazo legal.","evitar":"Control de plazos y promociones periódicas (ver módulo de Alertas: 205 expedientes activos ≥18 meses sin movimiento). Atender el requerimiento de los 45 días.","marco":"LFT art. 772 (inactividad de 45 días naturales → requerimiento al trabajador) y art. 773 (se tiene por desistida la acción si no hay promoción en 4 meses). Prescripción: arts. 516-522. Tesis aislada reg. 2025181 'CADUCIDAD EN EL JUICIO LABORAL', Tribunal Colegiado de Circuito, 11a Época, Gaceta del SJF Libro 17 (sep 2022) — valor ORIENTADOR, no obligatorio.","verif":"verificado"},
 "Desistimiento":{"causa":"La parte se desistió de la acción; en ocasiones es estratégico (precedido de convenio).","evitar":"Documentar si el desistimiento derivó de un convenio favorable a la UdeG; auditar si fue evitable.","marco":"Ley de Amparo art. 63 fr. I (sobreseimiento por desistimiento del quejoso).","verif":"verificado"},
 "Infundada":{"causa":"La pretensión o el recurso carecieron de sustento jurídico suficiente.","evitar":"Análisis de viabilidad previo (probabilidad de éxito) antes de litigar o recurrir.","marco":"Según la vía (LFT / CNPP / CFPC / leyes locales).","verif":"a confirmar"},
 "Desfavorable":{"causa":"En materia laboral, suele derivar de despido tenido por injustificado o de deficiencia probatoria de la parte patronal (UdeG); con frecuencia por falta del aviso de despido por escrito.","evitar":"Expediente laboral robusto: contratos, rescisión debidamente fundada y motivada, AVISO DE DESPIDO por escrito (su omisión vuelve injustificado el despido, art. 47 LFT), y defensa procesal en tiempo.","marco":"LFT art. 47 (causas de rescisión sin responsabilidad para el patrón; sin aviso por escrito el despido se reputa injustificado), art. 48 (reinstalación o indemnización de 3 meses + salarios vencidos hasta máx. 12 meses por reforma 2012, e intereses sobre 15 meses al 2% mensual capitalizable si se excede), art. 50 (indemnizaciones). Art. 123-A fr. XXII constitucional (estabilidad en el empleo: cumplir contrato o indemnizar 3 meses, a elección del trabajador).","verif":"verificado"},
}
sent_cnt=collections.Counter(e["sent"] for e in E if e["sent"])
EXITO={"Sobresee","Desechó","Niega","Caducidad","Desistimiento","Infundada"}
lecciones=[]
for s in list(EXITO)+["Desfavorable"]:
    if s in LEC:
        casos=[{"exp":e["exp"],"materia":e["materia"],"dep":e["dep"],"abogado":e["abogado"]} for e in E if e["sent"]==s]
        lecciones.append({"sentido":s,"tipo":"Éxito UdeG" if s in EXITO else "Adverso","n":sent_cnt.get(s,0),
                          **LEC[s],"casos":casos})

data={"corte":CORTE.isoformat(),"alertas":{"vencimientos":venc,"inactividad":inact[:40],"contingente":conting,
       "kpi":{"venc":len(venc),"inact":len(inact),"conting":len(conting),
              "pasivo_riesgo":round(sum(c["monto"] for c in conting))}},
      "fichas":fichas,"lecciones":lecciones}
json.dump(data,open(OUT+"alertas_data.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("vencimientos:",len(venc),"| inactividad>=18m:",len(inact),"| contingente(alto+):",len(conting),
      "| pasivo en riesgo: ${:,.0f}".format(data["alertas"]["kpi"]["pasivo_riesgo"]))
print("fichas de riesgo:",len(fichas),"| lecciones:",[(l["sentido"],l["n"]) for l in lecciones])
