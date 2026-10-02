# -*- coding: utf-8 -*-
import subprocess,re
B="/Users/edithroque/Documents/CLAUDE/"
DEL=[
 '<a href="masc_SIGEJ.html">🤝 MASC</a>',
 '<a href="resp_SIGEJ.html">⚖️ Responsabilidades</a>',
 '<a href="alertas_centro_SIGEJ.html">🔔 Alertas</a>',
 '<a href="abogados_SIGEJ.html">👤 Abogados</a>',
 '<a href="documental_SIGEJ.html">🗂️ Documental</a>',
 '<a href="captura_expediente_SIGEJ.html">➕ Captura</a>',
 '<a href="modulo_expedientes_SIGEJ.html">📁 Expedientes</a>',
 '<a href="asesoria_SIGEJ.html">💡 Asesoría</a>',
 '<a href="proyectos_SIGEJ.html">📌 Proyectos</a>',
]
NAV_PLAIN='<a href="normatividad_SIGEJ.html">📖 Normatividad</a>'
NAV_ACT='<a href="normatividad_SIGEJ.html" class="act">📖 Normatividad</a>'
LINK='<a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a>'
PERM=[
 ("'normatividad_SIGEJ','portal_SIGEJ'","'normatividad_SIGEJ','contencioso_SIGEJ','portal_SIGEJ'"),
 ("'oficialia_SIGEJ','modulo_expedientes_SIGEJ','portal_SIGEJ'","'oficialia_SIGEJ','contencioso_SIGEJ','modulo_expedientes_SIGEJ','portal_SIGEJ'"),
]
CARD_OLD='<a class="app a4" href="normatividad_SIGEJ.html"><div class="ic">📖</div><h3>Normatividad Universitaria</h3><p>Coordinación de Normatividad: técnica legislativa (cuadros comparativos, dictámenes), estatutos y reglamentos, repositorio normativo con historia de reformas, órganos colegiados (CGU), responsabilidades universitarias, desincorporación de bienes y observatorio legislativo. Arts. 224-227 RIAG-UdeG.</p><div class="go">Abrir normatividad →</div></a>'
CARD_NEW=CARD_OLD+'<a class="app" href="contencioso_SIGEJ.html"><div class="ic">⚔️</div><h3>Asuntos Contenciosos</h3><p>Módulo unificado: todos los juicios y litigios de la UdeG, MASC, responsabilidades administrativas, centro de alertas, seguimiento por abogado, estructura documental, captura, expedientes, asesoría y proyectos.</p><div class="go">Abrir asuntos contenciosos →</div></a>'
CARD_DEL=['masc','resp','alertas_centro','abogados','documental','captura_expediente','modulo_expedientes','asesoria','proyectos']

# módulos que PERMANECEN en navbar (se barren); excluye los 9 retirados, los 3 legados y el nuevo
targets=['inicio','ejecutivo','html','instrumentos','portal','patrimonio','internacional','normatividad',
 'buscador','reportes','horas','transp','oficialia','chat','notif','bitacora']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s;nv=0;cd=0;pm=0
    if name=='inicio':
        for h in CARD_DEL:
            s2=re.sub(r'<a class="app[^"]*" href="'+h+'_SIGEJ\.html">.*?</a>','',s)
            if s2!=s:cd+=1;s=s2
        if CARD_OLD in s and 'contencioso_SIGEJ.html' not in s:s=s.replace(CARD_OLD,CARD_NEW)
    else:
        for d in DEL:
            if d in s:s=s.replace(d,'');nv+=1
        if 'contencioso_SIGEJ.html' not in s.split('class="navbar"')[1].split('</div>')[0]:
            if NAV_PLAIN in s:s=s.replace(NAV_PLAIN,NAV_PLAIN+LINK,1)
            elif NAV_ACT in s:s=s.replace(NAV_ACT,NAV_ACT+LINK,1)
    for a,b in PERM:
        if a in s:pm+=s.count(a);s=s.replace(a,b)
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} navdel:{nv} carddel:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'} {out.stdout.strip()[:32]}{out.stderr.strip()[:120]}")

sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read();so=ss
for a,b in PERM:ss=ss.replace(a,b)
if ss!=so:open(sf,"w",encoding="utf-8").write(ss);print("_acceso_snippet.html sincronizado")
