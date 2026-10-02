# -*- coding: utf-8 -*-
# AGENDA DE LA PERSONA TITULAR DE LA ABOGACÍA GENERAL — transparencia proactiva.
# Se administra en el Centro Ejecutivo y se PUBLICA en Transparencia (vista pública, solo eventos marcados como públicos).
# Modos: ?embed=1 (oculta encabezado/navbar para embeber)  ·  ?pub=1 (vista pública de solo lectura para Transparencia).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Agenda del Titular'")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="agenda_titular_SIGEJ.html" class="act">📅 Agenda del Titular</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Agenda de la Persona Titular de la Abogacía General</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.wrap{max-width:1240px;margin:auto;padding:16px 18px 44px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul2)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.grid{display:grid;gap:8px}
label.lb{font-size:11px;color:#64748b;display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
textarea{min-height:52px;resize:vertical}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:8px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bg{background:var(--ok);color:#fff;font-weight:700}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:7px 6px;vertical-align:top}
.bdg{padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;background:#eef2f7;color:#0a4d8c;white-space:nowrap}
.bdg.pub{background:#e7f7ee;color:#128c4a}.bdg.priv{background:#f1f5f9;color:#64748b}
.bdg.Programada{background:#eef6ff;color:#0a4d8c}.bdg.Realizada{background:#e7f7ee;color:#128c4a}.bdg.Cancelada{background:#fdeaea;color:#c0392b}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.acts button{margin-right:4px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
.pubonly{display:none}
body.pub .adminonly{display:none!important}
body.pub .pubonly{display:block}
@media print{.navbar,header,.card.alta,.card.filtros,.acts,footer,.note{display:none!important}body{background:#fff}}
</style></head><body>
<header><h1>📅 Agenda de la Persona Titular de la Abogacía General</h1><div class="s">Universidad de Guadalajara · Oficina de la Abogacía General · transparencia proactiva de la agenda pública</div></header>
__NAV__
<div class="wrap">
 <div class="pubonly note" style="background:#e7f7ee;border-color:#bfe6cf;color:#128c4a"><b>Agenda pública</b> de la persona titular de la Abogacía General. Publicación proactiva conforme a las obligaciones de transparencia; se muestran únicamente las actividades marcadas como <b>públicas</b>. Los datos personales de terceros y la información reservada no se difunden.</div>
 <div class="kpis" id="kpis"></div>
 <div class="card alta adminonly">
  <b style="color:#0a4d8c">➕ Registrar / actualizar actividad</b>
  <input type="hidden" id="fid">
  <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(160px,1fr));margin-top:8px">
   <div><label class="lb">Fecha *</label><input id="fdate" type="date"></div>
   <div><label class="lb">Hora inicio</label><input id="fhora" type="time"></div>
   <div><label class="lb">Hora fin</label><input id="ffin" type="time"></div>
   <div><label class="lb">Tipo</label><select id="ftipo"></select></div>
   <div><label class="lb">Estado</label><select id="festado"><option>Programada</option><option>Realizada</option><option>Cancelada</option></select></div>
   <div><label class="lb">¿Pública?</label><select id="fpub"><option value="1">Sí — agenda pública</option><option value="0">No — reservada/interna</option></select></div>
  </div>
  <div class="grid" style="grid-template-columns:1fr 1fr;margin-top:6px">
   <div><label class="lb">Título de la actividad *</label><input id="ftit" placeholder="p. ej. Sesión del Consejo General Universitario"></div>
   <div><label class="lb">Lugar</label><input id="flugar" placeholder="p. ej. Sala de Rectoría / Videoconferencia"></div>
  </div>
  <div class="grid" style="grid-template-columns:1fr 1fr;margin-top:6px">
   <div><label class="lb">Con / dependencia</label><input id="fcon" placeholder="p. ej. Rectoría General / Contraloría"></div>
   <div><label class="lb">Asunto / descripción</label><input id="fasunto" placeholder="Breve descripción pública del asunto"></div>
  </div>
  <div style="margin-top:6px"><label class="lb">Notas internas (no se publican)</label><textarea id="fnotas" placeholder="Observaciones para uso interno de la Oficina"></textarea></div>
  <div style="margin-top:8px"><button class="bg" onclick="guardar()">💾 Guardar actividad</button> <button class="bd" onclick="limpiarForm()">Limpiar</button> <span id="fmsg" style="font-size:12px;color:#128c4a;margin-left:8px"></span></div>
 </div>
 <div class="card filtros">
  <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">
   <div><label class="lb">Buscar</label><input id="q" placeholder="título, asunto, lugar…" oninput="render()"></div>
   <div><label class="lb">Tipo</label><select id="ftf" onchange="render()"></select></div>
   <div><label class="lb">Estado</label><select id="fef" onchange="render()"><option value="">Todos</option><option>Programada</option><option>Realizada</option><option>Cancelada</option></select></div>
   <div><label class="lb">Desde</label><input id="d1" type="date" onchange="render()"></div>
   <div><label class="lb">Hasta</label><input id="d2" type="date" onchange="render()"></div>
   <div style="display:flex;align-items:end;gap:6px"><button class="b1 mini" onclick="expCSV()">⬇️ CSV</button><button class="bd mini" onclick="window.print()">🖨️ Imprimir</button></div>
  </div>
 </div>
 <div class="grid" style="grid-template-columns:1.4fr 1fr"><div class="card" style="overflow:auto"><table><thead><tr><th>Fecha</th><th>Hora</th><th>Actividad</th><th>Tipo</th><th>Estado</th><th class="adminonly">Pública</th><th class="adminonly">Acciones</th></tr></thead><tbody id="tb"></tbody></table><div id="cap" style="font-size:11px;color:#64748b;padding:6px"></div></div><div class="card"><b style="color:#0a4d8c">Actividades por tipo</b><canvas id="c1" height="170"></canvas></div></div>
 <div class="note adminonly">🔒 Marca <b>¿Pública? = Sí</b> en las actividades que deben difundirse; solo esas aparecen en la vista pública de <b>Transparencia</b>. Las notas internas nunca se publican. La agenda se comparte automáticamente al Centro Ejecutivo y a Transparencia (misma fuente de datos).</div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
var KEY='sigej_agenda_titular';
var TIPOS=['Audiencia','Reunión de trabajo','Sesión de órgano colegiado','Firma de convenio','Evento institucional','Comparecencia','Capacitación / foro','Otro'];
var PUB=/[?&]pub=1/.test(location.search);
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function load(){var a=J(KEY);return Array.isArray(a)?a:[];}
function save(a){localStorage.setItem(KEY,JSON.stringify(a));}
function seed(){if(load().length)return;var s=[
 {id:'AG-0001',fecha:'2026-07-03',hora:'10:00',fin:'12:00',tipo:'Sesión de órgano colegiado',tit:'Sesión del H. Consejo General Universitario',lugar:'Paraninfo Enrique Díaz de León',con:'Rectoría General',asunto:'Dictámenes y asuntos jurídicos del orden del día',pub:1,estado:'Programada',notas:''},
 {id:'AG-0002',fecha:'2026-07-06',hora:'09:30',fin:'10:30',tipo:'Reunión de trabajo',tit:'Reunión con Coordinación General Jurídica',lugar:'Oficina de la Abogacía General',con:'CGJ',asunto:'Seguimiento de asuntos contenciosos prioritarios',pub:1,estado:'Programada',notas:'Preparar carpeta de laborales'},
 {id:'AG-0003',fecha:'2026-07-08',hora:'12:00',fin:'13:00',tipo:'Firma de convenio',tit:'Firma de convenio de colaboración académica',lugar:'Rectoría General',con:'Dependencia externa',asunto:'Formalización de instrumento jurídico interinstitucional',pub:1,estado:'Programada',notas:''},
 {id:'AG-0004',fecha:'2026-07-09',hora:'16:00',fin:'17:00',tipo:'Audiencia',tit:'Audiencia interna (asunto reservado)',lugar:'Oficina de la Abogacía General',con:'',asunto:'Asunto en trámite',pub:0,estado:'Programada',notas:'Reservado'},
 {id:'AG-0005',fecha:'2026-06-25',hora:'11:00',fin:'12:30',tipo:'Comparecencia',tit:'Comparecencia ante órgano de control',lugar:'Contraloría General',con:'Contraloría General',asunto:'Atención a requerimiento institucional',pub:1,estado:'Realizada',notas:''}
];save(s);}
function fillTipos(){var o='<option value="">Todos</option>'+TIPOS.map(function(t){return '<option>'+esc(t)+'</option>';}).join('');el('ftf').innerHTML=o;el('ftipo').innerHTML=TIPOS.map(function(t){return '<option>'+esc(t)+'</option>';}).join('');}
function guardar(){var a=load();var id=el('fid').value||('AG-'+String(a.length+1).padStart(4,'0'));
 var tit=el('ftit').value.trim(),fecha=el('fdate').value;
 if(!fecha||!tit){el('fmsg').style.color='#c0392b';el('fmsg').textContent='Fecha y título son obligatorios.';return;}
 var rec={id:id,fecha:fecha,hora:el('fhora').value,fin:el('ffin').value,tipo:el('ftipo').value,tit:tit,lugar:el('flugar').value.trim(),con:el('fcon').value.trim(),asunto:el('fasunto').value.trim(),pub:el('fpub').value==='1'?1:0,estado:el('festado').value,notas:el('fnotas').value.trim()};
 var ix=-1;for(var i=0;i<a.length;i++){if(a[i].id===id){ix=i;break;}}
 if(ix>=0)a[ix]=rec;else a.push(rec);save(a);
 if(window.__bitlog)__bitlog('Acción',(ix>=0?'Actualiza':'Registra')+' actividad de agenda del titular: '+tit);
 el('fmsg').style.color='#128c4a';el('fmsg').textContent='✓ Guardado.';limpiarForm();render();}
function editar(id){var a=load();var r=null;a.forEach(function(x){if(x.id===id)r=x;});if(!r)return;
 el('fid').value=r.id;el('fdate').value=r.fecha;el('fhora').value=r.hora||'';el('ffin').value=r.fin||'';el('ftipo').value=r.tipo||TIPOS[0];el('festado').value=r.estado||'Programada';el('fpub').value=r.pub?'1':'0';el('ftit').value=r.tit||'';el('flugar').value=r.lugar||'';el('fcon').value=r.con||'';el('fasunto').value=r.asunto||'';el('fnotas').value=r.notas||'';
 window.scrollTo(0,0);}
function borrar(id){if(!confirm('¿Eliminar esta actividad de la agenda?'))return;var a=load().filter(function(x){return x.id!==id;});save(a);if(window.__bitlog)__bitlog('Acción','Elimina actividad de agenda del titular');render();}
function togglePub(id){var a=load();a.forEach(function(x){if(x.id===id)x.pub=x.pub?0:1;});save(a);render();}
function limpiarForm(){['fid','fhora','ffin','ftit','flugar','fcon','fasunto','fnotas'].forEach(function(i){el(i).value='';});el('fdate').value='';el('ftipo').value=TIPOS[0];el('festado').value='Programada';el('fpub').value='1';}
function filtered(){var a=load();if(PUB)a=a.filter(function(x){return x.pub&&x.estado!=='Cancelada';});
 var q=norm(el('q').value),tf=el('ftf').value,ef=el('fef').value,d1=el('d1').value,d2=el('d2').value;
 a=a.filter(function(x){return (!q||norm((x.tit||'')+' '+(x.asunto||'')+' '+(x.lugar||'')+' '+(x.con||'')).indexOf(q)>=0)&&(!tf||x.tipo===tf)&&(!ef||x.estado===ef)&&(!d1||x.fecha>=d1)&&(!d2||x.fecha<=d2);});
 a.sort(function(p,q2){return (p.fecha+(p.hora||'')).localeCompare(q2.fecha+(q2.hora||''));});return a;}
function render(){var rows=filtered();var all=load();var hoy='2026-07-02';
 var prox=all.filter(function(x){return x.fecha>=hoy&&x.estado==='Programada';}).length;
 var pub=all.filter(function(x){return x.pub;}).length;
 el('kpis').innerHTML='<div class="kpi"><div class="n">'+rows.length+'</div><div class="l">'+(PUB?'Actividades públicas':'En el filtro')+'</div></div>'+
  (PUB?'':'<div class="kpi"><div class="n">'+all.length+'</div><div class="l">Actividades totales</div></div>')+
  '<div class="kpi"><div class="n">'+prox+'</div><div class="l">Próximas programadas</div></div>'+
  '<div class="kpi"><div class="n">'+pub+'</div><div class="l">Marcadas públicas</div></div>';
 var tip={};rows.forEach(function(x){tip[x.tipo]=(tip[x.tipo]||0)+1;});
 el('tb').innerHTML=rows.length?rows.map(function(x){
   var pb=x.pub?'<span class="bdg pub">Pública</span>':'<span class="bdg priv">Reservada</span>';
   var hr=(x.hora||'—')+(x.fin?'–'+x.fin:'');
   var act='<button class="bd mini" onclick="editar(\''+x.id+'\')">✏️</button><button class="bd mini" onclick="togglePub(\''+x.id+'\')">'+(x.pub?'🙈':'👁️')+'</button><button class="bd mini" onclick="borrar(\''+x.id+'\')">🗑️</button>';
   return '<tr><td style="white-space:nowrap">'+esc(x.fecha)+'</td><td style="white-space:nowrap">'+esc(hr)+'</td><td><b>'+esc(x.tit)+'</b>'+(x.asunto?'<br><span style="color:#64748b;font-size:11px">'+esc(x.asunto)+'</span>':'')+(x.lugar?'<br><span style="color:#94a3b8;font-size:11px">📍 '+esc(x.lugar)+(x.con?' · '+esc(x.con):'')+'</span>':'')+'</td><td><span class="bdg">'+esc(x.tipo||'')+'</span></td><td><span class="bdg '+esc(x.estado)+'">'+esc(x.estado)+'</span></td><td class="adminonly">'+pb+'</td><td class="adminonly acts">'+act+'</td></tr>';
 }).join(''):'<tr><td colspan="7" style="text-align:center;color:#64748b;padding:16px">Sin actividades con estos filtros.</td></tr>';
 el('cap').textContent=rows.length+' actividad(es).';
 drawChart(tip);}
function drawChart(tip){try{var k=Object.keys(tip);if(window.__c1)__c1.destroy();
 window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:k,datasets:[{data:k.map(function(t){return tip[t];}),backgroundColor:['#0a4d8c','#1aa39a','#e08e0b','#1f9d6b','#8b5cf6','#c0392b','#64748b','#0891b2']}]},options:{plugins:{legend:{position:'bottom',labels:{font:{size:9}}}}}});}catch(e){}}
function expCSV(){var rows=filtered();var out=[['Fecha','HoraInicio','HoraFin','Tipo','Titulo','Lugar','Con','Asunto','Estado','Publica']].concat(rows.map(function(x){return [x.fecha,x.hora,x.fin,x.tipo,x.tit,x.lugar,x.con,x.asunto,x.estado,x.pub?'Si':'No'];}));
 var csv=out.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');
 var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='agenda_titular_'+new Date().toISOString().slice(0,10)+'.csv';a.click();}
if(PUB)document.body.classList.add('pub');
seed();fillTipos();limpiarForm();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{background:#fff!important}.wrap{padding-top:8px!important}";document.head.appendChild(st);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"agenda_titular_SIGEJ.html","w",encoding="utf-8").write(out)
print("agenda_titular_SIGEJ.html OK -",len(out),"bytes")
