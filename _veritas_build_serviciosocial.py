# -*- coding: utf-8 -*-
# MÓDULO: Servicio Social y Prácticas Profesionales · Convenios (Onda 3 · #1).
# Captura y búsqueda de convenios MARCO de servicio social/prácticas (estilo Instrumentos CLM). El seguro del prestador NO se rastrea a nivel de convenio marco (es operativo por estudiante).
# Base real: serviciosocial.udg.mx/Convenios (Dependencia + Vigencia). Integración con ese sistema = backend.
import re
B="/Users/edithroque/Documents/CLAUDE/"
# Padrón real de convenios de servicio social (importado del Excel oficial USS, 1,022 registros 2020-2026).
SEEDJ=open(B+"serviciosocial_convenios.json",encoding="utf-8").read()
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Servicio Social · Convenios'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','serviciosocial_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="serviciosocial_SIGEJ.html" class="act">🤝 Servicio Social · Convenios</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Servicio Social y Prácticas · Convenios</title>
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
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🤝 Servicio Social y Prácticas Profesionales · Convenios</h1><div class="s">Captura y búsqueda de convenios de servicio social · vigencias · objeto · dependencias · base: serviciosocial.udg.mx</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 sector:['Gobierno municipal','Gobierno estatal','Gobierno federal','Salud','Educativo','Asociación civil / OSC','Empresa privada','Cámara / colegio profesional','Ambiental','Cultural','Otro'],
 tipo:['Servicio social','Prácticas profesionales','Ambos'],
 modalidad:['Presencial','En línea','Mixta'],
 cu:['Toda la Red','CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUCostaSur','CUSur','CUCiénega','CUAltos','CULagos','CUNorte','CUValles','CUTonalá','SEMS','UDGVirtual']
};
const ESTADOS=['Solicitud','En revisión jurídica','En firma','Vigente','Por vencer','Vencido','Cancelado'];
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 's'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function CV(){return L('sigej_serviciosocial');}
function bit(a){if(window.__bitlog)__bitlog('Servicio Social · Convenios',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Servicio Social · Convenios',texto:t,folio:f||'',modulo:'Servicio Social · Convenios',leida:false});S('sigej_notificaciones',N);}
function estadoReal(c){if(/Cancelado/.test(c.estado))return 'Cancelado';var d=dr(c.fin);if(/Vigente|Por vencer/.test(c.estado)){if(d!==null&&d<0)return 'Vencido';if(d!==null&&d<=90)return 'Por vencer';return 'Vigente';}return c.estado;}
function estClass(e){return /Vigente/.test(e)?'g':/Vencido|Cancelado/.test(e)?'r':/Por vencer|revisi|firma|Solicitud/.test(e)?'y':'n';}
const SEED=__SEED__;
function isDemo(A){return A.length<=4&&A.every(function(x){return /^CSS-2026-00/.test(x.folio||'');});}
function seed(){var cur=localStorage.getItem('sigej_serviciosocial');
 if(cur){try{var A=JSON.parse(cur);if(A.length&&!isDemo(A))return;}catch(e){return;}}
 S('sigej_serviciosocial',JSON.parse(JSON.stringify(SEED)));}

var TABS=[['t1','🛰️ Centro de mando'],['t2','➕ Alta y captura'],['t3','🔀 Flujos'],['t4','⚠️ Riesgos'],['t5','🔔 Alertas'],['t6','🧠 Conocimiento'],['t8','🗄️ Archivo'],['t7','🌐 Portal de dependencias']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vConv();else if(VIEW==='t3')vFlujos();else if(VIEW==='t4')vRiesgos();else if(VIEW==='t5')vAlertas();else if(VIEW==='t6')vConoc();else if(VIEW==='t8')vArchivo();else vPortal();}
// --- Archivística · Ley General de Archivos (DOF 15/06/2018): trámite → concentración → histórico/baja.
// Plazos SUGERIDOS; los oficiales los fija el Catálogo de Disposición Documental (CADIDO) de la UdeG.
var ARCH={tramite:2,concentracion:5};
function addYears(f,n){if(!f)return '';var d=new Date(f+'T00:00:00');if(isNaN(d))return '';d.setFullYear(d.getFullYear()+n);return d.toISOString().slice(0,10);}
function concluido(x){return /Concluido|Cancelado|Vencido/.test(estadoReal(x))||/Concluido|Cancelado/i.test(x.estado||'');}
function archivo(x){var vivo=!concluido(x);var base=x.fConclusion||x.fin||'';
 var fTransfer=vivo?'':addYears(base,ARCH.tramite);var fBaja=fTransfer?addYears(fTransfer,ARCH.concentracion):'';var h=hoy();var fase;
 if(vivo)fase='Archivo de trámite';else if(fTransfer&&h>=fBaja)fase='Baja documental / histórico';else if(fTransfer&&h>=fTransfer)fase='Archivo de concentración';else fase='Trámite (por transferir)';
 return {fase:fase,fTransfer:fTransfer,fBaja:fBaja,base:base};}
function archClass(f){return /Baja/.test(f)?'r':/concentración/i.test(f)?'y':/por transferir/i.test(f)?'b':'g';}
function movs(x){var m=(x.movimientos||[]).slice();if(!m.length&&(x.oficio||x.fApertura))m.push({fecha:x.fApertura||'',oficio:x.oficio||'',area:x.oficioArea||'USS',desc:'Apertura de expediente'});return m;}

function vPanel(){var A=CV();
 var vig=A.filter(function(x){return estadoReal(x)==='Vigente';}).length;
 var pv=A.filter(function(x){return estadoReal(x)==='Por vencer';}).length;
 var venc=A.filter(function(x){return estadoReal(x)==='Vencido';}).length;
 var sol=A.filter(function(x){return /Solicitud|revisi|firma/i.test(x.estado);}).length;
 var plazas=A.filter(function(x){return estadoReal(x)==='Vigente';}).reduce(function(a,x){return a+(+x.plazas||0);},0);
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+A.length+'</div><div class="l">Convenios</div></div><div class="kpi g"><div class="n">'+vig+'</div><div class="l">Vigentes</div></div><div class="kpi y"><div class="n">'+pv+'</div><div class="l">Por vencer (≤90d)</div></div><div class="kpi r"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div><div class="kpi"><div class="n">'+sol+'</div><div class="l">Solicitudes / en trámite</div></div><div class="kpi"><div class="n">'+plazas+'</div><div class="l">Plazas (vigentes)</div></div></div>';
 var ri=[];if(pv)ri.push(pv+' por vencer');if(venc)ri.push(venc+' vencidos');
 var al=ri.length?'<div class="alert">🚨 <b>Riesgo jurídico:</b> '+ri.join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">🛰️ Centro de mando · Servicio Social</h2><p class="lead">Padrón real de convenios de servicio social (fuente: USS). Vigencias, objeto, dependencia y estatus.</p><div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px"><button class="b1 mini" onclick="expCSV()">⬇️ Padrón CSV</button><button class="bd mini" onclick="goV(\'t2\')">📄 Ver padrón / alta</button><button class="bd mini" onclick="goV(\'t4\')">⚠️ Riesgos</button></div>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Convenios por sector</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Convenios por estatus</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Convenios por año de apertura</b><canvas id="c3" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Expedientes por fase archivística</b><canvas id="c4" height="150"></canvas></div></div>'+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Top 8 dependencias / contrapartes</b><canvas id="c5" height="160"></canvas></div><div class="card"><b style="color:#0a4d8c">Convenios abiertos por año</b><canvas id="c6" height="160"></canvas></div></div>'+
  '<div class="note">ℹ️ Base y padrón oficial en <b>serviciosocial.udg.mx/Convenios</b>; la sincronización automática (y la <b>solicitud-de-convenios</b> en línea) es integración de fase backend. Este módulo complementa el CLM general de <b>Instrumentos Jurídicos</b>.</div>';
 try{var s={};A.forEach(function(x){s[x.sector]=(s[x.sector]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'bar',data:{labels:Object.keys(s),datasets:[{data:Object.values(s),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});
  var g={};A.forEach(function(x){var k=estadoReal(x);g[k]=(g[k]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'doughnut',data:{labels:Object.keys(g),datasets:[{data:Object.values(g),backgroundColor:['#1f9d6b','#d4a32c','#c0392b','#64748b','#0a4d8c','#1aa39a']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  function yr(x){var m=(x.folio||'').match(/SS-(\d{4})-/);return m?m[1]:((x.fApertura||x.ini||'').slice(0,4)||'s/f');}
  var ya={};A.forEach(function(x){var k=yr(x);ya[k]=(ya[k]||0)+1;});var yk=Object.keys(ya).sort();if(window.__c3)__c3.destroy();window.__c3=new Chart(el('c3'),{type:'bar',data:{labels:yk,datasets:[{data:yk.map(function(k){return ya[k];}),backgroundColor:'#1aa39a'}]},options:{plugins:{legend:{display:false}}}});
  var fa={};A.forEach(function(x){var k=archivo(x).fase;fa[k]=(fa[k]||0)+1;});if(window.__c4)__c4.destroy();window.__c4=new Chart(el('c4'),{type:'doughnut',data:{labels:Object.keys(fa),datasets:[{data:Object.values(fa),backgroundColor:['#15803d','#0a4d8c','#b45309','#c0392b']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var dp={};A.forEach(function(x){dp[x.dependencia]=(dp[x.dependencia]||0)+1;});var top=Object.keys(dp).map(function(k){return [k,dp[k]];}).sort(function(a,b){return b[1]-a[1];}).slice(0,8);if(window.__c5)__c5.destroy();window.__c5=new Chart(el('c5'),{type:'bar',data:{labels:top.map(function(t){return t[0].length>26?t[0].slice(0,26)+'…':t[0];}),datasets:[{data:top.map(function(t){return t[1];}),backgroundColor:'#d4a32c'}]},options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{y:{ticks:{font:{size:8}}}}}});
  if(window.__c6)__c6.destroy();window.__c6=new Chart(el('c6'),{type:'line',data:{labels:yk,datasets:[{data:yk.map(function(k){return ya[k];}),borderColor:'#0a4d8c',backgroundColor:'rgba(10,77,140,.12)',fill:true,tension:.3}]},options:{plugins:{legend:{display:false}}}});}catch(e){}
}
function convForm(){return '<div class="grid">'+
  '<div class="f"><label>Dependencia / institución receptora *</label><input id="c_dep" list="dl_dep"></div>'+
  '<div class="f"><label>Sector</label><select id="c_sec">'+opt(D.sector,'')+'</select></div>'+
  '<div class="f"><label>Tipo</label><select id="c_tipo">'+opt(D.tipo,'')+'</select></div>'+
  '<div class="f"><label>CU / programa beneficiado</label><select id="c_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Vigencia inicio</label><input id="c_ini" type="date"></div>'+
  '<div class="f"><label>Vigencia fin</label><input id="c_fin" type="date"></div>'+
  '<div class="f"><label>Plazas</label><input id="c_plz" type="number" min="0"></div>'+
  '<div class="f"><label>Modalidad</label><select id="c_mod">'+opt(D.modalidad,'')+'</select></div>'+
  '<div class="f"><label>Representante de la contraparte</label><input id="c_resp"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Objeto</label><input id="c_obj"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Responsabilidad / cláusulas de riesgo</label><input id="c_respons"></div>'+
  '<div class="f" style="grid-column:1/-1"><div style="font-size:11px;font-weight:700;color:#0a4d8c;border-top:1px solid var(--line);padding-top:6px">🗄️ Expediente y archivo (Ley General de Archivos)</div></div>'+
  '<div class="f"><label>Fecha de apertura del expediente</label><input id="c_fap" type="date"></div>'+
  '<div class="f"><label>Oficio de apertura del expediente</label><input id="c_oficio"></div>'+
  '<div class="f"><label>Oficio del área que envía</label><input id="c_ofarea"></div>'+
  '<div class="f"><label>No. de expediente interno</label><input id="c_exp"></div>'+
  '<div class="f"><label>No. de expediente de Rectoría</label><input id="c_rect"></div>'+
  '<div class="f"><label>No. de conclusión interna</label><input id="c_ncon"></div>'+
  '<div class="f"><label>Fecha de conclusión interna</label><input id="c_fcon" type="date"></div>'+
  '<div class="f"><label>Etiqueta archivo muerto</label><input id="c_etiq"></div>'+
  '</div><datalist id="dl_dep">'+[].concat.apply([],CV().map(function(x){return x.dependencia;})).filter(function(v,i,a){return a.indexOf(v)===i;}).map(function(v){return '<option value="'+esc(v)+'">';}).join('')+'</datalist>';}
function vConv(){var A=CV();var q=norm(val('cq')),fe=val('cfe'),fs=val('cfs');
 var form='<div class="collap" id="cf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar convenio — clic para abrir/cerrar</div><div class="bd2">'+convForm()+'<div style="margin-top:8px"><button class="b3" onclick="addConv(\'Vigente\')">＋ Registrar convenio</button> <span id="c_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="cq" value="'+esc(val('cq'))+'" placeholder="🔎 Buscar (dependencia, objeto, sector, CU)…" oninput="render()" style="flex:1;min-width:180px"><select id="cfs" onchange="render()" style="max-width:160px"><option value="">Todo sector</option>'+opt(D.sector,fs)+'</select><select id="cfe" onchange="render()" style="max-width:150px"><option value="">Todo estado</option>'+opt(['Vigente','Por vencer','Vencido','Solicitud','En revisión jurídica','Cancelado'],fe)+'</select></div>';
 var rows=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){var er=estadoReal(o.x);return (!q||norm(JSON.stringify(o.x)).indexOf(q)>=0)&&(!fs||o.x.sector===fs)&&(!fe||er===fe||o.x.estado===fe);});
 var tbl='<table><tr><th>Folio</th><th>Dependencia</th><th>Sector</th><th>Tipo</th><th>Vigencia</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var er=estadoReal(x);var d=dr(x.fin);return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.dependencia)+'</b></td><td style="font-size:11px">'+esc(x.sector)+'</td><td style="font-size:11px">'+esc(x.tipo)+'</td><td>'+esc(x.fin||'—')+(er==='Por vencer'?' <span class="bdg y">'+d+'d</span>':'')+'</td><td><span class="bdg '+estClass(er)+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin convenios.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📄 Convenios de servicio social y prácticas</h2><p class="lead">Padrón con dependencia, objeto, vigencia y estatus. Estilo Instrumentos (CLM), especializado en servicio social.</p>'+form+ctrl+tbl;
}
function addConv(est){if(!val('c_dep')){el('c_msg').style.color='#c0392b';el('c_msg').textContent='Indica la dependencia.';return;}
 var A=CV();var folio='CSS-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 var fap=val('c_fap');var ofi=val('c_oficio');var ofa=val('c_ofarea');
 var c={id:uid(),folio:folio,dependencia:val('c_dep'),sector:val('c_sec'),tipo:val('c_tipo'),cu:val('c_cu'),objeto:val('c_obj'),ini:val('c_ini'),fin:val('c_fin'),plazas:+val('c_plz')||0,modalidad:val('c_mod'),resp:val('c_resp'),respons:val('c_respons'),estado:est||'Vigente',origen:'Captura SIGEJ',
  fApertura:fap,oficio:ofi,oficioArea:ofa,expediente:val('c_exp'),rectoria:val('c_rect'),numConclusion:val('c_ncon'),fConclusion:val('c_fcon'),etiqueta:val('c_etiq'),
  movimientos:(ofi||ofa||fap)?[{fecha:fap||hoy(),oficio:ofi,area:ofa||'USS',desc:'Apertura de expediente'}]:[],
  docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta ('+ (est||'Vigente') +')'}]};
 A.push(c);S('sigej_serviciosocial',A);bit('Alta convenio '+folio+' · '+val('c_dep'));
 el('c_msg').style.color='#1f9d6b';el('c_msg').textContent='✓ '+folio+' registrado.';render();}
function ficha(i){var A=CV();var x=A[i];if(!x)return;var er=estadoReal(x);
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos (convenio firmado, póliza, anexos).</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+esc(x.dependencia)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+' · '+esc(x.sector)+' · '+esc(x.tipo)+' <span class="bdg '+estClass(er)+'">'+esc(er)+'</span></div>'+
  '<div class="comp"><b>Objeto:</b> '+esc(x.objeto||'—')+'<br><b>CU/programa:</b> '+esc(x.cu)+' · <b>Plazas:</b> '+(x.plazas||'—')+' · <b>Modalidad:</b> '+esc(x.modalidad||'—')+'<br><b>Vigencia:</b> '+esc(x.ini||'—')+' → '+esc(x.fin||'—')+'<br><b>Representante contraparte:</b> '+esc(x.resp||'—')+' · <b>Origen:</b> '+esc(x.origen||'—')+(x.oficio?'<br><b>Oficio de apertura:</b> '+esc(x.oficio):'')+(x.expediente?' · <b>Exp. interno:</b> '+esc(x.expediente):'')+(x.rectoria?' · <b>No. Rectoría:</b> '+esc(x.rectoria):'')+(x.etiqueta?' · <b>Etiqueta:</b> '+esc(x.etiqueta):'')+'</div>'+
  '<div class="comp"><b>⚖️ Responsabilidad / cláusulas:</b> '+esc(x.respons||'—')+'</div>'+
  (function(){var ar=archivo(x);return '<div class="comp" style="border-left:4px solid '+({r:'#c0392b',y:'#b45309',b:'#0a4d8c',g:'#15803d'}[archClass(ar.fase)])+'"><b>🗄️ Gestión documental / archivo</b> <span class="bdg '+archClass(ar.fase)+'">'+esc(ar.fase)+'</span>'+
   '<div style="margin-top:5px;font-size:12px"><b>Apertura de expediente:</b> '+esc(x.fApertura||'—')+' · <b>Oficio de apertura:</b> '+esc(x.oficio||'—')+'<br><b>Oficio del área que envía:</b> '+esc(x.oficioArea||'—')+'<br><b>Exp. interno:</b> '+esc(x.expediente||'—')+' · <b>Exp. Rectoría:</b> '+esc(x.rectoria||'—')+'<br><b>Conclusión interna:</b> No. '+esc(x.numConclusion||'—')+' · '+esc(x.fConclusion||'—')+'<br><b>Vigencia documental (base):</b> '+esc(ar.base||'—')+'<br><b>Transferencia a concentración:</b> '+esc(ar.fTransfer||'—')+' · <b>Fecha de baja:</b> '+esc(ar.fBaja||'—')+'<br><b>Etiqueta archivo muerto:</b> '+esc(x.etiqueta||'—')+'</div>'+
   '<div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap;align-items:center"><input id="fcon_'+i+'" type="date" value="'+esc(x.fConclusion||'')+'" style="width:auto"><button class="b3 mini" onclick="setConcl('+i+')">Registrar conclusión interna</button></div>'+
   '<div style="font-size:10.5px;color:#94a3b8;margin-top:5px">Plazos sugeridos (Ley General de Archivos): '+ARCH.tramite+' años en trámite tras la conclusión → concentración; '+ARCH.concentracion+' años en concentración → baja. Los plazos oficiales los fija el CADIDO de la UdeG.</div></div>';})()+
  '<div class="comp"><b>📨 Historial de oficios (movimientos)</b><div style="margin-top:4px">'+(movs(x).length?movs(x).map(function(m){return '<div style="font-size:11px;color:#334155;border-bottom:1px solid #eef2f7;padding:3px 0">'+esc(m.fecha||'—')+' · <b>'+esc(m.oficio||'s/n')+'</b> · '+esc(m.area||'')+' — '+esc(m.desc||'')+'</div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin movimientos.</span>')+
   '<div style="margin-top:6px;display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:4px"><input id="mv_f_'+i+'" type="date"><input id="mv_o_'+i+'" placeholder="No. de oficio"><input id="mv_a_'+i+'" placeholder="Área que envía"><input id="mv_d_'+i+'" placeholder="Descripción"></div><div style="margin-top:5px"><button class="b3 mini" onclick="addMov('+i+')">＋ Agregar movimiento</button></div></div>'+
  '<div class="comp"><b>Estado</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+['En revisión jurídica','En firma','Vigente','Concluido','Cancelado'].map(function(e){return '<button class="bd mini" onclick="setEstado('+i+',\''+e+'\')">'+e+'</button>';}).join('')+'</div></div>'+
  '<div class="comp"><b>🗂️ Expediente</b> <button class="bd mini" onclick="convAdj('+i+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp" style="border-left:4px solid #0a4d8c"><b>📝 Seguimiento (notas del equipo)</b><div style="margin-top:4px">'+((x.seguimiento||[]).length?(x.seguimiento||[]).slice().reverse().map(function(s){return '<div style="font-size:11.5px;color:#334155;border-bottom:1px solid #eef2f7;padding:4px 0"><b style="color:#0a4d8c">'+esc(s.usuario)+'</b> <span style="color:#94a3b8;font-size:10px">'+esc(s.ts)+'</span><br>'+esc(s.texto)+'</div>';}).join(''):'<span style="color:#94a3b8;font-size:12px">Sin notas.</span>')+'</div><div style="margin-top:6px"><textarea id="seg_'+i+'" rows="2" placeholder="Escribe una nota de seguimiento del expediente…"></textarea><button class="b3 mini" style="margin-top:5px" onclick="addSeg('+i+')">＋ Agregar nota</button></div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bw mini" onclick="convWord('+i+')">📄 Ficha (Word)</button> <button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEstado(i,e){var A=CV();var x=A[i];if(x.estado===e)return;x.estado=e;x.traza.push({ts:nowS(),usuario:P,accion:'Estado → '+e});S('sigej_serviciosocial',A);bit(x.folio+' → '+e);if(/Vigente|Cancelado/.test(e))notif('Convenio '+x.dependencia+' → '+e,x.folio);ficha(i);}
function addSeg(i){var A=CV();var x=A[i];var t=val('seg_'+i);if(!t){alert('Escribe la nota.');return;}x.seguimiento=x.seguimiento||[];x.seguimiento.push({ts:nowS(),usuario:P,texto:t});S('sigej_serviciosocial',A);bit(x.folio+' · nota de seguimiento');ficha(i);}
function addMov(i){var A=CV();var x=A[i];var f=val('mv_f_'+i),o=val('mv_o_'+i),a=val('mv_a_'+i),d=val('mv_d_'+i);
 if(!o&&!d){alert('Indica al menos el número de oficio o la descripción del movimiento.');return;}
 x.movimientos=x.movimientos||[];x.movimientos.push({fecha:f||hoy(),oficio:o,area:a,desc:d});
 x.traza=x.traza||[];x.traza.push({ts:nowS(),usuario:P,accion:'Movimiento de oficio: '+(o||'s/n')+' '+(d||'')});
 S('sigej_serviciosocial',A);bit(x.folio+' · movimiento '+(o||''));ficha(i);}
function setConcl(i){var A=CV();var x=A[i];var f=val('fcon_'+i);if(!f){alert('Indica la fecha de conclusión interna.');return;}
 x.fConclusion=f;if(!/Cancelado/.test(x.estado))x.estado='Concluido';x.traza=x.traza||[];x.traza.push({ts:nowS(),usuario:P,accion:'Conclusión interna registrada ('+f+')'});
 S('sigej_serviciosocial',A);bit(x.folio+' conclusión '+f);ficha(i);}
var _AT=null;
function convAdj(i){_AT=i;el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Convenio firmado / Anexo / Acuse / Oficio / Otro):','Convenio firmado')||'Documento';var r=new FileReader();r.onload=function(){var A=CV();A[_AT].docs=A[_AT].docs||[];A[_AT].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});A[_AT].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat+': '+f.name});S('sigej_serviciosocial',A);ficha(_AT);};r.readAsDataURL(f);};el('fileIn').click();}
function convWord(i){var x=CV()[i];var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Ficha de convenio de servicio social — '+esc(x.folio)+'</h3><p><b>Dependencia:</b> '+esc(x.dependencia)+'<br><b>Sector/Tipo:</b> '+esc(x.sector)+' / '+esc(x.tipo)+'<br><b>CU/programa:</b> '+esc(x.cu)+' · <b>Plazas:</b> '+(x.plazas||'')+'<br><b>Vigencia:</b> '+esc(x.ini)+' a '+esc(x.fin)+'<br><b>Objeto:</b> '+esc(x.objeto)+'<br><b>Responsabilidad:</b> '+esc(x.respons)+'<br><b>Estado:</b> '+esc(estadoReal(x))+'</p></body></html>';var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ConvenioSS_'+x.folio+'.doc';a.click();}
/* ---- Flujos (BPMN del convenio de servicio social) + solicitudes ---- */
var FLUJO=[['Solicitud','Dependencia solicitante'],['Revisión jurídica','Abogacía / Enlace con la Red'],['Firma','Titular / apoderado'],['Vigencia','Resguardo y seguimiento'],['Conclusión','Cierre / archivo']];
function vFlujos(){var A=CV();
 var pend=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){return /Solicitud|revisi|firma/i.test(o.x.estado);});
 var byEst={};A.forEach(function(x){var e=estadoReal(x);byEst[e]=(byEst[e]||0)+1;});
 var flow=FLUJO.map(function(s,i){return '<div style="flex:1;min-width:140px;background:#f8fafc;border:1px solid var(--line);border-left:4px solid #0a4d8c;border-radius:8px;padding:10px"><b style="color:#0a4d8c">'+(i+1)+'. '+s[0]+'</b><div style="font-size:11px;color:#64748b">'+s[1]+'</div></div>';}).join('<div style="align-self:center;color:#94a3b8;font-weight:700">→</div>');
 var chips=Object.keys(byEst).sort().map(function(e){return '<span class="bdg '+estClass(e)+'" style="margin:2px">'+esc(e)+': '+byEst[e]+'</span>';}).join(' ');
 var form='<div class="collap" id="sf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Nueva solicitud de convenio (dependencia solicitante) — clic para abrir/cerrar</div><div class="bd2">'+convForm()+'<div style="margin-top:8px"><button class="b3" onclick="addConv(\'Solicitud\')">＋ Registrar solicitud</button> <span id="c_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Dependencia</th><th>Sector</th><th>Estado</th><th>Acción</th></tr>'+
  (pend.length?pend.map(function(o){var x=o.x;return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.dependencia)+'</b></td><td style="font-size:11px">'+esc(x.sector)+'</td><td><span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></td><td><button class="b1 mini" onclick="ficha('+o.i+')">Gestionar</button> <button class="b3 mini" onclick="setEstado('+o.i+',\'Vigente\')">Aprobar</button></td></tr>';}).join(''):'<tr><td colspan="5" class="empty">Sin solicitudes en trámite.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🔀 Flujo de convenios de servicio social</h2><p class="lead">Ruta: solicitud → revisión jurídica → firma → vigencia → conclusión.</p>'+
  '<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">'+flow+'</div>'+
  '<div class="card"><b style="color:#0a4d8c">Convenios por etapa / estado</b><div style="margin-top:6px">'+chips+'</div></div>'+
  '<h2 class="h" style="font-size:15px;margin-top:14px">📥 Solicitudes en trámite</h2>'+form+tbl;
}
/* ---- Riesgos ---- */
function vRiesgos(){var A=CV();
 var venc=A.filter(function(x){return estadoReal(x)==='Vencido';});
 var pv=A.filter(function(x){return estadoReal(x)==='Por vencer';});
 function tabla(arr){return arr.length?('<table><tr><th>Folio</th><th>Dependencia</th><th>Sector</th><th>Vigencia</th><th>Estado</th></tr>'+arr.map(function(x){var idx=A.indexOf(x);return '<tr class="row" onclick="ficha('+idx+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.dependencia)+'</b></td><td style="font-size:11px">'+esc(x.sector)+'</td><td>'+esc(x.fin||'—')+'</td><td><span class="bdg '+estClass(estadoReal(x))+'">'+esc(estadoReal(x))+'</span></td></tr>';}).join('')+'</table>'):'<div class="empty">Ninguno.</div>';}
 el('panel').innerHTML='<h2 class="h">⚠️ Riesgos jurídicos</h2><p class="lead">Control de vencimientos de los convenios de servicio social: convenios vencidos y próximos a vencer.</p>'+
  '<div class="kpis"><div class="kpi r"><div class="n">'+venc.length+'</div><div class="l">Vencidos</div></div><div class="kpi y"><div class="n">'+pv.length+'</div><div class="l">Por vencer (≤90d)</div></div></div>'+
  '<div class="card"><b style="color:#c0392b">⏰ Vencidos</b>'+tabla(venc)+'</div>'+
  '<div class="card"><b style="color:#b45309">📆 Por vencer (≤90 días)</b>'+tabla(pv)+'</div>';
}
/* ---- Alertas ---- */
function vAlertas(){var A=CV();var items=[];
 A.forEach(function(x,i){var er=estadoReal(x);var d=dr(x.fin);
  if(er==='Por vencer')items.push(['y','📆',x,'Vence en '+d+' días ('+x.fin+')',i]);
  if(er==='Vencido')items.push(['r','⏰',x,'Vencido desde '+x.fin,i]);
 });
 items.sort(function(a,b){return (a[0]==='r'?0:1)-(b[0]==='r'?0:1);});
 el('panel').innerHTML='<h2 class="h">🔔 Alertas</h2><p class="lead">'+items.length+' alerta(s) accionable(s). Clic para abrir el expediente.</p>'+
  (items.length?items.map(function(t){return '<div class="alert" style="background:'+(t[0]==='r'?'#fdeaea':'#fef3e2')+';border-color:'+(t[0]==='r'?'#e7a0a0':'#f0c987')+';color:'+(t[0]==='r'?'#a02020':'#8a5a12')+';cursor:pointer" onclick="ficha('+t[4]+')">'+t[1]+' <b>'+esc(t[2].dependencia)+'</b> ('+esc(t[2].folio)+') — '+esc(t[3])+'</div>';}).join(''):'<div class="empty">✅ Sin alertas.</div>');
}
/* ---- Conocimiento ---- */
function vConoc(){var KB=L('sigej_ss_kb');
 var marco='<div class="card"><b style="color:#0a4d8c">📚 Marco de referencia</b><ul style="font-size:12px;color:#334155;line-height:1.6;margin:6px 0 0"><li>El servicio social es requisito de titulación conforme a la normativa universitaria y federal aplicable.</li><li>Cada convenio marco debe precisar el <b>objeto</b>, la <b>vigencia</b> y la <b>responsabilidad</b> de la dependencia receptora.</li><li>Padrón oficial: <b>serviciosocial.udg.mx</b>. La <b>Coordinación de Enlace con la Red</b> da soporte jurídico (Art. 219 frac. IX RIAG). Contacto: <b>abogral@udg.mx</b>.</li></ul></div>';
 var form='<div class="card"><b style="color:#0a4d8c">➕ Nota / plantilla de conocimiento</b><div class="grid" style="margin-top:6px"><input id="kb_t" placeholder="Título"><input id="kb_tag" placeholder="Etiqueta (Cláusula, Trámite, Vigencia…)"></div><textarea id="kb_x" placeholder="Contenido…" style="margin-top:6px" rows="3"></textarea><div style="margin-top:6px"><button class="b3 mini" onclick="addKB()">Guardar</button></div></div>';
 var list=KB.length?KB.map(function(k,i){return '<div class="comp"><b>'+esc(k.t)+'</b> <span class="bdg b">'+esc(k.tag||'Nota')+'</span> <button class="bd mini" style="float:right" onclick="delKB('+i+')">✕</button><div style="margin-top:4px;font-size:12px;white-space:pre-wrap">'+esc(k.x)+'</div></div>';}).join(''):'<div class="empty">Sin notas aún.</div>';
 el('panel').innerHTML='<h2 class="h">🧠 Conocimiento</h2><p class="lead">Base de conocimiento del servicio social: marco de referencia, plantillas y notas del equipo.</p>'+marco+form+list;
}
function addKB(){var t=val('kb_t');if(!t){alert('Título requerido.');return;}var KB=L('sigej_ss_kb');KB.push({t:t,tag:val('kb_tag'),x:val('kb_x'),ts:nowS()});S('sigej_ss_kb',KB);bit('KB: '+t);render();}
function delKB(i){var KB=L('sigej_ss_kb');KB.splice(i,1);S('sigej_ss_kb',KB);render();}
/* ---- Archivo (Ley General de Archivos) ---- */
function vArchivo(){var A=CV();var ff=val('af');
 var byFase={};A.forEach(function(x){var f=archivo(x).fase;byFase[f]=(byFase[f]||0)+1;});
 var kp='<div class="kpis">'+['Archivo de trámite','Trámite (por transferir)','Archivo de concentración','Baja documental / histórico'].map(function(f){return '<div class="kpi '+archClass(f)+'"><div class="n">'+(byFase[f]||0)+'</div><div class="l">'+f+'</div></div>';}).join('')+'</div>';
 var fases=['','Archivo de trámite','Trámite (por transferir)','Archivo de concentración','Baja documental / histórico'];
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px"><select id="af" onchange="render()" style="max-width:240px"><option value="">Todas las fases</option>'+opt(fases.slice(1),ff)+'</select><button class="bd mini" onclick="expArch()">⬇️ Cuadro de archivo (CSV)</button></div>';
 var rows=A.map(function(x,i){return {x:x,i:i,a:archivo(x)};}).filter(function(o){return !ff||o.a.fase===ff;});
 var tbl='<table><tr><th>Folio</th><th>Dependencia</th><th>Apertura</th><th>Conclusión</th><th>Fase archivística</th><th>Transferencia</th><th>Baja</th><th>Etiqueta</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x,a=o.a;return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.dependencia)+'</b></td><td>'+esc(x.fApertura||'—')+'</td><td>'+esc(x.fConclusion||x.fin||'—')+'</td><td><span class="bdg '+archClass(a.fase)+'">'+esc(a.fase)+'</span></td><td>'+esc(a.fTransfer||'—')+'</td><td>'+esc(a.fBaja||'—')+'</td><td>'+esc(x.etiqueta||'—')+'</td></tr>';}).join(''):'<tr><td colspan="8" class="empty">Sin expedientes en esta fase.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🗄️ Archivo · gestión documental</h2><p class="lead">Ciclo vital del expediente conforme a la <b>Ley General de Archivos</b> (DOF 15/06/2018): archivo de <b>trámite</b> → <b>concentración</b> → <b>histórico/baja</b>, con transferencias y fecha de baja.</p>'+kp+
  '<div class="note">📏 Plazos <b>sugeridos</b>: '+ARCH.tramite+' años en trámite tras la conclusión (transferencia primaria a concentración) y '+ARCH.concentracion+' años en concentración antes de la baja documental. <b>Los plazos oficiales y los valores documentales los fija el Catálogo de Disposición Documental (CADIDO) de la UdeG</b>; aquí se calculan como referencia.</div>'+
  ctrl+tbl;
}
function expArch(){var A=CV();var rows=[['Folio','Dependencia','Apertura expediente','Oficio apertura','Exp. interno','Exp. Rectoria','Conclusion interna','Fecha conclusion','Fase archivistica','Fecha transferencia','Fecha baja','Etiqueta archivo muerto']].concat(A.map(function(x){var a=archivo(x);return [x.folio,x.dependencia,x.fApertura,x.oficio,x.expediente,x.rectoria,x.numConclusion,x.fConclusion,a.fase,a.fTransfer,a.fBaja,x.etiqueta];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='cuadro_archivo_servicio_social_'+hoy()+'.csv';a.click();}
/* ---- Portal de dependencias y contrapartes ---- */
function vPortal(){el('panel').innerHTML='<h2 class="h">🌐 Portal de dependencias y contrapartes</h2><p class="lead">Portal para que dependencias externas y contrapartes gestionen y den seguimiento a sus convenios de servicio social.</p><iframe src="portal_SIGEJ.html?embed=1" title="Portal de Dependencias y Contrapartes" style="width:100%;height:78vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe>';}
function expCSV(){var A=CV();var rows=[['Folio','Dependencia','Sector','Tipo','CU','Objeto','Inicio','Fin','Plazas','Modalidad','Responsabilidad','Estado','Origen']].concat(A.map(function(x){return [x.folio,x.dependencia,x.sector,x.tipo,x.cu,x.objeto,x.ini,x.fin,x.plazas,x.modalidad,x.respons,estadoReal(x),x.origen];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='convenios_servicio_social_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP).replace("__SEED__",SEEDJ)
open(B+"serviciosocial_SIGEJ.html","w",encoding="utf-8").write(out)
print("serviciosocial_SIGEJ.html OK -",len(out),"bytes | seed convenios:",SEEDJ.count('"folio"'))
