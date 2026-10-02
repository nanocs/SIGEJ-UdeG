# -*- coding: utf-8 -*-
# Barrido: integra Centro Ejecutivo en navbar + permisos de todos los módulos que permanecen.
# No toca comando/conocimiento/altadir (se preservan en disco, ya integrados en Centro Ejecutivo).
import re
B="/Users/edithroque/Documents/CLAUDE/"

NAV_DEL=[
 '<a href="comando_SIGEJ.html">🛰️ Centro de Mando</a>',
 '<a href="conocimiento_SIGEJ.html">🧠 Inteligencia</a>',
 '<a href="alta_direccion_SIGEJ.html">🎯 Sala de Mando</a>',
]
NAV_INS=('<a href="SIGEJ_inicio.html">🏠 Inicio</a>',
         '<a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a>')

PERM=[
 ("'Jefa de Unidad':['SIGEJ_inicio','comando_SIGEJ','dashboard_SIGEJ','alta_direccion_SIGEJ','modulo_expedientes_SIGEJ','captura_expediente_SIGEJ','horas_SIGEJ','documental_SIGEJ','buscador_SIGEJ','reportes_SIGEJ','asesoria_SIGEJ','proyectos_SIGEJ','conocimiento_SIGEJ','abogados_SIGEJ','oficialia_SIGEJ','masc_SIGEJ','resp_SIGEJ','alertas_centro_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']",
  "'Jefa de Unidad':['SIGEJ_inicio','centro_ejecutivo_SIGEJ','dashboard_SIGEJ','modulo_expedientes_SIGEJ','captura_expediente_SIGEJ','horas_SIGEJ','documental_SIGEJ','buscador_SIGEJ','reportes_SIGEJ','asesoria_SIGEJ','proyectos_SIGEJ','abogados_SIGEJ','oficialia_SIGEJ','masc_SIGEJ','resp_SIGEJ','alertas_centro_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']"),
 ("'Abogado':['SIGEJ_inicio','comando_SIGEJ','dashboard_SIGEJ','modulo_expedientes_SIGEJ','captura_expediente_SIGEJ','horas_SIGEJ','documental_SIGEJ','buscador_SIGEJ','reportes_SIGEJ','asesoria_SIGEJ','proyectos_SIGEJ','conocimiento_SIGEJ','masc_SIGEJ','alertas_centro_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']",
  "'Abogado':['SIGEJ_inicio','dashboard_SIGEJ','modulo_expedientes_SIGEJ','captura_expediente_SIGEJ','horas_SIGEJ','documental_SIGEJ','buscador_SIGEJ','reportes_SIGEJ','asesoria_SIGEJ','proyectos_SIGEJ','masc_SIGEJ','alertas_centro_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']"),
 ("'Auxiliar jurídico':['SIGEJ_inicio','modulo_expedientes_SIGEJ','captura_expediente_SIGEJ','horas_SIGEJ','documental_SIGEJ','buscador_SIGEJ','reportes_SIGEJ','asesoria_SIGEJ','proyectos_SIGEJ','conocimiento_SIGEJ','oficialia_SIGEJ','alertas_centro_SIGEJ','chat_SIGEJ']",
  "'Auxiliar jurídico':['SIGEJ_inicio','modulo_expedientes_SIGEJ','captura_expediente_SIGEJ','horas_SIGEJ','documental_SIGEJ','buscador_SIGEJ','reportes_SIGEJ','asesoria_SIGEJ','proyectos_SIGEJ','oficialia_SIGEJ','alertas_centro_SIGEJ','chat_SIGEJ']"),
 ("'Consulta':['SIGEJ_inicio','comando_SIGEJ','dashboard_SIGEJ','alta_direccion_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']",
  "'Consulta':['SIGEJ_inicio','dashboard_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']"),
]

# Tarjetas de inicio (sin navbar)
INICIO_CARDS=[
 ('<a class="app a4" href="comando_SIGEJ.html"><div class="ic">🛰️</div><h3>Centro de Mando Inteligente</h3><p>Cuadro de mando AUTOACTUALIZABLE: recalcula en vivo con toda captura o modificación (nuevos expedientes, cambios de estado, MASC, responsabilidades). Sin actualizaciones manuales.</p><div class="go">Abrir centro de mando →</div></a>',
  '<a class="app a4" href="centro_ejecutivo_SIGEJ.html"><div class="ic">🧭</div><h3>Centro Ejecutivo</h3><p>Módulo unificado de dirección: Centro de Mando autoactualizable, Cuadro de Mando Integral (BSC), Inteligencia Jurídica y Sala de Mando. Acceso restringido a la dirección.</p><div class="go">Abrir centro ejecutivo →</div></a>'),
 ('<a class="app" href="conocimiento_SIGEJ.html"><div class="ic">🧠</div><h3>Inteligencia Jurídica</h3><p>Legal Analytics + Knowledge Management por tipo de resultado: causa raíz, lección aprendida, checklist preventivo y memo en Word.</p><div class="go">Abrir inteligencia →</div></a>',''),
 ('<a class="app a2" href="alta_direccion_SIGEJ.html"><div class="ic">🎯</div><h3>Sala de Mando</h3><p>Módulo de Alta Dirección: las 8 preguntas directivas en tiempo real (activos, litigiosidad, riesgo, pasivo, carga, tasa de éxito, atención inmediata).</p><div class="go">Abrir sala de mando →</div></a>',''),
]

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental',
 'horas','html','masc','modulo','oficialia','proyectos','reportes','resp','transp','inicio']

import subprocess
for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s
    rep={'navdel':0,'navins':0,'perm':0,'card':0}
    if name!='inicio':
        for d in NAV_DEL:
            if d in s:s=s.replace(d,'');rep['navdel']+=1
        if NAV_INS[0] in s:
            s=s.replace(NAV_INS[0],NAV_INS[1]);rep['navins']+=1
    else:
        for a,b in INICIO_CARDS:
            if a in s:s=s.replace(a,b);rep['card']+=1
    for a,b in PERM:
        if a in s:s=s.replace(a,b);rep['perm']+=1
    if s!=orig:
        open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    ok=out.returncode==0
    print(f"{name:10s} navdel:{rep['navdel']} navins:{rep['navins']} card:{rep['card']} perm:{rep['perm']} run:{'OK' if ok else 'ERR'}  {out.stdout.strip()[:50]}{out.stderr.strip()[:120]}")

# sincroniza snippet de acceso standalone
sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read();so=ss
for a,b in PERM:
    ss=ss.replace(a,b)
if ss!=so:open(sf,"w",encoding="utf-8").write(ss);print("_acceso_snippet.html sincronizado")
