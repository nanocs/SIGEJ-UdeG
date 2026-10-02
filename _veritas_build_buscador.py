# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/comando_data.json",encoding="utf-8"))
DATA=json.dumps({"exp":d["exp"]},ensure_ascii=False)
NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html" class="act">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Buscador Global</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--ok:#1f9d6b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#f4f6f9;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:14px 24px}
header h1{margin:0;font-size:18px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:18px 24px;max-width:1050px;margin:auto}
.sb{display:flex;gap:8px;margin-bottom:8px}.sb input{flex:1;padding:13px 16px;border:1px solid var(--line);border-radius:12px;font-size:15px}
.sb button{padding:13px 20px;border:none;border-radius:12px;background:var(--teal);color:#fff;font-weight:600;cursor:pointer}
.fl{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;align-items:center}.fl select,.fl input{padding:7px 9px;border:1px solid var(--line);border-radius:7px;font-size:12px}
.fl button{padding:7px 11px;border:none;border-radius:7px;background:#64748b;color:#fff;font-size:12px;font-weight:600;cursor:pointer}
.warn{background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:8px 11px;font-size:11px;color:#8a6d1a;margin-bottom:14px}
.gr{margin-bottom:18px}.gr h3{font-size:13px;color:var(--azul);border-bottom:2px solid var(--line);padding-bottom:5px;margin:0 0 8px}
.rs{background:#fff;border-radius:10px;padding:11px 14px;margin-bottom:7px;box-shadow:0 1px 3px rgba(0,0,0,.06);border-left:4px solid var(--teal)}
.rs .t{font-size:13.5px;font-weight:600;color:var(--azul)}.rs .m{font-size:11.5px;color:var(--mut);margin-top:2px}
.rs a{color:var(--azul2);text-decoration:none;font-size:11.5px}
.chip{font-size:10px;padding:1px 7px;border-radius:9px;background:#eef2f7;color:#475569;margin-left:5px}
.empty{color:var(--mut);text-align:center;padding:30px}
footer{padding:14px 24px;color:var(--mut);font-size:11px;text-align:center}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}.qc{background:#e6f0fb;color:var(--azul2);border:1px solid #cfe0f5;border-radius:14px;padding:4px 11px;font-size:11.5px;cursor:pointer}
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
<header><h1>🔍 SIGEJ-UdeG · Buscador Global</h1><div class="s">Busca en expedientes, convenios, responsabilidades y documentos — lenguaje natural, palabras clave, fechas, materias</div></header>
__NAV__
<div class="wrap">
 <div class="sb"><input id="q" placeholder="Busca en TODO el sistema: expediente, oficio, persona, abogado, chofer, contraparte, dependencia, juzgado, convenio, palabra clave…" onkeydown="if(event.key=='Enter')run()"><button onclick="run()">🔍 Buscar</button></div>
 <div class="fl">
  <select id="fmod"><option value="">Todos los módulos</option></select>
  <select id="fanio"><option value="">Todo año</option></select>
  <select id="fest"><option value="">Todo estado</option></select>
  <select id="fresp"><option value="">Todo responsable / abogado</option></select>
  <select id="fniv"><option value="">Todo riesgo</option><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
  <input id="fdep" placeholder="Dependencia / persona / texto…" style="min-width:170px">
  <button onclick="run()">Aplicar filtros</button>
  <button onclick="limpiar()">Limpiar</button>
 </div>
 <div class="fl" style="margin-top:-8px">
  <input id="favn" placeholder="Nombre para guardar esta búsqueda" style="min-width:200px">
  <button onclick="guardarFav()">⭐ Guardar consulta</button>
  <button onclick="expCSV()">⬇ CSV</button>
  <button onclick="expWord()">📄 Word</button>
  <span id="cnt" style="font-size:12px;color:#64748b"></span>
 </div>
 <div class="chips" id="favs"></div>
 <div class="chips" id="chips"></div>
 <div class="warn">🔎 Búsqueda por <b>palabras clave + filtros estructurados simultáneos</b> sobre <b>TODOS los módulos</b> (tokeniza y rankea por relevancia). La <b>búsqueda semántica / lenguaje natural tipo ChatGPT</b>, los <b>embeddings</b>, la <b>detección de duplicados/patrones</b> y el <b>OCR de imágenes</b> = fase backend. Entiende consultas como "amparo laboral CUCEA 2024", "convenio recursos federales", "asuntos del abogado…". Cada búsqueda se registra en la bitácora (Transparencia General).</div>
 <div id="res"><div class="empty">Escribe tu consulta, usa los filtros o un atajo de arriba.</div></div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;
const norm=s=>(s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
const el=id=>document.getElementById(id);
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
let ALL=[],RES=[];
function loadAll(){const A=[];
 function push(mod,ic,arr,m){(arr||[]).forEach(function(e){try{var r=m(e);if(r){r.mod=mod;r.ic=ic;r.txt=(r.txt||'').toLowerCase();A.push(r);}}catch(x){}});}
 push('Litigio / Contencioso','⚖️',D.exp,e=>({folio:e.num,tit:(e.mat||'')+(e.via?' · '+e.via:''),est:e.est,resp:e.resp,anio:e.an?String(e.an):'',niv:e.niv,link:'modulo_expedientes_SIGEJ.html',txt:[e.num,e.mat,e.dep,e.resp,e.est,e.centro].join(' ')}));
 push('Instrumentos','📜',J('sigej_instrumentos'),e=>({folio:e.folio,tit:e.tipo+(e.obj?' · '+e.obj:''),est:e.estado,resp:e.resp,anio:(e.firma||e.ini||'').slice(0,4),niv:e.nivel,link:'instrumentos_SIGEJ.html',txt:[e.folio,e.tipo,e.obj,e.dep,e.contra,e.resp].join(' ')}));
 push('Patrimonio intangible','🧩',J('sigej_patrimonio'),e=>({folio:e.folio,tit:e.titulo||e.tipo,est:e.estado,resp:e.resp,anio:(e.sol||'').slice(0,4),niv:e.nivel,link:'patrimonio_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.cu,e.autor].join(' ')}));
 push('Asuntos internacionales','🌎',J('sigej_internacional'),e=>({folio:e.folio,tit:e.titulo,est:e.estado,resp:e.resp||'',anio:(e.ini||'').slice(0,4),niv:e.nivel,link:'internacional_SIGEJ.html',txt:[e.folio,e.titulo,e.pais,e.cu,e.dep,e.resp].join(' ')}));
 push('Normatividad','📖',J('sigej_normatividad'),e=>({folio:e.folio,tit:e.tipo+(e.norma?' · '+e.norma:''),est:e.estado,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:e.nivel,link:'normatividad_SIGEJ.html',txt:[e.folio,e.tipo,e.norma,e.objeto,e.materia,e.resp].join(' ')}));
 push('MASC','🤝',J('sigej_masc'),e=>({folio:e.exp||e.num||e.id||'MASC',tit:(e.tipo||'Convenio')+(e.actor?' · '+e.actor:''),est:e.cumplimiento||e.estado,resp:e.responsable,anio:(e.fecha||'').slice(0,4),niv:'',link:'masc_SIGEJ.html',txt:[e.exp,e.tipo,e.actor,e.demandado,e.responsable].join(' ')}));
 push('Responsabilidades (LGRA)','⚖️',J('sigej_resp'),e=>({folio:e.folio||e.id,tit:e.clasif||e.falta||'Procedimiento',est:e.estado,resp:e.responsable,anio:(e.finicio||'').slice(0,4),niv:'',link:'resp_SIGEJ.html',txt:[e.folio,e.clasif,e.autoridad,e.estado].join(' ')}));
 push('Asesoría / consultas','💡',J('sigej_asesoria'),e=>({folio:e.folio||e.id,tit:e.asunto||e.tipo||'Consulta',est:e.estado,resp:e.responsable||e.abogado,anio:(e.fecha||'').slice(0,4),niv:'',link:'asesoria_SIGEJ.html',txt:[e.folio,e.asunto,e.tipo,e.dependencia].join(' ')}));
 push('Proyectos','📌',J('sigej_proyectos'),e=>({folio:e.id,tit:e.nombre,est:e.estado,resp:e.resp,anio:(e.ini||'').slice(0,4),niv:'',link:'proyectos_SIGEJ.html',txt:[e.nombre,e.tipo,e.dep,e.resp].join(' ')}));
 push('Solicitudes UTI','🔎',J('sigej_uti'),e=>({folio:e.folio,tit:(e.texto||'Solicitud').slice(0,50),est:e.estado||'Registrada',resp:e.responsable,anio:(e.fecha||e.fsol||'').slice(0,4),niv:'',link:'transparencia_SIGEJ.html',txt:[e.folio,e.texto,e.materia,e.respuesta].join(' ')}));
 push('Oficios (Control)','📋',J('sigej_oficios'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.asunto?' · '+e.asunto:''),est:e.estatus,resp:e.resp,anio:e.anio||(e.fecha||'').slice(0,4),niv:'',link:'oficialia_SIGEJ.html',txt:[e.folio,e.tipo,e.asunto,e.demi,e.ddest,e.dest,(e.kw||[]).join(' '),(e.exp||[]).join(' '),e.estatus].join(' ')}));
 push('Help Desk (tickets)','🛠️',J('sigej_helpdesk'),e=>({folio:e.id,tit:(e.tipo||'')+(e.asunto?' · '+e.asunto:''),est:e.estado,resp:e.tec,anio:(e.creado||'').slice(0,4),niv:e.prio,link:'helpdesk_SIGEJ.html',txt:[e.id,e.tipo,e.cat,e.asunto,e.sol,e.dep,e.tec,e.estado].join(' ')}));
 push('Administración · Contable','💵',J('sigej_adm_contable'),e=>({folio:e.id,tit:(e.tipo||'')+(e.concepto?' · '+e.concepto:''),est:e.estado,resp:e.por,anio:(e.fecha||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.tipo,e.concepto,e.benef,e.part,e.exp,e.estado].join(' ')}));
 push('Administración · Bienes','🏷️',J('sigej_adm_bienes'),e=>({folio:e.id,tit:e.desc,est:e.estado,resp:e.resg,anio:(e.adq||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.desc,e.marca,e.modelo,e.etiq,e.serie,e.resg,e.estado].join(' ')}));
 push('Administración · Personal','👥',J('sigej_adm_personal'),e=>({folio:e.id,tit:(e.tipo||'')+(e.nombre?' · '+e.nombre:''),est:e.estado,resp:e.nombre,anio:(e.fecha||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.tipo,e.nombre,e.puesto,e.contr,e.area,e.estado].join(' ')}));
 push('Viáticos / Comisiones','🧳',J('sigej_adm_viaticos'),e=>({folio:e.folio,tit:(e.comis||'')+(e.obj?' · '+e.obj:''),est:e.estado,resp:e.abog||e.comis,anio:(e.fecha||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.folio,e.comis,e.obj,e.dest,e.drec,e.exp,e.abog,e.estado].join(' ')}));
 push('Logística · Comisiones','🚐',J('sigej_log_comisiones'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.destino?' · '+e.destino:''),est:e.estado,resp:e.chofer||e.abog,anio:(e.fecha||'').slice(0,4),niv:e.prio,link:'oficialia_SIGEJ.html',txt:[e.folio,e.tipo,e.destino,e.sol,e.abog,e.chofer,e.vehiculo,e.exp,e.area,e.estado].join(' ')}));
 push('Actuaciones externas','🚶',J('sigej_actuaciones'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.sub?' · '+e.sub:''),est:e.estado,resp:e.abog,anio:(e.fecha||'').slice(0,4),niv:'',link:'contencioso_SIGEJ.html',txt:[e.folio,e.tipo,e.sub,e.exp,e.org,e.juz,e.of,e.obj,e.abog,e.mat,e.estado].join(' ')}));
 push('Conocimiento · Biblioteca','📚',J('sigej_biblioteca'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.autor?' · '+e.autor:''),est:e.estado,resp:e.autor,anio:e.anio||'',niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.subtitulo,e.autor,e.materia,e.isbn,e.kw,e.tipo].join(' ')}));
 push('Conocimiento · Préstamos','🔄',J('sigej_prestamos'),e=>({folio:e.folio,tit:(e.libro||'')+(e.usuario?' · '+e.usuario:''),est:e.estado,resp:e.usuario,anio:(e.fpres||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.libro,e.usuario,e.area,e.estado].join(' ')}));
 push('Gestión del Conocimiento','🧠',J('sigej_conocimiento'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:'',resp:e.autor,anio:e.anio||'',niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.autor,e.materia,e.kw,e.resumen].join(' ')}));
 push('Capacitación','🎓',J('sigej_capacitacion'),e=>({folio:e.folio,tit:(e.tema||'')+(e.clase?' · '+e.clase:''),est:e.estado,resp:e.instructor,anio:(e.fsol||e.fprog||'').slice(0,4),niv:e.prioridad,link:'desarrollo_SIGEJ.html',txt:[e.folio,e.tema,e.clase,e.tipo,e.dep,e.instructor,e.estado].join(' ')}));
 push('Investigación jurídica','🔬',J('sigej_invest'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.autor,anio:(e.fecha||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.autor,e.materia,e.pub,e.orcid].join(' ')}));
 push('Difusión cultura jurídica','📣',J('sigej_difusion'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.resp,anio:(e.fpub||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.canal,e.resp].join(' ')}));
 push('Observatorio jurídico','🛰️',J('sigej_observatorio'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.fuente?' · '+e.fuente:''),est:e.prioridad,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:e.prioridad,link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.fuente,e.materia,e.accion].join(' ')}));
 push('Innovación jurídica','💡',J('sigej_innovacion'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.resp,e.impacto].join(' ')}));
 push('Gestión editorial','📖',J('sigej_editorial'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.autor,anio:(e.fecha||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.autor,e.isbn,e.doi].join(' ')}));
 push('Servicio social · Convenios','🤝',J('sigej_serviciosocial'),e=>({folio:e.folio,tit:(e.dependencia||'')+(e.objeto?' · '+e.objeto:''),est:e.estado,resp:e.resp,anio:(e.fin||'').slice(0,4),niv:'',link:'serviciosocial_SIGEJ.html',txt:[e.folio,e.dependencia,e.sector,e.objeto,e.cu,e.tipo,e.seguro].join(' ')}));
 push('Derechos Humanos (recomendaciones)','🕊️',J('sigej_derechoshumanos'),e=>({folio:e.folio,tit:(e.tipo||'')+' · '+(e.organismo||'').split(' — ')[0]+(e.derecho?' · '+e.derecho:''),est:e.estado,resp:e.resp,anio:(e.fRecep||'').slice(0,4),niv:'',link:'contencioso_SIGEJ.html',txt:[e.folio,e.organismo,e.tipo,e.numero,e.derecho,e.area,e.hechos].join(' ')}));
 push('Investigación (gobierno)','🔬',J('sigej_inv_investigadores'),e=>({folio:e.folio,tit:(e.nombre||'')+(e.snii&&e.snii!=='No'?' · '+e.snii:''),est:e.prodep,resp:e.nombre,anio:(e.fAlta||'').slice(0,4),niv:'',link:'gobinv_SIGEJ.html',txt:[e.folio,e.nombre,e.cu,e.area,e.snii,e.ca,e.lgac].join(' ')}));
 push('Laboratorios','🧪',J('sigej_lab'),e=>({folio:e.folio,tit:(e.nombre||'')+(e.bsl?' · '+e.bsl:''),est:e.estado,resp:e.respTecnico,anio:(e.fVenc||'').slice(0,4),niv:'',link:'laboratorios_SIGEJ.html',txt:[e.folio,e.nombre,e.cu,e.tipo,e.bsl,e.respTecnico,e.licencia].join(' ')}));
 push('Programas académicos','🎓',J('sigej_programas'),e=>({folio:e.folio,tit:(e.nombre||'')+(e.tramite?' · '+e.tramite:''),est:e.estado,resp:'',anio:(e.fApertura||'').slice(0,4),niv:'',link:'programas_SIGEJ.html',txt:[e.folio,e.nombre,e.nivel,e.cu,e.tramite,e.rpe].join(' ')}));
 push('Hospitales / Salud','🏥',J('sigej_hosp_est'),e=>({folio:e.folio,tit:(e.nombre||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.respSanitario,anio:(e.fVenc||'').slice(0,4),niv:'',link:'hospitales_SIGEJ.html',txt:[e.folio,e.nombre,e.cu,e.tipo,e.respSanitario,e.licNum].join(' ')}));
 push('Derecho Deportivo','🏅',J('sigej_deportivo'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.entidad?' · '+e.entidad:''),est:e.estado,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:'',link:'deportivo_SIGEJ.html',txt:[e.folio,e.tipo,e.ambito,e.entidad,e.organismo,e.derecho,e.hechos,e.resp].join(' ')}));
 ALL=A;return A;}
