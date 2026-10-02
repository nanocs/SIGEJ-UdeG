# -*- coding: utf-8 -*-
# MÓDULO: Cumplimiento de Auditorías y Observaciones (Onda 1 · Legal Governance).
# Seguimiento a auditorías internas/externas (Contraloría, ASF, ASEJ) y solventación de observaciones. NO duplica UTI (acceso a la información vive en Transparencia).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Auditorías'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','auditorias_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="auditorias_SIGEJ.html" class="act">🔎 Auditorías</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Cumplimiento de Auditorías</title>
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
.tab{padding:9px 13px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px}
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
textarea{min-height:52px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bw{background:var(--gold);color:#3a2c05;font-weight:700}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}
.note{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:95vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🔎 Cumplimiento de Auditorías y Observaciones</h1><div class="s">Auditorías internas y externas (Contraloría · ASF · ASEJ) · seguimiento y solventación · Legal Governance</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 entes:['Auditoría Interna / Contraloría','Auditoría Superior de la Federación (ASF)','Auditoría Superior del Estado de Jalisco (ASEJ)','Órgano Interno de Control','Despacho externo','SAT / Fiscal','Otra'],
 tipos:['Financiera','Control interno','Cumplimiento','Desempeño','Obra pública','Integral','Seguimiento'],
 cat:['Documental','Normativa','Financiera','Presupuestal','Administrativa','Patrimonial'],
 estAud:['En proceso','Concluida','En seguimiento'],
 estObs:['Abierta','En solventación','Solventada','No solventada','Recurrida','Prescrita'],
 areas:['Coordinación de lo Contencioso','Coordinación de Enlace con la Red','Coordinación de Normatividad','Secretaría General','Área Contable','Área de Personal','Control Patrimonial','Tesorería','Compras','Rectoría General','Centro Universitario']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'a'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function AUD(){return L('sigej_auditorias');}
function allObs(){var r=[];AUD().forEach(function(a){(a.obs||[]).forEach(function(o,j){r.push({a:a,o:o,j:j});});});return r;}
function bit(acc){if(window.__bitlog)__bitlog('Auditoría',acc);}
function seed(){if(localStorage.getItem('sigej_auditorias'))return;S('sigej_auditorias',[
 {id:uid(),folio:'AUD-2026-001',ente:'Auditoría Superior del Estado de Jalisco (ASEJ)',tipo:'Financiera',ejercicio:'2024',dep:'Área Contable',alcance:'Ingresos propios y egresos 2024',fini:'2026-03-01',ffin:'2026-05-30',estado:'En seguimiento',obs:[
   {id:uid(),desc:'Falta de comprobación de gastos por $120,000',cat:'Financiera',monto:120000,resp:'Área Contable',flim:'2026-08-15',estado:'En solventación',plan:'Integrar comprobantes CFDI',recom:'Fortalecer control de comprobación',docs:[],traza:[{ts:nowS(),usuario:'Contraloría',accion:'Observación registrada'}]},
   {id:uid(),desc:'Contrato sin garantía de cumplimiento',cat:'Normativa',monto:0,resp:'Compras',flim:'2026-06-20',estado:'Abierta',plan:'',recom:'Exigir fianza en contratos > umbral',docs:[],traza:[{ts:nowS(),usuario:'Contraloría',accion:'Observación registrada'}]}
 ]},
 {id:uid(),folio:'AUD-2026-002',ente:'Auditoría Interna / Contraloría',tipo:'Control interno',ejercicio:'2025',dep:'Control Patrimonial',alcance:'Inventario de bienes muebles',fini:'2026-04-10',ffin:'2026-05-10',estado:'En seguimiento',obs:[
   {id:uid(),desc:'Bienes sin etiqueta de resguardo',cat:'Patrimonial',monto:0,resp:'Control Patrimonial',flim:'2026-07-01',estado:'Solventada',plan:'Etiquetado completo',recom:'Conciliar inventario semestral',docs:[],traza:[{ts:nowS(),usuario:'Contraloría',accion:'Observación registrada'},{ts:nowS(),usuario:'Control Patrimonial',accion:'Solventada con evidencia'}]}
 ]}
]);}

var TABS=[['t1','📊 Panel'],['t2','🗂️ Auditorías'],['t3','📌 Observaciones'],['t4','📤 Reportes']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vAud();else if(VIEW==='t3')vObs();else vRep();}

function obsBadge(o){var c=o.estado==='Solventada'?'g':/No solventada|Recurrida/.test(o.estado)?'r':o.estado==='Abierta'?'n':'y';var d=dr(o.flim);var v=(o.estado!=='Solventada'&&o.estado!=='Prescrita'&&d!==null&&d<0)?' <span class="bdg r">vencida</span>':(o.estado!=='Solventada'&&d!==null&&d>=0&&d<=15?' <span class="bdg y">'+d+'d</span>':'');return '<span class="bdg '+c+'">'+esc(o.estado)+'</span>'+v;}

/* ---- Panel ---- */
function vPanel(){var A=AUD();var obs=allObs();
 var abiertas=obs.filter(function(x){return /Abierta|En solventaci/.test(x.o.estado);}).length;
 var solv=obs.filter(function(x){return x.o.estado==='Solventada';}).length;
 var venc=obs.filter(function(x){var d=dr(x.o.flim);return x.o.estado!=='Solventada'&&x.o.estado!=='Prescrita'&&d!==null&&d<0;}).length;
 var montoObs=obs.reduce(function(a,x){return a+(+x.o.monto||0);},0);
 var montoSolv=obs.filter(function(x){return x.o.estado==='Solventada';}).reduce(function(a,x){return a+(+x.o.monto||0);},0);
 var pct=obs.length?Math.round(100*solv/obs.length):0;
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+A.length+'</div><div class="l">Auditorías</div></div><div class="kpi"><div class="n">'+obs.length+'</div><div class="l">Observaciones</div></div><div class="kpi y"><div class="n">'+abiertas+'</div><div class="l">Abiertas / en solventación</div></div><div class="kpi g"><div class="n">'+solv+'</div><div class="l">Solventadas ('+pct+'%)</div></div><div class="kpi r"><div class="n">'+venc+'</div><div class="l">Vencidas</div></div><div class="kpi"><div class="n" style="font-size:16px">'+M(montoObs)+'</div><div class="l">Monto observado</div></div></div>';
 var prox=obs.filter(function(x){var d=dr(x.o.flim);return x.o.estado!=='Solventada'&&d!==null&&d<=15;}).sort(function(a,b){return dr(a.o.flim)-dr(b.o.flim);});
 var al=prox.length?'<div class="alert">⏰ <b>Solventaciones por vencer / vencidas:</b> '+prox.slice(0,6).map(function(x){var d=dr(x.o.flim);return esc(x.a.folio)+' · '+esc(x.o.resp)+' '+(d<0?'<b>vencida '+(-d)+'d</b>':'en '+d+'d');}).join(' · ')+'</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de cumplimiento</h2><p class="lead">Estado de solventación de observaciones de auditoría. Monto solventado: '+M(montoSolv)+' de '+M(montoObs)+'.</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Observaciones por estado</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Observaciones por ente auditor</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La integración con los sistemas de la <b>ASF/ASEJ/Contraloría</b> y la carga masiva de cédulas es fase backend; aquí se administra el seguimiento y la solventación. Las <b>solicitudes de acceso a la información</b> se gestionan en el módulo de <b>Transparencia General (UTI)</b>.</div>';
 try{var est={};obs.forEach(function(x){est[x.o.estado]=(est[x.o.estado]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(est),datasets:[{data:Object.values(est),backgroundColor:['#94a3b8','#e08e0b','#1f9d6b','#c0392b','#6b7280','#0a4d8c']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var ent={};obs.forEach(function(x){var e=x.a.ente.split(' ')[0]+(/ASF|ASEJ/.test(x.a.ente)?' '+(x.a.ente.match(/ASF|ASEJ/)||[''])[0]:'');ent[x.a.ente.replace(/ \(.*/,'').slice(0,18)]=(ent[x.a.ente.replace(/ \(.*/,'').slice(0,18)]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:Object.keys(ent),datasets:[{data:Object.values(ent),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
/* ---- Auditorías ---- */
function vAud(){var A=AUD();
 var form='<div class="collap" id="af"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar auditoría — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Ente auditor</label><select id="a_ente">'+opt(D.entes,'')+'</select></div>'+
  '<div class="f"><label>Tipo</label><select id="a_tipo">'+opt(D.tipos,'')+'</select></div>'+
  '<div class="f"><label>Ejercicio</label><input id="a_ej" placeholder="2024"></div>'+
  '<div class="f"><label>Dependencia auditada</label><select id="a_dep">'+opt(D.areas,'')+'</select></div>'+
  '<div class="f"><label>Fecha inicio</label><input id="a_fini" type="date"></div>'+
  '<div class="f"><label>Fecha fin</label><input id="a_ffin" type="date"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Alcance</label><input id="a_alc"></div></div>'+
  '<div style="margin-top:8px"><button class="b3" onclick="addAud()">＋ Registrar auditoría</button> <span id="a_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Ente</th><th>Ejercicio</th><th>Dependencia</th><th>Observaciones</th><th>Estado</th></tr>'+
  (A.length?A.map(function(a,i){var ab=(a.obs||[]).filter(function(o){return o.estado!=='Solventada';}).length;return '<tr class="row" onclick="ficha('+i+')"><td><b>'+esc(a.folio)+'</b></td><td style="font-size:11px">'+esc(a.ente.replace(/ \(.*/,''))+'</td><td>'+esc(a.ejercicio)+'</td><td style="font-size:11px">'+esc(a.dep)+'</td><td>'+(a.obs||[]).length+(ab?' <span class="bdg y">'+ab+' abiertas</span>':' <span class="bdg g">al día</span>')+'</td><td>'+esc(a.estado)+'</td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin auditorías.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🗂️ Auditorías</h2><p class="lead">Registra la auditoría y sus observaciones; da seguimiento a la solventación.</p>'+form+tbl;
}
function addAud(){if(!val('a_ej')){el('a_msg').style.color='#c0392b';el('a_msg').textContent='Indica el ejercicio.';return;}
 var A=AUD();var folio='AUD-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 A.push({id:uid(),folio:folio,ente:val('a_ente'),tipo:val('a_tipo'),ejercicio:val('a_ej'),dep:val('a_dep'),alcance:val('a_alc'),fini:val('a_fini'),ffin:val('a_ffin'),estado:'En proceso',obs:[]});
 S('sigej_auditorias',A);bit('Alta de auditoría '+folio);el('a_msg').style.color='#1f9d6b';el('a_msg').textContent='✓ '+folio+' registrada.';vAud();}
function ficha(i){var A=AUD();var a=A[i];if(!a)return;
 var obs=(a.obs||[]).map(function(o,j){return '<div class="comp"><div style="display:flex;justify-content:space-between;gap:6px"><b>'+esc(o.desc)+'</b>'+obsBadge(o)+'</div><div style="font-size:11.5px;color:#475569;margin-top:3px">'+esc(o.cat)+' · resp: '+esc(o.resp)+(o.monto?' · '+M(o.monto):'')+' · límite: '+esc(o.flim||'—')+'</div><div style="margin-top:5px"><button class="bd mini" onclick="verObs('+i+','+j+')">Ver / solventar</button></div></div>';}).join('')||'<div class="empty">Sin observaciones. Agrega la primera.</div>';
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+esc(a.folio)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(a.ente)+' · '+esc(a.tipo)+' · ejercicio '+esc(a.ejercicio)+'</div>'+
  '<div class="comp"><b>Dependencia:</b> '+esc(a.dep)+'<br><b>Alcance:</b> '+esc(a.alcance||'—')+'<br><b>Periodo:</b> '+esc(a.fini||'—')+' → '+esc(a.ffin||'—')+' · <b>Estado:</b> '+esc(a.estado)+'</div>'+
  '<div style="font-weight:700;color:#0a4d8c;margin:10px 0 4px">📌 Observaciones ('+(a.obs||[]).length+') <button class="b3 mini" onclick="addObsForm('+i+')">＋ Agregar</button></div>'+
  '<div id="obsForm"></div>'+obs+
  '<div style="margin-top:10px"><button class="bw mini" onclick="audWord('+i+')">📄 Cédula (Word)</button> <button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function addObsForm(i){el('obsForm').innerHTML='<div class="comp"><div class="grid"><div class="f"><label>Observación</label><input id="o_desc"></div><div class="f"><label>Categoría</label><select id="o_cat">'+opt(D.cat,'')+'</select></div><div class="f"><label>Responsable</label><input id="o_resp"></div><div class="f"><label>Monto observado</label><input id="o_monto" type="number" min="0"></div><div class="f"><label>Fecha límite solventación</label><input id="o_flim" type="date"></div><div class="f" style="grid-column:1/-1"><label>Recomendación</label><input id="o_recom"></div></div><div style="margin-top:6px"><button class="b3 mini" onclick="addObs('+i+')">Guardar observación</button></div></div>';}
function addObs(i){var A=AUD();var a=A[i];if(!val('o_desc')){alert('Describe la observación.');return;}
 a.obs=a.obs||[];a.obs.push({id:uid(),desc:val('o_desc'),cat:val('o_cat'),monto:+val('o_monto')||0,resp:val('o_resp'),flim:val('o_flim'),estado:'Abierta',plan:'',recom:val('o_recom'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Observación registrada'}]});
 a.estado='En seguimiento';S('sigej_auditorias',A);bit('Observación en '+a.folio+': '+val('o_desc').slice(0,40));ficha(i);}
function verObs(i,j){var A=AUD();var a=A[i];var o=a.obs[j];
 var docs=(o.docs||[]).length?(o.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin evidencia.</span>';
 var tz=(o.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<div class="back" style="color:#0a4d8c;cursor:pointer;font-size:12.5px" onclick="ficha('+i+')">← '+esc(a.folio)+'</div><h2 style="margin:6px 0 2px;color:#0a4d8c;font-size:16px">Observación</h2><div style="margin-bottom:6px">'+obsBadge(o)+'</div>'+
  '<div class="comp">'+esc(o.desc)+'<br><b>Categoría:</b> '+esc(o.cat)+' · <b>Responsable:</b> '+esc(o.resp)+(o.monto?' · <b>Monto:</b> '+M(o.monto):'')+'<br><b>Límite:</b> '+esc(o.flim||'—')+'<br><b>Recomendación:</b> '+esc(o.recom||'—')+(o.plan?'<br><b>Plan de acción:</b> '+esc(o.plan):'')+'</div>'+
  '<div class="comp"><b>📎 Evidencia de solventación</b> <button class="bd mini" onclick="obsAdj('+i+','+j+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>Cambiar estado</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+D.estObs.map(function(e){return '<button class="bd mini" onclick="obsEstado('+i+','+j+',\''+e+'\')">'+e+'</button>';}).join('')+'</div><div style="margin-top:6px"><input id="o_plan" placeholder="Plan de acción / nota de solventación" value="'+esc(o.plan||'')+'"><button class="bd mini" style="margin-top:5px" onclick="obsPlan('+i+','+j+')">Guardar plan</button></div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad (inalterable)</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
}
function obsEstado(i,j,est){var A=AUD();var o=A[i].obs[j];if(o.estado===est)return;var antes=o.estado;o.estado=est;o.traza.push({ts:nowS(),usuario:P,accion:'Estado: '+antes+' → '+est});S('sigej_auditorias',A);bit('Observación '+A[i].folio+' → '+est);
 if(est==='Solventada'||/vencid/.test(est)){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Auditorías',texto:'Observación de '+A[i].folio+' → '+est,folio:A[i].folio,modulo:'Auditorías',leida:false});S('sigej_notificaciones',N);}
 verObs(i,j);}
function obsPlan(i,j){var A=AUD();var o=A[i].obs[j];o.plan=val('o_plan');o.traza.push({ts:nowS(),usuario:P,accion:'Plan de acción actualizado'});S('sigej_auditorias',A);verObs(i,j);}
var _AT=null;
function obsAdj(i,j){_AT={i:i,j:j};el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var r=new FileReader();r.onload=function(){var A=AUD();var o=A[_AT.i].obs[_AT.j];o.docs=o.docs||[];o.docs.push({nombre:f.name,tipo:f.type,data:r.result,fecha:hoy()});o.traza.push({ts:nowS(),usuario:P,accion:'Evidencia adjuntada: '+f.name});S('sigej_auditorias',A);verObs(_AT.i,_AT.j);};r.readAsDataURL(f);};el('fileIn').click();}
/* ---- Observaciones (seguimiento transversal) ---- */
function vObs(){var obs=allObs();var fe=val('fEst'),q=(val('oq')||'').toLowerCase();
 var venc=obs.filter(function(x){var d=dr(x.o.flim);return x.o.estado!=='Solventada'&&x.o.estado!=='Prescrita'&&d!==null&&d<0;});
 var al=venc.length?'<div class="alert">🚨 <b>'+venc.length+' observación(es) vencida(s) sin solventar.</b></div>':'';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px"><input id="oq" value="'+esc(val('oq'))+'" placeholder="🔎 Buscar…" oninput="render()" style="flex:1;min-width:160px"><select id="fEst" onchange="render()" style="max-width:200px"><option value="">Todos los estados</option>'+opt(D.estObs,fe)+'</select></div>';
 var rows=obs.filter(function(x){return (!fe||x.o.estado===fe)&&(!q||JSON.stringify(x.o).toLowerCase().indexOf(q)>=0||x.a.folio.toLowerCase().indexOf(q)>=0);});
 var tbl='<table><tr><th>Auditoría</th><th>Observación</th><th>Responsable</th><th>Monto</th><th>Límite</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(x){return '<tr class="row" onclick="openObs(\''+x.a.id+'\','+x.j+')"><td>'+esc(x.a.folio)+'<br><span style="font-size:10px;color:#64748b">'+esc(x.a.ente.replace(/ \(.*/,''))+'</span></td><td style="font-size:11.5px">'+esc((x.o.desc||'').slice(0,50))+'</td><td style="font-size:11px">'+esc(x.o.resp)+'</td><td>'+(x.o.monto?M(x.o.monto):'—')+'</td><td>'+esc(x.o.flim||'—')+'</td><td>'+obsBadge(x.o)+'</td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin observaciones.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📌 Seguimiento de observaciones</h2><p class="lead">Worklist transversal de todas las auditorías. Clic para ver y solventar.</p>'+al+ctrl+tbl;
}
function openObs(aid,j){var A=AUD();var i=A.map(function(a){return a.id;}).indexOf(aid);if(i<0)return;verObs(i,j);el('drw').classList.add('on');}
/* ---- Reportes ---- */
function vRep(){var obs=allObs();
 el('panel').innerHTML='<h2 class="h">📤 Reportes</h2><p class="lead">Matriz de observaciones y solventación.</p><div style="display:flex;gap:8px;margin-bottom:12px"><button class="b1 mini" onclick="expCSV()">⬇️ Matriz CSV</button></div>'+
  '<table><tr><th>Auditoría</th><th>Ente</th><th>Observación</th><th>Categoría</th><th>Monto</th><th>Estado</th></tr>'+obs.map(function(x){return '<tr><td>'+esc(x.a.folio)+'</td><td style="font-size:11px">'+esc(x.a.ente.replace(/ \(.*/,''))+'</td><td style="font-size:11px">'+esc((x.o.desc||'').slice(0,44))+'</td><td>'+esc(x.o.cat)+'</td><td>'+(x.o.monto?M(x.o.monto):'—')+'</td><td>'+esc(x.o.estado)+'</td></tr>';}).join('')+'</table>';
}
function expCSV(){var obs=allObs();var rows=[['Auditoría','Ente','Ejercicio','Observación','Categoría','Responsable','Monto','Límite','Estado']].concat(obs.map(function(x){return [x.a.folio,x.a.ente,x.a.ejercicio,x.o.desc,x.o.cat,x.o.resp,x.o.monto,x.o.flim,x.o.estado];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='auditorias_'+hoy()+'.csv';a.click();}
function audWord(i){var a=AUD()[i];var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Cédula de seguimiento — '+esc(a.folio)+'</h3><p><b>Ente:</b> '+esc(a.ente)+' · <b>Tipo:</b> '+esc(a.tipo)+' · <b>Ejercicio:</b> '+esc(a.ejercicio)+'<br><b>Dependencia:</b> '+esc(a.dep)+' · <b>Alcance:</b> '+esc(a.alcance||'')+'</p><table border="1" cellpadding="4" style="border-collapse:collapse"><tr><th>Observación</th><th>Categoría</th><th>Monto</th><th>Límite</th><th>Estado</th></tr>'+(a.obs||[]).map(function(o){return '<tr><td>'+esc(o.desc)+'</td><td>'+esc(o.cat)+'</td><td>'+M(o.monto)+'</td><td>'+esc(o.flim||'')+'</td><td>'+esc(o.estado)+'</td></tr>';}).join('')+'</table></body></html>';var b=new Blob(['﻿'+h],{type:'application/msword'});var u=document.createElement('a');u.href=URL.createObjectURL(b);u.download='Cedula_'+a.folio+'.doc';u.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"auditorias_SIGEJ.html","w",encoding="utf-8").write(out)
print("auditorias_SIGEJ.html OK -",len(out),"bytes")
