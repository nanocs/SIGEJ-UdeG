# -*- coding: utf-8 -*-
# MÓDULO CONTENEDOR: Gestión Jurídica Especializada — agrupa (embebe) Gobierno de la Investigación, Programas Académicos, Laboratorios y Hospitales.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Gestión'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','gestion_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="gestion_SIGEJ.html" class="act">🗂️ Gestión</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Gestión Jurídica Especializada</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:#0a1f3c}
header{background:linear-gradient(120deg,#0b2540,#24476f);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabbar{display:flex;gap:6px;flex-wrap:wrap;padding:12px 18px 0;max-width:1320px;margin:auto}
.tb{padding:10px 14px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:13px;color:#334155}
.tb.on{background:#24476f;color:#fff;font-weight:700}
.wrap{max-width:1320px;margin:auto;padding:0 18px 30px}
.ct{display:none}.ct.on{display:block}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:12px 0}
iframe{width:100%;height:86vh;border:1px solid var(--line);border-radius:0 12px 12px 12px;background:#eef2f7}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:10px}
</style></head><body>
<header><h1>🗂️ Gestión Jurídica Especializada</h1><div class="s">Investigación · Programas Académicos · Laboratorios · Hospitales — con trazabilidad a Oficialía de Partes y Transparencia</div></header>
__NAV__
<div class="tabbar" id="tabbar"></div>
<div class="wrap"><div id="secs"></div>
 <div class="note">🔗 Cada gestión deja constancia en la <b>bitácora de auditoría (Transparencia General)</b> y puede recibir turnos desde <b>Oficialía de Partes</b>. El registro captado queda como antecedente en su módulo.</div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const TABS=[
 ['g1','🔬 Gobierno de la Investigación','gobinv_SIGEJ.html?embed=1'],
 ['g2','🎓 Programas Académicos','programas_SIGEJ.html?embed=1'],
 ['g3','🧪 Laboratorios','laboratorios_SIGEJ.html?embed=1'],
 ['g4','🏥 Hospitales y Salud','hospitales_SIGEJ.html?embed=1'],
 ['g5','🏅 Derecho Deportivo','deportivo_SIGEJ.html?embed=1']
];
document.getElementById('tabbar').innerHTML=TABS.map((t,i)=>'<button class="tb'+(i===0?' on':'')+'" data-t="'+t[0]+'" onclick="tab(\''+t[0]+'\')">'+t[1]+'</button>').join('');
document.getElementById('secs').innerHTML=TABS.map((t,i)=>'<section id="'+t[0]+'" class="ct'+(i===0?' on':'')+'"><iframe id="if_'+t[0]+'" data-src="'+t[2]+'" title="'+t[1]+'"'+(i===0?' src="'+t[2]+'"':'')+'></iframe></section>').join('');
function tab(id){document.querySelectorAll('.ct').forEach(s=>s.classList.toggle('on',s.id===id));
 document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 const fr=document.getElementById('if_'+id);if(fr&&!fr.src)fr.src=fr.dataset.src;}
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"gestion_SIGEJ.html","w",encoding="utf-8").write(out)
print("gestion_SIGEJ.html OK -",len(out),"bytes")