function fillFilters(){
 const mods=[...new Set(ALL.map(r=>r.mod))].sort();el('fmod').innerHTML='<option value="">Todos los módulos</option>'+mods.map(m=>'<option>'+m+'</option>').join('');
 const ys=[...new Set(ALL.map(r=>r.anio).filter(Boolean))].sort().reverse();el('fanio').innerHTML='<option value="">Todo año</option>'+ys.map(y=>'<option>'+y+'</option>').join('');
 const es=[...new Set(ALL.map(r=>r.est).filter(Boolean))].sort();el('fest').innerHTML='<option value="">Todo estado</option>'+es.map(x=>'<option>'+x+'</option>').join('');
 const rs=[...new Set(ALL.map(r=>r.resp).filter(Boolean))].sort();el('fresp').innerHTML='<option value="">Todo responsable / abogado</option>'+rs.map(x=>'<option>'+x+'</option>').join('');}
function score(text,toks){text=norm(text);let s=0;toks.forEach(t=>{if(text.indexOf(t)>=0)s++;});return s;}
function run(){const raw=el('q').value.trim();const toks=norm(raw).split(/\s+/).filter(t=>t.length>1);
 const fmod=el('fmod').value,fanio=el('fanio').value,fest=el('fest').value,fresp=el('fresp').value,fniv=el('fniv').value,fdep=norm(el('fdep').value);
 let r=ALL.map(o=>({o:o,s:toks.length?score(o.txt+' '+(o.folio||'')+' '+(o.tit||'')+' '+(o.resp||''),toks):1}))
  .filter(x=>{const o=x.o;if(toks.length&&x.s===0)return false;if(fmod&&o.mod!==fmod)return false;if(fanio&&o.anio!==fanio)return false;if(fest&&o.est!==fest)return false;if(fresp&&o.resp!==fresp)return false;if(fniv&&o.niv!==fniv)return false;if(fdep&&(o.txt+' '+(o.tit||'')+' '+(o.resp||'')).indexOf(fdep)<0)return false;return true;})
  .sort((a,b)=>b.s-a.s);
 RES=r.map(x=>x.o);el('cnt').textContent=RES.length+' resultado(s)';
 if(window.__bitlog)__bitlog('Búsqueda',(raw||'(filtros)')+' → '+RES.length+' result.');
 if(!RES.length){el('res').innerHTML='<div class="empty">Sin resultados'+(raw?' para "'+raw+'"':'')+'. Ajusta el texto o los filtros.</div>';return;}
 const byMod={};RES.forEach(o=>{(byMod[o.mod]=byMod[o.mod]||[]).push(o);});
 const mods=Object.keys(byMod).sort((a,b)=>byMod[b].length-byMod[a].length);
 let html='';
 mods.forEach(m=>{const arr=byMod[m];html+='<div class="gr"><h3>'+(arr[0].ic||'')+' '+m+' ('+arr.length+')</h3>'+arr.slice(0,25).map(o=>'<div class="rs"><div class="t">'+(o.folio||'(s/folio)')+(o.est?' <span class="chip">'+o.est+'</span>':'')+(o.niv?' <span class="chip">'+o.niv+'</span>':'')+(o.anio?' <span class="chip">'+o.anio+'</span>':'')+'</div><div class="m">'+(o.tit||'')+(o.resp?' · '+o.resp:'')+' <a href="'+o.link+'">abrir módulo →</a></div></div>').join('')+(arr.length>25?'<div class="m" style="text-align:center;color:#64748b">… 25 de '+arr.length+'</div>':'')+'</div>';});
 el('res').innerHTML=html;}
