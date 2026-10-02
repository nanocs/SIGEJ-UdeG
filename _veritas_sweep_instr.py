# -*- coding: utf-8 -*-
# Integra el módulo Instrumentos Jurídicos en navbar (tras Expedientes), inicio y permisos (equipo jurídico).
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"

NAV_OLD='<a href="modulo_expedientes_SIGEJ.html">📁 Expedientes</a>'
NAV_NEW=NAV_OLD+'<a href="instrumentos_SIGEJ.html">📜 Instrumentos</a>'
PERM_OLD="'modulo_expedientes_SIGEJ','captura_expediente_SIGEJ'"
PERM_NEW="'modulo_expedientes_SIGEJ','instrumentos_SIGEJ','captura_expediente_SIGEJ'"
CARD_OLD='<a class="app a3" href="modulo_expedientes_SIGEJ.html"><div class="ic">📁</div><h3>Módulo de Expedientes</h3><p>Consulta con 7 filtros, ficha completa, documentos digitalizados, pruebas, agenda, Kanban movible, Gantt y NLP por expediente.</p><div class="go">Abrir módulo →</div></a>'
CARD_NEW=CARD_OLD+'<a class="app a2" href="instrumentos_SIGEJ.html"><div class="ic">📜</div><h3>Instrumentos Jurídicos (CLM)</h3><p>Legal ERP / Contract Lifecycle Management: convenios, contratos e instrumentos especiales con ciclo de vida, matriz de competencias OAG/CGRH/CGSAIT, expediente electrónico, riesgos, obligaciones, alertas y cláusuloteca.</p><div class="go">Abrir instrumentos →</div></a>'

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental','ejecutivo',
 'horas','html','masc','modulo','oficialia','proyectos','reportes','resp','transp','inicio']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;pm=0;cd=0
    if name=='inicio':
        if CARD_OLD in s:s=s.replace(CARD_OLD,CARD_NEW);cd=1
    else:
        if NAV_OLD in s and 'instrumentos_SIGEJ.html' not in s.split('class="navbar"')[1].split('</div>')[0]:
            s=s.replace(NAV_OLD,NAV_NEW,1);nv=1
    pm=s.count(PERM_OLD)
    if PERM_OLD in s:s=s.replace(PERM_OLD,PERM_NEW)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} nav:{nv} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'}  {out.stdout.strip()[:42]}{out.stderr.strip()[:120]}")

# sincroniza snippet de acceso standalone
sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read()
if PERM_OLD in ss:open(sf,"w",encoding="utf-8").write(ss.replace(PERM_OLD,PERM_NEW));print("_acceso_snippet.html sincronizado")
