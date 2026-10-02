# -*- coding: utf-8 -*-
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"
NAV_PLAIN='<a href="alertas_centro_SIGEJ.html">🔔 Alertas</a>'
NAV_ACT='<a href="alertas_centro_SIGEJ.html" class="act">🔔 Alertas</a>'
LINK='<a href="notificaciones_SIGEJ.html">📬 Notificaciones</a>'
PERM_OLD="'alertas_centro_SIGEJ','chat_SIGEJ'"
PERM_NEW="'alertas_centro_SIGEJ','notificaciones_SIGEJ','chat_SIGEJ'"
CARD_OLD='<a class="app" href="alertas_centro_SIGEJ.html"><div class="ic">🔔</div><h3>Centro de Alertas</h3><p>Bandeja unificada de vencimientos: audiencias/términos, parcialidades MASC, prescripción de responsabilidades y riesgo de caducidad, por urgencia.</p><div class="go">Abrir alertas →</div></a>'
CARD_NEW=CARD_OLD+'<a class="app a4" href="notificaciones_SIGEJ.html"><div class="ic">📬</div><h3>Centro de Notificaciones</h3><p>Bandeja personal por perfil: tus aprobaciones, firmas pendientes, vencimientos, obligaciones, agenda, MASC y prescripción — unificadas de toda la suite, con marcado de leídas.</p><div class="go">Abrir notificaciones →</div></a>'

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental','ejecutivo',
 'horas','html','instrumentos','masc','modulo','oficialia','portal','proyectos','reportes','resp','transp','inicio']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;cd=0;pm=0
    if name=='inicio':
        if CARD_OLD in s and 'notificaciones_SIGEJ.html' not in s:s=s.replace(CARD_OLD,CARD_NEW);cd=1
    else:
        if 'notificaciones_SIGEJ.html' not in s.split('class="navbar"')[1].split('</div>')[0]:
            if NAV_PLAIN in s:s=s.replace(NAV_PLAIN,NAV_PLAIN+LINK,1);nv=1
            elif NAV_ACT in s:s=s.replace(NAV_ACT,NAV_ACT+LINK,1);nv=1
    if PERM_OLD in s:pm=s.count(PERM_OLD);s=s.replace(PERM_OLD,PERM_NEW)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} nav:{nv} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'}  {out.stdout.strip()[:38]}{out.stderr.strip()[:120]}")

sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read()
if PERM_OLD in ss:open(sf,"w",encoding="utf-8").write(ss.replace(PERM_OLD,PERM_NEW));print("_acceso_snippet.html sincronizado")
