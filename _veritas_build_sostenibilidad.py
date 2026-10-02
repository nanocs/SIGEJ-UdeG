# -*- coding: utf-8 -*-
# MÓDULO: Cumplimiento en Sostenibilidad y Ambiental (Onda 3 · #4, cierra la onda).
# Obligaciones y trámites jurídicos ambientales, certificados/permisos/licencias, proyectos y ODS, con marco legal FEDERAL y ESTATAL (Jalisco) verificado.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Sostenibilidad'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','sostenibilidad_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="sostenibilidad_SIGEJ.html" class="act">🌱 Sostenibilidad</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Cumplimiento en Sostenibilidad</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#0a5b3a,#1f9d6b);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#06402a;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c9e8d9;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:#0a5b3a;color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:#0a5b3a;font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:#0a5b3a}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:#0a5b3a;cursor:pointer;font-size:13px}
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
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}.bdg.f{background:#e6f0fb;color:#0a4d8c}.bdg.e{background:#e6f6ee;color:#0a5b3a}
.ods{display:inline-block;background:#0a5b3a;color:#fff;border-radius:6px;padding:1px 6px;font-size:10px;font-weight:700;margin:1px}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.leybox{background:#f8fafc;border:1px solid var(--line);border-left:4px solid #0a5b3a;border-radius:10px;padding:11px 13px;margin-bottom:8px;font-size:12.5px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🌱 Cumplimiento en Sostenibilidad y Ambiental</h1><div class="s">Obligaciones y trámites jurídicos ambientales · certificados y permisos · proyectos y ODS · marco legal federal y estatal (Jalisco)</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const LEYFED=[
 ['Ley General del Equilibrio Ecológico y la Protección al Ambiente (LGEEPA)','SEMARNAT / PROFEPA'],
 ['Ley General para la Prevención y Gestión Integral de los Residuos (LGPGIR)','SEMARNAT'],
 ['Ley General de Cambio Climático (LGCC)','SEMARNAT / INECC'],
 ['Ley de Aguas Nacionales','CONAGUA'],
 ['Ley General de Vida Silvestre','SEMARNAT'],
 ['Ley General de Desarrollo Forestal Sustentable','SEMARNAT / CONAFOR'],
 ['Normas Oficiales Mexicanas (NOM) ambientales','SEMARNAT'],
 ['Ley de la Agencia de Seguridad, Energía y Ambiente','ASEA']
];
const LEYJAL=[
 ['Ley Estatal del Equilibrio Ecológico y la Protección al Ambiente (Jalisco)','SEMADET / PROEPA'],
 ['Ley de Gestión Integral de los Residuos del Estado de Jalisco','SEMADET'],
 ['Ley para la Acción ante el Cambio Climático del Estado de Jalisco','SEMADET'],
 ['Ley de Desarrollo Forestal Sustentable para el Estado de Jalisco','SEMADET / CONAFOR'],
 ['Reglamentos municipales (ecología, agua, residuos)','Ayuntamientos']
];
const D={
 ambito:['Federal','Estatal (Jalisco)','Municipal'],
 autoridad:['SEMARNAT','PROFEPA','CONAGUA','ASEA','INECC','CONAFOR','SEMADET (Jalisco)','PROEPA (Jalisco)','SIAPA','Ayuntamiento','Otra'],
 tipoTram:['Manifestación de Impacto Ambiental (MIA)','Licencia Ambiental Única (LAU)','Registro de generador de residuos peligrosos','Plan de manejo de residuos','Cédula de Operación Anual (COA)','Concesión/permiso de descarga de aguas residuales','Registro Nacional de Emisiones (RENE)','Licencia ambiental municipal','Dictamen de impacto ambiental estatal','Informe / estudio ambiental','Auditoría ambiental voluntaria (PROFEPA)','Otra obligación ambiental'],
 estObl:['Cumplida / vigente','En proceso','Por vencer','Vencida','Pendiente','Observada'],
 tipoCert:['Certificado','Permiso','Licencia','Concesión','Dictamen','Registro'],
 estProy:['En diseño','En ejecución','Concluido','Suspendido'],
 cu:['Administración General / Red','CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUCostaSur','CUSur','CUCiénega','CUAltos','CULagos','CUNorte','CUValles','CUTonalá','SEMS','Coord. Gral. Administrativa'],
 ods:['ODS 1 Fin de la pobreza','ODS 2 Hambre cero','ODS 3 Salud y bienestar','ODS 4 Educación de calidad','ODS 5 Igualdad de género','ODS 6 Agua limpia y saneamiento','ODS 7 Energía asequible y no contaminante','ODS 8 Trabajo decente','ODS 9 Industria e innovación','ODS 10 Reducción de desigualdades','ODS 11 Ciudades y comunidades sostenibles','ODS 12 Producción y consumo responsables','ODS 13 Acción por el clima','ODS 14 Vida submarina','ODS 15 Vida de ecosistemas terrestres','ODS 16 Paz, justicia e instituciones','ODS 17 Alianzas']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'z'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function OBL(){return L('sigej_sost_oblig');}
function CERT(){return L('sigej_sost_cert');}
function PROY(){return L('sigej_sost_proy');}
function bit(a){if(window.__bitlog)__bitlog('Sostenibilidad',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Sostenibilidad',texto:t,folio:f||'',modulo:'Sostenibilidad',leida:false});S('sigej_notificaciones',N);}
function oReal(x){if(x.estado==='Cumplida / vigente'){var d=dr(x.fVenc);if(d!==null&&d<0)return 'Vencida';if(d!==null&&d<=60)return 'Por vencer';}return x.estado;}
function oClass(e){return /Cumplida|vigente/.test(e)?'g':/Vencida|Observada/.test(e)?'r':/Por vencer|proceso|Pendiente/.test(e)?'y':'n';}
function leyes(){return LEYFED.map(function(x){return x[0];}).concat(LEYJAL.map(function(x){return x[0];}));}
function seed(){if(localStorage.getItem('sigej_sost_oblig'))return;
 S('sigej_sost_oblig',[
  {id:uid(),folio:'AMB-2026-001',tipo:'Concesión/permiso de descarga de aguas residuales',desc:'Descarga de aguas residuales de laboratorios',ambito:'Federal',autoridad:'CONAGUA',fundamento:'Ley de Aguas Nacionales',resp:'Coord. Gral. Administrativa',cu:'CUCEI',fIni:'2024-01-15',fVenc:'2026-08-30',estado:'Cumplida / vigente',ods:['ODS 6 Agua limpia y saneamiento'],docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
  {id:uid(),folio:'AMB-2026-002',tipo:'Registro de generador de residuos peligrosos',desc:'Residuos peligrosos biológico-infecciosos (RPBI)',ambito:'Federal',autoridad:'SEMARNAT',fundamento:'Ley General para la Prevención y Gestión Integral de los Residuos (LGPGIR)',resp:'CUCS',cu:'CUCS',fIni:'2023-06-01',fVenc:'2026-06-30',estado:'Cumplida / vigente',ods:['ODS 12 Producción y consumo responsables'],docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
  {id:uid(),folio:'AMB-2026-003',tipo:'Dictamen de impacto ambiental estatal',desc:'Obra nueva en Centro Universitario',ambito:'Estatal (Jalisco)',autoridad:'SEMADET (Jalisco)',fundamento:'Ley Estatal del Equilibrio Ecológico y la Protección al Ambiente (Jalisco)',resp:'Obras',cu:'CUTonalá',fIni:'2025-11-01',fVenc:'',estado:'En proceso',ods:['ODS 11 Ciudades y comunidades sostenibles'],docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
 ]);
 S('sigej_sost_cert',[{id:uid(),folio:'CERT-001',tipo:'Certificado',nombre:'Auditoría Ambiental — Certificado de Industria Limpia',autoridad:'PROFEPA',num:'PROFEPA-XXXX',fEmision:'2025-03-01',fVenc:'2027-03-01',estado:'Vigente',docs:[]}]);
 S('sigej_sost_proy',[{id:uid(),folio:'PSOS-001',nombre:'Campus sustentable — energía solar',objetivo:'Instalación fotovoltaica y eficiencia energética',cu:'Red',ods:['ODS 7 Energía asequible y no contaminante','ODS 13 Acción por el clima'],estado:'En ejecución',avance:40,resp:'Coord. Sustentabilidad',ini:'2026-01-01',fin:'2027-12-31'}]);
}

var TABS=[['t1','📊 Panel'],['t2','⚖️ Obligaciones y trámites'],['t3','📜 Certificados y permisos'],['t4','🎯 Proyectos y ODS'],['t5','📚 Marco legal'],['t6','📤 Reportes']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vObl();else if(VIEW==='t3')vCert();else if(VIEW==='t4')vProy();else if(VIEW==='t5')vMarco();else vRep();}

function vPanel(){var O=OBL(),C=CERT(),Pr=PROY();
 var cump=O.filter(function(x){return oReal(x)==='Cumplida / vigente';}).length;
 var proc=O.filter(function(x){return oReal(x)==='En proceso'||oReal(x)==='Pendiente';}).length;
 var venc=O.filter(function(x){return oReal(x)==='Vencida';}).length;
 var pv=O.filter(function(x){return oReal(x)==='Por vencer';}).length;
 var fed=O.filter(function(x){return x.ambito==='Federal';}).length,est=O.filter(function(x){return /Estatal/.test(x.ambito);}).length;
 var certPv=C.filter(function(x){var d=dr(x.fVenc);return d!==null&&d<=90;}).length;
 var odsSet={};O.concat(Pr).forEach(function(x){(x.ods||[]).forEach(function(o){odsSet[o]=1;});});
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+O.length+'</div><div class="l">Obligaciones/trámites</div></div><div class="kpi g"><div class="n">'+cump+'</div><div class="l">Cumplidas/vigentes</div></div><div class="kpi y"><div class="n">'+(proc+pv)+'</div><div class="l">En proceso / por vencer</div></div><div class="kpi r"><div class="n">'+venc+'</div><div class="l">Vencidas</div></div><div class="kpi"><div class="n">'+fed+' / '+est+'</div><div class="l">Federal / Estatal</div></div><div class="kpi"><div class="n">'+C.length+'</div><div class="l">Certificados/permisos</div></div><div class="kpi"><div class="n">'+Pr.length+'</div><div class="l">Proyectos</div></div><div class="kpi g"><div class="n">'+Object.keys(odsSet).length+'</div><div class="l">ODS atendidos</div></div></div>';
 var ri=[];if(venc)ri.push(venc+' obligación(es) vencida(s)');if(pv)ri.push(pv+' por vencer (≤60d)');if(certPv)ri.push(certPv+' certificado(s) por vencer (≤90d)');
 var al=ri.length?'<div class="alert">🚨 <b>Riesgo de cumplimiento ambiental:</b> '+ri.join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de cumplimiento ambiental</h2><p class="lead">Obligaciones y trámites jurídicos ante autoridades federales (SEMARNAT/PROFEPA/CONAGUA/ASEA) y estatales (SEMADET/PROEPA · Jalisco), certificados, proyectos y ODS.</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a5b3a">Obligaciones por ámbito</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a5b3a">Obligaciones por estado</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La conexión con los portales de <b>SEMARNAT (SINAT/COA), CONAGUA (REPDA), PROFEPA</b> y <b>SEMADET (Jalisco)</b> para consultar folios y vencimientos reales es fase backend. El marco legal se cita por su denominación oficial; el <b>texto y las reformas vigentes de cada artículo deben verificarse</b> en la fuente (ver pestaña «Marco legal»).</div>';
 try{var a={};O.forEach(function(x){a[x.ambito]=(a[x.ambito]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(a),datasets:[{data:Object.values(a),backgroundColor:['#0a4d8c','#0a5b3a','#d4a32c']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var e={};O.forEach(function(x){var k=oReal(x);e[k]=(e[k]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:Object.keys(e),datasets:[{data:Object.values(e),backgroundColor:'#1f9d6b'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
function vObl(){var O=OBL();var q=(val('oq')||'').toLowerCase(),fa=val('ofa'),fe=val('ofe');
 var form='<div class="collap" id="of"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar obligación / trámite ambiental — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Tipo de trámite / obligación</label><select id="o_tipo">'+opt(D.tipoTram,'')+'</select></div>'+
  '<div class="f"><label>Ámbito</label><select id="o_amb">'+opt(D.ambito,'')+'</select></div>'+
  '<div class="f"><label>Autoridad</label><select id="o_aut">'+opt(D.autoridad,'')+'</select></div>'+
  '<div class="f"><label>Fundamento legal</label><select id="o_fund">'+opt(leyes(),'')+'</select></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="o_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Responsable</label><input id="o_resp"></div>'+
  '<div class="f"><label>Inicio</label><input id="o_ini" type="date"></div>'+
  '<div class="f"><label>Vencimiento</label><input id="o_venc" type="date"></div>'+
  '<div class="f"><label>Estado</label><select id="o_est">'+opt(D.estObl,'En proceso')+'</select></div>'+
  '<div class="f"><label>ODS principal</label><select id="o_ods">'+opt(['(ninguno)'].concat(D.ods),'')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Descripción</label><input id="o_desc"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addObl()">＋ Registrar</button> <span id="o_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="oq" value="'+esc(val('oq'))+'" placeholder="🔎 Buscar…" oninput="render()" style="flex:1;min-width:160px"><select id="ofa" onchange="render()" style="max-width:160px"><option value="">Todo ámbito</option>'+opt(D.ambito,fa)+'</select><select id="ofe" onchange="render()" style="max-width:150px"><option value="">Todo estado</option>'+opt(['Cumplida / vigente','Por vencer','Vencida','En proceso','Pendiente','Observada'],fe)+'</select></div>';
 var rows=O.map(function(x,i){return {x:x,i:i};}).filter(function(o){var er=oReal(o.x);return (!q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0)&&(!fa||o.x.ambito===fa)&&(!fe||er===fe);});
 var tbl='<table><tr><th>Folio</th><th>Trámite / obligación</th><th>Ámbito</th><th>Autoridad</th><th>Vence</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var er=oReal(x);return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.tipo)+'</b><br><span style="font-size:10px;color:#64748b">'+esc((x.desc||'').slice(0,40))+'</span></td><td><span class="bdg '+(/Federal/.test(x.ambito)?'f':'e')+'">'+esc(x.ambito)+'</span></td><td style="font-size:11px">'+esc(x.autoridad)+'</td><td>'+esc(x.fVenc||'—')+'</td><td><span class="bdg '+oClass(er)+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin obligaciones registradas.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">⚖️ Obligaciones y trámites jurídicos ambientales</h2><p class="lead">Cada obligación se vincula a su <b>fundamento legal</b> (federal o estatal) y a la autoridad competente, con vencimiento y evidencia.</p>'+form+ctrl+tbl;
}
function addObl(){if(!val('o_desc')&&!val('o_tipo')){el('o_msg').style.color='#c0392b';el('o_msg').textContent='Indica el tipo/descripción.';return;}
 var O=OBL();var folio='AMB-'+(new Date().getFullYear())+'-'+String(O.length+1).padStart(3,'0');
 var od=val('o_ods');O.push({id:uid(),folio:folio,tipo:val('o_tipo'),desc:val('o_desc'),ambito:val('o_amb'),autoridad:val('o_aut'),fundamento:val('o_fund'),resp:val('o_resp'),cu:val('o_cu'),fIni:val('o_ini'),fVenc:val('o_venc'),estado:val('o_est'),ods:(od&&od!=='(ninguno)'?[od]:[]),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de obligación'}]});
 S('sigej_sost_oblig',O);bit('Alta obligación '+folio);var dd=dr(val('o_venc'));if(dd!==null&&dd<=60)notif('Obligación ambiental '+val('o_tipo')+' por vencer',folio);
 el('o_msg').style.color='#1f9d6b';el('o_msg').textContent='✓ '+folio+' registrada.';vObl();}
function ficha(i){var O=OBL();var x=O[i];if(!x)return;var er=oReal(x);
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin evidencia (resolución, permiso, informe, comprobante).</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a5b3a">'+esc(x.tipo)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+' · <span class="bdg '+(/Federal/.test(x.ambito)?'f':'e')+'">'+esc(x.ambito)+'</span> <span class="bdg '+oClass(er)+'">'+esc(er)+'</span></div>'+
  '<div class="comp"><b>Descripción:</b> '+esc(x.desc||'—')+'<br><b>Autoridad:</b> '+esc(x.autoridad)+' · <b>Responsable:</b> '+esc(x.resp||'—')+' · <b>CU:</b> '+esc(x.cu||'—')+'<br><b>Vigencia:</b> '+esc(x.fIni||'—')+' → '+esc(x.fVenc||'—')+'</div>'+
  '<div class="comp" style="border-left:4px solid #0a5b3a"><b>⚖️ Fundamento legal</b><br>'+esc(x.fundamento||'—')+(x.ods&&x.ods.length?'<br><b>ODS:</b> '+x.ods.map(function(o){return '<span class="ods">'+esc(o)+'</span>';}).join(' '):'')+'</div>'+
  '<div class="comp"><b>Estado</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+D.estObl.map(function(e){return '<button class="bd mini" onclick="setEst('+i+',\''+e+'\')">'+e.split(' ')[0]+'</button>';}).join('')+'</div></div>'+
  '<div class="comp"><b>🗂️ Evidencia</b> <button class="bd mini" onclick="oblAdj('+i+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEst(i,e){var O=OBL();var x=O[i];if(x.estado===e)return;x.estado=e;x.traza.push({ts:nowS(),usuario:P,accion:'Estado → '+e});S('sigej_sost_oblig',O);bit(x.folio+' → '+e);if(/Vencida|Observada/.test(e))notif('Obligación ambiental '+x.tipo+' → '+e,x.folio);ficha(i);}
var _AT=null;
function oblAdj(i){_AT=i;el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Resolución / Permiso / Informe / Comprobante de pago / Otro):','Resolución')||'Documento';var r=new FileReader();r.onload=function(){var O=OBL();O[_AT].docs=O[_AT].docs||[];O[_AT].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});O[_AT].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat});S('sigej_sost_oblig',O);ficha(_AT);};r.readAsDataURL(f);};el('fileIn').click();}
/* ---- Certificados ---- */
function vCert(){var C=CERT();
 var form='<div class="collap" id="cf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar certificado / permiso / licencia — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Tipo</label><select id="ce_tipo">'+opt(D.tipoCert,'')+'</select></div>'+
  '<div class="f"><label>Nombre</label><input id="ce_nom"></div>'+
  '<div class="f"><label>Autoridad</label><select id="ce_aut">'+opt(D.autoridad,'')+'</select></div>'+
  '<div class="f"><label>Número</label><input id="ce_num"></div>'+
  '<div class="f"><label>Emisión</label><input id="ce_em" type="date"></div>'+
  '<div class="f"><label>Vencimiento</label><input id="ce_vc" type="date"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addCert()">＋ Registrar</button> <span id="ce_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Certificado / permiso</th><th>Autoridad</th><th>Número</th><th>Vigencia</th><th>Estado</th></tr>'+
  (C.length?C.map(function(x){var d=dr(x.fVenc);var er=d!==null&&d<0?'Vencido':d!==null&&d<=90?'Por vencer':x.estado;var c=/Vencido/.test(er)?'r':/Por vencer/.test(er)?'y':'g';return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b><br><span style="font-size:10px;color:#64748b">'+esc(x.tipo)+'</span></td><td style="font-size:11px">'+esc(x.autoridad)+'</td><td style="font-size:11px">'+esc(x.num||'—')+'</td><td>'+esc(x.fVenc||'—')+'</td><td><span class="bdg '+c+'">'+esc(er)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin certificados.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📜 Certificados, permisos y licencias ambientales</h2><p class="lead">Certificados (p. ej. Industria Limpia · PROFEPA), permisos y licencias con su vigencia.</p>'+form+tbl;
}
function addCert(){if(!val('ce_nom')){el('ce_msg').style.color='#c0392b';el('ce_msg').textContent='Indica el nombre.';return;}
 var C=CERT();C.push({id:uid(),folio:'CERT-'+String(C.length+1).padStart(3,'0'),tipo:val('ce_tipo'),nombre:val('ce_nom'),autoridad:val('ce_aut'),num:val('ce_num'),fEmision:val('ce_em'),fVenc:val('ce_vc'),estado:'Vigente',docs:[]});
 S('sigej_sost_cert',C);bit('Alta certificado '+val('ce_nom'));el('ce_msg').style.color='#1f9d6b';el('ce_msg').textContent='✓ registrado.';vCert();}
/* ---- Proyectos y ODS ---- */
function vProy(){var Pr=PROY();
 var form='<div class="collap" id="pf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar proyecto de sostenibilidad — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre</label><input id="pr_nom"></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="pr_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>ODS principal</label><select id="pr_ods">'+opt(D.ods,'')+'</select></div>'+
  '<div class="f"><label>Estado</label><select id="pr_est">'+opt(D.estProy,'')+'</select></div>'+
  '<div class="f"><label>Avance (%)</label><input id="pr_av" type="number" min="0" max="100"></div>'+
  '<div class="f"><label>Responsable</label><input id="pr_resp"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Objetivo</label><input id="pr_obj"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addProy()">＋ Registrar</button> <span id="pr_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var cards=Pr.length?Pr.map(function(x){return '<div class="card"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><b style="color:#0a5b3a">'+esc(x.nombre)+'</b><span class="bdg '+(x.estado==='Concluido'?'g':x.estado==='Suspendido'?'r':'y')+'">'+esc(x.estado)+'</span></div><div style="font-size:12px;color:#475569;margin:4px 0">'+esc(x.objetivo||'')+' · '+esc(x.cu||'')+' · resp. '+esc(x.resp||'—')+'</div><div>'+(x.ods||[]).map(function(o){return '<span class="ods">'+esc(o)+'</span>';}).join(' ')+'</div><div style="height:8px;background:#eef2f7;border-radius:6px;overflow:hidden;margin-top:8px"><div style="height:100%;width:'+(x.avance||0)+'%;background:#0a5b3a"></div></div><div style="font-size:11px;color:#64748b;margin-top:2px">Avance '+(x.avance||0)+'%</div></div>';}).join(''):'<div class="empty">Sin proyectos de sostenibilidad.</div>';
 el('panel').innerHTML='<h2 class="h">🎯 Proyectos de sostenibilidad y ODS</h2><p class="lead">Proyectos alineados a la Agenda 2030 (Objetivos de Desarrollo Sostenible).</p>'+form+cards;
}
function addProy(){if(!val('pr_nom')){el('pr_msg').style.color='#c0392b';el('pr_msg').textContent='Indica el nombre.';return;}
 var Pr=PROY();Pr.push({id:uid(),folio:'PSOS-'+String(Pr.length+1).padStart(3,'0'),nombre:val('pr_nom'),objetivo:val('pr_obj'),cu:val('pr_cu'),ods:val('pr_ods')?[val('pr_ods')]:[],estado:val('pr_est'),avance:+val('pr_av')||0,resp:val('pr_resp'),ini:hoy(),fin:''});
 S('sigej_sost_proy',Pr);bit('Alta proyecto '+val('pr_nom'));el('pr_msg').style.color='#1f9d6b';el('pr_msg').textContent='✓ registrado.';vProy();}
/* ---- Marco legal ---- */
function vMarco(){
 var fed=LEYFED.map(function(x){return '<div class="leybox"><b>'+esc(x[0])+'</b><br><span style="font-size:11px;color:#64748b">Autoridad: '+esc(x[1])+'</span></div>';}).join('');
 var jal=LEYJAL.map(function(x){return '<div class="leybox" style="border-left-color:#0a4d8c"><b>'+esc(x[0])+'</b><br><span style="font-size:11px;color:#64748b">Autoridad: '+esc(x[1])+'</span></div>';}).join('');
 el('panel').innerHTML='<h2 class="h">📚 Marco legal ambiental aplicable</h2><p class="lead">Ordenamientos federales y del Estado de Jalisco que fundamentan las obligaciones y trámites ambientales de la Universidad.</p>'+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div><div style="font-weight:700;color:#0a5b3a;margin-bottom:6px">🇲🇽 Federal</div>'+fed+'</div><div><div style="font-weight:700;color:#0a4d8c;margin-bottom:6px">🏛️ Estatal (Jalisco)</div>'+jal+'</div></div>'+
  '<div class="note">📌 Denominaciones oficiales verificadas (Congreso/Gobierno de Jalisco y federales). El <b>texto vigente y las reformas de cada artículo deben consultarse en la fuente oficial</b> — no se reproduce aquí para evitar citas desactualizadas. La verificación en línea (DOF, Periódico Oficial de Jalisco) es fase backend.</div>';
}
/* ---- Reportes ---- */
function vRep(){var O=OBL();
 el('panel').innerHTML='<h2 class="h">📤 Reportes</h2><p class="lead">Matriz de cumplimiento ambiental.</p><div style="display:flex;gap:8px;margin-bottom:12px"><button class="b1 mini" onclick="expCSV()">⬇️ Matriz CSV</button></div>'+
  '<table><tr><th>Folio</th><th>Trámite</th><th>Ámbito</th><th>Autoridad</th><th>Fundamento</th><th>Vence</th><th>Estado</th></tr>'+O.map(function(x){return '<tr><td>'+esc(x.folio)+'</td><td>'+esc(x.tipo)+'</td><td>'+esc(x.ambito)+'</td><td style="font-size:11px">'+esc(x.autoridad)+'</td><td style="font-size:11px">'+esc((x.fundamento||'').slice(0,40))+'</td><td>'+esc(x.fVenc||'—')+'</td><td>'+esc(oReal(x))+'</td></tr>';}).join('')+'</table>';
}
function expCSV(){var O=OBL();var rows=[['Folio','Tramite','Ambito','Autoridad','Fundamento','Responsable','CU','Inicio','Vencimiento','Estado','ODS']].concat(O.map(function(x){return [x.folio,x.tipo,x.ambito,x.autoridad,x.fundamento,x.resp,x.cu,x.fIni,x.fVenc,oReal(x),(x.ods||[]).join('; ')];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='sostenibilidad_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"sostenibilidad_SIGEJ.html","w",encoding="utf-8").write(out)
print("sostenibilidad_SIGEJ.html OK -",len(out),"bytes")
