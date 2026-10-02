# -*- coding: utf-8 -*-
# TABLERO CONSOLIDADO DE SEGUIMIENTOS — reúne todas las notas de seguimiento (de módulo y por expediente) de todo el SIGEJ,
# filtrable por módulo, abogado/perfil y fecha. Para revisión de pendientes por la dirección.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Tablero de Seguimientos'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','seguimientos_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html" class="act">🧭 Seguimientos</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Tablero de Seguimientos</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.wrap{max-width:1280px;margin:auto;padding:16px 18px 44px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul2)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px}
input,select{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:8px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:7px 6px;vertical-align:top}
.bdg{padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;background:#eef2f7;color:#0a4d8c}
.bdg.mod{background:#fef3e2;color:#b45309}
a.lk{color:var(--azul2);text-decoration:none}a.lk:hover{text-decoration:underline}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
</style></head><body>
<header><h1>🧭 Tablero consolidado de Seguimientos</h1><div class="s">Todas las notas de seguimiento del sistema (de módulo y por expediente) en un solo lugar · para revisión de pendientes</div></header>
__NAV__
<div class="wrap">
 <div class="kpis" id="kpis"></div>
 <div class="card"><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">
   <div><label style="font-size:11px;color:#64748b">Buscar en texto</label><input id="fq" placeholder="palabra clave…" oninput="render()"></div>
   <div><label style="font-size:11px;color:#64748b">Módulo</label><select id="fmod" onchange="render()"></select></div>
   <div><label style="font-size:11px;color:#64748b">Abogado / perfil</label><select id="fusr" onchange="render()"></select></div>
   <div><label style="font-size:11px;color:#64748b">Desde</label><input id="fd1" type="date" onchange="render()"></div>
   <div><label style="font-size:11px;color:#64748b">Hasta</label><input id="fd2" type="date" onchange="render()"></div>
   <div style="display:flex;align-items:end;gap:6px"><button class="b1 mini" onclick="expCSV()">⬇️ CSV</button><button class="bd mini" onclick="limpiar()">Limpiar</button></div>
 </div></div>
 <div class="grid" style="grid-template-columns:1.3fr 1fr"><div class="card"><b style="color:#0a4d8c">Notas por módulo</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Top abogados / perfiles</b><canvas id="c2" height="150"></canvas></div></div>
 <div class="card" style="overflow:auto"><table><thead><tr><th>Fecha</th><th>Módulo</th><th>Expediente / folio</th><th>Abogado / perfil</th><th>Nota de seguimiento</th></tr></thead><tbody id="tb"></tbody></table><div id="cap" style="font-size:11px;color:#64748b;padding:6px"></div></div>
 <div class="note">🔎 Reúne el seguimiento a nivel <b>módulo</b> (notas del equipo por módulo) y a nivel <b>expediente</b> (notas en cada ficha). La confidencialidad de módulos aislados (p. ej. Solicitud de Convenios) se respeta: aquí solo se muestran notas de seguimiento, no documentos.</div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
/* Fuentes de seguimiento POR EXPEDIENTE: [clave, módulo, ícono, link, folioFn] */
var SRC=[
 ['sigej_instrumentos','Instrumentos Jurídicos','📜','instrumentos_SIGEJ.html',function(e){return e.folio;}],
 ['sigej_serviciosocial','Servicio Social · Convenios','🤝','serviciosocial_SIGEJ.html',function(e){return e.folio+' · '+(e.dependencia||'');}],
 ['sigej_oficios','Oficialía de Partes','📨','oficialia_SIGEJ.html',function(e){return e.folio;}],
 ['sigej_deportivo','Derecho Deportivo','🏅','deportivo_SIGEJ.html',function(e){return e.folio+' · '+(e.tipo||'');}],
 ['sigej_normatividad','Normatividad','📖','normatividad_SIGEJ.html',function(e){return e.folio;}],
 ['sigej_internacional','Asuntos Internacionales','🌎','internacional_SIGEJ.html',function(e){return e.folio;}],
 ['sigej_patrimonio','Patrimonio Intangible','🧩','patrimonio_SIGEJ.html',function(e){return (e.folio||'')+' · '+(e.titulo||'');}]
];
/* nombres amigables para las claves de página del seguimiento por módulo */
var MODNAME={instrumentos_SIGEJ:'Instrumentos',serviciosocial_SIGEJ:'Servicio Social',oficialia_SIGEJ:'Oficialía',deportivo_SIGEJ:'Derecho Deportivo',normatividad_SIGEJ:'Normatividad',internacional_SIGEJ:'Asuntos Internacionales',patrimonio_SIGEJ:'Patrimonio Intangible',administracion_SIGEJ:'Administración',masc_SIGEJ:'MASC',resp_SIGEJ:'Responsabilidades',asesoria_SIGEJ:'Asesoría',proyectos_SIGEJ:'Proyectos',horas_SIGEJ:'Horas',captura_expediente_SIGEJ:'Captura de expedientes',auditorias_SIGEJ:'Auditorías',sostenibilidad_SIGEJ:'Sostenibilidad',gobinv_SIGEJ:'Gobierno de la Investigación',programas_SIGEJ:'Programas',laboratorios_SIGEJ:'Laboratorios',hospitales_SIGEJ:'Hospitales',helpdesk_SIGEJ:'Help Desk',patrimonial_SIGEJ:'Patrimonio Inmobiliario',desarrollo_SIGEJ:'Conocimiento y Desarrollo'};
function loadAll(){var out=[];
 // por expediente
 SRC.forEach(function(s){var arr=J(s[0]);if(!Array.isArray(arr))return;arr.forEach(function(e){(e.seguimiento||[]).forEach(function(n){out.push({ts:n.ts||'',usuario:n.usuario||n.perfil||'(perfil)',texto:n.texto||'',modulo:s[1],ic:s[2],link:s[3],folio:s[4](e),nivel:'expediente'});});});});
 // Contencioso · expedientes (ENR)
 var enr=J('sigej_enr');if(enr&&typeof enr==='object'){Object.keys(enr).forEach(function(num){var en=enr[num];(en&&en.seguimiento||[]).forEach(function(n){out.push({ts:n.ts||'',usuario:n.usuario||n.perfil||'(perfil)',texto:n.texto||'',modulo:'Contencioso · Expedientes',ic:'⚔️',link:'contencioso_SIGEJ.html',folio:num,nivel:'expediente'});});});}
 // por módulo (widget flotante)
 var sm=J('sigej_seguimiento');if(sm&&typeof sm==='object'){Object.keys(sm).forEach(function(pk){(sm[pk]||[]).forEach(function(n){out.push({ts:n.ts||'',usuario:n.usuario||n.perfil||'(perfil)',texto:n.texto||'',modulo:(MODNAME[pk]||pk)+' (módulo)',ic:'📝',link:pk+'.html',folio:'—',nivel:'módulo'});});});}
 out.sort(function(a,b){return (b.ts||'').localeCompare(a.ts||'');});
 return out;}
function render(){var A=loadAll();
 var q=norm(el('fq').value),fm=el('fmod').value,fu=el('fusr').value,d1=el('fd1').value,d2=el('fd2').value;
 // poblar selects (una vez, conservando selección)
 fillSel('fmod',A.map(function(x){return x.modulo;}),fm);fillSel('fusr',A.map(function(x){return x.usuario;}),fu);
 var rows=A.filter(function(x){var f=(x.ts||'').slice(0,10);
   return (!q||norm(x.texto+' '+x.folio+' '+x.modulo+' '+x.usuario).indexOf(q)>=0)&&(!fm||x.modulo===fm)&&(!fu||x.usuario===fu)&&(!d1||f>=d1)&&(!d2||f<=d2);});
 // KPIs
 var mods={},usrs={};A.forEach(function(x){});rows.forEach(function(x){mods[x.modulo]=(mods[x.modulo]||0)+1;usrs[x.usuario]=(usrs[x.usuario]||0)+1;});
 var exp=rows.filter(function(x){return x.nivel==='expediente';}).length;
 el('kpis').innerHTML='<div class="kpi"><div class="n">'+rows.length+'</div><div class="l">Notas (filtro)</div></div>'+
  '<div class="kpi"><div class="n">'+A.length+'</div><div class="l">Notas totales</div></div>'+
  '<div class="kpi"><div class="n">'+exp+'</div><div class="l">Por expediente</div></div>'+
  '<div class="kpi"><div class="n">'+(rows.length-exp)+'</div><div class="l">Por módulo</div></div>'+
  '<div class="kpi"><div class="n">'+Object.keys(mods).length+'</div><div class="l">Módulos con notas</div></div>'+
  '<div class="kpi"><div class="n">'+Object.keys(usrs).length+'</div><div class="l">Autores</div></div>';
 el('tb').innerHTML=rows.length?rows.slice(0,500).map(function(x){return '<tr><td style="white-space:nowrap">'+esc(x.ts)+'</td><td>'+x.ic+' '+esc(x.modulo)+'</td><td style="font-size:11.5px"><a class="lk" href="'+x.link+'">'+esc(x.folio)+'</a></td><td>'+esc(x.usuario)+'</td><td>'+esc(x.texto)+'</td></tr>';}).join(''):'<tr><td colspan="5" style="text-align:center;color:#64748b;padding:16px">Sin notas con estos filtros.</td></tr>';
 el('cap').textContent=(rows.length>500?'Mostrando 500 de '+rows.length+'. Afina el filtro o exporta el CSV.':rows.length+' nota(s).');
 drawCharts(mods,usrs);
}
function fillSel(id,vals,cur){var e=el(id);if(e.getAttribute('data-n')==='1'&&e.value!==''){}var u=[];vals.forEach(function(v){if(v&&u.indexOf(v)<0)u.push(v);});u.sort();
 e.innerHTML='<option value="">Todos</option>'+u.map(function(v){return '<option'+(v===cur?' selected':'')+'>'+esc(v)+'</option>';}).join('');e.setAttribute('data-n','1');}
function drawCharts(mods,usrs){try{
 var mk=Object.keys(mods).sort(function(a,b){return mods[b]-mods[a];}).slice(0,10);
 if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'bar',data:{labels:mk.map(function(k){return k.length>20?k.slice(0,20)+'…':k;}),datasets:[{data:mk.map(function(k){return mods[k];}),backgroundColor:'#0a4d8c'}]},options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{y:{ticks:{font:{size:8}}}}}});
 var uk=Object.keys(usrs).sort(function(a,b){return usrs[b]-usrs[a];}).slice(0,8);
 if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:uk,datasets:[{data:uk.map(function(k){return usrs[k];}),backgroundColor:'#1aa39a'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}}
function limpiar(){['fq','fmod','fusr','fd1','fd2'].forEach(function(i){el(i).value='';});render();}
function expCSV(){var A=loadAll();var q=norm(el('fq').value),fm=el('fmod').value,fu=el('fusr').value,d1=el('fd1').value,d2=el('fd2').value;
 var rows=A.filter(function(x){var f=(x.ts||'').slice(0,10);return (!q||norm(x.texto+' '+x.folio+' '+x.modulo+' '+x.usuario).indexOf(q)>=0)&&(!fm||x.modulo===fm)&&(!fu||x.usuario===fu)&&(!d1||f>=d1)&&(!d2||f<=d2);});
 var out=[['Fecha','Modulo','Expediente/folio','Autor','Nota','Nivel']].concat(rows.map(function(x){return [x.ts,x.modulo,x.folio,x.usuario,x.texto,x.nivel];}));
 var csv=out.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='seguimientos_'+new Date().toISOString().slice(0,10)+'.csv';a.click();}
render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{background:#fff!important}.wrap{padding-top:8px!important}";document.head.appendChild(st);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"seguimientos_SIGEJ.html","w",encoding="utf-8").write(out)
print("seguimientos_SIGEJ.html OK -",len(out),"bytes | fuentes por-expediente:",out.count("_SIGEJ.html',function(e)"))
