# -*- coding: utf-8 -*-
# MÓDULO ARCHIVO (Gestión Documental) — Cuadro General de Clasificación (CGCA), Catálogo de Disposición Documental (CADIDO),
# transferencias y baja, e INVENTARIO GENERAL con trazabilidad a TODOS los módulos del SIGEJ.
# Marco real UdeG: Ley General de Archivos (DOF 15/06/2018), Ley de Archivos del Estado de Jalisco y sus Municipios,
# Lineamientos generales (mayo 2016), CGCA (2016) y CADIDO. Coordinación de Transparencia y Archivo General (CTAG).
import re
B="/Users/edithroque/Documents/CLAUDE/"
# Inventario real de ARCHIVO MUERTO (concentración) de la Coordinación de Enlace con la Red (corte feb-2025, ~2,369 expedientes).
AMJ=open(B+"archivo_muerto.json",encoding="utf-8").read()
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Archivo · Gestión Documental'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','archivo_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html" class="act">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Archivo · Gestión Documental</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1320px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1320px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:340px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}.kpi.b .n{color:var(--azul2)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:12px}
table{width:100%;border-collapse:collapse;font-size:12px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.b{background:#e6f0fb;color:#0a4d8c}.bdg.n{background:#eef2f7;color:#475569}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
input,select{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:7px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
.tree{font-size:12.5px}.tree .fondo{font-weight:800;color:var(--azul)}.tree .sec{margin:8px 0 2px;font-weight:700;color:var(--azul2)}.tree .serie{margin-left:16px;padding:3px 0;border-bottom:1px dashed #e2e8f0}
.leg{font-size:12.5px;line-height:1.6}.leg li{margin-bottom:5px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
</style></head><body>
<header><h1>🗄️ Archivo · Gestión Documental Institucional</h1><div class="s">Cuadro General de Clasificación (CGCA) · Catálogo de Disposición Documental (CADIDO) · transferencias y baja · inventario general con trazabilidad a todos los módulos</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · Alineado a la Coordinación de Transparencia y Archivo General (CTAG) · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function hoy(){return new Date().toISOString().slice(0,10);}
function pick(e,keys){for(var i=0;i<keys.length;i++){if(e&&e[keys[i]])return e[keys[i]];}return '';}
function y4(s){s=String(s||'');var m=s.match(/(\d{4})/);return m?m[1]:'';}

/* ===== Configuración de plazos (Catálogo de Disposición Documental). Ajustable; oficiales = CADIDO de la UdeG/CTAG. ===== */
function cfg(){var c=J('sigej_archivo_cfg');if(c&&c.tramite)return c;return {tramite:2,concentracion:5};}
function setCfg(t,c){localStorage.setItem('sigej_archivo_cfg',JSON.stringify({tramite:+t||2,concentracion:+c||5}));}

/* ===== Cuadro General de Clasificación Archivística (CGCA) — fondo → sección funcional → serie (módulo).
   Estructura ilustrativa alineada a las funciones de la OAG; la codificación oficial la determina la CTAG. ===== */
var SECCIONES=[
 ['1S','Asuntos contenciosos y medios alternativos',['Litigio / Contencioso','Actuaciones externas','MASC','Responsabilidades (LGRA)','Derechos Humanos']],
 ['2S','Instrumentos jurídicos y convenios',['Instrumentos Jurídicos','Servicio Social · Convenios','Asuntos Internacionales']],
 ['3S','Patrimonio y propiedad intelectual',['Patrimonio Intangible']],
 ['4S','Normatividad universitaria y asesoría',['Normatividad','Asesoría / consultas','Proyectos']],
 ['5S','Enlace con la Red y gestión especializada',['Investigación (gobierno)','Programas académicos','Laboratorios','Hospitales / Salud']],
 ['6S','Administración, recursos y control',['Administración','Auditorías','Help Desk / ITSM']],
 ['7S','Gestión documental, oficialía y transparencia',['Oficialía de Partes','Solicitudes de transparencia']]
];

/* ===== Fuentes de expedientes: TRAZABILIDAD a todos los módulos (clave localStorage → serie documental) ===== */
var SRC=[
 ['sigej_archivo_muerto','Archivo muerto (concentración)','🗄️','archivo_SIGEJ.html',function(e){return e.contenido||e.tipo||'Expediente';}],
 ['sigej_serviciosocial','Servicio Social · Convenios','🤝','serviciosocial_SIGEJ.html',function(e){return (e.dependencia||'')+(e.objeto?' · '+e.objeto:'');}],
 ['sigej_instrumentos','Instrumentos Jurídicos','📜','instrumentos_SIGEJ.html',function(e){return (e.tipo||'')+(e.obj?' · '+e.obj:'');}],
 ['sigej_oficios','Oficialía de Partes','📨','oficialia_SIGEJ.html',function(e){return (e.tipo||'')+(e.asunto?' · '+e.asunto:'');}],
 ['sigej_actuaciones','Actuaciones externas','🚶','contencioso_SIGEJ.html',function(e){return (e.tipo||'')+(e.obj?' · '+e.obj:'');}],
 ['sigej_masc','MASC','⚖️','masc_SIGEJ.html',function(e){return (e.tipo||'Convenio')+(e.actor?' · '+e.actor:'');}],
 ['sigej_resp','Responsabilidades (LGRA)','⚖️','resp_SIGEJ.html',function(e){return e.clasif||e.falta||'Procedimiento';}],
 ['sigej_deportivo','Derecho Deportivo (asuntos)','🏅','deportivo_SIGEJ.html',function(e){return (e.tipo||'')+(e.entidad?' · '+e.entidad:'');}],
 ['sigej_derechoshumanos','Derechos Humanos','🕊️','contencioso_SIGEJ.html',function(e){return (e.tipo||'')+' · '+(e.organismo||'').split(' — ')[0];}],
 ['sigej_patrimonio','Patrimonio Intangible','🧩','patrimonio_SIGEJ.html',function(e){return e.titulo||e.tipo||'Activo';}],
 ['sigej_internacional','Asuntos Internacionales','🌎','internacional_SIGEJ.html',function(e){return e.titulo||e.tipo||'Asunto';}],
 ['sigej_normatividad','Normatividad','📖','normatividad_SIGEJ.html',function(e){return (e.tipo||'')+(e.norma?' · '+e.norma:'');}],
 ['sigej_asesoria','Asesoría / consultas','💡','asesoria_SIGEJ.html',function(e){return e.asunto||e.tipo||'Consulta';}],
 ['sigej_proyectos','Proyectos','📌','proyectos_SIGEJ.html',function(e){return e.nombre||'Proyecto';}],
 ['sigej_inv_investigadores','Investigación (gobierno)','🔬','gobinv_SIGEJ.html',function(e){return e.nombre||'Investigador';}],
 ['sigej_lab','Laboratorios','🧪','laboratorios_SIGEJ.html',function(e){return (e.nombre||'')+(e.bsl?' · '+e.bsl:'');}],
 ['sigej_programas','Programas académicos','🎓','programas_SIGEJ.html',function(e){return e.nombre||'Programa';}],
 ['sigej_hosp_est','Hospitales / Salud','🏥','hospitales_SIGEJ.html',function(e){return (e.nombre||'')+(e.tipo?' · '+e.tipo:'');}],
 ['sigej_auditorias','Auditorías','🔎','auditorias_SIGEJ.html',function(e){return (e.tipo||'')+(e.obs?' · '+e.obs:'');}],
 ['sigej_adm_contable','Administración · Contable','💵','administracion_SIGEJ.html',function(e){return (e.tipo||'')+(e.concepto?' · '+e.concepto:'');}],
 ['sigej_adm_bienes','Administración · Bienes','🏷️','administracion_SIGEJ.html',function(e){return e.desc||'Bien';}],
 ['sigej_adm_personal','Administración · Personal','👥','administracion_SIGEJ.html',function(e){return (e.tipo||'')+(e.nombre?' · '+e.nombre:'');}],
 ['sigej_helpdesk','Help Desk / ITSM','🛠️','helpdesk_SIGEJ.html',function(e){return (e.tipo||'')+(e.asunto?' · '+e.asunto:'');}],
 ['sigej_uti','Solicitudes de transparencia','🔎','transparencia_general_SIGEJ.html',function(e){return (e.texto||'Solicitud').slice(0,50);}]
];
var ACTIVO=/(solicitud|elaboraci|revisi|firma|vigente|por vencer|en curso|en tr[aá]mite|abierto|nuevo|pendiente|en proceso|asignad|captur)/i;
var CONCL=/(concluid|terminad|cancelad|cerrad|archivad|cumplid|resuelt|vencid|baja|improceden|desechad|finaliz)/i;

var AM_SEED=__AMSEED__;
function seedAM(){if(!localStorage.getItem('sigej_archivo_muerto'))localStorage.setItem('sigej_archivo_muerto',JSON.stringify(AM_SEED));}
function loadAll(){var out=[];var c=cfg();
 SRC.forEach(function(s){J(s[0]).forEach(function(e,idx){
  var estado=String(pick(e,['estado','est','estatus','cumplimiento','prodep'])||'');
  var apertura=pick(e,['fApertura','fapertura','fAlta','fRecep','ini','creado','firma','fecha','fsol','adq']);
  var conclusion=pick(e,['fConclusion','fcierre','fFin','fconclusion']);
  var fin=pick(e,['fin','fVenc','venceSol','termino']);
  var etiqueta=pick(e,['etiqueta']);
  var folio=pick(e,['folio','num','exp','id'])||(s[0].replace('sigej_','').toUpperCase()+'-'+(idx+1));
  var vivo=ACTIVO.test(estado)&&!CONCL.test(estado);
  if(!estado){ // sin estado: si hay fin pasado, se considera concluido
   vivo=!(fin&&fin<hoy());
  }
  var base=conclusion||fin||'';var h=hoy();var fase,fT,fB;
  var transferido=!!e._archTransfer;var fReal=e._archTransferFecha||'';var tFolio=e._archTransferFolio||'';
  var baja=!!e._archBaja;var bFolio=e._archBajaFolio||'';var bFecha=e._archBajaFecha||'';
  if(vivo){fase='Trámite';fT='';fB='';}
  else if(transferido){fT=fReal;fB=addY(fReal,c.concentracion);fase=(fB&&h>=fB)?'Histórico / Baja':'Concentración';}
  else {fT=addY(base,c.tramite);fB=fT?addY(fT,c.concentracion):'';if(fT&&h>=fB)fase='Histórico / Baja';else if(fT&&h>=fT)fase='Concentración';else fase='Trámite (por transferir)';}
  if(baja)fase='Baja documental (autorizada)';
  out.push({srcKey:s[0],srcIdx:idx,modulo:s[1],ic:s[2],link:s[3],folio:String(folio),tit:s[4](e),estado:estado||'—',apertura:apertura||'',conclusion:conclusion||fin||'',fase:fase,fTransfer:fT,fBaja:fB,transferido:transferido,transferFolio:tFolio,baja:baja,bajaFolio:bFolio,bajaFecha:bFecha,etiqueta:etiqueta||'',anio:y4(apertura||fin||conclusion),txt:norm([folio,s[4](e),s[1],estado,etiqueta].join(' '))});
 });});
 return out;}
function addY(f,n){if(!f)return '';var d=new Date(String(f).slice(0,10)+'T00:00:00');if(isNaN(d))return '';d.setFullYear(d.getFullYear()+(+n||0));return d.toISOString().slice(0,10);}
function faseClass(f){return /Baja|Histórico/.test(f)?'r':/Concentración/.test(f)?'y':/por transferir/i.test(f)?'b':'g';}

var TABS=[['t1','🗄️ Panel'],['t2','📇 Cuadro de clasificación (CGCA)'],['t3','📋 Disposición documental (CADIDO)'],['t4','🔄 Transferencias y baja'],['t7','📚 Registro de actas'],['t5','🔍 Inventario general'],['t6','⚖️ Normatividad']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){if(VIEW==='t1')vPanel();else if(VIEW==='t2')vCGCA();else if(VIEW==='t3')vCADIDO();else if(VIEW==='t4')vTrans();else if(VIEW==='t7')vActas();else if(VIEW==='t5')vInv();else vNorm();}
/* ===== Registro de actas (transferencias y bajas) ===== */
function logActa(o){var L=J('sigej_archivo_actas');L.push(o);localStorage.setItem('sigej_archivo_actas',JSON.stringify(L));}
function esPermanente(mod){return /Normatividad|Patrimonio|Instrumentos|Derechos Humanos/.test(mod);}
function nextBaja(){var s=(+(localStorage.getItem('sigej_archivo_baja_seq')||0))+1;localStorage.setItem('sigej_archivo_baja_seq',s);return s;}

function vPanel(){var A=loadAll();var f={};A.forEach(function(x){f[x.fase]=(f[x.fase]||0)+1;});
 var byMod={};A.forEach(function(x){byMod[x.modulo]=(byMod[x.modulo]||0)+1;});
 var kp='<div class="kpis"><div class="kpi b"><div class="n">'+A.length+'</div><div class="l">Expedientes en el sistema</div></div>'+
  '<div class="kpi g"><div class="n">'+(f['Trámite']||0)+'</div><div class="l">Archivo de trámite</div></div>'+
  '<div class="kpi b"><div class="n">'+(f['Trámite (por transferir)']||0)+'</div><div class="l">Por transferir</div></div>'+
  '<div class="kpi y"><div class="n">'+(f['Concentración']||0)+'</div><div class="l">Archivo de concentración</div></div>'+
  '<div class="kpi r"><div class="n">'+(f['Histórico / Baja']||0)+'</div><div class="l">Histórico / baja</div></div>'+
  '<div class="kpi"><div class="n">'+SRC.length+'</div><div class="l">Módulos con trazabilidad</div></div></div>';
 el('panel').innerHTML='<h2 class="h">🗄️ Panel de archivo institucional</h2><p class="lead">Ciclo vital documental (Ley General de Archivos): trámite → concentración → histórico/baja, agregado desde <b>todos los módulos</b> del SIGEJ.</p>'+kp+
  '<div class="grid"><div class="card"><b style="color:#0a4d8c">Expedientes por fase archivística</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Expedientes por serie / módulo</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="grid"><div class="card"><b style="color:#0a4d8c">Expedientes por año de apertura</b><canvas id="c3" height="150"></canvas></div></div>'+
  '<div class="note">🏛️ Alineado a la <b>Coordinación de Transparencia y Archivo General (CTAG)</b> de la UdeG. Los instrumentos oficiales (CGCA 2016 y CADIDO) y los plazos de conservación los emite la CTAG; este módulo los operacionaliza sobre los expedientes vivos del sistema.</div>';
 try{if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(f),datasets:[{data:Object.values(f),backgroundColor:['#15803d','#0a4d8c','#b45309','#c0392b']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var mk=Object.keys(byMod).sort(function(a,b){return byMod[b]-byMod[a];});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:mk.map(function(k){return k.length>22?k.slice(0,22)+'…':k;}),datasets:[{data:mk.map(function(k){return byMod[k];}),backgroundColor:'#0a4d8c'}]},options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{y:{ticks:{font:{size:8}}}}}});
  var ya={};A.forEach(function(x){if(x.anio)ya[x.anio]=(ya[x.anio]||0)+1;});var yk=Object.keys(ya).sort();if(window.__c3)__c3.destroy();window.__c3=new Chart(el('c3'),{type:'bar',data:{labels:yk,datasets:[{data:yk.map(function(k){return ya[k];}),backgroundColor:'#1aa39a'}]},options:{plugins:{legend:{display:false}}}});}catch(e){}
}
function vCGCA(){var A=loadAll();var cnt={};A.forEach(function(x){cnt[x.modulo]=(cnt[x.modulo]||0)+1;});
 var tree='<div class="tree"><div class="fondo">📁 Fondo: Universidad de Guadalajara · Oficina de la Abogacía General</div>'+
  SECCIONES.map(function(sec){return '<div class="sec">'+sec[0]+' · '+sec[1]+'</div>'+sec[2].map(function(serie){var n=0;Object.keys(cnt).forEach(function(m){if(m.indexOf(serie)>=0||serie.indexOf(m)>=0)n+=cnt[m];});return '<div class="serie">📄 '+esc(serie)+' <span class="bdg n">'+n+' exp.</span></div>';}).join('');}).join('')+'</div>';
 el('panel').innerHTML='<h2 class="h">📇 Cuadro General de Clasificación Archivística (CGCA)</h2><p class="lead">Estructura funcional: <b>fondo → sección → serie documental</b>. Cada módulo del SIGEJ es una serie documental.</p>'+
  '<div class="card">'+tree+'</div>'+
  '<div class="note">📐 El CGCA de la UdeG fue desarrollado en 2016 por la CTAG y refleja la estructura funcional institucional. La codificación oficial (fondo/sección/serie) la determina la CTAG; aquí se presenta la organización funcional de la OAG con el conteo real de expedientes por serie.</div>';
}
function vCADIDO(){var c=cfg();var A=loadAll();
 var series=[];SECCIONES.forEach(function(sec){sec[2].forEach(function(s){series.push([sec[0],s]);});});
 var rows=series.map(function(p){var n=0;A.forEach(function(x){if(x.modulo.indexOf(p[1])>=0||p[1].indexOf(x.modulo)>=0)n++;});
  var perm=/Normatividad|Patrimonio|Instrumentos|Derechos Humanos/.test(p[1]);
  return '<tr><td>'+p[0]+'</td><td><b>'+esc(p[1])+'</b></td><td>'+n+'</td><td>'+c.tramite+' años</td><td>'+c.concentracion+' años</td><td>'+(perm?'Administrativo, legal e <b>histórico</b>':'Administrativo y legal')+'</td><td><span class="bdg '+(perm?'g':'y')+'">'+(perm?'Conservación permanente':'Baja documental')+'</span></td></tr>';}).join('');
 el('panel').innerHTML='<h2 class="h">📋 Catálogo de Disposición Documental (CADIDO)</h2><p class="lead">Valores documentales, vigencia y plazos de conservación por serie, y disposición final (baja o conservación permanente).</p>'+
  '<div class="card" style="border-left:4px solid #0a4d8c"><b style="color:#0a4d8c">⏱️ Plazos de conservación (configurables)</b><div style="display:flex;gap:8px;flex-wrap:wrap;align-items:end;margin-top:6px"><div style="max-width:150px"><label style="font-size:11px;color:#64748b">Años en trámite</label><input id="cf_t" type="number" min="0" value="'+c.tramite+'"></div><div style="max-width:150px"><label style="font-size:11px;color:#64748b">Años en concentración</label><input id="cf_c" type="number" min="0" value="'+c.concentracion+'"></div><button class="b1 mini" onclick="guardarCfg()">Guardar plazos</button> <span id="cf_msg" style="font-size:12px;color:#1f9d6b"></span></div></div>'+
  '<div class="card" style="overflow:auto"><table><tr><th>Sección</th><th>Serie documental</th><th>Exp.</th><th>Vigencia (trámite)</th><th>Concentración</th><th>Valores documentales</th><th>Disposición final</th></tr>'+rows+'</table></div>'+
  '<div class="note">⚖️ Los <b>valores documentales</b> (administrativo, legal, fiscal, contable, histórico), la <b>vigencia documental</b> y los <b>plazos de conservación</b> oficiales los fija el <b>CADIDO</b> aprobado por la CTAG y el Grupo Interdisciplinario. Los valores mostrados son de referencia y ajustables.</div>';
}
function guardarCfg(){setCfg(el('cf_t').value,el('cf_c').value);el('cf_msg').textContent='✓ Plazos guardados.';render();}
function vTrans(){var A=loadAll();
 var porTransf=A.filter(function(x){return x.fase==='Trámite (por transferir)';});
 var enConc=A.filter(function(x){return x.fase==='Concentración';});
 var baja=A.filter(function(x){return x.fase==='Histórico / Baja';});
 function tabla(arr,tipo){return arr.length?('<div class="card" style="overflow:auto"><table><tr><th>Serie</th><th>Folio</th><th>Asunto</th><th>Conclusión</th><th>'+tipo+'</th><th>Etiqueta</th></tr>'+arr.slice(0,400).map(function(x){return '<tr class="row" onclick="location.href=\''+x.link+'\'"><td>'+x.ic+' '+esc(x.modulo)+'</td><td>'+esc(x.folio)+'</td><td>'+esc(x.tit).slice(0,60)+'</td><td>'+esc(x.conclusion||'—')+'</td><td>'+esc(tipo==='Fecha de baja'?x.fBaja:x.fTransfer)+'</td><td>'+esc(x.etiqueta||'—')+'</td></tr>';}).join('')+'</table>'+(arr.length>400?'<div style="font-size:11px;color:#64748b;padding:6px">Mostrando 400 de '+arr.length+'.</div>':'')+'</div>'):'<div class="card" style="color:#64748b;font-size:12px">Ninguno.</div>';}
 var series=[];porTransf.forEach(function(x){if(series.indexOf(x.modulo)<0)series.push(x.modulo);});series.sort();
 el('panel').innerHTML='<h2 class="h">🔄 Transferencias y baja documental</h2><p class="lead">Expedientes según su etapa: transferencia primaria (trámite→concentración), permanencia en concentración y baja documental / histórico.</p>'+
  '<div class="kpis"><div class="kpi b"><div class="n">'+porTransf.length+'</div><div class="l">Transferencia primaria (a concentración)</div></div><div class="kpi y"><div class="n">'+enConc.length+'</div><div class="l">En concentración</div></div><div class="kpi r"><div class="n">'+baja.length+'</div><div class="l">Baja / histórico</div></div></div>'+
  '<div style="display:flex;gap:8px;margin-bottom:8px;flex-wrap:wrap"><button class="bd mini" onclick="expInv()">⬇️ Cuadro de archivo (CSV)</button><button class="bd mini" onclick="expInvWord()">📄 Inventario (Word/oficio)</button></div>'+
  '<div class="card" style="border-left:4px solid #0a4d8c"><b style="color:#0a4d8c">📄 Relación de entrega-recepción · transferencia primaria a concentración</b><p style="font-size:11.5px;color:#64748b;margin:4px 0 8px">Genera el acta formal (Word) de transferencia de los expedientes «por transferir» de una serie al archivo de concentración, conforme a la Ley General de Archivos.</p><div style="display:flex;gap:8px;flex-wrap:wrap;align-items:end"><div style="max-width:300px;flex:1"><label style="font-size:11px;color:#64748b">Serie / área que transfiere</label><select id="tr_serie"><option value="">Todas las series listas para transferir</option>'+series.map(function(m){return '<option>'+esc(m)+'</option>';}).join('')+'</select></div><button class="b1 mini" onclick="expTransferWord()">📄 Generar relación de entrega-recepción</button></div></div>'+
  '<h2 class="h" style="font-size:14px">📥 Listos para transferencia primaria</h2>'+tabla(porTransf,'Fecha de transferencia')+
  '<h2 class="h" style="font-size:14px">🗃️ En archivo de concentración</h2>'+tabla(enConc,'Fecha de baja')+
  '<h2 class="h" style="font-size:14px">⏰ Baja documental / histórico (vencidos)</h2>'+
  (function(){var bser=[];baja.forEach(function(x){if(!esPermanente(x.modulo)&&bser.indexOf(x.modulo)<0)bser.push(x.modulo);});bser.sort();
   return '<div class="card" style="border-left:4px solid #7a1f1f"><b style="color:#7a1f1f">🗑️ Acta de baja documental</b><p style="font-size:11.5px;color:#64748b;margin:4px 0 8px">Genera el acta de baja (Word) de los expedientes que ya cumplieron su plazo en concentración, con dictamen del <b>Grupo Interdisciplinario</b>. Las series de <b>conservación permanente</b> (Normatividad, Patrimonio, Instrumentos, DH) NO se dan de baja: pasan al archivo histórico.</p><div style="display:flex;gap:8px;flex-wrap:wrap;align-items:end"><div style="max-width:300px;flex:1"><label style="font-size:11px;color:#64748b">Serie / área</label><select id="bj_serie"><option value="">Todas las series susceptibles de baja</option>'+bser.map(function(m){return '<option>'+esc(m)+'</option>';}).join('')+'</select></div><button class="b1 mini" style="background:#7a1f1f" onclick="expBajaWord()">🗑️ Generar acta de baja documental</button></div></div>';})()+
  tabla(baja,'Fecha de baja');
}
function vInv(){var A=loadAll();var q=norm(inv_q()),fm=inv_f('inv_mod'),ff=inv_f('inv_fase'),fa=inv_f('inv_anio');
 var mods=[];A.forEach(function(x){if(mods.indexOf(x.modulo)<0)mods.push(x.modulo);});mods.sort();
 var anios=[];A.forEach(function(x){if(x.anio&&anios.indexOf(x.anio)<0)anios.push(x.anio);});anios.sort();
 var rows=A.filter(function(x){return (!q||x.txt.indexOf(q)>=0)&&(!fm||x.modulo===fm)&&(!ff||x.fase===ff)&&(!fa||x.anio===fa);});
 var ctrl='<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(140px,1fr));margin-bottom:8px"><input id="inv_q" value="'+esc(inv_q())+'" placeholder="🔎 Folio / asunto / serie" oninput="render()"><select id="inv_mod" onchange="render()"><option value="">Toda serie</option>'+mods.map(function(m){return '<option'+(m===fm?' selected':'')+'>'+esc(m)+'</option>';}).join('')+'</select><select id="inv_fase" onchange="render()"><option value="">Toda fase</option>'+['Trámite','Trámite (por transferir)','Concentración','Histórico / Baja','Baja documental (autorizada)'].map(function(m){return '<option'+(m===ff?' selected':'')+'>'+m+'</option>';}).join('')+'</select><select id="inv_anio" onchange="render()"><option value="">Todo año</option>'+anios.map(function(m){return '<option'+(m===fa?' selected':'')+'>'+m+'</option>';}).join('')+'</select></div>';
 var tbl='<div class="card" style="overflow:auto"><table><tr><th>Serie / módulo</th><th>Folio</th><th>Asunto</th><th>Apertura</th><th>Conclusión</th><th>Fase</th><th>Transferencia</th><th>Baja</th><th>Etiqueta</th><th>Carátula</th></tr>'+
  (rows.length?rows.slice(0,600).map(function(x){return '<tr class="row" onclick="location.href=\''+x.link+'\'"><td>'+x.ic+' '+esc(x.modulo)+'</td><td>'+esc(x.folio)+'</td><td>'+esc(x.tit).slice(0,50)+'</td><td>'+esc(x.apertura||'—')+'</td><td>'+esc(x.conclusion||'—')+'</td><td><span class="bdg '+faseClass(x.fase)+'">'+esc(x.fase)+'</span>'+(x.transferido?' <span style="font-size:9px;color:#64748b" title="Transferido">📄'+esc(x.transferFolio)+'</span>':'')+'</td><td>'+esc(x.fTransfer||'—')+'</td><td>'+esc(x.fBaja||'—')+'</td><td>'+esc(x.etiqueta||'—')+'</td><td><button class="bd mini" title="Carátula imprimible" onclick="event.stopPropagation();caratula(\''+x.srcKey+'\','+x.srcIdx+')">🏷️</button></td></tr>';}).join(''):'<tr><td colspan="10" style="text-align:center;color:#64748b;padding:16px">Sin coincidencias.</td></tr>')+'</table>'+(rows.length>600?'<div style="font-size:11px;color:#64748b;padding:6px">Mostrando 600 de '+rows.length+'. Afina el filtro o exporta el inventario completo.</div>':'')+'</div>';
 el('panel').innerHTML='<h2 class="h">🔍 Inventario general de expedientes</h2><p class="lead">'+A.length+' expedientes de '+SRC.length+' módulos, con su metadato archivístico. '+rows.length+' en el filtro.</p><div style="display:flex;gap:8px;margin-bottom:8px;flex-wrap:wrap"><button class="b1 mini" onclick="expInv()">⬇️ Inventario general (CSV)</button><button class="bd mini" onclick="expInvWord()">📄 Inventario (Word/oficio)</button></div>'+ctrl+tbl;
}
function inv_q(){var e=el('inv_q');return e?e.value.trim():'';}
function inv_f(id){var e=el(id);return e?e.value:'';}
function invFiltered(){var A=loadAll();var q=norm(inv_q()),fm=inv_f('inv_mod'),ff=inv_f('inv_fase'),fa=inv_f('inv_anio');
 if(!q&&!fm&&!ff&&!fa)return A;
 return A.filter(function(x){return (!q||x.txt.indexOf(q)>=0)&&(!fm||x.modulo===fm)&&(!ff||x.fase===ff)&&(!fa||x.anio===fa);});}
function expInv(){var A=invFiltered();var rows=[['Serie/Modulo','Folio','Asunto','Estado','Apertura','Conclusion','Fase archivistica','Fecha transferencia','Fecha baja','Etiqueta archivo muerto']].concat(A.map(function(x){return [x.modulo,x.folio,x.tit,x.estado,x.apertura,x.conclusion,x.fase,x.fTransfer,x.fBaja,x.etiqueta];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='inventario_general_archivo_'+hoy()+'.csv';a.click();}
function expInvWord(){var A=invFiltered();var c=cfg();var f={};A.forEach(function(x){f[x.fase]=(f[x.fase]||0)+1;});
 var resumen=Object.keys(f).map(function(k){return k+': '+f[k];}).join(' · ');
 var perfil=localStorage.getItem('sigej_perfil')||'________________________';
 var filtro=(inv_q()||inv_f('inv_mod')||inv_f('inv_fase')||inv_f('inv_anio'))?'Selección filtrada':'Inventario completo';
 var head='<div style="text-align:center"><div style="font-size:13pt;font-weight:bold">UNIVERSIDAD DE GUADALAJARA</div><div style="font-size:11pt">Oficina de la Abogacía General · Coordinación de Enlace con la Red</div><div style="font-size:10pt">Área Coordinadora de Archivos · alineado a la Coordinación de Transparencia y Archivo General (CTAG)</div></div>';
 var meta='<p style="font-size:10.5pt"><b>ASUNTO:</b> Inventario General de Archivo — Cuadro de transferencia y disposición documental.<br><b>FECHA:</b> '+hoy()+' &nbsp; <b>ALCANCE:</b> '+filtro+' ('+A.length+' expedientes).<br><b>FUNDAMENTO:</b> Ley General de Archivos (DOF 15/06/2018); Ley de Archivos del Estado de Jalisco y sus Municipios. Plazos de conservación: '+c.tramite+' años en trámite y '+c.concentracion+' años en concentración (referencia; oficiales según el CADIDO de la UdeG/CTAG).<br><b>RESUMEN POR FASE:</b> '+resumen+'.</p>';
 var th='<tr style="background:#0a4d8c;color:#fff"><th>Serie / módulo</th><th>Folio</th><th>Asunto</th><th>Apertura</th><th>Conclusión</th><th>Fase archivística</th><th>Transferencia</th><th>Baja</th><th>Etiqueta A.M.</th></tr>';
 var body=A.map(function(x){return '<tr><td>'+esc(x.modulo)+'</td><td>'+esc(x.folio)+'</td><td>'+esc(x.tit).slice(0,70)+'</td><td>'+esc(x.apertura||'—')+'</td><td>'+esc(x.conclusion||'—')+'</td><td>'+esc(x.fase)+'</td><td>'+esc(x.fTransfer||'—')+'</td><td>'+esc(x.fBaja||'—')+'</td><td>'+esc(x.etiqueta||'—')+'</td></tr>';}).join('');
 var firma='<br><br><table style="width:100%;border:none"><tr><td style="border:none;text-align:center;width:50%">_______________________________<br>Elaboró · Responsable del archivo de trámite<br>'+esc(perfil)+'</td><td style="border:none;text-align:center;width:50%">_______________________________<br>Vo. Bo. · Coordinación de Enlace con la Red<br>Oficina de la Abogacía General</td></tr></table>';
 var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><style>body{font-family:Cambria,serif;font-size:10pt}table{border-collapse:collapse;width:100%;font-size:8.5pt}th,td{border:1px solid #999;padding:3px 4px;text-align:left}</style></head><body>'+head+'<hr>'+meta+'<table>'+th+body+'</table>'+firma+'<p style="font-size:8pt;color:#555;margin-top:10px">Documento generado por SIGEJ-UdeG · La aprobación formal de transferencias y bajas corresponde a la CTAG y al Grupo Interdisciplinario.</p></body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='inventario_general_archivo_'+hoy()+'.doc';a.click();}
function nextTransfer(){var s=(+(localStorage.getItem('sigej_archivo_transfer_seq')||0))+1;localStorage.setItem('sigej_archivo_transfer_seq',s);return s;}
function valorDoc(mod){return /Normatividad|Patrimonio|Instrumentos|Derechos Humanos/.test(mod)?'Administrativo, legal e histórico':'Administrativo y legal';}
function expTransferWord(){var serieSel=(el('tr_serie')?el('tr_serie').value:'');var c=cfg();
 var A=loadAll().filter(function(x){return x.fase==='Trámite (por transferir)'&&(!serieSel||x.modulo===serieSel);});
 if(!A.length){alert('No hay expedientes listos para transferencia primaria'+(serieSel?' en la serie seleccionada.':'.'));return;}
 A.sort(function(a,b){return (a.conclusion||'').localeCompare(b.conclusion||'');});
 if(!confirm('Se generará el acta y se marcarán '+A.length+' expediente(s) como TRANSFERIDOS al archivo de concentración con fecha '+hoy()+'. El inventario reflejará el cambio de fase. ¿Continuar?')){return;}
 var seq=nextTransfer();var folio='TP-'+(new Date().getFullYear())+'-'+String(seq).padStart(4,'0');
 var perfil=localStorage.getItem('sigej_perfil')||'________________________';
 var serieName=serieSel||'Varias series de la Oficina de la Abogacía General';
 var fechas=A.map(function(x){return x.apertura||x.conclusion;}).filter(Boolean).sort();
 var extremas=(fechas[0]||'—')+' a '+(fechas[fechas.length-1]||'—');
 var bajaMin=A.map(function(x){return x.fBaja;}).filter(Boolean).sort()[0]||'—';
 var head='<div style="text-align:center"><div style="font-size:13pt;font-weight:bold">UNIVERSIDAD DE GUADALAJARA</div><div style="font-size:11pt">Oficina de la Abogacía General · Coordinación de Enlace con la Red</div><div style="font-size:11pt;font-weight:bold;margin-top:6px">INVENTARIO DE TRANSFERENCIA PRIMARIA<br>RELACIÓN DE ENTREGA-RECEPCIÓN AL ARCHIVO DE CONCENTRACIÓN</div></div>';
 var meta='<table style="width:100%;font-size:10pt;border:none;margin-top:8px"><tr><td style="border:none"><b>No. de transferencia:</b> '+folio+'</td><td style="border:none"><b>Fecha:</b> '+hoy()+'</td></tr>'+
  '<tr><td style="border:none" colspan="2"><b>Área / serie que transfiere (archivo de trámite):</b> '+esc(serieName)+'</td></tr>'+
  '<tr><td style="border:none" colspan="2"><b>Área receptora:</b> Archivo de Concentración de la Universidad de Guadalajara</td></tr>'+
  '<tr><td style="border:none"><b>Expedientes transferidos:</b> '+A.length+'</td><td style="border:none"><b>Fechas extremas:</b> '+extremas+'</td></tr>'+
  '<tr><td style="border:none" colspan="2"><b>Plazo de conservación en concentración:</b> '+c.concentracion+' años (baja a partir de '+bajaMin+', según CADIDO)</td></tr></table>'+
  '<p style="font-size:9.5pt"><b>Fundamento:</b> Ley General de Archivos (DOF 15/06/2018), art. relativo a la transferencia primaria — traslado controlado y sistemático de expedientes de consulta esporádica del archivo de trámite al archivo de concentración; y Ley de Archivos del Estado de Jalisco y sus Municipios.</p>';
 var th='<tr style="background:#0a4d8c;color:#fff"><th>No.</th><th>Serie documental</th><th>No. de expediente / folio</th><th>Asunto / descripción</th><th>Fechas extremas</th><th>Fojas</th><th>Valores documentales</th><th>Vigencia en concentración (baja)</th><th>Ubicación / etiqueta</th></tr>';
 var body=A.map(function(x,i){return '<tr><td>'+(i+1)+'</td><td>'+esc(x.modulo)+'</td><td>'+esc(x.folio)+'</td><td>'+esc(x.tit).slice(0,70)+'</td><td>'+esc(x.apertura||'—')+' a '+esc(x.conclusion||'—')+'</td><td>—</td><td>'+valorDoc(x.modulo)+'</td><td>'+esc(x.fBaja||'—')+'</td><td>'+esc(x.etiqueta||'—')+'</td></tr>';}).join('');
 var firma='<br><br><table style="width:100%;border:none;font-size:10pt"><tr><td style="border:none;text-align:center;width:33%">_____________________________<br>ENTREGA<br>Responsable del archivo de trámite<br>'+esc(perfil)+'</td><td style="border:none;text-align:center;width:33%">_____________________________<br>RECIBE<br>Responsable del archivo de concentración</td><td style="border:none;text-align:center;width:34%">_____________________________<br>Vo. Bo.<br>Área Coordinadora de Archivos (CTAG)</td></tr></table>';
 var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><style>body{font-family:Cambria,serif;font-size:10pt}table{border-collapse:collapse;width:100%;font-size:8.5pt}th,td{border:1px solid #999;padding:3px 4px;text-align:left;vertical-align:top}</style></head><body>'+head+'<hr>'+meta+'<table>'+th+body+'</table>'+firma+'<p style="font-size:8pt;color:#555;margin-top:10px">Documento generado por SIGEJ-UdeG ('+folio+'). La aprobación formal de la transferencia y su cotejo físico corresponde a la CTAG y al Grupo Interdisciplinario.</p></body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='relacion_entrega_recepcion_'+folio+'.doc';a.click();
 // Marcar la transferencia como efectuada (fecha real + folio) en cada módulo de origen → el inventario cambia de fase a Concentración.
 var byKey={};A.forEach(function(x){(byKey[x.srcKey]=byKey[x.srcKey]||[]).push(x.srcIdx);});
 Object.keys(byKey).forEach(function(k){var arr=J(k);byKey[k].forEach(function(ix){if(arr[ix]){arr[ix]._archTransfer=true;arr[ix]._archTransferFecha=hoy();arr[ix]._archTransferFolio=folio;}});localStorage.setItem(k,JSON.stringify(arr));});
 logActa({folio:folio,tipo:'Transferencia primaria',fecha:hoy(),serie:serieName,n:A.length});
 if(window.__bitlog)__bitlog('Archivo · Gestión Documental','Transferencia primaria '+folio+' efectuada — '+A.length+' expedientes a concentración');
 alert('✅ Acta '+folio+' generada. '+A.length+' expediente(s) marcados como transferidos al archivo de concentración (fecha '+hoy()+').');
 render();}
function expBajaWord(){var serieSel=(el('bj_serie')?el('bj_serie').value:'');var c=cfg();
 var A=loadAll().filter(function(x){return x.fase==='Histórico / Baja'&&!esPermanente(x.modulo)&&(!serieSel||x.modulo===serieSel);});
 if(!A.length){alert('No hay expedientes con plazo de conservación cumplido y susceptibles de baja'+(serieSel?' en la serie seleccionada.':'.')+' (Las series de conservación permanente van al archivo histórico, no a baja.)');return;}
 A.sort(function(a,b){return (a.conclusion||'').localeCompare(b.conclusion||'');});
 if(!confirm('Se generará el ACTA DE BAJA DOCUMENTAL y se marcarán '+A.length+' expediente(s) como dados de baja (fecha '+hoy()+'). Esta acción refleja la eliminación documental autorizada. ¿Continuar?')){return;}
 var seq=nextBaja();var folio='BD-'+(new Date().getFullYear())+'-'+String(seq).padStart(4,'0');
 var perfil=localStorage.getItem('sigej_perfil')||'________________________';
 var serieName=serieSel||'Varias series de la Oficina de la Abogacía General';
 var fechas=A.map(function(x){return x.apertura||x.conclusion;}).filter(Boolean).sort();var extremas=(fechas[0]||'—')+' a '+(fechas[fechas.length-1]||'—');
 var head='<div style="text-align:center"><div style="font-size:13pt;font-weight:bold">UNIVERSIDAD DE GUADALAJARA</div><div style="font-size:11pt">Oficina de la Abogacía General · Coordinación de Enlace con la Red</div><div style="font-size:11pt;font-weight:bold;margin-top:6px">ACTA DE BAJA DOCUMENTAL</div></div>';
 var meta='<table style="width:100%;font-size:10pt;border:none;margin-top:8px"><tr><td style="border:none"><b>No. de baja:</b> '+folio+'</td><td style="border:none"><b>Fecha:</b> '+hoy()+'</td></tr>'+
  '<tr><td style="border:none" colspan="2"><b>Serie / área:</b> '+esc(serieName)+'</td></tr>'+
  '<tr><td style="border:none"><b>Expedientes propuestos a baja:</b> '+A.length+'</td><td style="border:none"><b>Fechas extremas:</b> '+extremas+'</td></tr></table>'+
  '<p style="font-size:9.5pt"><b>Fundamento:</b> Ley General de Archivos (DOF 15/06/2018) — <i>baja documental</i>: eliminación de la documentación que ha prescrito su vigencia, valores documentales y, en su caso, plazos de conservación (concentración: '+c.concentracion+' años); y Ley de Archivos del Estado de Jalisco y sus Municipios. Requiere dictamen de valoración y autorización del <b>Grupo Interdisciplinario</b> y del Archivo General.</p>';
 var th='<tr style="background:#7a1f1f;color:#fff"><th>No.</th><th>Serie documental</th><th>No. de expediente / folio</th><th>Asunto / descripción</th><th>Fechas extremas</th><th>Vigencia cumplida (concentración)</th><th>Valores documentales</th><th>Etiqueta A.M.</th></tr>';
 var body=A.map(function(x,i){return '<tr><td>'+(i+1)+'</td><td>'+esc(x.modulo)+'</td><td>'+esc(x.folio)+'</td><td>'+esc(x.tit).slice(0,70)+'</td><td>'+esc(x.apertura||'—')+' a '+esc(x.conclusion||'—')+'</td><td>'+esc(x.fBaja||'—')+'</td><td>'+valorDoc(x.modulo)+'</td><td>'+esc(x.etiqueta||'—')+'</td></tr>';}).join('');
 var firma='<br><br><table style="width:100%;border:none;font-size:10pt"><tr><td style="border:none;text-align:center;width:33%">_____________________________<br>SOLICITA<br>Responsable del archivo de concentración<br>'+esc(perfil)+'</td><td style="border:none;text-align:center;width:33%">_____________________________<br>DICTAMINA · Vo. Bo.<br>Grupo Interdisciplinario</td><td style="border:none;text-align:center;width:34%">_____________________________<br>AUTORIZA<br>Área Coordinadora de Archivos (CTAG)</td></tr></table>';
 var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><style>body{font-family:Cambria,serif;font-size:10pt}table{border-collapse:collapse;width:100%;font-size:8.5pt}th,td{border:1px solid #999;padding:3px 4px;text-align:left;vertical-align:top}</style></head><body>'+head+'<hr>'+meta+'<table>'+th+body+'</table>'+firma+'<p style="font-size:8pt;color:#555;margin-top:10px">Documento generado por SIGEJ-UdeG ('+folio+'). La baja documental es definitiva y requiere la aprobación formal del Grupo Interdisciplinario y de la CTAG; las series de conservación permanente NO se dan de baja (pasan al archivo histórico).</p></body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='acta_baja_documental_'+folio+'.doc';a.click();
 var byKey={};A.forEach(function(x){(byKey[x.srcKey]=byKey[x.srcKey]||[]).push(x.srcIdx);});
 Object.keys(byKey).forEach(function(k){var arr=J(k);byKey[k].forEach(function(ix){if(arr[ix]){arr[ix]._archBaja=true;arr[ix]._archBajaFecha=hoy();arr[ix]._archBajaFolio=folio;}});localStorage.setItem(k,JSON.stringify(arr));});
 logActa({folio:folio,tipo:'Baja documental',fecha:hoy(),serie:serieName,n:A.length});
 if(window.__bitlog)__bitlog('Archivo · Gestión Documental','Baja documental '+folio+' — '+A.length+' expedientes');
 alert('✅ Acta de baja '+folio+' generada. '+A.length+' expediente(s) marcados como dados de baja.');
 render();}
function vActas(){var L=J('sigej_archivo_actas').slice().reverse();
 var tp=L.filter(function(a){return /Transferencia/.test(a.tipo);});var bd=L.filter(function(a){return /Baja/.test(a.tipo);});
 var expT=tp.reduce(function(s,a){return s+(+a.n||0);},0);var expB=bd.reduce(function(s,a){return s+(+a.n||0);},0);
 var kp='<div class="kpis"><div class="kpi b"><div class="n">'+tp.length+'</div><div class="l">Actas de transferencia (TP)</div></div><div class="kpi r"><div class="n">'+bd.length+'</div><div class="l">Actas de baja (BD)</div></div><div class="kpi y"><div class="n">'+expT+'</div><div class="l">Expedientes transferidos</div></div><div class="kpi r"><div class="n">'+expB+'</div><div class="l">Expedientes dados de baja</div></div></div>';
 var tbl=L.length?('<div class="card" style="overflow:auto"><table><tr><th>Folio</th><th>Tipo</th><th>Fecha</th><th>Serie / área</th><th>Expedientes</th></tr>'+L.map(function(a){return '<tr><td><b>'+esc(a.folio)+'</b></td><td><span class="bdg '+(/Baja/.test(a.tipo)?'r':'b')+'">'+esc(a.tipo)+'</span></td><td>'+esc(a.fecha)+'</td><td>'+esc(a.serie)+'</td><td>'+esc(a.n)+'</td></tr>';}).join('')+'</table></div>'):'<div class="card" style="color:#64748b;font-size:12px">Aún no se han generado actas. Genera transferencias o bajas en la pestaña «Transferencias y baja».</div>';
 el('panel').innerHTML='<h2 class="h">📚 Registro de actas de archivo</h2><p class="lead">Historial de las actas de transferencia primaria (TP) y de baja documental (BD) generadas, con folio, fecha, serie y número de expedientes.</p>'+kp+
  (L.length?'<div style="display:flex;gap:8px;margin-bottom:8px"><button class="bd mini" onclick="expActasCSV()">⬇️ Registro de actas (CSV)</button></div>':'')+tbl+
  '<div class="note">🧾 Cada acta queda registrada aquí y en la bitácora del sistema. El folio (TP-/BD-) es consecutivo y persistente; el detalle de expedientes de cada acta se conserva en su documento Word y en el inventario (fase y folio de transferencia).</div>';
}
function expActasCSV(){var L=J('sigej_archivo_actas');var rows=[['Folio','Tipo','Fecha','Serie/Area','Expedientes']].concat(L.map(function(a){return [a.folio,a.tipo,a.fecha,a.serie,a.n];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='registro_actas_archivo_'+hoy()+'.csv';a.click();}
function caratula(k,ix){var A=loadAll();var x=null;for(var i=0;i<A.length;i++){if(A[i].srcKey===k&&A[i].srcIdx===ix){x=A[i];break;}}
 if(!x){alert('Expediente no encontrado.');return;}
 var sec='';SECCIONES.forEach(function(s){if(s[2].some(function(se){return x.modulo.indexOf(se)>=0||se.indexOf(x.modulo)>=0;}))sec=s[0]+' · '+s[1];});
 var perm=esPermanente(x.modulo);var qr='SIGEJ|'+x.folio+'|'+x.modulo+'|'+x.fase+(x.transferFolio?'|'+x.transferFolio:'');
 var datos=[['Fondo','Universidad de Guadalajara · Oficina de la Abogacía General'],['Sección',sec||'—'],['Serie documental',x.modulo],['No. de expediente / folio',x.folio],['Asunto',x.tit],['Fechas extremas',(x.apertura||'—')+' a '+(x.conclusion||'—')],['Valores documentales',valorDoc(x.modulo)],['Disposición documental',perm?'Conservación permanente (archivo histórico)':'Baja documental'],['Fase archivística',x.fase],['Transferencia a concentración',x.fTransfer||'—'],['Fecha de baja / vencimiento',x.fBaja||'—'],['Etiqueta archivo muerto / ubicación',x.etiqueta||'—']];
 var rowsHtml=datos.map(function(r){return '<tr><th style="width:40%">'+r[0]+'</th><td>'+esc(r[1])+'</td></tr>';}).join('');
 var w=window.open('','_blank','width=820,height=1000');if(!w){alert('Permite ventanas emergentes para imprimir la carátula.');return;}
 var doc='<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Carátula '+esc(x.folio)+'</title>'+
  '<scr'+'ipt src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></scr'+'ipt>'+
  '<style>body{font-family:Cambria,Georgia,serif;color:#111;margin:0;padding:26px}.hoja{border:3px solid #00254a;border-radius:8px;padding:22px;max-width:730px;margin:auto}h1{font-size:15pt;text-align:center;color:#00254a;margin:0}h2{font-size:10.5pt;text-align:center;margin:2px 0 12px;font-weight:normal}.tit{text-align:center;font-size:11pt;font-weight:bold;color:#00254a}.folio{font-size:20pt;font-weight:bold;text-align:center;letter-spacing:1px;margin:6px 0}table{width:100%;border-collapse:collapse;font-size:10.5pt;margin-top:10px}th,td{border:1px solid #999;padding:5px 8px;text-align:left;vertical-align:top}th{background:#eef2f7;color:#00254a}.qrbox{text-align:center;margin:16px 0 4px}.code{font-family:monospace;font-size:9.5pt;margin-top:4px;word-break:break-all}.pie{font-size:8pt;color:#555;text-align:center;margin-top:10px}button{margin:14px auto;display:block;padding:8px 18px;border:none;border-radius:8px;background:#0a4d8c;color:#fff;font-size:12pt;cursor:pointer}@media print{button{display:none}body{padding:0}}</style></head><body>'+
  '<button onclick="window.print()">🖨️ Imprimir carátula</button>'+
  '<div class="hoja"><h1>UNIVERSIDAD DE GUADALAJARA</h1><h2>Oficina de la Abogacía General · Área Coordinadora de Archivos (CTAG)</h2>'+
  '<div class="tit">CARÁTULA DE EXPEDIENTE</div><div class="folio">'+esc(x.folio)+'</div>'+
  '<table>'+rowsHtml+'</table>'+
  '<div class="qrbox"><div id="qr" style="display:inline-block"></div><div class="code">'+esc(qr)+'</div></div>'+
  '<div class="pie">Documento generado por SIGEJ-UdeG · '+hoy()+' · conforme a la Ley General de Archivos. El código QR contiene el identificador del expediente para su localización física.</div></div>'+
  '<scr'+'ipt>try{new QRCode(document.getElementById("qr"),{text:'+JSON.stringify(qr)+',width:118,height:118,correctLevel:QRCode.CorrectLevel.M});}catch(e){document.getElementById("qr").textContent="[QR: "+'+JSON.stringify(x.folio)+'+"]";}</scr'+'ipt>'+
  '</body></html>';
 w.document.write(doc);w.document.close();
 if(window.__bitlog)__bitlog('Archivo · Gestión Documental','Carátula de expediente '+x.folio);}
function vNorm(){el('panel').innerHTML='<h2 class="h">⚖️ Marco normativo archivístico</h2><p class="lead">Fundamento de la gestión documental de la Universidad de Guadalajara.</p>'+
  '<div class="card"><ul class="leg">'+
   '<li><b>Ley General de Archivos</b> (DOF 15/06/2018) — define archivo de trámite, concentración e histórico; transferencias primaria y secundaria; baja documental; y el <b>Catálogo de Disposición Documental</b> y el <b>Cuadro General de Clasificación Archivística</b> como instrumentos de control.</li>'+
   '<li><b>Ley de Archivos del Estado de Jalisco y sus Municipios</b> — marco estatal aplicable a los sujetos obligados de Jalisco.</li>'+
   '<li><b>Lineamientos generales para la organización y conservación de los archivos</b> (mayo 2016).</li>'+
   '<li><b>Cuadro General de Clasificación Archivística (CGCA)</b> de la UdeG (2016) y <b>Catálogo de Disposición Documental (CADIDO)</b>.</li>'+
   '<li>Instrumentos y valoración a cargo del <b>Grupo Interdisciplinario</b> y del <b>Área Coordinadora de Archivos</b>.</li>'+
  '</ul></div>'+
  '<div class="card"><b style="color:#0a4d8c">🏛️ Coordinación de Transparencia y Archivo General (CTAG)</b><div style="font-size:12.5px;color:#334155;margin-top:5px">Instancia responsable de la política archivística de la UdeG.<br>Pedro Moreno 834, Col. Centro, Guadalajara, Jalisco · Tel. (33) 3134-2200 Ext. 12470<br><a href="https://www.transparencia.udg.mx/Archivistica" target="_blank" rel="noopener">transparencia.udg.mx/Archivistica</a></div></div>'+
  '<div class="note">🔗 Este módulo operacionaliza el ciclo archivístico sobre los expedientes de todo el SIGEJ; la aprobación formal de instrumentos y bajas corresponde a la CTAG y al Grupo Interdisciplinario.</div>';
}
seedAM();buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP).replace("__AMSEED__",AMJ)
open(B+"archivo_SIGEJ.html","w",encoding="utf-8").write(out)
print("archivo_SIGEJ.html OK -",len(out),"bytes | fuentes:",out.count("','")," | secciones CGCA: 7")
