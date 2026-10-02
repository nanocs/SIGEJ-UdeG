# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/abogados_data.json",encoding="utf-8"))
DATA=json.dumps(d,ensure_ascii=False)
NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="modulo_expedientes_SIGEJ.html">📁 Expedientes</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="proyectos_SIGEJ.html">📌 Proyectos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="asesoria_SIGEJ.html">💡 Asesoría</a><a href="captura_expediente_SIGEJ.html">➕ Captura</a><a href="abogados_SIGEJ.html" class="act">👤 Abogados</a><a href="documental_SIGEJ.html">🗂️ Documental</a><a href="transparencia_SIGEJ.html">🔎 Transparencia</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="masc_SIGEJ.html">🤝 MASC</a><a href="resp_SIGEJ.html">⚖️ Responsabilidades</a><a href="alertas_centro_SIGEJ.html">🔔 Alertas</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Seguimiento por Abogado</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#f4f6f9;--ok:#1f9d6b;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:14px 24px}
header h1{margin:0;font-size:18px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:10px 13px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:18px 24px;max-width:1300px;margin:auto}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:11px;margin-bottom:14px}
.kpi{background:#fff;border-radius:10px;padding:13px;box-shadow:0 1px 3px rgba(0,0,0,.07);border-left:4px solid var(--teal)}
.kpi .n{font-size:24px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut)}
.kpi.r{border-left-color:var(--red)}.kpi.g{border-left-color:var(--ok)}.kpi.y{border-left-color:var(--gold)}
.card{background:#fff;border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.07);margin-bottom:16px}
.card h2{margin:0 0 12px;font-size:15px;color:var(--azul)}
table{width:100%;border-collapse:collapse;font-size:12.5px}th,td{padding:7px 9px;text-align:left;border-bottom:1px solid var(--line)}th{color:var(--mut)}
select{padding:5px 7px;border:1px solid var(--line);border-radius:6px;font-size:12px}
.st{font-size:11px;padding:2px 8px;border-radius:9px;font-weight:600}
.st-Activo{background:#e6f6ee;color:#1f7a4d}.st-Incapacidad{background:#fef3e0;color:#b9770e}.st-Renuncia{background:#fdecea;color:#c0392b}.st-Suspensión{background:#fdecea;color:#c0392b}.st-Baja{background:#eef2f7;color:#475569}.st-Comisión{background:#e6f0fb;color:#0a4d8c}
.pill{font-size:10px;padding:1px 7px;border-radius:9px;font-weight:600}
.p-Crítico{background:#fdecea;color:#c0392b}.p-Alto{background:#fef3e0;color:#b9770e}.p-Medio{background:#e6f6f4;color:#138a7f}.p-Bajo{background:#eef2f7;color:#64748b}
button{padding:8px 14px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff;background:var(--azul2)}
.ok{color:var(--ok);font-weight:700}.pend{color:var(--red);font-weight:700}
footer{padding:14px 24px;color:var(--mut);font-size:11px;text-align:center}
.warn{background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:9px 11px;font-size:11.5px;color:#8a6d1a;margin-bottom:14px}
.f{display:flex;flex-direction:column;gap:3px}.f label{font-size:12px;color:var(--mut);font-weight:600}
.f input{padding:8px;border:1px solid var(--line);border-radius:7px;font-size:13px}
.tzh{font-size:13px;font-weight:700;color:var(--azul);margin:14px 0 6px;border-bottom:2px solid var(--line);padding-bottom:4px}
.addrow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:8px 0}
.addrow input,.addrow select{padding:6px 8px;border:1px solid var(--line);border-radius:6px;font-size:12px}
.actual{background:#e6f6ee;color:#1f7a4d;font-weight:600;font-size:10px;padding:1px 7px;border-radius:9px}
.rol{font-size:10px;padding:1px 7px;border-radius:9px;background:#0a4d8c;color:#fff;font-weight:600}
.doc{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 9px;border:1px solid var(--line);border-radius:7px;margin:4px 0;font-size:12.5px}
.del{color:#c0392b;cursor:pointer}
/* HDR-UNIF · encabezado institucional unificado SIGEJ-UdeG */
header{background:linear-gradient(120deg,#00254a 0%,#0a4d8c 100%)!important;color:#fff!important;border-bottom:none!important;padding:14px 24px!important}
header h1{margin:0!important;font-size:18px!important;font-weight:700!important;color:#fff!important;letter-spacing:.2px}
header h1 a{color:#fff}
header .s,header .sub{opacity:.85!important;font-size:12px!important;margin-top:3px!important;color:#e6eefb!important}
header .badge{background:rgba(255,255,255,.15)!important;border:1px solid rgba(255,255,255,.3)!important;color:#fff!important}
header .live{background:rgba(255,255,255,.14)!important;border:1px solid rgba(255,255,255,.32)!important;color:#eafff5!important}
.navbar{background:#06182c!important;border-bottom:1px solid #14304f!important}
/* LIGHT-UNIF · tema claro institucional — Manual VI (fondo blanco, tarjetas con sombra, pie naranja) */
body{background:#eef2f7!important;color:#0a1f3c!important}
.card,.kpi,.it,.panel{box-shadow:0 1px 3px rgba(2,40,90,.07)!important}
.navbar a{color:#c2d2e8!important}.navbar a:hover,.navbar a.act{color:#fff!important}
.warn{background:#fff8e6!important;border:1px solid #e7c66b!important;color:#8a6d1a!important}
.kpi.g .n{color:#15803d!important}.kpi.r .n{color:#c0392b!important}.kpi.y .n{color:#b45309!important}
.bd{background:#64748b!important;color:#fff!important}
footer{background:#e8731c!important;color:#fff!important;border-top:3px solid #c75e10!important;margin-top:20px}
</style></head><body>
<header><h1>👤 SIGEJ-UdeG · Seguimiento de Expedientes por Abogado</h1><div class="s">Estatus del personal, bajas/incapacidades y reasignación de cartera — Oficina de la Abogacía General</div></header>
__NAV__
<div class="wrap">
 <div class="warn">⚠️ El sistema NO sabe a quién se canalizó cada expediente (no consta en el dato): aquí <b>tú lo registras</b>. Precargué los estatus que indicaste (bajas y la incapacidad de Tania). Reasignaciones y estatus se guardan localmente.</div>
 <div class="kpis" id="kpis"></div>
 <div class="card"><h2>Plantilla de abogados — estatus editable</h2><table id="tlaw"></table></div>
 <div class="card"><h2>Bandeja de reasignación — expedientes de personal no activo
   <label style="float:right;font-size:12px;font-weight:400"><input type="checkbox" id="solo_pend" checked onchange="render()"> solo pendientes</label></h2>
   <table id="treas"></table>
   <div style="margin-top:12px"><button onclick="expReas()">⬇ Exportar reasignaciones</button></div>
 </div>
 <div class="card"><h2>🧭 Trazabilidad / cadena de responsables por expediente</h2>
  <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end">
   <div class="f" style="max-width:320px"><label>Buscar expediente</label><input id="tz_exp" list="l_nums" placeholder="ej. 44/2003-S" oninput="tzShow()"><datalist id="l_nums"></datalist></div>
   <button onclick="expTraza()" style="background:var(--ok)">⬇ Exportar trazabilidad (CSV)</button>
   <button onclick="wordTraza()" style="background:#2b579a">📄 Informe (Word)</button>
  </div>
  <div id="tz_body" style="margin-top:8px;color:#64748b;font-size:13px">Escribe o selecciona un número de expediente para ver y registrar su cadena de responsables.</div>
 </div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;
const DEF={};D.lawyers.forEach(l=>DEF[l.nombre]=l.status);
let ASTAT=Object.assign({},DEF,JSON.parse(localStorage.getItem('sigej_abostatus')||'{}'));
let REASIG=JSON.parse(localStorage.getItem('sigej_reasig')||'{}');
function saveA(){localStorage.setItem('sigej_abostatus',JSON.stringify(ASTAT));}
function saveR(){localStorage.setItem('sigej_reasig',JSON.stringify(REASIG));}
function activos(){return D.lawyers.filter(l=>(ASTAT[l.nombre]||'Activo')==='Activo').map(l=>l.nombre);}
function setSt(nm,v){ASTAT[nm]=v;saveA();render();}
function setRe(num,v){if(v)REASIG[num]=v;else delete REASIG[num];saveR();render();}
function afectados(){let out=[];D.lawyers.forEach(l=>{if((ASTAT[l.nombre]||'Activo')!=='Activo'){(D.expedientes[l.nombre]||[]).forEach(e=>{if(e.activo)out.push(Object.assign({},e,{original:l.nombre}));});}});return out;}
function render(){
 const af=afectados(),reas=af.filter(e=>REASIG[e.num]).length;
 const inactivos=D.lawyers.filter(l=>(ASTAT[l.nombre]||'Activo')!=='Activo').length;
 document.getElementById('kpis').innerHTML=[[D.lawyers.length,'Abogados',''],[inactivos,'No activos','y'],[af.length,'Exp. activos afectados','r'],[reas,'Reasignados','g'],[af.length-reas,'Pendientes','r']]
  .map(x=>`<div class="kpi ${x[2]}"><div class="n">${x[0]}</div><div class="l">${x[1]}</div></div>`).join('');
 const OP=D.estatus_opciones;
 document.getElementById('tlaw').innerHTML='<tr><th>Abogado</th><th>Activos</th><th>Total</th><th>Estatus</th><th>Recibe reasignados</th></tr>'+
  D.lawyers.map(l=>{const st=ASTAT[l.nombre]||'Activo';const rec=Object.entries(REASIG).filter(([n,v])=>v===l.nombre).length;
   return `<tr><td><b>${l.nombre}</b></td><td>${l.activos}</td><td>${l.n}</td><td><select onchange="setSt('${l.nombre.replace(/'/g,"")}',this.value)">${OP.map(o=>`<option ${o===st?'selected':''}>${o}</option>`).join('')}</select> <span class="st st-${st}">${st}</span></td><td>${rec?'<span class="ok">+'+rec+'</span>':''}</td></tr>`;}).join('');
 const act=activos();const af2=document.getElementById('solo_pend').checked?afectados().filter(e=>!REASIG[e.num]):afectados();
 af2.sort((a,b)=>b.score-a.score);
 document.getElementById('treas').innerHTML=af2.length?('<tr><th>Expediente</th><th>Materia</th><th>Estado</th><th>Riesgo</th><th>Responsable original</th><th>Reasignar a</th><th></th></tr>'+
  af2.map(e=>`<tr><td><b>${e.num}</b></td><td>${e.materia}</td><td>${e.estado}</td><td><span class="pill p-${e.nivel}">${e.nivel}</span></td><td>${e.original.split(' ').slice(0,2).join(' ')} <span class="st st-${ASTAT[e.original]}">${ASTAT[e.original]}</span></td>`+
   `<td><select onchange="setRe('${e.num}',this.value)"><option value="">— pendiente —</option>${act.map(a=>`<option ${REASIG[e.num]===a?'selected':''}>${a}</option>`).join('')}</select></td><td>${REASIG[e.num]?'<span class="ok">✓</span>':'<span class="pend">•</span>'}</td></tr>`).join('')):'<tr><td colspan="7" style="color:#1f7a4d;padding:12px">✓ No hay expedientes pendientes de reasignar.</td></tr>';}
// ---- Trazabilidad / cadena de responsables ----
let TZ=JSON.parse(localStorage.getItem('sigej_traza')||'{}');
function saveT(){localStorage.setItem('sigej_traza',JSON.stringify(TZ));}
function tz(num){if(!TZ[num])TZ[num]={resp:[],inst:[]};return TZ[num];}
const ALLNOM=D.lawyers.map(l=>l.nombre);
document.getElementById('l_nums').innerHTML=D.nums.map(n=>`<option>${n}</option>`).join('');
function tzShow(){const num=document.getElementById('tz_exp').value.trim();const B=document.getElementById('tz_body');
 const ix=D.index[num];if(!ix){B.innerHTML='<span style="color:#94a3b8">Expediente no encontrado en la base.</span>';return;}
 const t=tz(num);const actual=REASIG[num]||ix.responsable;
 const dl='<datalist id="l_nom">'+ALLNOM.map(n=>`<option>${n}</option>`).join('')+'</datalist>';
 const resp=t.resp.slice().sort((a,b)=>(a.desde||'').localeCompare(b.desde||''));
 const inst=t.inst.slice().sort((a,b)=>(a.desde||'').localeCompare(b.desde||''));
 B.innerHTML=dl+
  `<div style="background:#f4f6f9;border-radius:8px;padding:10px;font-size:13px"><b>${num}</b> · ${ix.materia} · ${ix.estado} · riesgo ${ix.nivel} · año ${ix.anio||'—'} · inicio ${ix.fecha_inicio||'—'}<br>`+
  `Responsable actual: <b>${actual}</b> ${REASIG[num]?'<span class="actual">reasignado</span>':''} ${ASTAT[ix.responsable]&&ASTAT[ix.responsable]!=='Activo'?'· orig. '+ix.responsable+' ('+ASTAT[ix.responsable]+')':''}</div>`+
  `<div class="tzh">Cadena de responsables (abogados que han llevado el asunto)</div>`+
  (resp.length?resp.map((e,i)=>`<div class="doc"><span>👤 ${e.nombre} <span class="rol">${e.rol||'Responsable'}</span> · ${e.desde||'?'} → ${e.hasta||'<span class=actual>actual</span>'} ${e.nota?'· '+e.nota:''}</span><span class="del" onclick="tzDel('${num}','resp',${t.resp.indexOf(e)})">✕</span></div>`).join(''):'<span style="color:#94a3b8;font-size:12px">Sin historial capturado. Agrega quién lo ha llevado.</span>')+
  `<div class="addrow"><input id="rz_nom" list="l_nom" placeholder="Abogado" style="min-width:170px"><select id="rz_rol"><option>Responsable</option><option>Co-responsable</option><option>Anterior</option></select><input id="rz_d" type="date" title="desde"><input id="rz_h" type="date" title="hasta"><input id="rz_nota" placeholder="nota"><button onclick="tzAddResp('${num}')">+ Agregar</button></div>`+
  `<div class="tzh">Cadena institucional (revisión jerárquica en el tiempo)</div>`+
  (inst.length?inst.map(e=>`<div class="doc"><span>🏛️ <span class="rol">${e.rol}</span> ${e.nombre} · ${e.desde||'?'} → ${e.hasta||'<span class=actual>actual</span>'}</span><span class="del" onclick="tzDel('${num}','inst',${t.inst.indexOf(e)})">✕</span></div>`).join(''):'<span style="color:#94a3b8;font-size:12px">Sin cadena institucional. Registra Abogado General / Coordinador / Jefe de Unidad y su periodo.</span>')+
  `<div class="addrow"><select id="iz_rol"><option>Abogado General</option><option>Coordinador Jurídico</option><option>Jefe de Unidad</option></select><input id="iz_nom" placeholder="Nombre" style="min-width:170px"><input id="iz_d" type="date" title="desde"><input id="iz_h" type="date" title="hasta"><button onclick="tzAddInst('${num}')">+ Agregar</button></div>`;}
function tzAddResp(num){const n=document.getElementById('rz_nom').value.trim();if(!n){alert('Indica el abogado.');return;}
 tz(num).resp.push({nombre:n,rol:document.getElementById('rz_rol').value,desde:document.getElementById('rz_d').value,hasta:document.getElementById('rz_h').value,nota:document.getElementById('rz_nota').value});saveT();tzShow();}
function tzAddInst(num){const n=document.getElementById('iz_nom').value.trim();if(!n){alert('Indica el nombre.');return;}
 tz(num).inst.push({rol:document.getElementById('iz_rol').value,nombre:n,desde:document.getElementById('iz_d').value,hasta:document.getElementById('iz_h').value});saveT();tzShow();}
function tzDel(num,tipo,i){tz(num)[tipo].splice(i,1);saveT();tzShow();}
function tzRows(){const out=[];Object.keys(TZ).forEach(num=>{const ix=D.index[num]||{};
 (TZ[num].resp||[]).forEach(e=>out.push({num:num,materia:ix.materia||'',cadena:'Responsable',rol:e.rol||'Responsable',nombre:e.nombre,desde:e.desde||'',hasta:e.hasta||'actual',nota:e.nota||''}));
 (TZ[num].inst||[]).forEach(e=>out.push({num:num,materia:ix.materia||'',cadena:'Institucional',rol:e.rol,nombre:e.nombre,desde:e.desde||'',hasta:e.hasta||'actual',nota:''}));});
 return out;}
function expTraza(){const R=tzRows();if(!R.length){alert('Aún no hay trazabilidad capturada.');return;}
 const cols=['num','materia','cadena','rol','nombre','desde','hasta','nota'];const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const csv=cols.join(',')+'\n'+R.map(r=>cols.map(c=>esc(r[c])).join(',')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='trazabilidad_expedientes.csv';a.click();}
function wordTraza(){const nums=Object.keys(TZ).filter(n=>(TZ[n].resp&&TZ[n].resp.length)||(TZ[n].inst&&TZ[n].inst.length));
 if(!nums.length){alert('Aún no hay trazabilidad capturada.');return;}
 let body='<h1>Informe de trazabilidad de expedientes</h1><p>Oficina de la Abogacía General · Universidad de Guadalajara · SIGEJ-UdeG</p>';
 nums.sort().forEach(num=>{const ix=D.index[num]||{};const t=TZ[num];
  body+=`<h2>Expediente ${num}</h2><p><b>Materia:</b> ${ix.materia||'—'} · <b>Estado:</b> ${ix.estado||'—'} · <b>Responsable actual:</b> ${REASIG[num]||ix.responsable||'—'}</p>`;
  body+='<h3>Cadena de responsables</h3><table border=1 cellpadding=4 style="border-collapse:collapse"><tr><th>Rol</th><th>Abogado</th><th>Desde</th><th>Hasta</th><th>Nota</th></tr>';
  (t.resp||[]).sort((a,b)=>(a.desde||'').localeCompare(b.desde||'')).forEach(e=>body+=`<tr><td>${e.rol||'Responsable'}</td><td>${e.nombre}</td><td>${e.desde||'?'}</td><td>${e.hasta||'actual'}</td><td>${e.nota||''}</td></tr>`);
  body+='</table><h3>Cadena institucional</h3><table border=1 cellpadding=4 style="border-collapse:collapse"><tr><th>Cargo</th><th>Nombre</th><th>Desde</th><th>Hasta</th></tr>';
  (t.inst||[]).sort((a,b)=>(a.desde||'').localeCompare(b.desde||'')).forEach(e=>body+=`<tr><td>${e.rol}</td><td>${e.nombre}</td><td>${e.desde||'?'}</td><td>${e.hasta||'actual'}</td></tr>`);
  body+='</table>';});
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri,Arial">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Informe_trazabilidad.doc';a.click();}
function expReas(){const af=afectados();if(!af.length)return;const cols=['num','materia','estado','nivel','responsable_original','reasignado_a','estatus_original'];
 const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const csv=cols.join(',')+'\n'+af.map(e=>[e.num,e.materia,e.estado,e.nivel,e.original,REASIG[e.num]||'',ASTAT[e.original]].map(esc).join(',')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='reasignaciones.csv';a.click();}
render();
</script><script>
/* SIGEJ — Control de acceso por perfil (capa de interfaz, sin backend) */
(function(){
 var SOLO=['SIGEJ_inicio','buscador_SIGEJ'];var JEFE=['SIGEJ_inicio','dashboard_SIGEJ','instrumentos_SIGEJ','patrimonio_SIGEJ','internacional_SIGEJ','normatividad_SIGEJ','contencioso_SIGEJ','buscador_SIGEJ','transparencia_general_SIGEJ','oficialia_SIGEJ','helpdesk_SIGEJ','administracion_SIGEJ','chat_SIGEJ','notificaciones_SIGEJ','alertas_centro_SIGEJ','recepcion_SIGEJ','biblioteca_SIGEJ','cumplimiento_SIGEJ','laboral_SIGEJ'];var ABOG=['SIGEJ_inicio','dashboard_SIGEJ','instrumentos_SIGEJ','patrimonio_SIGEJ','internacional_SIGEJ','normatividad_SIGEJ','contencioso_SIGEJ','buscador_SIGEJ','oficialia_SIGEJ','helpdesk_SIGEJ','chat_SIGEJ','notificaciones_SIGEJ','alertas_centro_SIGEJ','recepcion_SIGEJ','biblioteca_SIGEJ','cumplimiento_SIGEJ','laboral_SIGEJ'];var PERMS={'Administrador':null,'Abogado General':null,'Coordinador Jurídico':null,'Coordinador de Enlace con la Red':null,'Coordinador de Normatividad':null,'Secretaría General':SOLO,'Director':SOLO,'Coordinador General':SOLO,'Jefe de Unidad de lo Contencioso':JEFE,'Jefe de Unidad de Atención y Servicios Legales':JEFE,'Jefe de Unidad de Patrimonio Intangible':JEFE,'Jefe de Unidad de Asuntos Internacionales':JEFE,'Jefe de Unidad de Instrumentos Jurídicos':JEFE,'Jefe de Unidad de Capacitación, Investigación y Difusión':JEFE,'Jefe de Unidad de Estatutos y Reglamentos':JEFE,'Jefe de Unidad de Normatividad Administrativa':JEFE,'Jefe de Unidad de Apoyo a Órganos Colegiados':JEFE,'Jefe del Área Contable':JEFE,'Jefe del Área de Personal':JEFE,'Jefe del Área de Sistemas':JEFE,'Jefe de Oficialía de Partes':JEFE,'Jefe de Mensajería':JEFE,'Abogado':ABOG,'Analista':ABOG,'Asistente':ABOG,'Sistemas':null};
 var ROLES=Object.keys(PERMS);
 var perfil=localStorage.getItem('sigej_perfil');
 var pageKey=(location.pathname.split('/').pop()||'SIGEJ_inicio.html').replace('.html','')||'SIGEJ_inicio';
 function allowed(p){return PERMS[p]===null?null:PERMS[p];}
 function overlay(html){var d=document.createElement('div');d.style.cssText='position:fixed;inset:0;background:rgba(8,20,38,.78);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;font-family:Segoe UI,system-ui,sans-serif';d.innerHTML='<div style="background:#fff;border-radius:16px;max-width:440px;width:100%;padding:26px;box-shadow:0 12px 40px rgba(0,0,0,.4)">'+html+'</div>';document.body.appendChild(d);return d;}
 function pick(){
  var __G=[['Nivel 100 · Administración',['Administrador']],['Nivel 90 · Dirección superior',['Abogado General']],['Nivel 80 · Coordinaciones',['Coordinador Jurídico','Coordinador de Enlace con la Red','Coordinador de Normatividad']],['Nivel 70 · Secretaría y Dirección',['Secretaría General','Director','Coordinador General']],['Nivel 50 · Jefaturas de Unidad y Área',['Jefe de Unidad de lo Contencioso','Jefe de Unidad de Atención y Servicios Legales','Jefe de Unidad de Patrimonio Intangible','Jefe de Unidad de Asuntos Internacionales','Jefe de Unidad de Instrumentos Jurídicos','Jefe de Unidad de Capacitación, Investigación y Difusión','Jefe de Unidad de Estatutos y Reglamentos','Jefe de Unidad de Normatividad Administrativa','Jefe de Unidad de Apoyo a Órganos Colegiados','Jefe del Área Contable','Jefe del Área de Personal','Jefe del Área de Sistemas','Jefe de Oficialía de Partes','Jefe de Mensajería']],['Nivel 30 · Operativo jurídico',['Abogado','Analista']],['Nivel 10 · Apoyo',['Asistente']],['Nivel 1 · Sistemas',['Sistemas']]];var __u={};var opt=__G.map(function(g){var o=g[1].filter(function(r){return PERMS.hasOwnProperty(r);}).map(function(r){__u[r]=1;return '<option>'+r+'</option>';}).join('');return o?'<optgroup label="'+g[0]+'">'+o+'</optgroup>':'';}).join('');var __r=ROLES.filter(function(r){return !__u[r];}).map(function(r){return '<option>'+r+'</option>';}).join('');if(__r)opt+='<optgroup label="Otros">'+__r+'</optgroup>';
  var d=overlay('<h2 style="margin:0 0 4px;color:#00254a;font-size:19px">⚖️ SIGEJ-UdeG</h2><div style="color:#64748b;font-size:13px;margin-bottom:16px">Selecciona tu perfil para personalizar el acceso.</div><label style="font-size:12px;color:#64748b;font-weight:600">Perfil</label><select id="__perf" style="width:100%;padding:10px;border:1px solid #e2e8f0;border-radius:8px;font-size:14px;margin:4px 0 16px">'+opt+'</select><button id="__ok" style="width:100%;padding:11px;border:none;border-radius:9px;background:#1f9d6b;color:#fff;font-weight:600;font-size:14px;cursor:pointer">Entrar</button><div style="font-size:10.5px;color:#94a3b8;margin-top:12px">Control de interfaz (prototipo): personaliza la vista, no sustituye autenticación. La seguridad real (MFA, backend) es fase de implementación.</div>');
  d.querySelector('#__ok').onclick=function(){localStorage.setItem('sigej_perfil',d.querySelector('#__perf').value);location.reload();};
 }
 function badge(){
  var b=document.createElement('div');b.style.cssText='position:fixed;right:12px;bottom:12px;z-index:9000;background:#00254a;color:#fff;border-radius:20px;padding:7px 13px;font-size:12px;box-shadow:0 3px 12px rgba(0,0,0,.3);font-family:Segoe UI,system-ui,sans-serif';
  var __HD=['Administrador','Sistemas','Jefe del Área de Sistemas'];var __ver=__HD.indexOf(perfil)>=0;b.innerHTML='👤 '+(__ver?perfil:'Sesión activa')+' <span style="opacity:.6">·</span> <span id="__chg" style="cursor:pointer;text-decoration:underline">salir</span>';
  document.body.appendChild(b);
  b.querySelector('#__chg').onclick=function(){localStorage.removeItem('sigej_perfil');localStorage.removeItem('sigej_sesion');location.replace('acceso_SIGEJ.html');};
 }
 function apply(){
  var allow=allowed(perfil);
  document.querySelectorAll('.navbar a').forEach(function(a){var k=(a.getAttribute('href')||'').replace('.html','');if(k==='SIGEJ_inicio'||!k)return;if(allow&&allow.indexOf(k)<0)a.style.display='none';});
  if(allow&&allow.indexOf(pageKey)<0&&pageKey!=='SIGEJ_inicio'){
   overlay('<h2 style="margin:0 0 6px;color:#c0392b">Acceso restringido</h2><div style="color:#475569;font-size:13px;margin-bottom:16px">El perfil <b>'+perfil+'</b> no tiene acceso a este módulo.</div><a href="SIGEJ_inicio.html" style="display:inline-block;padding:10px 16px;background:#0a4d8c;color:#fff;border-radius:8px;text-decoration:none;font-weight:600">← Volver al inicio</a> <button onclick="localStorage.removeItem(\'sigej_perfil\');location.reload()" style="margin-left:8px;padding:10px 14px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;cursor:pointer">Cambiar perfil</button>');
   return;
  }
  if(perfil==='Consulta'){
   document.querySelectorAll('button').forEach(function(b){var t=(b.textContent||'')+ (b.title||'');if(/guardar|registrar|recibir|turnar|radicar|eliminar|adjuntar|reasignar|agendar|pagada|marcar|enviar/i.test(t)){b.disabled=true;b.style.opacity=.4;b.title='Perfil Consulta: solo lectura';}});
  }
 }
 if(!perfil){if(!/[?&]embed=1/.test(location.search)){location.replace('acceso_SIGEJ.html');}return;}else{apply();badge();if(['Abogado General','Sistemas','Secretaría General','Director','Coordinador General'].indexOf(perfil)>=0){setTimeout(function(){document.querySelectorAll('button,.lk,.del').forEach(function(b){var t=(b.textContent||'')+(b.title||'');if(/guardar|registrar|crear|captur|recibir|turnar|elimina|borrar|baja|adjuntar|generar|autoriz|pagar|aplicar|asignar|cargar demo|resolver|escalar|aprobar|publicar|solicitar|despach|＋/i.test(t)){b.disabled=true;b.style.opacity=.45;b.title='Perfil de solo lectura / consulta';}});},450);}}
})();
</script><script>
/* SIGEJ — Bitácora de auditoría (registro de interfaz, sin backend) */
(function(){try{
 var perfil=localStorage.getItem('sigej_perfil')||'(sin perfil)';
 var page=(location.pathname.split('/').pop()||'inicio').replace('.html','').replace('SIGEJ','').replace(/_/g,' ').trim()||'Inicio';
 function blog(tipo,accion){try{var L=JSON.parse(localStorage.getItem('sigej_bitacora')||'[]');L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:perfil,modulo:page,tipo:tipo,accion:String(accion||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);localStorage.setItem('sigej_bitacora',JSON.stringify(L));}catch(e){}}
 window.__bitlog=blog;
 blog('Acceso','Ingreso al módulo');
 var RX=/guardar|registrar|recibir|turnar|radicar|exportar|eliminar|adjuntar|reasignar|agendar|respuesta|oficio|acta|acuerdo|informe|csv|word|pagada|marcar|descargar|copiar/i;
 document.addEventListener('click',function(ev){try{var el=ev.target&&ev.target.closest&&ev.target.closest('button,.lk,.del');if(!el)return;var txt=(el.textContent||'').trim().replace(/\s+/g,' ');if(txt==='✕')txt='Eliminar registro';if((RX.test(txt)||txt==='Eliminar registro')&&txt.length<70)blog('Acción',txt);}catch(e){}},true);
}catch(e){}})();
</script><script>(function(){
 function norm(s){return (s||'').trim().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/\s+/g,' ');}
 function dedup(dl){var seen={};[].slice.call(dl.querySelectorAll('option')).forEach(function(o){var k=norm(o.value||o.textContent);if(!k){return;}if(seen[k]){o.remove();}else{seen[k]=1;}});}
 function run(){[].slice.call(document.querySelectorAll('datalist')).forEach(dedup);}
 if(document.readyState!=='loading'){run();}else{document.addEventListener('DOMContentLoaded',run);}
 setTimeout(run,800);
 try{var t;function sched(){clearTimeout(t);t=setTimeout(run,250);}
  var mo=new MutationObserver(function(muts){for(var i=0;i<muts.length;i++){var n=muts[i].target;while(n&&n.tagName!=='DATALIST'){n=n.parentElement;}if(n){sched();break;}}});
  mo.observe(document.documentElement,{childList:true,subtree:true});}catch(e){}
})();</script><script>(function(){
 var CONSULT=['buscador_SIGEJ','transparencia_general_SIGEJ','chat_SIGEJ','notificaciones_SIGEJ','SIGEJ_inicio','dashboard_SIGEJ','centro_ejecutivo_SIGEJ','bitacora_SIGEJ','reportes_SIGEJ','comando_SIGEJ','seguimiento_SIGEJ'];
 var pk=(location.pathname.split('/').pop()||'').replace('.html','');
 if(CONSULT.indexOf(pk)>=0)return;
 var dirty=false;
 function isSearch(el){if(el.id&&el.id.indexOf('__')===0)return true;var s=((el.id||'')+' '+(el.name||'')+' '+(el.placeholder||'')+' '+(el.className||'')).toLowerCase();return /buscar|search|filtro|filtrar|query|consulta/.test(s);}
 document.addEventListener('input',function(e){var el=e.target;if(!el||!/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName))return;if((el.type||'')==='search'||isSearch(el))return;if(((el.value||'')+'').length>0)dirty=true;},true);
 function clean(){dirty=false;}
 document.addEventListener('click',function(e){var t=e.target;if(!t)return;var n=t;for(var k=0;k<3&&n;k++){var x=((n.textContent||'')+' '+(n.title||'')).toLowerCase();if(/guardar|registrar|dar de alta|\bcrear\b|aceptar|\benviar\b|turnar|recibir|actualizar|aplicar/.test(x)){setTimeout(clean,60);break;}n=n.parentElement;}},true);
 document.addEventListener('submit',clean,true);
 window.addEventListener('beforeunload',function(e){if(dirty){e.preventDefault();e.returnValue='Tienes cambios de captura sin guardar. Si sales de la página se perderán.';return e.returnValue;}});
})();</script><script>(function(){
 if(/[?&]embed=1/.test(location.search))return;
 var pk=(location.pathname.split('/').pop()||'x').replace('.html','')||'x';
 var ISHOME=(pk==='SIGEJ_inicio');
 function ready(fn){if(document.readyState!=='loading')fn();else document.addEventListener('DOMContentLoaded',fn);}
 ready(function(){setTimeout(init,650);});
 function findNew(){
  var els=[].slice.call(document.querySelectorAll('button,a,.lk,[role=button]'));
  for(var i=0;i<els.length;i++){var e=els[i];if(e.id==='__uxnew'||e.id==='__uxhelp')continue;
   var t=((e.textContent||'')+' '+(e.title||'')).toLowerCase();
   if(/nuev|registrar|captur|\balta\b|dar de alta|añadir|levantar|＋/.test(t)&&e.offsetParent!==null)return e;}
  var inp=document.querySelector('form input,form textarea,form select,input[type=text],textarea');
  return (inp&&inp.offsetParent!==null)?inp:null;
 }
 function init(){
  if(!localStorage.getItem('sigej_perfil'))return;
  if(document.getElementById('__uxfab'))return;
  var hasNew=findNew();
  var bar=document.createElement('div');bar.id='__uxfab';
  bar.style.cssText='position:fixed;left:14px;bottom:14px;z-index:9000;display:flex;flex-direction:column;gap:8px;align-items:flex-start;font-family:Segoe UI,system-ui,sans-serif';
  var help=document.createElement('button');help.type='button';help.id='__uxhelp';help.textContent='❔ Ayuda';
  help.style.cssText='border:none;border-radius:20px;padding:7px 13px;font-size:12px;background:#0a4d8c;color:#fff;cursor:pointer;box-shadow:0 3px 12px rgba(0,0,0,.25)';
  help.onclick=function(){tour();};
  bar.appendChild(help);
  if(!ISHOME&&hasNew){var fab=document.createElement('button');fab.type='button';fab.id='__uxnew';fab.textContent='＋ Nuevo';
   fab.style.cssText='border:none;border-radius:24px;padding:12px 20px;font-size:15px;font-weight:700;background:#1aa39a;color:#fff;cursor:pointer;box-shadow:0 5px 18px rgba(26,163,154,.45)';
   fab.onclick=goNew;bar.appendChild(fab);}
  document.body.appendChild(bar);
  if(!ISHOME&&!localStorage.getItem('sigej_tour_'+pk))tour();
 }
 function goNew(){var e=findNew();if(!e){toast('Esta página es de consulta: no tiene captura.');return;}
  e.scrollIntoView({behavior:'smooth',block:'center'});
  var o=e.style.boxShadow;e.style.transition='box-shadow .3s';e.style.boxShadow='0 0 0 4px rgba(26,163,154,.65)';
  setTimeout(function(){try{e.focus();}catch(_){}},420);setTimeout(function(){e.style.boxShadow=o;},1900);}
 function toast(m){var d=document.createElement('div');d.textContent=m;d.style.cssText='position:fixed;left:50%;bottom:84px;transform:translateX(-50%);background:#00254a;color:#fff;padding:10px 16px;border-radius:10px;font:13px Segoe UI,system-ui;z-index:99998;box-shadow:0 4px 16px rgba(0,0,0,.3)';document.body.appendChild(d);setTimeout(function(){d.remove();},2600);}
 function tour(){
  var STEPS=[['📝 Captura y consulta','Da de alta o busca registros con los botones y formularios de esta página. El botón verde «＋ Nuevo» (abajo a la izquierda) te lleva directo a la captura.'],
   ['📎 Expediente electrónico','Adjunta archivos por categoría a cada registro. El botón «🔎 OCR» puede leer el documento y autocompletar campos.'],
   ['🔗 Todo conectado','Cada registro queda con trazabilidad y aparece en el buscador de Transparencia General. Lo que entra por Oficialía de Partes se vuelve antecedente en su módulo.']];
  var i=0;var ov=document.createElement('div');
  ov.style.cssText='position:fixed;inset:0;background:rgba(8,20,38,.72);z-index:99990;display:flex;align-items:center;justify-content:center;padding:20px;font-family:Segoe UI,system-ui,sans-serif';
  function close(){try{localStorage.setItem('sigej_tour_'+pk,'1');}catch(_){}ov.remove();}
  function draw(){var s=STEPS[i];
   ov.innerHTML='<div style="background:#fff;border-radius:16px;max-width:430px;width:100%;padding:24px;box-shadow:0 12px 40px rgba(0,0,0,.4)">'+
   '<div style="font-size:11px;color:#94a3b8;letter-spacing:.5px;margin-bottom:6px">GUÍA RÁPIDA · PASO '+(i+1)+' DE 3</div>'+
   '<h2 style="margin:0 0 8px;color:#00254a;font-size:19px">'+s[0]+'</h2>'+
   '<div style="color:#475569;font-size:13.5px;line-height:1.6">'+s[1]+'</div>'+
   '<div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px">'+
   '<button id="__tskip" style="background:none;border:none;color:#94a3b8;font-size:12px;cursor:pointer;text-decoration:underline">No volver a mostrar</button>'+
   '<div><button id="__tprev" style="padding:9px 14px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;cursor:pointer;margin-right:6px;'+(i===0?'display:none':'')+'">Atrás</button>'+
   '<button id="__tnext" style="padding:9px 18px;border:none;border-radius:8px;background:#1aa39a;color:#fff;font-weight:700;cursor:pointer">'+(i===2?'Entendido ✓':'Siguiente →')+'</button></div></div></div>';
   ov.querySelector('#__tnext').onclick=function(){if(i<2){i++;draw();}else close();};
   var pv=ov.querySelector('#__tprev');if(pv)pv.onclick=function(){if(i>0){i--;draw();}};
   ov.querySelector('#__tskip').onclick=close;}
  draw();document.body.appendChild(ov);
 }
})();</script><script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;margin-top:0!important}";document.head.appendChild(st);function clean(){try{var c=document.getElementById("__chg");if(c&&c.parentNode)c.parentNode.style.display="none";document.querySelectorAll("div[style*=\"99999\"]").forEach(function(o){o.remove();});}catch(e){}}clean();setTimeout(clean,150);setTimeout(clean,500);setTimeout(clean,1200);})();</script>
<script>
/* SIGEJ · PWA + RWD (responsive, Mobile First) + modo oscuro — capa universal */
(function(){try{
var isEmbed=/[?&]embed=1/.test(location.search);
/* --- PWA: manifest + meta + service worker (instalable en iOS/iPadOS/Android sin tienda) --- */
if(!isEmbed){
 function meta(n,c){var m=document.createElement('meta');m.name=n;m.content=c;document.head.appendChild(m);}
 if(!document.querySelector('link[rel="manifest"]')){var l=document.createElement('link');l.rel='manifest';l.href='sigej.webmanifest';document.head.appendChild(l);}
 meta('theme-color','#00254a');meta('mobile-web-app-capable','yes');meta('apple-mobile-web-app-capable','yes');meta('apple-mobile-web-app-status-bar-style','black-translucent');meta('apple-mobile-web-app-title','SIGEJ');
 var al=document.createElement('link');al.rel='apple-touch-icon';al.href='sigej_icon.svg';document.head.appendChild(al);
 if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('sigej_sw.js').catch(function(){});});}
}
/* --- RWD: endurecimiento responsivo universal (no altera la maqueta de escritorio) --- */
var css=document.createElement('style');css.setAttribute('data-sigej','rwd');
css.textContent=[
 'img,video,canvas{max-width:100%;height:auto}',
 'html{-webkit-text-size-adjust:100%}',
 '@media (max-width:768px){',
 '  .navbar{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch}',
 '  .navbar a{white-space:nowrap}',
 '  button,.tb,.tab,.ootb,.navbar a{min-height:40px}',
 '  table{display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;white-space:nowrap}',
 '  .kpis,.cards,.apps{grid-template-columns:1fr!important}',
 '  .grid[style*="1fr 1fr"],.grid[style*="1.3fr"],.grid[style*="1.4fr"]{grid-template-columns:1fr!important}',
 '  .panel{width:100%!important}',
 '}',
 '@media (max-width:480px){ header h1{font-size:16px!important} .wrap{padding-left:10px!important;padding-right:10px!important} }',
 /* modo oscuro global por inversión controlada (se re-invierte multimedia para no dañar imágenes/QR/iframes) */
 'html.sigej-dark{filter:invert(0.92) hue-rotate(180deg);background:#0e1626}',
 'html.sigej-dark img,html.sigej-dark canvas,html.sigej-dark iframe,html.sigej-dark video,html.sigej-dark svg,html.sigej-dark .cov,html.sigej-dark .fichacov,html.sigej-dark .acuse .q img{filter:invert(1) hue-rotate(180deg)}',
 '#sigejDark{position:fixed;left:16px;bottom:16px;z-index:99990;background:#0a4d8c;color:#fff;border:none;border-radius:50%;width:42px;height:42px;font-size:18px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.3)}'
].join('\n');
document.head.appendChild(css);
if(localStorage.getItem('sigej_dark')==='1')document.documentElement.classList.add('sigej-dark');
if(!isEmbed){
 var db=document.createElement('button');db.id='sigejDark';db.type='button';db.title='Modo claro / oscuro';db.textContent=localStorage.getItem('sigej_dark')==='1'?'☀️':'🌙';
 db.onclick=function(){var on=document.documentElement.classList.toggle('sigej-dark');localStorage.setItem('sigej_dark',on?'1':'0');db.textContent=on?'☀️':'🌙';};
 if(document.body)document.body.appendChild(db);
}
}catch(e){}})();
</script>

<script>
/* SIGEJ · Panel universal "Normativa aplicable" (asistente jurídico normativo por pantalla) */
(function(){try{
if(/[?&]embed=1/.test(location.search))return;
var pk=(location.pathname.split('/').pop()||'x').replace('.html','')||'x';
if(/^(index|acceso_SIGEJ|SIGEJ_inicio)$/.test(pk))return;if(!document.body)return;
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function ec(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
var DEF=[
 {amb:'Interna',cat:'Contratos',nombre:'Normatividad de Contratos',url:'https://secgral.udg.mx/normatividad/contratos',mods:['instrumentos_SIGEJ']},
 {amb:'Interna',cat:'Contratos',nombre:'Empresa Universitaria',url:'https://secgral.udg.mx/normatividad/contratos/empresa-universitaria',mods:['instrumentos_SIGEJ','patrimonio_SIGEJ']},
 {amb:'Interna',cat:'Acuerdos',nombre:'Acuerdos de Rectoría General',url:'https://secgral.udg.mx/acuerdos/rectoria-general',mods:[]},
 {amb:'Interna',cat:'Acuerdos',nombre:'Acuerdos Comisión de Hacienda',url:'https://secgral.udg.mx/acuerdos/comision-de-hacienda',mods:['instrumentos_SIGEJ','administracion_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Comisión de Hacienda',url:'https://secgral.udg.mx/circulares/comision-de-hacienda',mods:['administracion_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Comisión de Responsabilidades y Sanciones',url:'https://secgral.udg.mx/circulares/comision-de-responsabilidades-y-sanciones',mods:['contencioso_SIGEJ','resp_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Rectoría General',url:'https://secgral.udg.mx/circulares/rectoria-general',mods:[]},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Secretaría General',url:'https://secgral.udg.mx/circulares/secretaria-general',mods:['oficialia_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Anuales',url:'https://secgral.udg.mx/circulares-anuales',mods:[]},
 {amb:'Interna',cat:'Normatividad',nombre:'Normatividad General',url:'https://secgral.udg.mx/normatividad/general',mods:['normatividad_SIGEJ','instrumentos_SIGEJ','contencioso_SIGEJ']},
 {amb:'Interna',cat:'Normatividad',nombre:'Normatividad Específica',url:'https://secgral.udg.mx/normatividad/especifica',mods:['normatividad_SIGEJ']},
 {amb:'Interna',cat:'Órganos colegiados',nombre:'Sesiones del CGU',url:'http://www.hcgu.udg.mx/sesioneshcgu',mods:['normatividad_SIGEJ']},
 {amb:'Interna',cat:'Órganos colegiados',nombre:'Dictámenes del CGU',url:'http://www.hcgu.udg.mx/dictamenes',mods:['normatividad_SIGEJ','instrumentos_SIGEJ']},
 {amb:'Interna',cat:'Órganos colegiados',nombre:'Sesiones de Comisiones',url:'http://www.hcgu.udg.mx/sesiones-de-comisiones',mods:['normatividad_SIGEJ']},
 {amb:'Externa',cat:'Federal',nombre:'Legislación Federal (Diputados)',url:'https://www.diputados.gob.mx/LeyesBiblio/index.htm',mods:['instrumentos_SIGEJ','contencioso_SIGEJ','internacional_SIGEJ','patrimonio_SIGEJ']},
 {amb:'Externa',cat:'Federal',nombre:'Reglamentos Federales',url:'https://www.diputados.gob.mx/LeyesBiblio/regla.htm',mods:['instrumentos_SIGEJ','contencioso_SIGEJ']},
 {amb:'Externa',cat:'Estatal',nombre:'Legislación de Jalisco',url:'https://congresoweb.congresojal.gob.mx/BibliotecaVirtual/LeyesEstatales.cfm',mods:['contencioso_SIGEJ','instrumentos_SIGEJ','oficialia_SIGEJ']},
 {amb:'Externa',cat:'NOM',nombre:'Normas Oficiales Mexicanas',url:'https://platiica.economia.gob.mx/normalizacion/normas-oficiales-mexicanas/',mods:['patrimonio_SIGEJ','internacional_SIGEJ']}
];
function REPO(){var r=J('sigej_repo_normativo');return Array.isArray(r)&&r.length?r:DEF;}
var base=pk;
var rel=REPO().filter(function(x){return (x.mods||[]).indexOf(base)>=0;});
var gen=REPO().filter(function(x){return !(x.mods||[]).length&&x.amb==='Interna';});
var b=document.createElement('div');b.textContent='📖 Normativa';
b.style.cssText='position:fixed;right:16px;bottom:100px;background:#5a2e8c;color:#fff;padding:9px 14px;border-radius:22px;font:600 12.5px system-ui,sans-serif;cursor:pointer;z-index:99994;box-shadow:0 4px 14px rgba(0,0,0,.25)';
var p=document.createElement('div');
p.style.cssText='position:fixed;right:16px;bottom:146px;width:360px;max-width:94vw;max-height:74vh;background:#fff;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 12px 34px rgba(0,0,0,.3);z-index:99995;display:none;flex-direction:column;overflow:hidden';
document.body.appendChild(b);document.body.appendChild(p);
function link(x){return '<a href="'+ec(x.url)+'" target="_blank" rel="noopener" style="display:flex;gap:7px;align-items:center;padding:7px 9px;border:1px solid #eef2f7;border-radius:8px;margin-bottom:5px;text-decoration:none;color:#0a2f4f;font:12px system-ui,sans-serif"><span>'+(x.amb==='Interna'?'🏛️':'🌐')+'</span><span>'+ec(x.nombre)+'</span><span style="margin-left:auto;font-size:10px;color:#94a3b8">↗</span></a>';}
function render(){p.innerHTML='<div style="background:#5a2e8c;color:#fff;padding:9px 12px;font:700 13px system-ui,sans-serif;display:flex;justify-content:space-between;align-items:center"><span>📖 Normativa aplicable</span><span id="__nx" style="cursor:pointer;font-size:16px">✕</span></div><div style="overflow:auto;padding:10px 12px;flex:1">'+
 (rel.length?'<div style="font:600 11px system-ui,sans-serif;color:#5a2e8c;margin-bottom:5px">RELACIONADA CON ESTE MÓDULO</div>'+rel.map(link).join(''):'<div style="font:12px system-ui,sans-serif;color:#94a3b8;margin-bottom:6px">Sin normas mapeadas específicamente a este módulo.</div>')+
 '<div style="font:600 11px system-ui,sans-serif;color:#5a2e8c;margin:8px 0 5px">NORMATIVIDAD INSTITUCIONAL</div>'+gen.slice(0,5).map(link).join('')+
 '<a href="cumplimiento_SIGEJ.html" style="display:block;text-align:center;margin-top:8px;background:#0a4d8c;color:#fff;border-radius:8px;padding:8px;text-decoration:none;font:600 12px system-ui,sans-serif">⚖️ Abrir Motor de Cumplimiento</a>'+
 '<div style="font:10.5px system-ui,sans-serif;color:#64748b;margin-top:8px">Repositorio administrado por la Coordinación de Normatividad. Términos y plazos conforme a la ley aplicable.</div></div>';
 p.querySelector('#__nx').onclick=function(){p.style.display='none';};}
b.onclick=function(){var o=p.style.display!=='none';if(o){p.style.display='none';}else{render();p.style.display='flex';}};
}catch(e){}})();
</script>
</body></html>"""
open("/Users/edithroque/Documents/CLAUDE/abogados_SIGEJ.html","w",encoding="utf-8").write(TPL.replace("__DATA__",DATA).replace("__NAV__",NAV))
print("abogados_SIGEJ.html OK")
