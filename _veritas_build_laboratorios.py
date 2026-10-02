# -*- coding: utf-8 -*-
# MÓDULO: Gestión Jurídica de Laboratorios (Onda 4 · #3, cierra la onda cliente).
# Laboratorios y niveles de bioseguridad (BSL), materiales y residuos peligrosos (RPBI/precursores), permisos, comités de bioseguridad/bioética e incidentes. Marco federal y estatal verificado.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Laboratorios'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','laboratorios_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="laboratorios_SIGEJ.html" class="act">🧪 Laboratorios</a><a href="hospitales_SIGEJ.html">🏥 Hospitales y Salud</a><a href="sostenibilidad_SIGEJ.html">🌱 Sostenibilidad</a><a href="gobinv_SIGEJ.html">🔬 Investigación</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Gestión Jurídica de Laboratorios</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--lab:#0d7a6f;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:#eef2f7;color:var(--ink)}
header{background:linear-gradient(120deg,#0a5b52,#0d7a6f);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.92;font-size:12px;margin-top:3px}
.navbar{background:#073f39;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c6ebe4;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:var(--lab);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:var(--lab);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--lab)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:var(--lab);cursor:pointer;font-size:13px}
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
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}
.bsl{padding:2px 8px;border-radius:6px;font-size:10.5px;font-weight:700;color:#fff}
.bsl1{background:#1f9d6b}.bsl2{background:#d4a32c}.bsl3{background:#e08e0b}.bsl4{background:#c0392b}.bsln{background:#94a3b8}
.leybox{background:#f8fafc;border:1px solid var(--line);border-left:4px solid var(--lab);border-radius:10px;padding:11px 13px;margin-bottom:8px;font-size:12.5px}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🧪 Gestión Jurídica de Laboratorios</h1><div class="s">Bioseguridad (BSL) · materiales y residuos peligrosos (RPBI/precursores) · permisos y comités · incidentes · marco federal y estatal</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const LEYFED=[
 ['Ley General de Salud (establecimientos, sustancias controladas, precursores)','COFEPRIS'],
 ['Ley General para la Prevención y Gestión Integral de los Residuos (LGPGIR)','SEMARNAT'],
 ['NOM-087-SEMARNAT-SSA1-2002 — Residuos peligrosos biológico-infecciosos (RPBI)','SEMARNAT / SSA'],
 ['NOM-052-SEMARNAT-2005 — Residuos peligrosos (características CRETIB)','SEMARNAT'],
 ['Ley Federal para el Control de Precursores Químicos y Productos Químicos Esenciales','SEDENA / SAT'],
 ['Ley de Bioseguridad de Organismos Genéticamente Modificados','CIBIOGEM'],
 ['Reglamento de la Ley General de Salud en materia de investigación para la salud','CONBIOÉTICA'],
 ['Material radiactivo / fuentes selladas','CNSNS']
];
const LEYJAL=[
 ['Ley de Gestión Integral de los Residuos del Estado de Jalisco','SEMADET'],
 ['Ley Estatal del Equilibrio Ecológico y la Protección al Ambiente (Jalisco)','SEMADET / PROEPA']
];
const D={
 tipoLab:['Químico','Biológico / microbiología','Clínico','Investigación','Docencia','Bioterio / animal','Físico','Radiológico','Genómica / OGM'],
 bsl:['BSL-1','BSL-2','BSL-3','BSL-4','No aplica'],
 estLic:['Vigente','Por vencer','Vencida','En trámite','Aviso de funcionamiento'],
 catMat:['Sustancia controlada (psicotrópico/estupefaciente)','Precursor químico','Residuo peligroso (RP · CRETIB)','RPBI (biológico-infeccioso)','Material radiactivo','OGM / material genético','Reactivo peligroso'],
 autMat:['COFEPRIS','SEDENA','SEMARNAT','PROFEPA','CNSNS','CIBIOGEM','SEMADET (Jalisco)'],
 tipoBio:['Dictamen de comité de bioseguridad','Dictamen de comité de bioética','Protocolo de bioseguridad','Capacitación','Incidente','Accidente','Simulacro'],
 dictamen:['Aprobado','Aprobado con condiciones','En revisión','Rechazado','Vencido'],
 estInc:['Abierto','En atención','Cerrado'],
 cu:['CUCEI','CUCS','CUCBA','CUCEA','CUCosta','CUTonalá','CUCiénega','CULagos','CUValles','SEMS','Coord. Gral. de Investigación'],
 estGen:['Registrado','En trámite','Sin registro','Vencido']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'lb'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function LAB(){return L('sigej_lab');}
function MAT(){return L('sigej_lab_mat');}
function BIO(){return L('sigej_lab_bio');}
function bit(a){if(window.__bitlog)__bitlog('Laboratorios',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Laboratorios',texto:t,folio:f||'',modulo:'Laboratorios',leida:false});S('sigej_notificaciones',N);}
function bslTag(b){var n=(b||'').replace('BSL-','');var c=b==='No aplica'?'bsln':'bsl'+n;return '<span class="bsl '+c+'">'+esc(b||'—')+'</span>';}
function licReal(x){var d=dr(x.fVenc);if(x.estado==='Vigente'&&d!==null){if(d<0)return 'Vencida';if(d<=90)return 'Por vencer';}return x.estado;}
function seed(){if(localStorage.getItem('sigej_lab'))return;
 S('sigej_lab',[
  {id:uid(),folio:'LAB-001',nombre:'Laboratorio de Química Analítica',cu:'CUCEI',tipo:'Químico',bsl:'BSL-1',respTecnico:'Dr. Responsable',cedula:'XXXXXXX',licencia:'LS-XXXX (COFEPRIS)',aviso:'AF-XXXX',fVenc:'2026-10-15',estado:'Vigente',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
  {id:uid(),folio:'LAB-002',nombre:'Laboratorio de Microbiología',cu:'CUCS',tipo:'Biológico / microbiología',bsl:'BSL-2',respTecnico:'Q.F.B. Responsable',cedula:'XXXXXXX',licencia:'',aviso:'AF-XXXX',fVenc:'2026-08-05',estado:'Vigente',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
 ]);
 S('sigej_lab_mat',[
  {id:uid(),folio:'MAT-001',lab:'Laboratorio de Química Analítica',cat:'Precursor químico',nombre:'Ácido sulfúrico (precursor)',autoridad:'SEDENA',permiso:'PC-XXXX',cantidad:'50 L',planManejo:true,vigencia:'2026-12-31',estado:'Registrado',docs:[]},
  {id:uid(),folio:'MAT-002',lab:'Laboratorio de Microbiología',cat:'RPBI (biológico-infeccioso)',nombre:'Cultivos y cepas',autoridad:'SEMARNAT',permiso:'GEN-XXXX',cantidad:'>25 kg/mes',planManejo:true,vigencia:'2026-07-30',estado:'Registrado',docs:[]}
 ]);
 S('sigej_lab_bio',[
  {id:uid(),folio:'BIO-001',lab:'Laboratorio de Microbiología',tipo:'Dictamen de comité de bioseguridad',comite:'Comité de Bioseguridad CUCS',dictamen:'Aprobado con condiciones',riesgo:'BSL-2',fecha:'2026-05-10',estado:'Abierto',desc:'Manejo de agentes biológicos nivel 2',docs:[]}
 ]);
}

var TABS=[['t1','📊 Panel'],['t2','🧪 Laboratorios'],['t3','☣️ Materiales y residuos peligrosos'],['t4','🛡️ Bioseguridad e incidentes'],['t5','📚 Marco y reportes']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vLab();else if(VIEW==='t3')vMat();else if(VIEW==='t4')vBio();else vMarco();}

function vPanel(){var LA=LAB(),MA=MAT(),BI=BIO();
 var vig=LA.filter(function(x){return licReal(x)==='Vigente';}).length,pv=LA.filter(function(x){return licReal(x)==='Por vencer';}).length,venc=LA.filter(function(x){return licReal(x)==='Vencida';}).length;
 var bsl34=LA.filter(function(x){return /BSL-3|BSL-4/.test(x.bsl);}).length;
 var rpbi=MA.filter(function(x){return /RPBI/.test(x.cat);}).length;
 var matPv=MA.filter(function(x){var d=dr(x.vigencia);return d!==null&&d<=90;}).length;
 var inc=BI.filter(function(x){return /Incidente|Accidente/.test(x.tipo)&&x.estado!=='Cerrado';}).length;
 var bioCond=BI.filter(function(x){return /condiciones|revisi/i.test(x.dictamen||'');}).length;
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+LA.length+'</div><div class="l">Laboratorios</div></div><div class="kpi g"><div class="n">'+vig+'</div><div class="l">Licencias vigentes</div></div><div class="kpi y"><div class="n">'+pv+'</div><div class="l">Por vencer</div></div><div class="kpi r"><div class="n">'+venc+'</div><div class="l">Vencidas</div></div><div class="kpi r"><div class="n">'+bsl34+'</div><div class="l">BSL-3/4 (alto riesgo)</div></div><div class="kpi"><div class="n">'+MA.length+'</div><div class="l">Materiales/residuos peligrosos</div></div><div class="kpi y"><div class="n">'+rpbi+'</div><div class="l">RPBI</div></div><div class="kpi r"><div class="n">'+inc+'</div><div class="l">Incidentes abiertos</div></div></div>';
 var ri=[];if(venc)ri.push(venc+' licencia(s) vencida(s)');if(pv)ri.push(pv+' licencia(s) por vencer');if(matPv)ri.push(matPv+' permiso(s) de materiales por vencer');if(inc)ri.push(inc+' incidente(s) abierto(s)');
 var al=ri.length?'<div class="alert">🚨 <b>Riesgo de cumplimiento en laboratorios:</b> '+ri.join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de laboratorios</h2><p class="lead">Bioseguridad, licencias, materiales y residuos peligrosos (RPBI/precursores), comités e incidentes de los laboratorios de la Red (CUCEI, CUCS, CUCBA y afines).</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0d7a6f">Laboratorios por nivel de bioseguridad</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0d7a6f">Materiales/residuos por categoría</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La <b>NOM-087-SEMARNAT-SSA1-2002</b> obliga a los laboratorios clínicos, docentes y de investigación a manejar los <b>RPBI</b> (registro como generador ante SEMARNAT cuando se superan 25 kg/mes o 1 kg/día). Los <b>precursores químicos</b> se controlan ante <b>SEDENA</b>; las sustancias controladas ante <b>COFEPRIS</b>; los comités de bioseguridad/bioética ante <b>CONBIOÉTICA</b>. La conexión con esos padrones es fase backend.</div>';
 try{var b={};LA.forEach(function(x){b[x.bsl]=(b[x.bsl]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(b),datasets:[{data:Object.values(b),backgroundColor:['#1f9d6b','#d4a32c','#e08e0b','#c0392b','#94a3b8']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var m={};MA.forEach(function(x){var k=x.cat.replace(/ \(.*/,'').slice(0,20);m[k]=(m[k]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:Object.keys(m),datasets:[{data:Object.values(m),backgroundColor:'#0d7a6f'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
/* ---- Laboratorios ---- */
function vLab(){var LA=LAB();var q=(val('lq')||'').toLowerCase();
 var form='<div class="collap" id="lf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar laboratorio — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre *</label><input id="l_nom"></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="l_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Tipo</label><select id="l_tipo">'+opt(D.tipoLab,'')+'</select></div>'+
  '<div class="f"><label>Nivel de bioseguridad (BSL)</label><select id="l_bsl">'+opt(D.bsl,'')+'</select></div>'+
  '<div class="f"><label>Responsable técnico</label><input id="l_resp"></div>'+
  '<div class="f"><label>Cédula profesional</label><input id="l_ced"></div>'+
  '<div class="f"><label>Licencia sanitaria (COFEPRIS)</label><input id="l_lic"></div>'+
  '<div class="f"><label>Aviso de funcionamiento</label><input id="l_av"></div>'+
  '<div class="f"><label>Vigencia licencia</label><input id="l_venc" type="date"></div>'+
  '<div class="f"><label>Estado</label><select id="l_est">'+opt(D.estLic,'Vigente')+'</select></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addLab()">＋ Registrar</button> <span id="l_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var rows=LA.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:6px 0"><input id="lq" value="'+esc(val('lq'))+'" placeholder="🔎 Buscar laboratorio…" oninput="render()" style="width:100%"></div><table><tr><th>Folio</th><th>Laboratorio</th><th>Tipo</th><th>BSL</th><th>Responsable téc.</th><th>Licencia</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var er=licReal(x);var c=/Vigente/.test(er)?'g':/Vencida/.test(er)?'r':'y';return '<tr class="row" onclick="ficha(\'lab\','+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b><br><span style="font-size:10px;color:#64748b">'+esc(x.cu||'')+'</span></td><td style="font-size:11px">'+esc(x.tipo)+'</td><td>'+bslTag(x.bsl)+'</td><td style="font-size:11px">'+esc(x.respTecnico||'—')+'</td><td><span class="bdg '+c+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin laboratorios.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🧪 Laboratorios y bioseguridad</h2><p class="lead">Registro de laboratorios con su nivel de bioseguridad (BSL-1 a BSL-4), responsable técnico y licencia sanitaria.</p>'+form+tbl;
}
function addLab(){if(!val('l_nom')){el('l_msg').style.color='#c0392b';el('l_msg').textContent='Indica el nombre.';return;}
 var LA=LAB();LA.push({id:uid(),folio:'LAB-'+String(LA.length+1).padStart(3,'0'),nombre:val('l_nom'),cu:val('l_cu'),tipo:val('l_tipo'),bsl:val('l_bsl'),respTecnico:val('l_resp'),cedula:val('l_ced'),licencia:val('l_lic'),aviso:val('l_av'),fVenc:val('l_venc'),estado:val('l_est'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de laboratorio'}]});
 S('sigej_lab',LA);bit('Alta laboratorio '+val('l_nom'));var d=dr(val('l_venc'));if(d!==null&&d<=90)notif('Licencia de '+val('l_nom')+' por vencer','');if(/BSL-3|BSL-4/.test(val('l_bsl')))notif('Laboratorio '+val('l_nom')+' de alto riesgo ('+val('l_bsl')+')','');el('l_msg').style.color='#1f9d6b';el('l_msg').textContent='✓ registrado.';vLab();}
/* ---- Materiales y residuos ---- */
function vMat(){var MA=MAT();var q=(val('mq')||'').toLowerCase();
 var form='<div class="collap" id="mf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar material / residuo peligroso — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Categoría</label><select id="m_cat">'+opt(D.catMat,'')+'</select></div>'+
  '<div class="f"><label>Nombre / sustancia</label><input id="m_nom"></div>'+
  '<div class="f"><label>Laboratorio</label><input id="m_lab" list="dlLab"></div>'+
  '<div class="f"><label>Autoridad</label><select id="m_aut">'+opt(D.autMat,'')+'</select></div>'+
  '<div class="f"><label>Permiso / registro</label><input id="m_perm"></div>'+
  '<div class="f"><label>Cantidad</label><input id="m_cant"></div>'+
  '<div class="f"><label>Vigencia</label><input id="m_vig" type="date"></div>'+
  '<div class="f"><label>Estado del registro</label><select id="m_est">'+opt(D.estGen,'Registrado')+'</select></div>'+
  '<div class="f"><label>¿Plan de manejo?</label><select id="m_plan"><option>Sí</option><option>No</option></select></div>'+
  '</div><datalist id="dlLab">'+LAB().map(function(x){return '<option value="'+esc(x.nombre)+'">';}).join('')+'</datalist>'+
  '<div style="margin-top:8px"><button class="b3" onclick="addMat()">＋ Registrar</button> <span id="m_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var rows=MA.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:6px 0"><input id="mq" value="'+esc(val('mq'))+'" placeholder="🔎 Buscar material…" oninput="render()" style="width:100%"></div><table><tr><th>Folio</th><th>Sustancia</th><th>Categoría</th><th>Laboratorio</th><th>Autoridad</th><th>Plan</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var d=dr(x.vigencia);var er=x.estado==='Registrado'&&d!==null&&d<0?'Vencido':x.estado;var c=/Registrado/.test(er)?'g':/Vencido|Sin registro/.test(er)?'r':'y';return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b></td><td style="font-size:11px">'+esc(x.cat)+'</td><td style="font-size:11px">'+esc(x.lab||'—')+'</td><td style="font-size:11px">'+esc(x.autoridad)+'</td><td>'+(x.planManejo?'<span class="bdg g">Sí</span>':'<span class="bdg r">No</span>')+'</td><td><span class="bdg '+c+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="7" class="empty">Sin materiales.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">☣️ Materiales y residuos peligrosos</h2><p class="lead">Sustancias controladas, precursores químicos (SEDENA), residuos peligrosos (RP/CRETIB), RPBI (NOM-087), material radiactivo y OGM, con su permiso/registro y plan de manejo.</p>'+form+tbl;
}
function addMat(){if(!val('m_nom')){el('m_msg').style.color='#c0392b';el('m_msg').textContent='Indica la sustancia.';return;}
 var MA=MAT();MA.push({id:uid(),folio:'MAT-'+String(MA.length+1).padStart(3,'0'),lab:val('m_lab'),cat:val('m_cat'),nombre:val('m_nom'),autoridad:val('m_aut'),permiso:val('m_perm'),cantidad:val('m_cant'),planManejo:val('m_plan')==='Sí',vigencia:val('m_vig'),estado:val('m_est'),docs:[]});
 S('sigej_lab_mat',MA);bit('Alta material peligroso '+val('m_nom'));if(val('m_plan')!=='Sí'||val('m_est')==='Sin registro')notif('Material peligroso '+val('m_nom')+' sin plan de manejo/registro','');el('m_msg').style.color='#1f9d6b';el('m_msg').textContent='✓ registrado.';vMat();}
/* ---- Bioseguridad e incidentes ---- */
function vBio(){var BI=BIO();
 var form='<div class="collap" id="bf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar dictamen / protocolo / incidente — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Tipo</label><select id="b_tipo">'+opt(D.tipoBio,'')+'</select></div>'+
  '<div class="f"><label>Laboratorio</label><input id="b_lab" list="dlLab2"></div>'+
  '<div class="f"><label>Comité</label><input id="b_com"></div>'+
  '<div class="f"><label>Dictamen</label><select id="b_dic">'+opt(D.dictamen,'')+'</select></div>'+
  '<div class="f"><label>Nivel de riesgo</label><select id="b_riesgo">'+opt(D.bsl,'')+'</select></div>'+
  '<div class="f"><label>Fecha</label><input id="b_fec" type="date"></div>'+
  '<div class="f"><label>Estado (incidentes)</label><select id="b_est">'+opt(D.estInc,'')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Descripción</label><input id="b_desc"></div>'+
  '</div><datalist id="dlLab2">'+LAB().map(function(x){return '<option value="'+esc(x.nombre)+'">';}).join('')+'</datalist>'+
  '<div style="margin-top:8px"><button class="b3" onclick="addBio()">＋ Registrar</button> <span id="b_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Tipo</th><th>Laboratorio</th><th>Comité/Dictamen</th><th>Riesgo</th><th>Estado</th></tr>'+
  (BI.length?BI.map(function(x){var c=/Aprobado$/.test(x.dictamen)?'g':/Rechazado|Vencido/.test(x.dictamen)?'r':/Incidente|Accidente/.test(x.tipo)&&x.estado!=='Cerrado'?'r':'y';return '<tr><td>'+esc(x.folio)+'</td><td style="font-size:11.5px">'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.lab||'—')+'</td><td style="font-size:11px">'+esc(x.comite||'')+(x.dictamen?' · '+esc(x.dictamen):'')+'</td><td>'+esc(x.riesgo||'—')+'</td><td><span class="bdg '+c+'">'+esc(x.estado||x.dictamen||'—')+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin registros.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🛡️ Bioseguridad, comités e incidentes</h2><p class="lead">Dictámenes de comités de bioseguridad/bioética (CONBIOÉTICA), protocolos, capacitación e incidentes/accidentes de laboratorio.</p>'+form+tbl;
}
function addBio(){if(!val('b_tipo')){el('b_msg').style.color='#c0392b';el('b_msg').textContent='Indica el tipo.';return;}
 var BI=BIO();BI.push({id:uid(),folio:'BIO-'+String(BI.length+1).padStart(3,'0'),tipo:val('b_tipo'),lab:val('b_lab'),comite:val('b_com'),dictamen:val('b_dic'),riesgo:val('b_riesgo'),fecha:val('b_fec')||hoy(),estado:val('b_est'),desc:val('b_desc'),docs:[]});
 S('sigej_lab_bio',BI);bit('Alta bioseguridad '+val('b_tipo'));if(/Incidente|Accidente/.test(val('b_tipo')))notif('Incidente de laboratorio: '+val('b_desc'),'');if(/condiciones|Rechazado/.test(val('b_dic')))notif('Dictamen de bioseguridad → '+val('b_dic'),'');el('b_msg').style.color='#1f9d6b';el('b_msg').textContent='✓ registrado.';vBio();}
/* ---- Ficha (laboratorio) ---- */
function ficha(t,i){var x=LAB()[i];if(!x)return;
 var mats=MAT().filter(function(m){return m.lab===x.nombre;});
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos.</span>';
 var tz=(x.traza||[]).map(function(z){return '<div style="font-size:11px;color:#64748b">'+z.ts+' · '+esc(z.usuario)+' — '+esc(z.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0d7a6f">'+esc(x.nombre)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+' · '+esc(x.tipo)+' · '+bslTag(x.bsl)+' · '+esc(licReal(x))+'</div>'+
  '<div class="comp"><b>CU:</b> '+esc(x.cu||'—')+'<br><b>Responsable técnico:</b> '+esc(x.respTecnico||'—')+' (céd. '+esc(x.cedula||'—')+')<br><b>Licencia sanitaria:</b> '+esc(x.licencia||'—')+' · <b>Aviso:</b> '+esc(x.aviso||'—')+'<br><b>Vigencia:</b> '+esc(x.fVenc||'—')+'</div>'+
  '<div class="comp"><b>☣️ Materiales/residuos peligrosos ('+mats.length+')</b>'+(mats.length?mats.map(function(m){return '<div style="font-size:11.5px">• '+esc(m.nombre)+' — '+esc(m.cat)+' ('+esc(m.autoridad)+')'+(m.planManejo?' · plan ✓':' · <span style="color:#c0392b">sin plan</span>')+'</div>';}).join(''):'<div style="color:#64748b;font-size:12px">Sin materiales registrados.</div>')+'</div>'+
  '<div class="comp"><b>Estado de licencia</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+D.estLic.map(function(e){return '<button class="bd mini" onclick="setEstLab('+i+',\''+e+'\')">'+e.split(' ')[0]+'</button>';}).join('')+'</div></div>'+
  '<div class="comp"><b>🗂️ Expediente</b> <button class="bd mini" onclick="labAdj('+i+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEstLab(i,e){var LA=LAB();var x=LA[i];if(x.estado===e)return;x.estado=e;x.traza.push({ts:nowS(),usuario:P,accion:'Estado licencia → '+e});S('sigej_lab',LA);bit(x.folio+' → '+e);if(/Vencida/.test(e))notif('Licencia de '+x.nombre+' → '+e,x.folio);ficha('lab',i);}
var _AT=null;
function labAdj(i){_AT=i;el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Licencia sanitaria / Plan de manejo de residuos / Dictamen de bioseguridad / Bitácora / Otro):','Licencia sanitaria')||'Documento';var r=new FileReader();r.onload=function(){var LA=LAB();LA[_AT].docs=LA[_AT].docs||[];LA[_AT].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});LA[_AT].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat});S('sigej_lab',LA);ficha('lab',_AT);};r.readAsDataURL(f);};el('fileIn').click();}
/* ---- Marco y reportes ---- */
function vMarco(){
 var fed=LEYFED.map(function(x){return '<div class="leybox"><b>'+esc(x[0])+'</b><br><span style="font-size:11px;color:#64748b">Autoridad: '+esc(x[1])+'</span></div>';}).join('');
 var jal=LEYJAL.map(function(x){return '<div class="leybox" style="border-left-color:#0a4d8c"><b>'+esc(x[0])+'</b><br><span style="font-size:11px;color:#64748b">Autoridad: '+esc(x[1])+'</span></div>';}).join('');
 el('panel').innerHTML='<h2 class="h">📚 Marco legal y reportes</h2><p style="color:#64748b;font-size:12.5px;margin:0 0 12px">Ordenamientos federales y del Estado de Jalisco aplicables a los laboratorios universitarios.</p>'+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div><div style="font-weight:700;color:#0d7a6f;margin-bottom:6px">🇲🇽 Federal</div>'+fed+'</div><div><div style="font-weight:700;color:#0a4d8c;margin-bottom:6px">🏛️ Estatal (Jalisco)</div>'+jal+'</div></div>'+
  '<div style="display:flex;gap:8px;margin:8px 0"><button class="b1 mini" onclick="expCSV()">⬇️ Matriz de laboratorios (CSV)</button></div>'+
  '<div class="note">📌 Denominaciones oficiales verificadas (NOM-087-SEMARNAT-SSA1-2002, etc.). El <b>texto vigente de cada NOM/ley debe consultarse en la fuente</b>; la verificación en línea (DOF, COFEPRIS, SEMARNAT, SEDENA) es fase backend. Los datos de sustancias controladas/precursores son sensibles y de acceso restringido.</div>';
}
function expCSV(){var LA=LAB();var rows=[['Folio','Laboratorio','CU','Tipo','BSL','ResponsableTecnico','Cedula','Licencia','Aviso','Vigencia','Estado']].concat(LA.map(function(x){return [x.folio,x.nombre,x.cu,x.tipo,x.bsl,x.respTecnico,x.cedula,x.licencia,x.aviso,x.fVenc,licReal(x)];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='laboratorios_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);function clean(){try{document.querySelectorAll('div[style*="99999"]').forEach(function(o){o.remove();});var b=document.querySelector('div[style*="bottom:12px"][style*="right:12px"]');if(b)b.style.display="none";}catch(e){}}clean();setTimeout(clean,200);setTimeout(clean,800);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"laboratorios_SIGEJ.html","w",encoding="utf-8").write(out)
print("laboratorios_SIGEJ.html OK -",len(out),"bytes")
