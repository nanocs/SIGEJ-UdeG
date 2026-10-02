# -*- coding: utf-8 -*-
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"
NAV_OLD='<a href="transparencia_SIGEJ.html">🔎 Transparencia</a>'
NAV_NEW='<a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a>'
PERM=[
 ("'transparencia_SIGEJ'","'transparencia_general_SIGEJ','transparencia_SIGEJ'"),
 ("'notificaciones_SIGEJ','chat_SIGEJ']","'notificaciones_SIGEJ','chat_SIGEJ','transparencia_general_SIGEJ']"),
]
CARD_OLD='<a class="app a2" href="transparencia_SIGEJ.html"><div class="ic">🔎</div><h3>Transparencia</h3><p>Buscador flexible para solicitudes UTI (14 filtros, cuantía), registro consultable por folio y oficio de respuesta en Word.</p><div class="go">Abrir transparencia →</div></a>'
CARD_NEW='<a class="app a2" href="transparencia_general_SIGEJ.html"><div class="ic">📊</div><h3>Transparencia General</h3><p>Rendición de cuentas institucional: buscador global sobre TODOS los módulos y áreas, estadísticas, matrices, reportes consolidados (Word/CSV) y las solicitudes UTI integradas.</p><div class="go">Abrir transparencia general →</div></a>'

targets=['inicio','ejecutivo','html','instrumentos','portal','patrimonio','internacional','normatividad',
 'contencioso','buscador','reportes','horas','oficialia','chat','notif','bitacora']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;cd=0;pm=0
    if name=='inicio':
        if CARD_OLD in s and 'transparencia_general_SIGEJ.html' not in s:s=s.replace(CARD_OLD,CARD_NEW);cd=1
    else:
        if NAV_OLD in s:s=s.replace(NAV_OLD,NAV_NEW);nv=1
    for a,b in PERM:
        if a in s:pm+=s.count(a);s=s.replace(a,b)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} nav:{nv} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'} {out.stdout.strip()[:30]}{out.stderr.strip()[:120]}")

sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read();so=ss
for a,b in PERM:ss=ss.replace(a,b)
if ss!=so:open(sf,"w",encoding="utf-8").write(ss);print("_acceso_snippet.html sincronizado")