function limpiar(){['q','fdep','favn'].forEach(i=>el(i).value='');['fmod','fanio','fest','fresp','fniv'].forEach(i=>el(i).value='');el('cnt').textContent='';el('res').innerHTML='<div class="empty">Escribe tu consulta, usa los filtros o un atajo de arriba.</div>';}
function getFav(){return J('sigej_buscador_fav');}
function renderFav(){const f=getFav();el('favs').innerHTML=f.length?'<span style="font-size:11px;color:#64748b;align-self:center">⭐ Guardadas:</span> '+f.map((x,i)=>'<span class="qc" onclick="aplicarFav('+i+')">'+x.n+'</span><span class="qc" style="background:#fdeaea;color:#c0392b;margin-left:-3px" onclick="delFav('+i+')" title="eliminar">✕</span>').join(' '):'';}
function guardarFav(){const n=((el('favn').value||el('q').value)||'consulta').trim();const f=getFav();f.push({n:n,q:el('q').value,fmod:el('fmod').value,fanio:el('fanio').value,fest:el('fest').value,fresp:el('fresp').value,fniv:el('fniv').value,fdep:el('fdep').value});localStorage.setItem('sigej_buscador_fav',JSON.stringify(f));el('favn').value='';renderFav();if(window.__bitlog)__bitlog('Acción','Guardar consulta: '+n);}
function aplicarFav(i){const x=getFav()[i];if(!x)return;el('q').value=x.q||'';el('fmod').value=x.fmod||'';el('fanio').value=x.fanio||'';el('fest').value=x.fest||'';el('fresp').value=x.fresp||'';el('fniv').value=x.fniv||'';el('fdep').value=x.fdep||'';run();}
function delFav(i){const f=getFav();f.splice(i,1);localStorage.setItem('sigej_buscador_fav',JSON.stringify(f));renderFav();}
function expCSV(){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';const cab=['modulo','folio','titulo','estado','responsable','anio','riesgo'];const rows=RES.map(o=>[o.mod,o.folio,o.tit,o.est,o.resp,o.anio,o.niv].map(esc).join(','));const b=new Blob(['﻿'+cab.join(',')+'\n'+rows.join('\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='busqueda_global.csv';a.click();if(window.__bitlog)__bitlog('Acción','Exportar CSV búsqueda ('+RES.length+')');}
function expWord(){var body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Buscador Global</div><h2>Resultados de búsqueda ('+RES.length+')</h2><table border="1" cellspacing="0" cellpadding="4" style="border-collapse:collapse;font-size:10pt;width:100%"><tr><th>Módulo</th><th>Folio</th><th>Título</th><th>Estado</th><th>Responsable</th><th>Año</th></tr>'+RES.slice(0,600).map(o=>'<tr><td>'+(o.mod||'')+'</td><td>'+(o.folio||'')+'</td><td>'+(o.tit||'')+'</td><td>'+(o.est||'')+'</td><td>'+(o.resp||'')+'</td><td>'+(o.anio||'')+'</td></tr>').join('')+'</table>';const h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:50px">'+body+'</body></html>';const b=new Blob(['﻿'+h],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='busqueda_global.doc';a.click();}
const QC=['amparo laboral','alto riesgo','CUCEA','helpdesk','viáticos','emplazamiento','convenio federal','marca'];
el('chips').innerHTML=QC.map(c=>'<span class="qc" onclick="el(\'q\').value=\''+c+'\';run()">'+c+'</span>').join('');
loadAll();fillFilters();renderFav();
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
})();</script><script>
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
</script>
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
open("/Users/edithroque/Documents/CLAUDE/buscador_SIGEJ.html","w",encoding="utf-8").write(TPL.replace("__DATA__",DATA).replace("__NAV__",NAV))
print("buscador_SIGEJ.html OK")
