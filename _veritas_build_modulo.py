# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/expedientes_data.json",encoding="utf-8"))
DATA=json.dumps(d,ensure_ascii=False)
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Módulo de Gestión Integral de Expedientes</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--amber:#e08e0b;--ok:#1f9d6b;
--bg:#f4f6f9;--card:#fff;--mut:#64748b;--line:#e2e8f0;--ink:#0a1f3c;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:16px 24px}
header h1{margin:0;font-size:18px}header .sub{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:16px 24px;max-width:1500px;margin:auto}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:var(--card);border-radius:10px;padding:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);border-left:4px solid var(--teal)}
.kpi .n{font-size:22px;font-weight:700;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut)}
.kpi.bad{border-left-color:var(--red)}.kpi.warn{border-left-color:var(--gold)}
.bar{background:var(--card);border-radius:10px;padding:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:12px}
.bar input,.bar select{padding:7px 9px;border:1px solid var(--line);border-radius:7px;font-size:12.5px;color:var(--ink)}
.bar input[type=text]{min-width:220px}
.bar button{padding:7px 12px;border:none;border-radius:7px;background:var(--azul2);color:#fff;cursor:pointer;font-size:12.5px}
.cnt{font-size:12px;color:var(--mut);margin-left:auto}
table{width:100%;border-collapse:collapse;background:var(--card);border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.07);font-size:12.5px}
th,td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--line)}
th{background:#eef2f7;color:var(--mut);font-weight:600;cursor:pointer;position:sticky;top:0}
tr:hover td{background:#f8fafc}
.num{color:var(--azul2);font-weight:600;cursor:pointer}
.sem{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:4px;vertical-align:middle}
.s-Crítico{background:var(--red)}.s-Alto{background:var(--amber)}.s-Medio{background:var(--teal)}.s-Bajo{background:#9fb3c8}
.pri{font-size:10.5px;padding:1px 7px;border-radius:9px;font-weight:600}
.p-Urgente{background:#fdecea;color:#c0392b}.p-Alta{background:#fef3e0;color:#b9770e}.p-Normal{background:#eef2f7;color:#64748b}
.modal{position:fixed;inset:0;background:rgba(8,20,38,.55);display:none;align-items:center;justify-content:center;z-index:50;padding:16px}
.modal.on{display:flex}.mbox{background:#fff;border-radius:14px;max-width:920px;width:100%;max-height:90vh;overflow:auto;padding:20px}
.mx{float:right;cursor:pointer;color:var(--mut);font-size:22px}
.fhdr{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;margin:10px 0}
.fld{background:#f4f6f9;border-radius:8px;padding:7px 10px}.fld .k{font-size:10px;color:var(--mut);text-transform:uppercase}.fld .v{font-size:13px;font-weight:600}
.cats{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.chip{font-size:11px;padding:3px 9px;border-radius:12px;background:#eef2f7;color:#475569}
.mh{font-size:13px;color:var(--azul);font-weight:700;margin:14px 0 6px;border-bottom:2px solid var(--line);padding-bottom:4px}
.act{font-size:12px;color:#334155;background:#f8fafc;border-radius:8px;padding:10px;max-height:200px;overflow:auto;white-space:pre-wrap}
.cap{font-size:11px;color:#8a6d1a;background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:6px 10px;display:inline-block}
.tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:6px 0}
.tools select,.tools input{padding:6px 8px;border:1px solid var(--line);border-radius:6px;font-size:12px}
.tools button{padding:6px 11px;border:none;border-radius:6px;background:#0a4d8c;color:#fff;cursor:pointer;font-size:12px}
.doc{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 9px;border:1px solid var(--line);border-radius:7px;margin:4px 0;font-size:12.5px}
.doc .lk{color:#0a4d8c;cursor:pointer;text-decoration:underline}
.doc .del{color:#c0392b;cursor:pointer}
.ag{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 9px;border-radius:7px;margin:4px 0;font-size:12.5px;border-left:4px solid #9fb3c8}
.ag.venc{background:#fdecea;border-left-color:#c0392b}.ag.urg{background:#fef3e0;border-left-color:#e08e0b}.ag.prox{background:#fffbe9;border-left-color:#d4a32c}.ag.ok{background:#f4f6f9}
.tb{font-size:10.5px;padding:1px 7px;border-radius:9px;background:#0a4d8c;color:#fff;font-weight:600}
.viewer{position:fixed;inset:0;background:rgba(8,20,38,.7);display:none;align-items:center;justify-content:center;z-index:60;padding:16px}
.viewer.on{display:flex}.vbox{background:#fff;border-radius:12px;max-width:1000px;width:100%;max-height:92vh;overflow:auto;padding:16px}
.wide{position:fixed;inset:0;background:rgba(8,20,38,.6);display:none;z-index:55;padding:18px;overflow:auto}
.wide.on{display:block}.wbox{background:#f4f6f9;border-radius:12px;max-width:1500px;margin:auto;padding:18px;min-height:90vh}
.kb{display:flex;gap:12px;overflow-x:auto;padding-bottom:8px}
.kcol{min-width:215px;background:#eef2f7;border-radius:10px;padding:8px;flex:0 0 auto}
.kcol h4{margin:0 0 8px;font-size:12.5px;color:var(--azul);display:flex;justify-content:space-between}
.kcard{background:#fff;border-radius:8px;padding:8px;margin-bottom:7px;box-shadow:0 1px 2px rgba(0,0,0,.08);cursor:pointer;border-left:3px solid var(--teal);font-size:11.5px}
.kcard.k-Crítico{border-left-color:var(--red)}.kcard.k-Alto{border-left-color:var(--amber)}.kcard.k-Medio{border-left-color:var(--teal)}.kcard.k-Bajo{border-left-color:#9fb3c8}
.kcard b{color:var(--azul)}
.gantt{background:#fff;border-radius:10px;padding:12px;overflow-x:auto}
.grow{display:flex;align-items:center;border-bottom:1px solid var(--line);min-height:34px}
.glabel{width:120px;flex:0 0 120px;font-size:11.5px;font-weight:600;color:var(--azul)}
.gtrack{position:relative;flex:1;height:24px}
.gmark{position:absolute;top:3px;width:15px;height:15px;border-radius:50%;transform:translateX(-50%);cursor:default;border:2px solid #fff}
.gaxis{display:flex;margin-left:120px;border-top:1px solid var(--line);font-size:10px;color:var(--mut)}
.gaxis span{flex:1;text-align:left;padding-top:3px}
footer{padding:14px 24px;color:var(--mut);font-size:11px;text-align:center}
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
<header style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap"><div><h1>📁 SIGEJ-UdeG · Módulo de Gestión Integral de Expedientes</h1>
<div class="sub">Oficina de la Abogacía General · Universidad de Guadalajara · corte <b id="fc"></b> · <span id="tot"></span> expedientes</div></div>
<div style="display:flex;gap:8px;flex-wrap:wrap"><a href="SIGEJ_inicio.html" style="text-decoration:none;background:rgba(255,255,255,.15);color:#fff;padding:9px 13px;border-radius:8px;font-size:13px;font-weight:600">🏠</a><button onclick="kanbanView()" style="background:#0a4d8c;color:#fff;border:none;padding:9px 14px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer">📋 Kanban</button>
<button onclick="ganttView()" style="background:#5d6d7e;color:#fff;border:none;padding:9px 14px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer">📊 Gantt</button>
<button onclick="agendaAll()" style="background:#d4a32c;color:#fff;border:none;padding:9px 14px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer">📅 Agenda</button>
<a href="captura_expediente_SIGEJ.html" style="text-decoration:none;background:#1f9d6b;color:#fff;padding:9px 16px;border-radius:8px;font-size:13px;font-weight:600">➕ Capturar</a></div></header>
<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="modulo_expedientes_SIGEJ.html" class="act">📁 Expedientes</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="proyectos_SIGEJ.html">📌 Proyectos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="asesoria_SIGEJ.html">💡 Asesoría</a><a href="captura_expediente_SIGEJ.html">➕ Captura</a><a href="abogados_SIGEJ.html">👤 Abogados</a><a href="documental_SIGEJ.html">🗂️ Documental</a><a href="transparencia_SIGEJ.html">🔎 Transparencia</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="masc_SIGEJ.html">🤝 MASC</a><a href="resp_SIGEJ.html">⚖️ Responsabilidades</a><a href="alertas_centro_SIGEJ.html">🔔 Alertas</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>
<div class="wrap">
 <div class="kpis" id="kpis"></div>
 <div class="bar">
  <input type="text" id="q" placeholder="🔎 Buscar nº, actor, demandado…" oninput="render()">
  <select id="f_materia_fina" onchange="render()"></select>
  <select id="f_via" onchange="render()"></select>
  <select id="f_estado" onchange="render()"></select>
  <select id="f_nivel_riesgo" onchange="render()"></select>
  <select id="f_anio" onchange="render()"></select>
  <select id="f_responsable" onchange="render()"></select>
  <select id="f_centro" onchange="render()"></select>
  <select id="f_dependencia" onchange="render()"></select>
  <button onclick="reset_()">Limpiar</button>
  <button onclick="expFiltered()" style="background:#1f9d6b">⬇ Exportar</button>
  <span class="cnt" id="cnt"></span>
 </div>
 <div style="max-height:62vh;overflow:auto;border-radius:10px">
 <table><thead><tr>
  <th onclick="sort_('num')">Expediente</th><th onclick="sort_('materia_fina')">Materia</th><th onclick="sort_('via')">Vía / Tipo</th>
  <th onclick="sort_('dependencia')">Dependencia</th><th onclick="sort_('responsable')">Responsable</th>
  <th onclick="sort_('estado')">Estado</th><th onclick="sort_('score')">Riesgo</th><th onclick="sort_('prioridad')">Prioridad</th><th onclick="sort_('monto')">Monto</th>
 </tr></thead><tbody id="tb"></tbody></table></div>
</div>
<div class="modal" id="modal"><div class="mbox"><span class="mx" onclick="cf()">✕</span><div id="mbody"></div></div></div>
<div class="viewer" id="viewer"><div class="vbox"><span class="mx" onclick="document.getElementById('viewer').classList.remove('on')" style="cursor:pointer;float:right;color:#64748b;font-size:22px">✕</span><h3 id="vtitle" style="margin:0 0 10px;color:#00254a"></h3><div id="vbody"></div></div></div>
<div class="modal" id="agenda"><div class="mbox"><span class="mx" onclick="document.getElementById('agenda').classList.remove('on')">✕</span><h2 style="margin:0 0 6px;color:#00254a">📅 Agenda y Alertas — vencimientos capturados</h2><div id="abody"></div></div></div>
<div class="wide" id="kanban"><div class="wbox"><span class="mx" style="float:right;cursor:pointer;color:#64748b;font-size:24px" onclick="document.getElementById('kanban').classList.remove('on')">✕</span><h2 style="margin:0 0 4px;color:#00254a">📋 Kanban — pipeline por estado procesal <button onclick="kreset()" style="font-size:11px;background:#eef2f7;color:#64748b;border:none;border-radius:6px;padding:4px 9px;cursor:pointer;float:right;margin-right:30px">↺ Restablecer estados</button></h2><div style="font-size:12px;color:#64748b;margin-bottom:12px">🖱️ <b>Arrastra una tarjeta</b> a otra columna para cambiar su estado procesal (se guarda localmente y se refleja en la tabla y la ficha). El punto verde ● marca los movidos. Hasta 25 por columna (mayor riesgo primero); clic abre la ficha.</div><div class="kb" id="kbody"></div></div></div>
<div class="wide" id="gantt"><div class="wbox"><span class="mx" style="float:right;cursor:pointer;color:#64748b;font-size:24px" onclick="document.getElementById('gantt').classList.remove('on')">✕</span><h2 style="margin:0 0 4px;color:#00254a">📊 Gantt — línea de tiempo de la agenda</h2><div style="font-size:12px;color:#64748b;margin-bottom:12px">Audiencias 🟦 · Términos 🟥 · Plazos 🟧 · Contestaciones 🟪 · Seguimientos 🟩. Captura agenda en las fichas para poblarlo.</div><div class="gantt" id="gbody"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const MAP={};D.expedientes.forEach(e=>MAP[e.id]=e);
const EST_OVR=JSON.parse(localStorage.getItem('sigej_estado')||'{}');
function recPri(e){const activo=e.estado.toUpperCase()!=='CONCLUIDO';return(activo&&(e.estado==='Laudo'||e.estado==='Sentencia'||e.nivel_riesgo==='Crítico'))?'Urgente':e.nivel_riesgo==='Alto'?'Alta':'Normal';}
D.expedientes.forEach(e=>{if(EST_OVR[e.num]&&EST_OVR[e.num]!==e.estado){e.estado=EST_OVR[e.num];e.prioridad=recPri(e);e.movido=true;}});
let DRAGID=null;
function kdrag(ev,id){DRAGID=id;try{ev.dataTransfer.setData('text',id);ev.dataTransfer.effectAllowed='move';}catch(x){}}
function kdrop(ev,st){ev.preventDefault();const id=DRAGID||(ev.dataTransfer&&ev.dataTransfer.getData('text'));if(!id)return;const e=MAP[id];
 if(!e||e.estado===st)return;e.estado=st;e.prioridad=recPri(e);e.movido=true;EST_OVR[e.num]=st;
 localStorage.setItem('sigej_estado',JSON.stringify(EST_OVR));DRAGID=null;kanbanView();render();}
function kreset(){if(Object.keys(EST_OVR).length&&confirm('¿Revertir todos los cambios de estado hechos en el Kanban?')){localStorage.removeItem('sigej_estado');location.reload();}}
document.getElementById('fc').textContent=D.corte;document.getElementById('tot').textContent=D.kpi.total;
const K=D.kpi;
document.getElementById('kpis').innerHTML=[[K.activos,'Activos',''],[K.concluidos,'Concluidos',''],[K.con_sentencia,'Con sentencia/laudo',''],
 [K.susp,'Susp. concedidas','warn'],[K.alto_riesgo,'Alto riesgo','bad'],[K.urgentes,'Urgentes','bad'],
 ['$'+(K.pasivo/1e6).toFixed(2)+'M','Pasivo (piso)','warn'],[K.responsables,'Responsables','']]
 .map(k=>`<div class="kpi ${k[2]}"><div class="n">${k[0]}</div><div class="l">${k[1]}</div></div>`).join('');
function fill(id,arr,lbl){const s=document.getElementById(id);s.innerHTML=`<option value="">${lbl}</option>`+arr.map(x=>`<option>${x}</option>`).join('');}
fill('f_materia_fina',D.catalogos.materia_fina,'Materia (fina)');fill('f_via',D.catalogos.via,'Vía');fill('f_estado',D.catalogos.estado,'Estado procesal');
fill('f_nivel_riesgo',D.catalogos.nivel_riesgo,'Nivel de riesgo');fill('f_anio',D.catalogos.anio,'Año');
fill('f_responsable',D.catalogos.responsable,'Responsable');fill('f_centro',D.catalogos.centro,'Centro/Tipo');
fill('f_dependencia',D.catalogos.dependencia,'Dependencia');
let SORT={k:'score',dir:-1};
function sort_(k){SORT.dir=SORT.k===k?-SORT.dir:-1;SORT.k=k;render();}
function val(id){return document.getElementById(id).value;}
function filtered(){const q=val('q').toLowerCase();
 return D.expedientes.filter(e=>{
  if(q&&!((e.num+' '+e.actor+' '+e.demandado).toLowerCase().includes(q)))return false;
  for(const f of ['materia_fina','via','estado','nivel_riesgo','responsable','centro','dependencia']){const v=val('f_'+f);if(v&&e[f]!==v)return false;}
  const ya=val('f_anio');if(ya&&String(e.anio)!==ya)return false;return true;})
  .sort((a,b)=>{let x=a[SORT.k],y=b[SORT.k];if(typeof x==='string'){x=x||'';y=y||'';return SORT.dir*x.localeCompare(y);}return SORT.dir*((x||0)-(y||0));});}
function render(){const L=filtered();const cap=L.slice(0,300);
 document.getElementById('cnt').textContent=L.length+' resultados'+(L.length>300?' (mostrando 300)':'');
 document.getElementById('tb').innerHTML=cap.map(e=>`<tr><td class="num" onclick="od('${e.id}')">${e.num}</td><td>${e.materia_fina}</td><td>${e.via==='Jurisdicción ordinaria'?e.tipo_juicio:e.via}</td>`+
  `<td>${(e.dependencia||'').slice(0,26)}</td><td>${(e.responsable||'').split(' ').slice(0,2).join(' ')}</td><td>${e.estado}</td>`+
  `<td><span class="sem s-${e.nivel_riesgo}"></span>${e.nivel_riesgo} (${e.score})</td><td><span class="pri p-${e.prioridad}">${e.prioridad}</span></td>`+
  `<td>${e.monto?'$'+e.monto.toLocaleString('es-MX'):'—'}</td></tr>`).join('');}
const DOCCATS=['Demanda','Contestación','Acuerdo','Sentencia/Laudo','Suspensión','Recurso','Prueba','Oficio','Convenio','Contrato','Minuta','Correo','Informe','Dictamen','Evidencia','Fotografía','Otro'];
let ENR=JSON.parse(localStorage.getItem('sigej_enr')||'{}');
function enr(num){if(!ENR[num])ENR[num]={pruebas:'',docs:[],agenda:[]};return ENR[num];}
function saveEnr(){try{localStorage.setItem('sigej_enr',JSON.stringify(ENR));}catch(e){alert('Almacenamiento local lleno: exporta y elimina documentos pesados.');}}
let TZ=JSON.parse(localStorage.getItem('sigej_traza')||'{}');
function mtz(num){if(!TZ[num])TZ[num]={resp:[],inst:[]};return TZ[num];}
function saveTZ(){localStorage.setItem('sigej_traza',JSON.stringify(TZ));}
const LAWNAMES=[...new Set(D.expedientes.map(e=>e.responsable))].filter(x=>x&&x!=='(sin asignar)');
function mtzAddResp(id){const e=MAP[id],n=document.getElementById('mrz_nom').value.trim();if(!n){alert('Indica el abogado.');return;}
 mtz(e.num).resp.push({nombre:n,rol:document.getElementById('mrz_rol').value,desde:document.getElementById('mrz_d').value,hasta:document.getElementById('mrz_h').value,nota:''});saveTZ();od(id);}
function mtzAddInst(id){const e=MAP[id],n=document.getElementById('miz_nom').value.trim();if(!n){alert('Indica el nombre.');return;}
 mtz(e.num).inst.push({rol:document.getElementById('miz_rol').value,nombre:n,desde:document.getElementById('miz_d').value,hasta:document.getElementById('miz_h').value});saveTZ();od(id);}
function mtzDel(id,tipo,i){mtz(MAP[id].num)[tipo].splice(i,1);saveTZ();od(id);}
const HOY=new Date(2026,5,18);
function diasRest(f){return Math.round((new Date(f+'T00:00:00')-HOY)/86400000);}
function claseDia(d){return d<0?'venc':d<=7?'urg':d<=30?'prox':'ok';}
function savePrb(id){enr(MAP[id].num).pruebas=document.getElementById('prb').value;saveEnr();}
function addSegM(id){const t=(document.getElementById('segt').value||'').trim();if(!t)return;const en=enr(MAP[id].num);en.seguimiento=en.seguimiento||[];en.seguimiento.push({ts:new Date().toISOString().slice(0,16).replace('T',' '),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',texto:t});saveEnr();od(id);}
function attachDoc(id){const e=MAP[id],cat=document.getElementById('dcat').value,files=document.getElementById('dfile').files;
 if(!files.length){alert('Selecciona un archivo.');return;}let pend=files.length;
 [...files].forEach(f=>{if(f.size>1600000){alert('"'+f.name+'" supera 1.5 MB (límite del prototipo local).');if(!--pend)od(id);return;}
  const rd=new FileReader();rd.onload=()=>{enr(e.num).docs.push({name:f.name,type:f.type,size:f.size,cat:cat,fecha:new Date().toISOString().slice(0,10),data:rd.result});saveEnr();if(!--pend)od(id);};rd.readAsDataURL(f);});}
function viewDoc(id,i){const dd=enr(MAP[id].num).docs[i],v=document.getElementById('vbody');
 if((dd.type||'').includes('pdf'))v.innerHTML='<iframe src="'+dd.data+'" style="width:100%;height:74vh;border:1px solid #e2e8f0;border-radius:8px"></iframe>';
 else if((dd.type||'').startsWith('image'))v.innerHTML='<img src="'+dd.data+'" style="max-width:100%;border-radius:8px">';
 else v.innerHTML='<a href="'+dd.data+'" download="'+dd.name+'">Descargar '+dd.name+'</a>';
 document.getElementById('vtitle').textContent=dd.cat+' · '+dd.name;document.getElementById('viewer').classList.add('on');}
function delDoc(id,i){enr(MAP[id].num).docs.splice(i,1);saveEnr();od(id);}
function addAg(id){const f=document.getElementById('afecha').value;if(!f){alert('Indica la fecha.');return;}
 enr(MAP[id].num).agenda.push({tipo:document.getElementById('atipo').value,fecha:f,nota:document.getElementById('anota').value});saveEnr();od(id);}
function delAg(id,fecha,tipo){const ag=enr(MAP[id].num).agenda,i=ag.findIndex(a=>a.fecha===fecha&&a.tipo===tipo);if(i>=0)ag.splice(i,1);saveEnr();od(id);}
function agendaAll(){let it=[];Object.keys(ENR).forEach(num=>(ENR[num].agenda||[]).forEach(a=>it.push({num:num,tipo:a.tipo,fecha:a.fecha,nota:a.nota})));
 it.sort((x,y)=>x.fecha.localeCompare(y.fecha));
 document.getElementById('abody').innerHTML=it.length?('<div style="font-size:12px;color:#64748b;margin:6px 0">'+it.length+' eventos · corte 18/jun/2026</div>'+it.map(a=>{const dd=diasRest(a.fecha);return `<div class="ag ${claseDia(dd)}"><span><span class="tb">${a.tipo}</span> Exp. <b>${a.num}</b> · ${a.fecha} ${a.nota?'· '+a.nota:''}</span><span><b>${dd<0?'venció hace '+(-dd):'en '+dd} d</b></span></div>`;}).join('')):'<span class="cap">Aún no hay agenda. Abre un expediente y agrega audiencias/términos/plazos.</span>';
 document.getElementById('agenda').classList.add('on');}
function kanbanView(){const order=['Demanda','SIN EMPLAZAR','Contestación','Pruebas','Alegatos','TRÁMITE','Amparo','Laudo','Sentencia','Apelación','Convenio','CONCLUIDO'];
 const g={};D.expedientes.forEach(e=>{(g[e.estado]=g[e.estado]||[]).push(e);});
 const ord=order.filter(o=>g[o]).concat(Object.keys(g).filter(k=>!order.includes(k)));
 document.getElementById('kbody').innerHTML=ord.map(st=>{const arr=g[st].slice().sort((a,b)=>b.score-a.score),top=arr.slice(0,25);
  return `<div class="kcol" ondragover="event.preventDefault()" ondrop="kdrop(event,'${st.replace(/'/g,"")}')"><h4><span>${st}</span><span>${arr.length}</span></h4>`+top.map(e=>`<div class="kcard k-${e.nivel_riesgo}" draggable="true" ondragstart="kdrag(event,'${e.id}')" onclick="document.getElementById('kanban').classList.remove('on');od('${e.id}')"><b>${e.num}</b> ${e.movido?'<span style="color:#1f9d6b">●</span>':''} · ${e.materia_fina}<br><span style="color:#64748b">${(e.responsable||'').split(' ').slice(0,2).join(' ')} · ${e.nivel_riesgo} (${e.score})</span></div>`).join('')+(arr.length>25?`<div style="font-size:11px;color:#64748b;text-align:center">+${arr.length-25} más</div>`:'')+`</div>`;}).join('');
 document.getElementById('kanban').classList.add('on');}
function ganttView(){let items=[];Object.keys(ENR).forEach(num=>(ENR[num].agenda||[]).forEach(a=>items.push({num:num,tipo:a.tipo,fecha:a.fecha,nota:a.nota})));
 const W=document.getElementById('gbody');
 if(!items.length){W.innerHTML='<span class="cap">No hay agenda capturada. Abre un expediente → "Agenda y alertas" y registra audiencias/términos/plazos para verlos en la línea de tiempo.</span>';document.getElementById('gantt').classList.add('on');return;}
 const ds=items.map(a=>new Date(a.fecha+'T00:00:00').getTime());let min=Math.min.apply(null,ds.concat(HOY.getTime())),max=Math.max.apply(null,ds.concat(HOY.getTime()));
 const span=Math.max(1,max-min),pos=t=>((t-min)/span*100);
 const color={Audiencia:'#0a4d8c',Término:'#c0392b',Plazo:'#e08e0b','Contestación':'#7e57c2',Seguimiento:'#1f9d6b'};
 const byNum={};items.forEach(a=>{(byNum[a.num]=byNum[a.num]||[]).push(a);});
 const rows=Object.keys(byNum).map(num=>{const marks=byNum[num].map(a=>`<span class="gmark" style="left:${pos(new Date(a.fecha+'T00:00:00').getTime())}%;background:${color[a.tipo]||'#888'}" title="${a.tipo} · ${a.fecha} ${a.nota||''}"></span>`).join('');
   return `<div class="grow"><div class="glabel">${num}</div><div class="gtrack"><span class="gmark" style="left:${pos(HOY.getTime())}%;background:#000;width:2px;border:none;border-radius:0;height:20px;top:1px" title="hoy"></span>${marks}</div></div>`;}).join('');
 W.innerHTML=rows+`<div class="gaxis"><span>${new Date(min).toISOString().slice(0,10)}</span><span style="text-align:right">${new Date(max).toISOString().slice(0,10)}</span></div>`;
 document.getElementById('gantt').classList.add('on');}
function fld(k,v){return `<div class="fld"><div class="k">${k}</div><div class="v">${v||'—'}</div></div>`;}
function od(id){const e=MAP[id];const en=enr(e.num);const en2=mtz(e.num);
 document.getElementById('mbody').innerHTML=`<h2 style="margin:0;color:#00254a">${e.num} <span class="pri p-${e.prioridad}">${e.prioridad}</span> <span class="sem s-${e.nivel_riesgo}"></span>${e.nivel_riesgo}·${e.score}</h2>`+
  `<div class="mh">Encabezado del expediente</div><div class="fhdr">`+
  fld('Materia (fina)',e.materia_fina)+fld('Vía',e.via)+fld('Tipo de juicio',e.tipo_juicio)+fld('Materia (base archivo)',e.materia)+fld('Dependencia',e.dependencia)+fld('Centro/Tipo',e.centro)+
  fld('Actor',e.actor)+fld('Demandado',e.demandado)+fld('Autoridad',e.autoridad)+fld('Responsable jurídico',e.responsable)+
  fld('Estado procesal',e.estado)+fld('Nivel de riesgo',e.nivel_riesgo+' ('+e.score+')')+fld('Probabilidad de éxito',e.prob_exito)+
  fld('Monto reclamado',e.monto?'$'+e.monto.toLocaleString('es-MX'):'—')+fld('Pasivo contingente',e.pasivo?'$'+e.pasivo.toLocaleString('es-MX'):'—')+
  fld('Fecha de inicio',e.fecha_inicio)+fld('Fecha de cierre',e.fecha_cierre)+fld('Último movimiento',e.ult_mov)+
  fld('Sistema/Régimen',e.sistema)+fld('Sentido resolución',e.sentido)+`</div>`+
  `<div class="fld" style="margin-bottom:6px"><div class="k">Observaciones</div><div class="v" style="font-weight:400">${e.observaciones||'—'}</div></div>`+
  `<div class="mh">Pruebas ofrecidas</div><textarea id="prb" rows="2" style="width:100%;padding:8px;border:1px solid #e2e8f0;border-radius:7px" placeholder="Describe las pruebas aportadas…">${(en.pruebas||'').replace(/"/g,'&quot;')}</textarea><div class="tools"><button onclick="savePrb('${e.id}')">Guardar pruebas</button></div>`+
  `<div class="mh">📝 Seguimiento (notas del equipo)</div>`+
  ((en.seguimiento&&en.seguimiento.length)?en.seguimiento.slice().reverse().map(s=>`<div style="font-size:11.5px;border-bottom:1px solid #eef2f7;padding:3px 0"><b style="color:#00254a">${s.usuario}</b> <span style="color:#94a3b8;font-size:10px">${s.ts}</span><br>${(s.texto||'').replace(/</g,'&lt;')}</div>`).join(''):'<span class="cap">Sin notas de seguimiento.</span>')+
  `<textarea id="segt" rows="2" style="width:100%;padding:8px;border:1px solid #e2e8f0;border-radius:7px;margin-top:5px" placeholder="Nota de seguimiento del expediente…"></textarea><div class="tools"><button onclick="addSegM('${e.id}')">Agregar nota</button></div>`+
  `<div class="mh">Documentos digitalizados (${en.docs.length})</div>`+
  `<div class="tools"><select id="dcat">`+DOCCATS.map(c=>`<option>${c}</option>`).join('')+`</select><input type="file" id="dfile" multiple accept="application/pdf,image/*"><button onclick="attachDoc('${e.id}')">📎 Adjuntar</button></div>`+
  (en.docs.length?en.docs.map((dd,i)=>`<div class="doc"><span>📄 <span class="tb">${dd.cat}</span> ${dd.name} <span style="color:#94a3b8">(${Math.round(dd.size/1024)} KB)</span></span><span><span class="lk" onclick="viewDoc('${e.id}',${i})">👁 ver</span> &nbsp;<span class="del" onclick="delDoc('${e.id}',${i})">✕</span></span></div>`).join(''):'<span class="cap">Aún sin documentos. Adjunta el expediente digitalizado (PDF/imagen).</span>')+
  `<div class="mh">Agenda y alertas del expediente</div>`+
  `<div class="tools"><select id="atipo"><option>Audiencia</option><option>Término</option><option>Plazo</option><option>Contestación</option><option>Seguimiento</option></select><input type="date" id="afecha"><input id="anota" placeholder="nota (opcional)" style="min-width:160px"><button onclick="addAg('${e.id}')">+ Agendar</button></div>`+
  (en.agenda.length?en.agenda.slice().sort((a,b)=>a.fecha.localeCompare(b.fecha)).map(a=>{const dd=diasRest(a.fecha);return `<div class="ag ${claseDia(dd)}"><span><span class="tb">${a.tipo}</span> ${a.fecha} ${a.nota?'· '+a.nota:''}</span><span><b>${dd<0?'venció hace '+(-dd):'en '+dd} d</b> <span class="del" onclick="delAg('${e.id}','${a.fecha}','${a.tipo}')">✕</span></span></div>`;}).join(''):'<span class="cap">Sin audiencias/términos capturados.</span>')+
  `<div class="mh">Extraído del expediente por NLP <span style="font-size:11px;font-weight:400;color:#8a6d1a">(orientativo — verificar)</span></div><div class="fhdr">`+
  fld('Resolución detectada',e.nlp_tipo_res)+fld('Fecha de resolución',e.nlp_fecha_res)+fld('Actuaciones (eventos)',e.nlp_eventos)+fld('Monto en texto',e.nlp_monto_texto?'$'+e.nlp_monto_texto.toLocaleString('es-MX'):'—')+fld('Prob. éxito (modelo ~61%)',e.pred_exito!=null?Math.round(e.pred_exito*100)+'%':'—')+`</div>`+
  (e.nlp_monto_anomalo?`<span class="cap">⚠ Monto anómalo detectado ($${e.nlp_monto_anomalo.toLocaleString('es-MX')}) — excluido por sanidad, REQUIERE verificación</span>`:'')+
  `<div class="mh">Cadena de responsables (trazabilidad)</div><datalist id="l_nom">`+LAWNAMES.map(n=>`<option>${n}</option>`).join('')+`</datalist>`+
  (en2.resp.length?en2.resp.slice().sort((a,b)=>(a.desde||'').localeCompare(b.desde||'')).map(x=>`<div class="doc"><span>👤 ${x.nombre} <span class="tb">${x.rol||'Responsable'}</span> · ${x.desde||'?'} → ${x.hasta||'actual'} ${x.nota?'· '+x.nota:''}</span><span class="del" onclick="mtzDel('${e.id}','resp',${en2.resp.indexOf(x)})">✕</span></div>`).join(''):'<span class="cap">Sin historial de responsables. Registra quién lo ha llevado.</span>')+
  `<div class="tools"><input id="mrz_nom" list="l_nom" placeholder="Abogado" style="min-width:150px"><select id="mrz_rol"><option>Responsable</option><option>Co-responsable</option><option>Anterior</option></select><input id="mrz_d" type="date" title="desde"><input id="mrz_h" type="date" title="hasta"><button onclick="mtzAddResp('${e.id}')">+ Responsable</button></div>`+
  (en2.inst.length?en2.inst.slice().sort((a,b)=>(a.desde||'').localeCompare(b.desde||'')).map(x=>`<div class="doc"><span>🏛️ <span class="tb">${x.rol}</span> ${x.nombre} · ${x.desde||'?'} → ${x.hasta||'actual'}</span><span class="del" onclick="mtzDel('${e.id}','inst',${en2.inst.indexOf(x)})">✕</span></div>`).join(''):'<span class="cap">Sin cadena institucional (Abogado General / Coordinador / Jefe de Unidad).</span>')+
  `<div class="tools"><select id="miz_rol"><option>Abogado General</option><option>Coordinador Jurídico</option><option>Jefe de Unidad</option></select><input id="miz_nom" placeholder="Nombre" style="min-width:150px"><input id="miz_d" type="date" title="desde"><input id="miz_h" type="date" title="hasta"><button onclick="mtzAddInst('${e.id}')">+ Institucional</button></div>`+
  `<div class="mh">Historial de actuaciones</div><div class="act">${e.actuaciones||'Sin actuaciones capturadas.'}</div>`;
 document.getElementById('modal').classList.add('on');}
function cf(){document.getElementById('modal').classList.remove('on');}
document.getElementById('modal').onclick=ev=>{if(ev.target.id=='modal')cf();};
function reset_(){['q','f_materia_fina','f_via','f_estado','f_nivel_riesgo','f_anio','f_responsable','f_centro','f_dependencia'].forEach(i=>document.getElementById(i).value='');render();}
function expFiltered(){const L=filtered();if(!L.length){alert('No hay resultados que exportar.');return;}
 const cols=['num','materia_fina','via','tipo_juicio','estado','nivel_riesgo','score','prioridad','dependencia','centro','responsable','autoridad','monto','anio','sentido','nlp_tipo_res','nlp_fecha_res','nlp_eventos','pred_exito'];
 const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const csv=cols.join(',')+'\n'+L.map(r=>cols.map(c=>esc(r[c])).join(',')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='expedientes_filtrados.csv';a.click();}
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
TPL=TPL.replace("__DATA__",DATA)
open("/Users/edithroque/Documents/CLAUDE/modulo_expedientes_SIGEJ.html","w",encoding="utf-8").write(TPL)
print("modulo_expedientes_SIGEJ.html OK -","%.0f KB"%(len(TPL)/1024))
