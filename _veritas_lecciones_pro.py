# -*- coding: utf-8 -*-
import csv, re, json, collections
PATH="/Users/edithroque/Documents/CLAUDE/juicios.tab"; OUT="/Users/edithroque/Documents/CLAUDE/"
rows=[]
with open(PATH,encoding="latin-1",newline="") as f:
    for r in csv.reader((l.replace("\x00","") for l in f),delimiter="\t"): rows.append(r)
clean=[r for r in rows if len(r)==25]
EST,AUT,PREST,SENT,ABO,EXP,DEP,MAT,HIST=0,1,2,12,9,10,17,24,6
seen=set();U=[]
for r in clean:
    e=r[EXP].strip();k=e or f"_s{len(U)}"
    if k in seen:continue
    seen.add(k);U.append(r)
try: NLP=json.load(open(OUT+"nlp_expedientes.json",encoding="utf-8"))
except Exception: NLP={}
def yr(v):
    m=re.search(r"/\s*(\d{2,4})",v or "")
    if not m:return None
    y=m.group(1);y=("20"+y if int(y)<50 else "19"+y) if len(y)==2 else y
    return int(y) if y.isdigit() and 1990<=int(y)<=2026 else None
# Knowledge base curada por tipo de resultado (Ishikawa + lección + acción + fundamento verificado)
KB={
 "Desfavorable":{"label":"Sentencia/Laudo desfavorable","clasif":"Adverso","riesgo":"Alto",
  "causas":["Falta del aviso de rescisión por escrito","Deficiencia probatoria","Documentación incompleta","Contestación extemporánea","Ausencia de testigos","Error en estrategia procesal"],
  "leccion":"Todo procedimiento de rescisión laboral debe incorporar AVISO DE RESCISIÓN por escrito y constancia de notificación, con expediente probatorio integrado.",
  "accion":"Checklist obligatorio de rescisión + capacitación + formato único de aviso (ver memo de prevención).",
  "factor":"Interno (la UdeG pudo prevenirlo)","evit":"Evitable","rep":"Alta",
  "fund":"LFT arts. 47 (rescisión; sin aviso → injustificado), 48 (reinstalación o indemnización 3 meses + salarios vencidos topados 12 meses), 50; art. 123-A fr. XXII const.","verif":"verificado"},
 "Desechó":{"label":"Desechamiento","clasif":"Éxito UdeG","riesgo":"Bajo",
  "causas":["Improcedencia manifiesta","Presentación extemporánea","Falta de interés jurídico","Acto inexistente"],
  "leccion":"Fortalecer revisión de procedencia y cómputo de plazos antes de presentar.","accion":"Checklist previo a la presentación.",
  "factor":"Externo/mixto","evit":"No evitable","rep":"Baja","fund":"Ley de Amparo arts. 17-18 (plazos) y 113 (desechamiento por motivo manifiesto e indudable de improcedencia).","verif":"verificado"},
 "Sobresee":{"label":"Sobreseimiento","clasif":"Éxito UdeG","riesgo":"Bajo",
  "causas":["Actualización de causal de improcedencia","Cese de efectos del acto reclamado","Sin materia"],
  "leccion":"Depurar la procedencia antes de promover y vigilar el cumplimiento para que el acto quede sin materia.","accion":"Revisión de procedencia + seguimiento de cumplimiento.",
  "factor":"Mixto","evit":"Parcialmente evitable","rep":"Media","fund":"Ley de Amparo art. 63 (causales de sobreseimiento); improcedencia art. 61.","verif":"verificado"},
 "Niega":{"label":"Negativa de amparo","clasif":"Éxito UdeG","riesgo":"Bajo",
  "causas":["Conceptos de violación infundados","Acto estimado constitucional/legal"],
  "leccion":"Reforzar agravios, ofrecer y desahogar pruebas idóneas y cuidar la técnica del amparo.","accion":"Plantillas de informe justificado y revisión técnica.",
  "factor":"Externo","evit":"No evitable","rep":"Baja","fund":"Ley de Amparo arts. 74 (requisitos de la sentencia) y 77 (efectos).","verif":"verificado"},
 "Caducidad":{"label":"Caducidad","clasif":"Éxito UdeG (procesal)","riesgo":"Medio",
  "causas":["Inactividad procesal del actor","Falta de promoción en el plazo legal"],
  "leccion":"Vigilar plazos e impulso procesal; atender el requerimiento de los 45 días.","accion":"Tablero de impulso procesal + alertas de inactividad (205 activos ≥18 meses).",
  "factor":"Externo","evit":"No evitable","rep":"Baja","fund":"LFT art. 772 (inactividad 45 días → requerimiento) y 773 (caducidad por falta de promoción en 4 meses).","verif":"verificado"},
 "Desistimiento":{"label":"Desistimiento","clasif":"Éxito UdeG","riesgo":"Bajo",
  "causas":["Desistimiento de la acción","Acuerdo previo / convenio"],
  "leccion":"Documentar si el desistimiento derivó de un convenio favorable.","accion":"Registro del motivo del desistimiento.",
  "factor":"Mixto","evit":"Parcialmente evitable","rep":"Baja","fund":"Ley de Amparo art. 63 fr. I (sobreseimiento por desistimiento).","verif":"verificado"},
 "Ampara y protege":{"label":"Amparo concedido a la contraparte","clasif":"Adverso","riesgo":"Alto",
  "causas":["Acto declarado inconstitucional/ilegal","Falta o deficiencia de fundamentación y motivación del acto","Violación al debido proceso"],
  "leccion":"Fundar y motivar todo acto de autoridad universitaria; respetar el debido proceso.","accion":"Revisión de legalidad previa + capacitación en fundamentación y motivación.",
  "factor":"Interno","evit":"Evitable","rep":"Media","fund":"Ley de Amparo — sentencias que conceden la protección (arts. 73-78, verificar).","verif":"a confirmar"},
 "Favorable":{"label":"Sentencia/Laudo favorable","clasif":"Éxito UdeG","riesgo":"Bajo",
  "causas":["Defensa sólida","Expediente probatorio integrado"],
  "leccion":"Replicar las buenas prácticas de integración probatoria y defensa.","accion":"Documentar el caso como precedente interno.",
  "factor":"Interno","evit":"—","rep":"Baja","fund":"LFT / Ley de Amparo según vía.","verif":"a confirmar"},
 "Por Convenio":{"label":"Convenio / Conciliación","clasif":"Parcialmente favorable","riesgo":"Medio",
  "causas":["Solución negociada (MASC)"],
  "leccion":"Evaluar conciliación temprana en asuntos de alto riesgo para acotar condena.","accion":"Protocolo MASC y criterios de transacción.",
  "factor":"Mixto","evit":"—","rep":"Media","fund":"LFT (convenios) y MASC; ratificación ante autoridad.","verif":"a confirmar"},
 "Incompetencia":{"label":"Incompetencia","clasif":"Neutro","riesgo":"Medio",
  "causas":["Falta de competencia del órgano","Vía incorrecta"],
  "leccion":"Verificar competencia y vía antes de promover.","accion":"Checklist de competencia.","factor":"Mixto","evit":"Parcialmente evitable","rep":"Baja","fund":"Reglas de competencia (verificar).","verif":"a confirmar"},
 "Infundada":{"label":"Acción/recurso infundado","clasif":"Éxito UdeG","riesgo":"Bajo",
  "causas":["Pretensión sin sustento jurídico"],
  "leccion":"Análisis de viabilidad previo (probabilidad de éxito).","accion":"Dictamen de viabilidad.","factor":"Externo","evit":"No evitable","rep":"Baja","fund":"Según la vía (verificar).","verif":"a confirmar"},
}
# checklists preventivos curados por tipo
CHK={
 "Desfavorable":["Aviso de rescisión por escrito entregado, con constancia de notificación","Causa de rescisión encuadrada en una fracción del art. 47 LFT","Expediente probatorio integrado (contrato, funciones, actas, advertencias)","Contestación presentada en tiempo (no extemporánea)","Testigos identificados y disponibles","Estrategia procesal validada por coordinación"],
 "Desechó":["Revisión de procedencia antes de presentar","Verificación del cómputo de plazos (arts. 17-18 Ley de Amparo)","Acreditación del interés jurídico","Confirmación de la existencia del acto reclamado"],
 "Sobresee":["Depurar la procedencia antes de promover","Vigilar el cumplimiento para evitar cese de efectos","Documentar la materia subsistente del juicio"],
 "Niega":["Reforzar conceptos de violación / agravios","Ofrecer y desahogar pruebas idóneas","Revisar la técnica del amparo","Informe justificado con constancias completas"],
 "Caducidad":["Control de plazos e impulso procesal periódico","Atender el requerimiento de los 45 días (art. 772 LFT)","Promover antes de los 4 meses (art. 773 LFT)","Vigilar el tablero de inactividad (alertas)"],
 "Ampara y protege":["Fundar y motivar todo acto de autoridad universitaria","Respetar el debido proceso","Revisión de legalidad previa a la emisión del acto"],
 "Desistimiento":["Documentar el motivo del desistimiento","Verificar si derivó de un convenio favorable a la UdeG"],
 "Por Convenio":["Evaluar conciliación temprana en asuntos de alto riesgo","Cuantificar la exposición antes de transar","Ratificación del convenio ante la autoridad"],
}
# indicios NLP de causa (keywords reales en historial/prestaciones)
CAU={"Aviso de rescisión/despido":re.compile(r"aviso de (rescisi|despido)|sin aviso",re.I),
 "Extemporaneidad":re.compile(r"extempor",re.I),"Reinstalación/indemnización":re.compile(r"reinstalaci|indemnizaci|salarios ca[ií]dos",re.I),
 "Improcedencia":re.compile(r"improceden",re.I),"Inactividad/caducidad":re.compile(r"caducidad|inactividad procesal",re.I),
 "Plazos/cómputo":re.compile(r"\bplazo\b|t[eé]rmino|c[oó]mputo",re.I),"Prueba/probatorio":re.compile(r"prueba|probatori",re.I)}
