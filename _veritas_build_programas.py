# -*- coding: utf-8 -*-
# MÓDULO: Gestión Jurídica de Programas Académicos (Onda 2 · #3, cierra la onda).
# Ciclo de vida jurídico de programas educativos: creación / modificación / actualización / supresión / reacreditación,
# dictamen del CGU (comisiones), registro RPE (interno UdeG), y RVOE (federal, N/A por autonomía). Enlaza con Normatividad (CGU).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Programas Académicos'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','programas_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="programas_SIGEJ.html" class="act">🎓 Programas Académicos</a><a href="normatividad_SIGEJ.html">📖 Normatividad (CGU)</a><a href="gobinv_SIGEJ.html">🔬 Investigación</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Gestión Jurídica de Programas Académicos</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:var(--azul);cursor:pointer;font-size:13px}
.collap>.bd2{padding:12px;display:none}.collap.open>.bd2{display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:9px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bw{background:var(--gold);color:#3a2c05;font-weight:700}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}.bdg.b{background:#e6f0fb;color:#0a4d8c}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.step{display:inline-block;font-size:10.5px;padding:2px 8px;border-radius:10px;margin:1px;background:#eef2f7;color:#64748b}.step.on{background:#0a4d8c;color:#fff}.step.done{background:#1f9d6b;color:#fff}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🎓 Gestión Jurídica de Programas Académicos</h1><div class="s">Creación · modificación · actualización · supresión · reacreditación · dictamen del CGU · registro RPE</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 nivel:['Bachillerato','Técnico Superior Universitario','Licenciatura','Especialidad','Maestría','Doctorado','Diplomado'],
 modalidad:['Escolarizada','No escolarizada','Mixta','Virtual','Dual'],
 tramite:['Creación','Modificación','Actualización curricular','Supresión','Reacreditación'],
 comision:['Comisión de Educación','Comisión de Hacienda','Comisión Conjunta Educación-Hacienda','Consejo de Centro Universitario','Consejo Universitario de Posgrado'],
 flujo:['Propuesta','En dictaminación','Dictamen de comisión','Aprobado por CGU','Publicado','Vigente'],
 cu:['CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUCostaSur','CUSur','CUCiénega','CUAltos','CULagos','CUNorte','CUValles','CUTonalá','SEMS','Sistema de Universidad Virtual (UDGVirtual)']
};
const ESTADOS=['Propuesta','En dictaminación','Dictamen de comisión','Aprobado por CGU','Publicado','Vigente','En modificación','Suprimido','Rechazado'];
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'a'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function PRG(){return L('sigej_programas');}
function bit(a){if(window.__bitlog)__bitlog('Programas académicos',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Programas académicos',texto:t,folio:f||'',modulo:'Programas Académicos',leida:false});S('sigej_notificaciones',N);}
function estClass(e){return /Vigente|Publicado|Aprobado/.test(e)?'g':/Suprimido|Rechazado/.test(e)?'r':/dictamin|Dictamen|modificaci|Propuesta/.test(e)?'y':'n';}
function seed(){if(localStorage.getItem('sigej_programas'))return;S('sigej_programas',[
 {id:uid(),folio:'PRG-2026-001',nombre:'Licenciatura en Ciencia de Datos',nivel:'Licenciatura',cu:'CUCEA',modalidad:'Escolarizada',tramite:'Creación',rpe:'',rvoe:'No aplica (institución autónoma)',estado:'En dictaminación',comision:'Comisión Conjunta Educación-Hacienda',dictNum:'',dictFecha:'',areaProp:'CUCEA',fApertura:'2027-08-01',creditos:400,obs:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:uid(),folio:'PRG-2026-002',nombre:'Maestría en Derecho Universitario',nivel:'Maestría',cu:'CUCSH',modalidad:'Mixta',tramite:'Creación',rpe:'RPE-CUCSH-114',rvoe:'No aplica (institución autónoma)',estado:'Vigente',comision:'Consejo Universitario de Posgrado',dictNum:'IV/2025/512',dictFecha:'2025-11-20',areaProp:'CUCSH',fApertura:'2026-01-15',creditos:110,obs:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'},{ts:nowS(),usuario:'Sistema',accion:'Aprobado por CGU · dictamen IV/2025/512'}]},
 {id:uid(),folio:'PRG-2026-003',nombre:'Licenciatura en Bibliotecología (baja matrícula)',nivel:'Licenciatura',cu:'CUCSH',modalidad:'Escolarizada',tramite:'Supresión',rpe:'RPE-CUCSH-045',rvoe:'No aplica (institución autónoma)',estado:'Dictamen de comisión',comision:'Comisión de Educación',dictNum:'',dictFecha:'',areaProp:'CUCSH',fApertura:'',creditos:0,obs:'Supresión por baja demanda; salvaguarda de estudiantes inscritos',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
]);}

var TABS=[['t1','📊 Panel'],['t2','🎓 Programas'],['t3','📋 Trámites en proceso'],['t4','📤 Reportes']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vPrg();else if(VIEW==='t3')vTram();else vRep();}

function vPanel(){var A=PRG();
 var vig=A.filter(function(x){return x.estado==='Vigente';}).length;
 var proc=A.filter(function(x){return /Propuesta|dictamin|Dictamen|modificaci/.test(x.estado);}).length;
 var crea=A.filter(function(x){return x.tramite==='Creación';}).length;
 var sup=A.filter(function(x){return x.tramite==='Supresión';}).length;
 var mod=A.filter(function(x){return /Modificaci|Actualizaci/.test(x.tramite);}).length;
 var post=A.filter(function(x){return /Maestría|Doctorado|Especialidad/.test(x.nivel);}).length;
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+A.length+'</div><div class="l">Programas</div></div><div class="kpi g"><div class="n">'+vig+'</div><div class="l">Vigentes</div></div><div class="kpi y"><div class="n">'+proc+'</div><div class="l">Trámites en proceso</div></div><div class="kpi"><div class="n">'+crea+'</div><div class="l">Creaciones</div></div><div class="kpi"><div class="n">'+mod+'</div><div class="l">Modificaciones</div></div><div class="kpi r"><div class="n">'+sup+'</div><div class="l">Supresiones</div></div><div class="kpi"><div class="n">'+post+'</div><div class="l">Posgrado</div></div></div>';
 var supAl=A.filter(function(x){return x.tramite==='Supresión'&&x.estado!=='Suprimido';});
 var al=supAl.length?'<div class="note" style="background:#fff8e6;border-color:#e7c66b;color:#8a6d1a">⚑ <b>'+supAl.length+' supresión(es) en proceso</b> — verificar salvaguarda de estudiantes inscritos y derechos adquiridos antes del dictamen.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de programas académicos</h2><p class="lead">Ciclo de vida jurídico de los programas educativos y su dictaminación ante el CGU.</p>'+kp+al+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Programas por nivel</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Trámites por tipo</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La UdeG es <b>institución autónoma</b>: sus programas se aprueban por el <b>Consejo General Universitario (CGU)</b> y se registran internamente (<b>RPE</b>); el <b>RVOE federal no aplica</b>. Los dictámenes del CGU se gestionan también en el módulo de <b>Normatividad</b>. La integración con <b>SIIAU</b> (matrícula, planes de estudio) es fase backend.</div>';
 try{var n={};A.forEach(function(x){n[x.nivel]=(n[x.nivel]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'bar',data:{labels:Object.keys(n),datasets:[{data:Object.values(n),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});
  var t={};A.forEach(function(x){t[x.tramite]=(t[x.tramite]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'doughnut',data:{labels:Object.keys(t),datasets:[{data:Object.values(t),backgroundColor:['#1f9d6b','#0a4d8c','#1aa39a','#c0392b','#d4a32c']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});}catch(e){}
}
function vPrg(){var A=PRG();var q=(val('pq')||'').toLowerCase(),ft=val('pft');
 var form='<div class="collap" id="pf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar programa / trámite — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre del programa *</label><input id="g_nom"></div>'+
  '<div class="f"><label>Nivel</label><select id="g_niv">'+opt(D.nivel,'')+'</select></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="g_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Modalidad</label><select id="g_mod">'+opt(D.modalidad,'')+'</select></div>'+
  '<div class="f"><label>Tipo de trámite</label><select id="g_tra">'+opt(D.tramite,'')+'</select></div>'+
  '<div class="f"><label>Comisión dictaminadora</label><select id="g_com">'+opt(D.comision,'')+'</select></div>'+
  '<div class="f"><label>RPE (registro interno)</label><input id="g_rpe"></div>'+
  '<div class="f"><label>Créditos</label><input id="g_cred" type="number" min="0"></div>'+
  '<div class="f"><label>Fecha de apertura</label><input id="g_ap" type="date"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Observaciones / justificación</label><input id="g_obs"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addPrg()">＋ Registrar</button> <span id="g_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="pq" value="'+esc(val('pq'))+'" placeholder="🔎 Buscar programa…" oninput="render()" style="flex:1;min-width:160px"><select id="pft" onchange="render()" style="max-width:190px"><option value="">Todo trámite</option>'+opt(D.tramite,ft)+'</select></div>';
 var rows=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){return (!q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0)&&(!ft||o.x.tramite===ft);});
 var tbl='<table><tr><th>Folio</th><th>Programa</th><th>Nivel</th><th>CU</th><th>Trámite</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b></td><td style="font-size:11px">'+esc(x.nivel)+'</td><td style="font-size:11px">'+esc(x.cu)+'</td><td><span class="bdg b">'+esc(x.tramite)+'</span></td><td><span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin programas.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🎓 Programas educativos</h2><p class="lead">Padrón de programas con su trámite (creación/modificación/supresión) y estado en el proceso de dictaminación.</p>'+form+ctrl+tbl;
}
function addPrg(){if(!val('g_nom')){el('g_msg').style.color='#c0392b';el('g_msg').textContent='Indica el nombre.';return;}
 var A=PRG();var folio='PRG-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 A.push({id:uid(),folio:folio,nombre:val('g_nom'),nivel:val('g_niv'),cu:val('g_cu'),modalidad:val('g_mod'),tramite:val('g_tra'),rpe:val('g_rpe'),rvoe:'No aplica (institución autónoma)',estado:'Propuesta',comision:val('g_com'),dictNum:'',dictFecha:'',areaProp:val('g_cu'),fApertura:val('g_ap'),creditos:+val('g_cred')||0,obs:val('g_obs'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta · trámite de '+val('g_tra')}]});
 S('sigej_programas',A);bit('Alta de programa '+folio+' ('+val('g_tra')+')');el('g_msg').style.color='#1f9d6b';el('g_msg').textContent='✓ '+folio+' registrado.';vPrg();}
function ficha(i){var A=PRG();var x=A[i];if(!x)return;
 var fl=D.flujo;var ci=fl.indexOf(x.estado);
 var steps=fl.map(function(s,k){return '<span class="step '+(k<ci?'done':k===ci?'on':'')+'">'+s+'</span>';}).join(' ');
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos (proyecto curricular, dictamen, acuerdo).</span>';
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+esc(x.nombre)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+' · '+esc(x.nivel)+' · '+esc(x.cu)+' · <span class="bdg b">'+esc(x.tramite)+'</span> <span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></div>'+
  '<div class="comp"><b>Modalidad:</b> '+esc(x.modalidad)+' · <b>Créditos:</b> '+(x.creditos||'—')+' · <b>Apertura:</b> '+esc(x.fApertura||'—')+'<br><b>RPE:</b> '+esc(x.rpe||'—')+' · <b>RVOE:</b> '+esc(x.rvoe)+'<br><b>Comisión:</b> '+esc(x.comision||'—')+(x.dictNum?'<br><b>Dictamen CGU:</b> '+esc(x.dictNum)+(x.dictFecha?' ('+esc(x.dictFecha)+')':''):'')+(x.obs?'<br><b>Obs.:</b> '+esc(x.obs):'')+'</div>'+
  '<div class="comp"><b>Flujo de dictaminación</b><div style="margin-top:5px;line-height:2">'+steps+'</div></div>'+
  '<div class="comp"><b>Acciones</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap"><button class="b1 mini" onclick="avanzar('+i+')">▶ Avanzar etapa</button><button class="bw mini" onclick="regDictamen('+i+')">🏛️ Registrar dictamen CGU</button>'+(x.tramite==='Supresión'?'<button class="bd mini" style="background:#5a2330;color:#fff" onclick="setEstado('+i+',\'Suprimido\')">🗑 Marcar suprimido</button>':'<button class="b3 mini" onclick="setEstado('+i+',\'Vigente\')">✔ Marcar vigente</button>')+' <button class="bd mini" onclick="prgAdj('+i+')">📎 Adjuntar</button></div></div>'+
  '<div class="comp"><b>🗂️ Expediente</b><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bw mini" onclick="prgWord('+i+')">📄 Ficha (Word)</button> <button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEstado(i,est){var A=PRG();var x=A[i];if(x.estado===est)return;x.estado=est;x.traza.push({ts:nowS(),usuario:P,accion:'Estado → '+est});S('sigej_programas',A);bit(x.folio+' → '+est);
 if(/Vigente|Publicado|Suprimido|Aprobado/.test(est))notif('Programa '+x.nombre+' → '+est,x.folio);ficha(i);}
function avanzar(i){var A=PRG();var x=A[i];var fl=D.flujo;var ci=fl.indexOf(x.estado);if(ci<0)ci=0;if(ci<fl.length-1){setEstado(i,fl[ci+1]);}else{setEstado(i,'Vigente');}}
function regDictamen(i){var A=PRG();var x=A[i];var num=prompt('Número de dictamen del CGU (ej. IV/2026/XXX):',x.dictNum||'');if(num===null)return;x.dictNum=num.trim();x.dictFecha=hoy();x.traza.push({ts:nowS(),usuario:P,accion:'Dictamen CGU registrado: '+num});if(x.estado==='En dictaminación'||x.estado==='Propuesta')x.estado='Dictamen de comisión';S('sigej_programas',A);bit('Dictamen CGU '+num+' · '+x.folio);notif('Dictamen del CGU registrado para '+x.nombre+': '+num,x.folio);ficha(i);}
var _AT=null;
function prgAdj(i){_AT=i;el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Proyecto curricular / Dictamen / Acuerdo CGU / Estudio de factibilidad / Otro):','Proyecto curricular')||'Documento';var r=new FileReader();r.onload=function(){var A=PRG();A[_AT].docs=A[_AT].docs||[];A[_AT].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});A[_AT].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat+': '+f.name});S('sigej_programas',A);ficha(_AT);};r.readAsDataURL(f);};el('fileIn').click();}
function prgWord(i){var x=PRG()[i];var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Ficha jurídica de programa académico — '+esc(x.folio)+'</h3><p><b>Programa:</b> '+esc(x.nombre)+'<br><b>Nivel/Modalidad:</b> '+esc(x.nivel)+' / '+esc(x.modalidad)+'<br><b>CU:</b> '+esc(x.cu)+'<br><b>Trámite:</b> '+esc(x.tramite)+' · <b>Estado:</b> '+esc(x.estado)+'<br><b>RPE:</b> '+esc(x.rpe)+' · <b>RVOE:</b> '+esc(x.rvoe)+'<br><b>Comisión dictaminadora:</b> '+esc(x.comision)+'<br><b>Dictamen CGU:</b> '+esc(x.dictNum||'pendiente')+' '+esc(x.dictFecha||'')+'</p><p><b>Observaciones:</b> '+esc(x.obs||'')+'</p></body></html>';var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Programa_'+x.folio+'.doc';a.click();}
/* ---- Trámites en proceso ---- */
function vTram(){var A=PRG().map(function(x,i){return {x:x,i:i};}).filter(function(o){return /Propuesta|dictamin|Dictamen|modificaci/i.test(o.x.estado);});
 var tbl='<table><tr><th>Folio</th><th>Programa</th><th>Trámite</th><th>Comisión</th><th>Estado</th></tr>'+
  (A.length?A.map(function(o){var x=o.x;return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b><br><span style="font-size:10px;color:#64748b">'+esc(x.cu)+'</span></td><td><span class="bdg b">'+esc(x.tramite)+'</span></td><td style="font-size:11px">'+esc(x.comision||'—')+'</td><td><span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="5" class="empty">Sin trámites en proceso.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📋 Trámites en proceso</h2><p class="lead">Programas en creación, modificación o supresión pendientes de dictamen/aprobación del CGU. Clic para gestionar.</p>'+tbl;
}
/* ---- Reportes ---- */
function vRep(){var A=PRG();
 el('panel').innerHTML='<h2 class="h">📤 Reportes</h2><p class="lead">Padrón jurídico de programas académicos.</p><div style="display:flex;gap:8px;margin-bottom:12px"><button class="b1 mini" onclick="expCSV()">⬇️ Padrón CSV</button></div>'+
  '<table><tr><th>Folio</th><th>Programa</th><th>Nivel</th><th>CU</th><th>Trámite</th><th>RPE</th><th>Dictamen</th><th>Estado</th></tr>'+A.map(function(x){return '<tr><td>'+esc(x.folio)+'</td><td>'+esc(x.nombre)+'</td><td>'+esc(x.nivel)+'</td><td style="font-size:11px">'+esc(x.cu)+'</td><td>'+esc(x.tramite)+'</td><td style="font-size:11px">'+esc(x.rpe||'—')+'</td><td style="font-size:11px">'+esc(x.dictNum||'—')+'</td><td>'+esc(x.estado)+'</td></tr>';}).join('')+'</table>';
}
function expCSV(){var A=PRG();var rows=[['Folio','Programa','Nivel','CU','Modalidad','Tramite','RPE','RVOE','Comision','Dictamen','FechaDictamen','Estado']].concat(A.map(function(x){return [x.folio,x.nombre,x.nivel,x.cu,x.modalidad,x.tramite,x.rpe,x.rvoe,x.comision,x.dictNum,x.dictFecha,x.estado];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='programas_academicos_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);function clean(){try{document.querySelectorAll('div[style*="99999"]').forEach(function(o){o.remove();});var b=document.querySelector('div[style*="bottom:12px"][style*="right:12px"]');if(b)b.style.display="none";}catch(e){}}clean();setTimeout(clean,200);setTimeout(clean,800);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"programas_SIGEJ.html","w",encoding="utf-8").write(out)
print("programas_SIGEJ.html OK -",len(out),"bytes")
