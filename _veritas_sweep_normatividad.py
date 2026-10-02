# -*- coding: utf-8 -*-
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"
NAV_PLAIN='<a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a>'
NAV_ACT='<a href="internacional_SIGEJ.html" class="act">🌎 Asuntos Internacionales</a>'
LINK='<a href="normatividad_SIGEJ.html">📖 Normatividad</a>'
PERM_OLD="'internacional_SIGEJ','portal_SIGEJ'"
PERM_NEW="'internacional_SIGEJ','normatividad_SIGEJ','portal_SIGEJ'"
CARD_OLD='<a class="app a3" href="internacional_SIGEJ.html"><div class="ic">🌎</div><h3>Asuntos Internacionales</h3><p>Global Mobility e immigration case management: derecho migratorio MX e internacional (visas, condición de estancia), movilidad del personal UdeG, convenios internacionales, traducción jurídica, riesgo internacional y conocimiento. Art. 221 RIAG-UdeG.</p><div class="go">Abrir asuntos internacionales →</div></a>'
CARD_NEW=CARD_OLD+'<a class="app a4" href="normatividad_SIGEJ.html"><div class="ic">📖</div><h3>Normatividad Universitaria</h3><p>Coordinación de Normatividad: técnica legislativa (cuadros comparativos, dictámenes), estatutos y reglamentos, repositorio normativo con historia de reformas, órganos colegiados (CGU), responsabilidades universitarias, desincorporación de bienes y observatorio legislativo. Arts. 224-227 RIAG-UdeG.</p><div class="go">Abrir normatividad →</div></a>'

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental','ejecutivo',
 'horas','html','instrumentos','internacional','masc','modulo','notif','oficialia','patrimonio','portal','proyectos','reportes','resp','transp','inicio']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;cd=0;pm=0
    if name=='inicio':
        if CARD_OLD in s and 'normatividad_SIGEJ.html' not in s:s=s.replace(CARD_OLD,CARD_NEW);cd=1
    else:
        if 'normatividad_SIGEJ.html' not in s.split('class="navbar"')[1].split('</div>')[0]:
            if NAV_PLAIN in s:s=s.replace(NAV_PLAIN,NAV_PLAIN+LINK,1);nv=1
            elif NAV_ACT in s:s=s.replace(NAV_ACT,NAV_ACT+LINK,1);nv=1
    if PERM_OLD in s:pm=s.count(PERM_OLD);s=s.replace(PERM_OLD,PERM_NEW)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} nav:{nv} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'}  {out.stdout.strip()[:32]}{out.stderr.strip()[:120]}")

sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read()
if PERM_OLD in ss:open(sf,"w",encoding="utf-8").write(ss.replace(PERM_OLD,PERM_NEW));print("_acceso_snippet.html sincronizado")
