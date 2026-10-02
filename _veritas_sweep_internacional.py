# -*- coding: utf-8 -*-
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"
NAV_PLAIN='<a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a>'
NAV_ACT='<a href="patrimonio_SIGEJ.html" class="act">🧩 Patrimonio Intangible</a>'
LINK='<a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a>'
PERM_OLD="'patrimonio_SIGEJ','portal_SIGEJ'"
PERM_NEW="'patrimonio_SIGEJ','internacional_SIGEJ','portal_SIGEJ'"
CARD_OLD='<a class="app a2" href="patrimonio_SIGEJ.html"><div class="ic">🧩</div><h3>Patrimonio Intangible (IPMS/TTO)</h3><p>Gestión de propiedad intelectual: patentes, marcas, derecho de autor, variedades vegetales, software y activos digitales; expediente electrónico, flujos por trámite, vigencias, titularidad, transferencia tecnológica (TRL), regalías y observancia. Art. 220 RIAG-UdeG.</p><div class="go">Abrir patrimonio →</div></a>'
CARD_NEW=CARD_OLD+'<a class="app a3" href="internacional_SIGEJ.html"><div class="ic">🌎</div><h3>Asuntos Internacionales</h3><p>Global Mobility e immigration case management: derecho migratorio MX e internacional (visas, condición de estancia), movilidad del personal UdeG, convenios internacionales, traducción jurídica, riesgo internacional y conocimiento. Art. 221 RIAG-UdeG.</p><div class="go">Abrir asuntos internacionales →</div></a>'

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental','ejecutivo',
 'horas','html','instrumentos','masc','modulo','notif','oficialia','patrimonio','portal','proyectos','reportes','resp','transp','inicio']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;cd=0;pm=0
    if name=='inicio':
        if CARD_OLD in s and 'internacional_SIGEJ.html' not in s:s=s.replace(CARD_OLD,CARD_NEW);cd=1
    else:
        if 'internacional_SIGEJ.html' not in s.split('class="navbar"')[1].split('</div>')[0]:
            if NAV_PLAIN in s:s=s.replace(NAV_PLAIN,NAV_PLAIN+LINK,1);nv=1
            elif NAV_ACT in s:s=s.replace(NAV_ACT,NAV_ACT+LINK,1);nv=1
    if PERM_OLD in s:pm=s.count(PERM_OLD);s=s.replace(PERM_OLD,PERM_NEW)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} nav:{nv} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'}  {out.stdout.strip()[:34]}{out.stderr.strip()[:120]}")

sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read()
if PERM_OLD in ss:open(sf,"w",encoding="utf-8").write(ss.replace(PERM_OLD,PERM_NEW));print("_acceso_snippet.html sincronizado")
