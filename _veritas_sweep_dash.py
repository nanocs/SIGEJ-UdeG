# -*- coding: utf-8 -*-
# Retira el Dashboard de la navbar y de los perfiles operativos (queda exclusivo de dirección,
# integrado en Centro Ejecutivo). Jefa de Unidad lo conserva (es dirección). No borra dashboard_SIGEJ.html.
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"

NAV_DEL='<a href="dashboard_SIGEJ.html">📊 Dashboard</a>'
PERM=[
 ("'Abogado':['SIGEJ_inicio','dashboard_SIGEJ','modulo_expedientes_SIGEJ'",
  "'Abogado':['SIGEJ_inicio','modulo_expedientes_SIGEJ'"),
 ("'Consulta':['SIGEJ_inicio','dashboard_SIGEJ','chat_SIGEJ','transparencia_SIGEJ']",
  "'Consulta':['SIGEJ_inicio','chat_SIGEJ','transparencia_SIGEJ']"),
]
INICIO=[
 ('<a class="app" href="dashboard_SIGEJ.html"><div class="ic">📊</div><h3>Cuadro de Mando Integral</h3><p>12 vistas: ejecutivo, litigios, productividad, desempeño, equidad, provisión, tiempos/cuellos, agenda, alertas, lecciones, riesgos y gobierno de datos.</p><div class="go">Abrir dashboard →</div></a>',''),
 ('<a class="app a4" href="centro_ejecutivo_SIGEJ.html"><div class="ic">🧭</div><h3>Centro Ejecutivo</h3><p>Módulo unificado de dirección: Centro de Mando autoactualizable, Cuadro de Mando Integral (BSC), Inteligencia Jurídica y Sala de Mando. Acceso restringido a la dirección.</p><div class="go">Abrir centro ejecutivo →</div></a>',
  '<a class="app a4" href="centro_ejecutivo_SIGEJ.html"><div class="ic">🧭</div><h3>Centro Ejecutivo</h3><p>Módulo unificado de dirección: Dashboard completo (12 vistas), Centro de Mando autoactualizable, Cuadro de Mando Integral (BSC), Inteligencia Jurídica y Sala de Mando. Acceso restringido a la dirección.</p><div class="go">Abrir centro ejecutivo →</div></a>'),
]

targets=['abogados','alertas','asesoria','bitacora','buscador','captura','chat','documental',
 'horas','html','masc','modulo','oficialia','proyectos','reportes','resp','transp','inicio']

for name in targets:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read();orig=s
    nd=0;pm=0;cd=0
    if name!='inicio':
        if NAV_DEL in s:s=s.replace(NAV_DEL,'');nd=s.count;nd=1
    else:
        for a,b in INICIO:
            if a in s:s=s.replace(a,b);cd+=1
    for a,b in PERM:
        if a in s:s=s.replace(a,b);pm+=1
    if s!=orig:open(f,"w",encoding="utf-8").write(s)
    out=subprocess.run(["python3",f],capture_output=True,text=True)
    print(f"{name:10s} navdash:{nd} card:{cd} perm:{pm} run:{'OK' if out.returncode==0 else 'ERR'}  {out.stdout.strip()[:46]}{out.stderr.strip()[:120]}")

# rebuild Centro Ejecutivo (ya editado: pestaña Dashboard + navbar sin Dashboard)
out=subprocess.run(["python3",B+"_veritas_build_ejecutivo.py"],capture_output=True,text=True)
print("ejecutivo  run:",'OK' if out.returncode==0 else 'ERR',out.stdout.strip()[:60],out.stderr.strip()[:120])

# sincroniza snippet de acceso standalone
sf=B+"_acceso_snippet.html";ss=open(sf,encoding="utf-8").read();so=ss
for a,b in PERM:ss=ss.replace(a,b)
if ss!=so:open(sf,"w",encoding="utf-8").write(ss);print("_acceso_snippet.html sincronizado")
