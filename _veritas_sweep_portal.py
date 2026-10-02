# -*- coding: utf-8 -*-
# Integra el Portal de Dependencias y Contrapartes en navbar (tras Instrumentos), inicio y permisos.
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"

NAV_PLAIN='<a href="instrumentos_SIGEJ.html">📜 Instrumentos</a>'
NAV_ACT='<a href="instrumentos_SIGEJ.html" class="act">📜 Instrumentos</a>'
PORTAL_LINK='<a href="portal_SIGEJ.html">🌐 Portal</a>'
PERM=[
 ("'instrumentos_SIGEJ','captura_expediente_SIGEJ'","'instrumentos_SIGEJ','portal_SIGEJ','captura_expediente_SIGEJ'"),
 ("'modulo_expedientes_SIGEJ','alertas_centro_SIGEJ'","'modulo_expedientes_SIGEJ','portal_SIGEJ','alertas_centro_SIGEJ'"),
]
CARD_OLD='<a class="app a2" href="instrumentos_SIGEJ.html"><div class="ic">📜</div><h3>Instrumentos Jurídicos (CLM)</h3><p>Legal ERP / Contract Lifecycle Management: convenios, contratos e instrumentos especiales con ciclo de vida, matriz de competencias OAG/CGRH/CGSAIT, expediente electrónico, riesgos, obligaciones, alertas y cláusuloteca.</p><div class="go">Abrir instrumentos →</div></a>'
CARD_NEW=CARD_OLD+'<a class="app a3" href="portal_SIGEJ.html"><div class="ic">🌐</div><h3>Portal de Dependencias y Contrapartes</h3><p>Autoservicio: las dependencias solicitan instrumentos y dan seguimiento; las contrapartes consultan estado, suben documentos y firman electrónicamente (simulado). Comparte el expediente con el CLM.</p><div class="go">Abrir portal →</div></a>'

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental','ejecutivo',
 'horas','html','instrumentos','masc','modulo','oficialia','proyectos','reportes','resp','transp','inicio']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;cd=0;pm=0
    if name=='inicio':
        if CARD_OLD in s and 'portal_SIGEJ.html' not in s:s=s.replace(CARD_OLD,CARD_NEW);cd=1
    else:
        if 'portal_SIGEJ.html' not in s.split('class="navbar"')[1].split('</div>')[0]:
            if NAV_PLAIN in s:s=s.replace(NAV_PLAIN,NAV_PLAIN+PORTAL_LINK,1);nv=1
            elif NAV_ACT in s:s=s.replace(NAV_ACT,NAV_ACT+PORTAL_LINK,1);nv=1
    for a,b in PERM:
        if a in s:pm+=s.count(a);s=s.replace(a,b)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} nav:{nv} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'}  {out.stdout.strip()[:40]}{out.stderr.strip()[:120]}")

sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read();so=ss
for a,b in PERM:ss=ss.replace(a,b)
if ss!=so:open(sf,"w",encoding="utf-8").write(ss);print("_acceso_snippet.html sincronizado")