EXITO={"Favorable","Sobresee","Desechó","Niega","Caducidad","Desistimiento","Infundada"}
out=[]
for sent in collections.Counter(r[SENT].strip() for r in U if r[SENT].strip()):
    grp=[r for r in U if r[SENT].strip()==sent]
    if len(grp)<1:continue
    kb=KB.get(sent,{"label":sent,"clasif":"—","riesgo":"Medio","causas":[],"leccion":"—","accion":"—","factor":"—","evit":"—","rep":"—","fund":"Según la vía (verificar).","verif":"a confirmar"})
    deps=collections.Counter(r[DEP].strip() for r in grp if r[DEP].strip()).most_common(5)
    abos=collections.Counter(r[ABO].strip() for r in grp if r[ABO].strip()).most_common(4)
    monto=sum(NLP.get(r[EXP].strip(),{}).get("monto_max",0) for r in grp)
    yc=collections.Counter()
    for r in grp:
        y=yr(r[EXP])
        if y:yc[y]+=1
    yrs=sorted(yc)
    act=yc[yrs[-1]] if yrs else 0;ant=yc[yrs[-2]] if len(yrs)>1 else 0
    tend=None
    if ant: tend=round(100*(act-ant)/ant)
    causas_nlp=[]
    for nom,rx in CAU.items():
        c=sum(1 for r in grp if rx.search((r[HIST] or "")+" "+(r[PREST] or "")))
        if c: causas_nlp.append([nom,c])
    causas_nlp.sort(key=lambda x:-x[1])
    out.append({"sent":sent,"label":kb["label"],"n":len(grp),"clasif":kb["clasif"],"riesgo":kb["riesgo"],
      "exito":sent in EXITO,"deps":deps,"abogados":abos,"impacto":round(monto),
      "tendencia":tend,"anio_actual":(yrs[-1] if yrs else None),
      "causas_nlp":causas_nlp[:5],"causas_kb":kb["causas"],"leccion":kb["leccion"],"accion":kb["accion"],
      "factor":kb["factor"],"evit":kb["evit"],"rep":kb["rep"],"fund":kb["fund"],"verif":kb["verif"],
      "checklist":CHK.get(sent,["Prevenir: "+c for c in kb["causas"]])})
out.sort(key=lambda x:-x["n"])
json.dump({"tipos":out,"corte":"2026-06-18"},open(OUT+"lecciones_pro.json","w",encoding="utf-8"),ensure_ascii=False)
print("tipos de resultado:",len(out))
for o in out[:6]:print(f"  {o['label']:30} n={o['n']:>3} riesgo={o['riesgo']:8} {o['clasif']:22} impacto ${o['impacto']:,} tend={o['tendencia']}")
