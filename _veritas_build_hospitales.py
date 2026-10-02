# -*- coding: utf-8 -*-
# MÓDULO: Gestión Jurídica de Hospitales Universitarios y Salud (Onda 4 · #2).
# Establecimientos y licencias sanitarias (COFEPRIS), convenios/sedes clínicas (IMSS/SSJ/Hospital Civil),
# responsabilidad sanitaria (CONAMED/CAMEJAL), consentimiento informado y expediente clínico (NOM-004). Marco federal y estatal (Jalisco) verificado.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Hospitales y Salud'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','hospitales_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="hospitales_SIGEJ.html" class="act">🏥 Hospitales y Salud</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="contencioso_SIGEJ.html">⚔️ Contencioso</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Hospitales Universitarios y Salud</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#7a1f2b,#c0392b);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.92;font-size:12px;margin-top:3px}
.navbar{background:#5a1620;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#f0d2d6;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:#c0392b;color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:#7a1f2b;font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:#7a1f2b}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:#7a1f2b;cursor:pointer;font-size:13px}
.collap>.bd2{padding:12px;display:none}.collap.open>.bd2{display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:9px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}.bdg.f{background:#e6f0fb;color:#0a4d8c}.bdg.e{background:#fdeae0;color:#7a1f2b}
.leybox{background:#f8fafc;border:1px solid var(--line);border-left:4px solid #c0392b;border-radius:10px;padding:11px 13px;margin-bottom:8px;font-size:12.5px}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🏥 Gestión Jurídica de Hospitales Universitarios y Salud</h1><div class="s">Licencias sanitarias · sedes y convenios clínicos · responsabilidad sanitaria (CONAMED/CAMEJAL) · consentimiento y expediente clínico</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const LEYFED=[
 ['Ley General de Salud','Secretaría de Salud / COFEPRIS'],
 ['NOM-004-SSA3-2012 — Expediente clínico','Secretaría de Salud'],
 ['NOM-016-SSA3 — Infraestructura y equipamiento hospitalario','Secretaría de Salud'],
 ['Licencia sanitaria / aviso de funcionamiento','COFEPRIS'],
 ['Ley General de Protección de Datos Personales (datos sensibles de salud)','INAI'],
 ['Arbitraje médico federal','CONAMED']
];
const LEYJAL=[
 ['Ley de Salud del Estado de Jalisco (art. 209 · CAMEJAL)','Secretaría de Salud Jalisco'],
 ['Comisión de Arbitraje Médico del Estado de Jalisco (CAMEJAL)','CAMEJAL'],
 ['OPD Hospital Civil de Guadalajara — marco de sedes clínicas','OPD Hospital Civil'],
 ['Reglamentos sanitarios estatales','SSJ / Ayuntamientos']
];
const D={
 tipoEst:['Hospital','Clínica','Laboratorio clínico','Consultorio','Unidad de salud CUCS','Banco de sangre','Farmacia universitaria','Centro de investigación clínica'],
 estLic:['Vigente','Por vencer','Vencida','En trámite','Aviso de funcionamiento'],
 tipoConv:['Sede clínica (internado de pregrado)','Servicio social en salud','Residencias médicas','Campo clínico / prácticas','Colaboración en salud','Investigación clínica'],
 contra:['IMSS','ISSSTE','Secretaría de Salud Jalisco (SSJ)','OPD Hospital Civil de Guadalajara','Secretaría de Salud federal','Hospital privado','DIF Jalisco','Otra'],
 tipoResp:['Queja ante CAMEJAL (Jalisco)','Queja ante CONAMED (federal)','Arbitraje médico','Demanda civil','Denuncia penal','Evento adverso / centinela','Recomendación CEDHJ'],
 estResp:['En proceso','Conciliación','Laudo / arbitraje','En litigio','Resuelto','Cerrado'],
 cu:['CUCS','CUCiénega','CUSur','CUCosta','CUAltos','CUTonalá','CUNorte','SEMS','Coord. Gral. Administrativa'],
 estConv:['Vigente','Por vencer','Vencido','En trámite','Cancelado']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'h'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function EST(){return L('sigej_hosp_est');}
function CONV(){return L('sigej_hosp_conv');}
function RESP(){return L('sigej_hosp_resp');}
function bit(a){if(window.__bitlog)__bitlog('Hospitales y Salud',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Hospitales y Salud',texto:t,folio:f||'',modulo:'Hospitales y Salud',leida:false});S('sigej_notificaciones',N);}
function licReal(x){var d=dr(x.fVenc);if(x.estado==='Vigente'&&d!==null){if(d<0)return 'Vencida';if(d<=90)return 'Por vencer';}return x.estado;}
function seed(){if(localStorage.getItem('sigej_hosp_est'))return;
 S('sigej_hosp_est',[
  {id:uid(),folio:'EST-001',nombre:'Clínica de Medicina Familiar CUCS',tipo:'Unidad de salud CUCS',cu:'CUCS',direccion:'Sierra Mojada, Guadalajara',licNum:'LS-XXXX (COFEPRIS)',aviso:'AF-XXXX',respSanitario:'Dr. Responsable Sanitario',cedula:'XXXXXXX',fVenc:'2026-09-30',estado:'Vigente',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
  {id:uid(),folio:'EST-002',nombre:'Laboratorio clínico CUCS',tipo:'Laboratorio clínico',cu:'CUCS',direccion:'Guadalajara',licNum:'',aviso:'AF-XXXX',respSanitario:'Q.F.B. Responsable',cedula:'XXXXXXX',fVenc:'2026-07-25',estado:'Vigente',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
 ]);
 S('sigej_hosp_conv',[
  {id:uid(),folio:'CVS-001',contra:'OPD Hospital Civil de Guadalajara',tipo:'Sede clínica (internado de pregrado)',objeto:'Internado médico de pregrado y campos clínicos',plazas:120,ini:'2025-01-01',fin:'2027-12-31',seguro:'Seguro escolar UdeG + responsabilidad de la sede',estado:'Vigente',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
  {id:uid(),folio:'CVS-002',contra:'IMSS',tipo:'Residencias médicas',objeto:'Residencias médicas en unidades IMSS',plazas:60,ini:'2024-03-01',fin:'2026-08-31',seguro:'Cobertura IMSS',estado:'Vigente',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
 ]);
 S('sigej_hosp_resp',[
  {id:uid(),folio:'RS-001',tipo:'Queja ante CAMEJAL (Jalisco)',estab:'Clínica de Medicina Familiar CUCS',desc:'Inconformidad por atención (paciente anonimizado)',autoridad:'CAMEJAL',reclamo:0,estado:'Conciliación',fecha:'2026-05-10',resp:'Área jurídica CUCS',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
 ]);
}

var TABS=[['t1','📊 Panel'],['t2','🏥 Establecimientos y licencias'],['t3','🤝 Convenios y sedes clínicas'],['t4','⚖️ Responsabilidad sanitaria'],['t5','📚 Marco y cumplimiento']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vEst();else if(VIEW==='t3')vConv();else if(VIEW==='t4')vResp();else vMarco();}

function vPanel(){var E=EST(),C=CONV(),R=RESP();
 var vig=E.filter(function(x){return licReal(x)==='Vigente';}).length;
 var pv=E.filter(function(x){return licReal(x)==='Por vencer';}).length;
 var venc=E.filter(function(x){return licReal(x)==='Vencida';}).length;
 var cvig=C.filter(function(x){var d=dr(x.fin);return x.estado==='Vigente'&&(d===null||d>=0);}).length;
 var abiertas=R.filter(function(x){return !/Resuelto|Cerrado/.test(x.estado);}).length;
 var eventos=R.filter(function(x){return /Evento adverso/.test(x.tipo);}).length;
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+E.length+'</div><div class="l">Establecimientos</div></div><div class="kpi g"><div class="n">'+vig+'</div><div class="l">Licencias vigentes</div></div><div class="kpi y"><div class="n">'+pv+'</div><div class="l">Licencias por vencer</div></div><div class="kpi r"><div class="n">'+venc+'</div><div class="l">Licencias vencidas</div></div><div class="kpi"><div class="n">'+cvig+'</div><div class="l">Convenios/sedes vigentes</div></div><div class="kpi r"><div class="n">'+abiertas+'</div><div class="l">Responsabilidad abierta</div></div><div class="kpi y"><div class="n">'+eventos+'</div><div class="l">Eventos adversos</div></div></div>';
 var ri=[];if(venc)ri.push(venc+' licencia(s) sanitaria(s) vencida(s)');if(pv)ri.push(pv+' por vencer (≤90d)');if(abiertas)ri.push(abiertas+' asunto(s) de responsabilidad sanitaria abierto(s)');
 var al=ri.length?'<div class="alert">🚨 <b>Riesgo sanitario-jurídico:</b> '+ri.join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de hospitales y salud</h2><p class="lead">Licencias sanitarias, convenios de sedes clínicas y responsabilidad sanitaria de las unidades de salud de la Red (CUCS y afines).</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#7a1f2b">Establecimientos por tipo</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#7a1f2b">Responsabilidad por vía</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La conexión con <b>COFEPRIS</b> (licencias/avisos), <b>Secretaría de Salud Jalisco</b>, <b>CONAMED/CAMEJAL</b> y el <b>expediente clínico electrónico (NOM-004)</b> es fase backend. Este módulo gestiona el <b>cumplimiento jurídico</b>; no almacena datos clínicos de pacientes (datos personales sensibles).</div>';
 try{var t={};E.forEach(function(x){t[x.tipo]=(t[x.tipo]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(t),datasets:[{data:Object.values(t),backgroundColor:['#c0392b','#7a1f2b','#e08e0b','#0a4d8c','#1aa39a','#6b7280','#d4a32c']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var v={};R.forEach(function(x){var k=x.tipo.replace(/ \(.*/,'').replace(/ ante /,' ');v[k]=(v[k]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:Object.keys(v),datasets:[{data:Object.values(v),backgroundColor:'#7a1f2b'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
/* ---- Establecimientos ---- */
function vEst(){var E=EST();var q=(val('eq')||'').toLowerCase();
 var form='<div class="collap" id="ef"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar establecimiento de salud — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre *</label><input id="e_nom"></div>'+
  '<div class="f"><label>Tipo</label><select id="e_tipo">'+opt(D.tipoEst,'')+'</select></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="e_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Dirección</label><input id="e_dir"></div>'+
  '<div class="f"><label>Licencia sanitaria (COFEPRIS)</label><input id="e_lic"></div>'+
  '<div class="f"><label>Aviso de funcionamiento</label><input id="e_av"></div>'+
  '<div class="f"><label>Responsable sanitario</label><input id="e_resp"></div>'+
  '<div class="f"><label>Cédula profesional</label><input id="e_ced"></div>'+
  '<div class="f"><label>Vigencia licencia</label><input id="e_venc" type="date"></div>'+
  '<div class="f"><label>Estado</label><select id="e_est">'+opt(D.estLic,'Vigente')+'</select></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addEst()">＋ Registrar</button> <span id="e_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var rows=E.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:6px 0"><input id="eq" value="'+esc(val('eq'))+'" placeholder="🔎 Buscar establecimiento…" oninput="render()" style="width:100%"></div><table><tr><th>Folio</th><th>Establecimiento</th><th>Tipo</th><th>Responsable sanitario</th><th>Licencia</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var er=licReal(x);var c=/Vigente/.test(er)?'g':/Vencida/.test(er)?'r':'y';return '<tr class="row" onclick="ficha(\'est\','+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b><br><span style="font-size:10px;color:#64748b">'+esc(x.cu||'')+'</span></td><td style="font-size:11px">'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.respSanitario||'—')+'</td><td style="font-size:11px">'+esc(x.licNum||x.aviso||'—')+'</td><td><span class="bdg '+c+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin establecimientos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🏥 Establecimientos y licencias sanitarias</h2><p class="lead">Unidades de salud con su licencia sanitaria/aviso de funcionamiento (COFEPRIS), responsable sanitario y vigencia.</p>'+form+tbl;
}
function addEst(){if(!val('e_nom')){el('e_msg').style.color='#c0392b';el('e_msg').textContent='Indica el nombre.';return;}
 var E=EST();E.push({id:uid(),folio:'EST-'+String(E.length+1).padStart(3,'0'),nombre:val('e_nom'),tipo:val('e_tipo'),cu:val('e_cu'),direccion:val('e_dir'),licNum:val('e_lic'),aviso:val('e_av'),respSanitario:val('e_resp'),cedula:val('e_ced'),fVenc:val('e_venc'),estado:val('e_est'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de establecimiento'}]});
 S('sigej_hosp_est',E);bit('Alta establecimiento '+val('e_nom'));var d=dr(val('e_venc'));if(d!==null&&d<=90)notif('Licencia sanitaria de '+val('e_nom')+' por vencer','');el('e_msg').style.color='#1f9d6b';el('e_msg').textContent='✓ registrado.';vEst();}
/* ---- Convenios y sedes ---- */
function vConv(){var C=CONV();
 var form='<div class="collap" id="cf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar convenio / sede clínica — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Contraparte</label><select id="cv_contra">'+opt(D.contra,'')+'</select></div>'+
  '<div class="f"><label>Tipo</label><select id="cv_tipo">'+opt(D.tipoConv,'')+'</select></div>'+
  '<div class="f"><label>Plazas</label><input id="cv_plz" type="number" min="0"></div>'+
  '<div class="f"><label>Inicio</label><input id="cv_ini" type="date"></div>'+
  '<div class="f"><label>Fin</label><input id="cv_fin" type="date"></div>'+
  '<div class="f"><label>Seguro / responsabilidad del estudiante</label><input id="cv_seg"></div>'+
  '<div class="f"><label>Estado</label><select id="cv_est">'+opt(D.estConv,'Vigente')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Objeto</label><input id="cv_obj"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addConv()">＋ Registrar</button> <span id="cv_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Contraparte</th><th>Tipo</th><th>Plazas</th><th>Vigencia</th><th>Estado</th></tr>'+
  (C.length?C.map(function(x,i){var d=dr(x.fin);var er=x.estado==='Vigente'&&d!==null&&d<0?'Vencido':x.estado==='Vigente'&&d!==null&&d<=90?'Por vencer':x.estado;var c=/Vigente/.test(er)?'g':/Vencido|Cancelado/.test(er)?'r':'y';return '<tr class="row" onclick="ficha(\'conv\','+i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.contra)+'</b></td><td style="font-size:11px">'+esc(x.tipo)+'</td><td>'+(x.plazas||0)+'</td><td>'+esc(x.fin||'—')+'</td><td><span class="bdg '+c+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin convenios.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🤝 Convenios y sedes clínicas</h2><p class="lead">Sedes de internado, servicio social en salud, residencias médicas y campos clínicos (IMSS, SSJ, Hospital Civil). Con cobertura de seguro/responsabilidad del prestador.</p>'+form+tbl;
}
function addConv(){if(!val('cv_obj')&&!val('cv_contra')){el('cv_msg').style.color='#c0392b';el('cv_msg').textContent='Indica contraparte/objeto.';return;}
 var C=CONV();C.push({id:uid(),folio:'CVS-'+String(C.length+1).padStart(3,'0'),contra:val('cv_contra'),tipo:val('cv_tipo'),objeto:val('cv_obj'),plazas:+val('cv_plz')||0,ini:val('cv_ini'),fin:val('cv_fin'),seguro:val('cv_seg'),estado:val('cv_est'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de convenio de salud'}]});
 S('sigej_hosp_conv',C);bit('Alta convenio salud '+val('cv_contra'));el('cv_msg').style.color='#1f9d6b';el('cv_msg').textContent='✓ registrado.';vConv();}
/* ---- Responsabilidad sanitaria ---- */
function vResp(){var R=RESP();
 var form='<div class="collap" id="rf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar asunto de responsabilidad sanitaria — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Vía / tipo</label><select id="r_tipo">'+opt(D.tipoResp,'')+'</select></div>'+
  '<div class="f"><label>Establecimiento</label><input id="r_est"></div>'+
  '<div class="f"><label>Autoridad</label><input id="r_aut" placeholder="CAMEJAL / CONAMED / Juzgado…"></div>'+
  '<div class="f"><label>Monto reclamado (MXN)</label><input id="r_rec" type="number" min="0"></div>'+
  '<div class="f"><label>Responsable jurídico</label><input id="r_resp"></div>'+
  '<div class="f"><label>Estado</label><select id="r_est">'+opt(D.estResp,'En proceso')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Descripción (paciente anonimizado — sin datos sensibles)</label><input id="r_desc"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addResp()">＋ Registrar</button> <span id="r_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Vía</th><th>Establecimiento</th><th>Autoridad</th><th>Reclamo</th><th>Estado</th></tr>'+
  (R.length?R.map(function(x,i){var c=/Resuelto|Cerrado/.test(x.estado)?'g':/litigio|Laudo/.test(x.estado)?'r':'y';return '<tr class="row" onclick="ficha(\'resp\','+i+')"><td>'+esc(x.folio)+'</td><td style="font-size:11px">'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.estab||'—')+'</td><td style="font-size:11px">'+esc(x.autoridad||'—')+'</td><td>'+(x.reclamo?M(x.reclamo):'—')+'</td><td><span class="bdg '+c+'">'+esc(x.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin asuntos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">⚖️ Responsabilidad sanitaria</h2><p class="lead">Quejas ante CAMEJAL (Jalisco) y CONAMED (federal), arbitraje médico, demandas, denuncias y eventos adversos. Los pacientes se registran anonimizados (datos sensibles).</p>'+form+tbl;
}
function addResp(){if(!val('r_desc')&&!val('r_tipo')){el('r_msg').style.color='#c0392b';el('r_msg').textContent='Indica la vía/descripción.';return;}
 var R=RESP();var folio='RS-'+String(R.length+1).padStart(3,'0');R.push({id:uid(),folio:folio,tipo:val('r_tipo'),estab:val('r_est'),desc:val('r_desc'),autoridad:val('r_aut'),reclamo:+val('r_rec')||0,estado:val('r_est'),fecha:hoy(),resp:val('r_resp'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de asunto de responsabilidad'}]});
 S('sigej_hosp_resp',R);bit('Alta responsabilidad sanitaria '+folio);notif('Nuevo asunto de responsabilidad sanitaria: '+val('r_tipo'),folio);el('r_msg').style.color='#1f9d6b';el('r_msg').textContent='✓ '+folio+' registrado.';vResp();}
/* ---- Ficha genérica ---- */
function ficha(t,i){var arr=t==='est'?EST():t==='conv'?CONV():RESP();var x=arr[i];if(!x)return;var key=t==='est'?'sigej_hosp_est':t==='conv'?'sigej_hosp_conv':'sigej_hosp_resp';
 var det='';
 if(t==='est'){det='<b>Tipo:</b> '+esc(x.tipo)+' · <b>CU:</b> '+esc(x.cu||'—')+'<br><b>Dirección:</b> '+esc(x.direccion||'—')+'<br><b>Licencia sanitaria:</b> '+esc(x.licNum||'—')+' · <b>Aviso:</b> '+esc(x.aviso||'—')+'<br><b>Responsable sanitario:</b> '+esc(x.respSanitario||'—')+' (céd. '+esc(x.cedula||'—')+')<br><b>Vigencia:</b> '+esc(x.fVenc||'—')+' · '+esc(licReal(x));}
 else if(t==='conv'){det='<b>Contraparte:</b> '+esc(x.contra)+' · <b>Tipo:</b> '+esc(x.tipo)+'<br><b>Objeto:</b> '+esc(x.objeto||'—')+'<br><b>Plazas:</b> '+(x.plazas||0)+' · <b>Vigencia:</b> '+esc(x.ini||'—')+' → '+esc(x.fin||'—')+'<br><b>Seguro/responsabilidad:</b> '+esc(x.seguro||'—')+' · <b>Estado:</b> '+esc(x.estado);}
 else{det='<b>Vía:</b> '+esc(x.tipo)+' · <b>Autoridad:</b> '+esc(x.autoridad||'—')+'<br><b>Establecimiento:</b> '+esc(x.estab||'—')+'<br><b>Descripción:</b> '+esc(x.desc||'—')+'<br><b>Reclamo:</b> '+(x.reclamo?M(x.reclamo):'—')+' · <b>Estado:</b> '+esc(x.estado);}
 var acc='';
 if(t==='est')acc=['Vigente','Por vencer','Vencida','En trámite'].map(function(e){return '<button class="bd mini" onclick="setEstado(\'est\','+i+',\''+e+'\')">'+e+'</button>';}).join(' ');
 else if(t==='resp')acc=D.estResp.map(function(e){return '<button class="bd mini" onclick="setEstado(\'resp\','+i+',\''+e+'\')">'+e.split(' ')[0]+'</button>';}).join(' ');
 else acc=D.estConv.map(function(e){return '<button class="bd mini" onclick="setEstado(\'conv\','+i+',\''+e+'\')">'+e+'</button>';}).join(' ');
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos.</span>';
 var tz=(x.traza||[]).map(function(z){return '<div style="font-size:11px;color:#64748b">'+z.ts+' · '+esc(z.usuario)+' — '+esc(z.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#7a1f2b">'+esc(x.nombre||x.contra||x.tipo)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+'</div>'+
  '<div class="comp">'+det+'</div>'+
  '<div class="comp"><b>Estado</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+acc+'</div></div>'+
  '<div class="comp"><b>🗂️ Expediente</b> <button class="bd mini" onclick="hAdj(\''+t+'\','+i+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEstado(t,i,e){var key=t==='est'?'sigej_hosp_est':t==='conv'?'sigej_hosp_conv':'sigej_hosp_resp';var arr=L(key);var x=arr[i];if(x.estado===e)return;x.estado=e;x.traza=x.traza||[];x.traza.push({ts:nowS(),usuario:P,accion:'Estado → '+e});S(key,arr);bit(x.folio+' → '+e);if(/Vencida|litigio/.test(e))notif((x.nombre||x.tipo)+' → '+e,x.folio);ficha(t,i);}
var _AT=null;
function hAdj(t,i){_AT={t:t,i:i};el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Licencia sanitaria / Convenio / Consentimiento informado / Resolución / Otro):','Documento')||'Documento';var key=_AT.t==='est'?'sigej_hosp_est':_AT.t==='conv'?'sigej_hosp_conv':'sigej_hosp_resp';var r=new FileReader();r.onload=function(){var arr=L(key);arr[_AT.i].docs=arr[_AT.i].docs||[];arr[_AT.i].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});arr[_AT.i].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat});S(key,arr);ficha(_AT.t,_AT.i);};r.readAsDataURL(f);};el('fileIn').click();}
/* ---- Marco y cumplimiento ---- */
function vMarco(){
 var fed=LEYFED.map(function(x){return '<div class="leybox"><b>'+esc(x[0])+'</b><br><span style="font-size:11px;color:#64748b">Autoridad: '+esc(x[1])+'</span></div>';}).join('');
 var jal=LEYJAL.map(function(x){return '<div class="leybox" style="border-left-color:#0a4d8c"><b>'+esc(x[0])+'</b><br><span style="font-size:11px;color:#64748b">Autoridad: '+esc(x[1])+'</span></div>';}).join('');
 el('panel').innerHTML='<h2 class="h">📚 Marco legal y cumplimiento sanitario</h2><p class="lead">Ordenamientos federales y del Estado de Jalisco aplicables a los establecimientos y servicios de salud universitarios.</p>'+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div><div style="font-weight:700;color:#7a1f2b;margin-bottom:6px">🇲🇽 Federal</div>'+fed+'</div><div><div style="font-weight:700;color:#0a4d8c;margin-bottom:6px">🏛️ Estatal (Jalisco)</div>'+jal+'</div></div>'+
  '<div class="card"><b style="color:#7a1f2b">📋 Cumplimiento clave</b><ul style="font-size:12.5px;color:#334155;line-height:1.7;margin:6px 0 0 16px;padding:0"><li><b>Consentimiento informado</b>: formatos por procedimiento (NOM-004-SSA3).</li><li><b>Expediente clínico</b>: integración y resguardo conforme a NOM-004; el expediente electrónico es fase backend.</li><li><b>Datos personales sensibles de salud</b>: tratamiento conforme a la Ley de Protección de Datos; este módulo NO almacena datos clínicos de pacientes.</li><li><b>Responsable sanitario</b> y <b>licencia/aviso</b> por establecimiento (COFEPRIS).</li></ul></div>'+
  '<div style="display:flex;gap:8px;margin-bottom:8px"><button class="b1 mini" onclick="expCSV()">⬇️ Matriz de establecimientos (CSV)</button></div>'+
  '<div class="note">📌 Denominaciones oficiales verificadas (CAMEJAL/CONAMED/Ley de Salud de Jalisco). El <b>texto vigente de cada artículo/NOM debe consultarse en la fuente</b>; la verificación en línea (DOF, Periódico Oficial de Jalisco, COFEPRIS) es fase backend.</div>';
}
function expCSV(){var E=EST();var rows=[['Folio','Establecimiento','Tipo','CU','LicenciaSanitaria','Aviso','ResponsableSanitario','Cedula','Vigencia','Estado']].concat(E.map(function(x){return [x.folio,x.nombre,x.tipo,x.cu,x.licNum,x.aviso,x.respSanitario,x.cedula,x.fVenc,licReal(x)];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='hospitales_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);function clean(){try{document.querySelectorAll('div[style*="99999"]').forEach(function(o){o.remove();});var b=document.querySelector('div[style*="bottom:12px"][style*="right:12px"]');if(b)b.style.display="none";}catch(e){}}clean();setTimeout(clean,200);setTimeout(clean,800);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"hospitales_SIGEJ.html","w",encoding="utf-8").write(out)
print("hospitales_SIGEJ.html OK -",len(out),"bytes")
