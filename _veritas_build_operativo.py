# -*- coding: utf-8 -*-
# MÓDULO OPERATIVO — copia gemela operativa (con trazabilidad) de los submódulos de autoservicio más usados
# internamente en la Oficina de la Abogacía General: Autoservicio, Requisición de papelería, Captura de oficios,
# Libro electrónico, Solicitud de viáticos y comisiones, Comisión y traslado, y Biblioteca y préstamos.
# Alcance por adscripción: cada persona ve SOLO lo de su coordinación/unidad en los 5 submódulos operativos
# (papelería, oficios, libro, viáticos, comisión y traslado). Autoservicio y Biblioteca son de alcance compartido.
# Perfiles de mando (Admin, Abogado General, Coordinaciones, Sistemas, Help Desk) pueden ver toda la Oficina.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Módulo Operativo'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','operativo_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="operativo_SIGEJ.html" class="act">🧰 Módulo Operativo</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Módulo Operativo</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#0b2540,#1a6d64);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#08221c;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2ded6;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.adscbar{background:#fff;border-bottom:1px solid var(--line);padding:9px 18px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;font-size:12.5px}
.adscbar .pill{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:16px;padding:4px 12px;font-weight:700}
.adscbar select{font-family:inherit;font-size:12.5px;padding:6px 8px;border:1px solid var(--line);border-radius:8px;min-width:210px}
.tabbar{display:flex;gap:5px;flex-wrap:wrap;padding:12px 18px 0;max-width:1320px;margin:auto}
.tb{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px;color:#334155}
.tb.on{background:#1a6d64;color:#fff;font-weight:700}
.wrap{max-width:1320px;margin:auto;padding:14px 18px 40px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:12px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px}
.kpi .n{font-size:22px;font-weight:800;color:var(--teal)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.grid{display:grid;gap:8px}
label.lb{font-size:11px;color:#64748b;display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
textarea{min-height:48px;resize:vertical}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:8px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bg{background:var(--ok);color:#fff;font-weight:700}.bo{background:var(--amber);color:#fff;font-weight:700}.mini{padding:5px 9px;font-size:11.5px}
.rec{border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:8px;background:#fff}
.rec .rh{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between}
.rec .rt{font-weight:700;color:#0a2f4f}
.rec .meta{font-size:11px;color:#94a3b8;margin-top:2px}
.rec .body{font-size:12.5px;color:#334155;margin-top:6px;line-height:1.6}
.rec .acts{margin-top:8px;display:flex;flex-wrap:wrap;gap:5px}
.bdg{padding:2px 9px;border-radius:11px;font-size:10px;font-weight:700;background:#eef2f7;color:#0a4d8c;white-space:nowrap}
.bdg.adsc{background:#f1f5f9;color:#475569}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.warn{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
@media print{.navbar,header,.adscbar,.tabbar,.card.alta,.card.filtros,.acts,.note,footer,.kpis{display:none!important}body{background:#fff}}
</style></head><body>
<header><h1>🧰 Módulo Operativo · Autoservicio interno</h1><div class="s">Oficina de la Abogacía General · trámites operativos frecuentes con trazabilidad y alcance por coordinación/unidad</div></header>
__NAV__
<div class="adscbar">
 <span>👤 <b id="ab_perfil"></b></span>
 <span>Mi adscripción: <select id="ab_adscr" onchange="setAdscr()"></select></span>
 <span id="ab_ambitoWrap" style="display:none">Ámbito: <select id="ab_ambito" onchange="setAmbito()"><option value="mia">Solo mi adscripción</option><option value="todo">Toda la Oficina</option></select></span>
 <span class="pill" id="ab_scope"></span>
</div>
<div class="tabbar" id="tabbar"></div>
<div class="wrap"><div id="pane"></div>
 <div class="note">🔒 En <b>Requisición de papelería, Captura de oficios, Libro electrónico, Viáticos y Comisión/Traslado</b> cada persona ve únicamente lo registrado en <b>su coordinación o unidad</b>. <b>Autoservicio</b> y <b>Biblioteca</b> son de alcance compartido. Cada movimiento deja constancia en la <b>bitácora de auditoría</b> (Transparencia). Los perfiles de mando y Help Desk pueden ver toda la Oficina.</div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function nowStr(){return new Date().toISOString().slice(0,16).replace('T',' ');}
function hoy(){return new Date().toISOString().slice(0,10);}
var PERFIL=localStorage.getItem('sigej_perfil')||'(perfil)';
var SUPER=['Administrador','Abogado General','Coordinador Jurídico','Coordinador de Enlace con la Red','Coordinador de Normatividad','Sistemas','Jefe del Área de Sistemas'];
function isSuper(){return SUPER.indexOf(PERFIL)>=0;}
/* Catálogo de adscripciones (coordinaciones + unidades/áreas de la Oficina de la Abogacía General) */
var ADSCR=['Abogacía General (Dirección)','Coordinación General Jurídica','Coordinación de Enlace con la Red','Coordinación de Normatividad',
 'Unidad de lo Contencioso','Unidad de Atención y Servicios Legales','Unidad de Patrimonio Intangible','Unidad de Asuntos Internacionales','Unidad de Instrumentos Jurídicos','Unidad de Capacitación, Investigación y Difusión','Unidad de Estatutos y Reglamentos','Unidad de Normatividad Administrativa','Unidad de Apoyo a Órganos Colegiados','Área Contable','Área de Personal','Área de Sistemas','Oficialía de Partes','Mensajería'];
/* Resuelve la adscripción del usuario: 1) sesión→IAM (unidad, si no coord); 2) override manual; 3) vacío */
function iamAdscr(){var ses=J('sigej_sesion');var code=ses&&ses.code;var U=J('sigej_usuarios');if(code&&Array.isArray(U)){for(var i=0;i<U.length;i++){if(String(U[i].numEmp||'').toLowerCase()===String(code).toLowerCase()){return U[i].unidad||U[i].coord||'';}}}return '';}
function myAdscr(){var ov=localStorage.getItem('sigej_op_adscr');if(ov)return ov;var ia=iamAdscr();return ia||'';}
function ambito(){if(!isSuper())return 'mia';return localStorage.getItem('sigej_op_ambito')||'todo';}
function setAdscr(){localStorage.setItem('sigej_op_adscr',el('ab_adscr').value);paintScope();render();}
function setAmbito(){localStorage.setItem('sigej_op_ambito',el('ab_ambito').value);paintScope();render();}
function paintScope(){el('ab_perfil').textContent=PERFIL;
 var sel=el('ab_adscr');if(!sel.dataset.done){sel.innerHTML='<option value="">— Selecciona —</option>'+ADSCR.map(function(a){return '<option>'+esc(a)+'</option>';}).join('');sel.dataset.done='1';}
 sel.value=myAdscr();
 if(isSuper()){el('ab_ambitoWrap').style.display='';el('ab_ambito').value=ambito();}
 var sc=isSuper()&&ambito()==='todo'?'🌐 Viendo TODA la Oficina':(myAdscr()?'🔒 Alcance: '+myAdscr():'⚠️ Define tu adscripción');
 el('ab_scope').textContent=sc;}
/* ===== Definición de submódulos (motor genérico) ===== */
var SUBS=[
 {id:'s1',icon:'🎫',title:'Autoservicio',key:'sigej_op_autoservicio',scoped:false,folio:'AS',
  estados:['Nuevo','En atención','Resuelto','Cerrado'],
  fields:[{k:'tipo',l:'Tipo',t:'select',o:['Incidencia','Solicitud de servicio']},{k:'cat',l:'Categoría',t:'select',o:['Equipo de cómputo','Sistema SIGEJ','Telefonía','Mobiliario','Accesos/usuario','Otro']},{k:'asunto',l:'Asunto',t:'text',req:1},{k:'prio',l:'Prioridad',t:'select',o:['Baja','Media','Alta']},{k:'desc',l:'Descripción',t:'ta'}]},
 {id:'s2',icon:'🖇️',title:'Requisición de papelería',key:'sigej_op_papeleria',scoped:true,folio:'REQ',
  estados:['Solicitada','Autorizada','Surtida','Rechazada'],
  fields:[{k:'articulo',l:'Artículo / insumo',t:'text',req:1},{k:'cant',l:'Cantidad',t:'num'},{k:'unidad',l:'Unidad',t:'select',o:['Pieza','Caja','Paquete','Resma','Kit']},{k:'fecha',l:'Fecha requerida',t:'date'},{k:'justif',l:'Justificación',t:'text'}]},
 {id:'s3',icon:'📝',title:'Captura de oficios',key:'sigej_op_oficios',scoped:true,folio:'OFI',oficialia:1,
  estados:['Borrador','Firmado','Enviado','Acuse recibido'],
  fields:[{k:'tipo',l:'Tipo',t:'select',o:['Interno','Externo']},{k:'dest',l:'Destinatario',t:'text',req:1},{k:'cargo',l:'Cargo / dependencia',t:'text'},{k:'asunto',l:'Asunto',t:'text',req:1},{k:'fecha',l:'Fecha',t:'date'},{k:'desc',l:'Contenido / síntesis',t:'ta'}]},
 {id:'s4',icon:'📖',title:'Libro electrónico',key:'sigej_op_libro',scoped:true,folio:'LIB',
  estados:['Registrado','Turnado','Archivado'],
  fields:[{k:'mov',l:'Movimiento',t:'select',o:['Entrada','Salida']},{k:'ref',l:'Folio / referencia',t:'text'},{k:'contra',l:'Remitente / destinatario',t:'text',req:1},{k:'asunto',l:'Asunto',t:'text',req:1},{k:'fecha',l:'Fecha',t:'date'},{k:'medio',l:'Medio',t:'select',o:['Físico','Electrónico']}]},
 {id:'s5',icon:'🧳',title:'Solicitud de viáticos y comisiones',key:'sigej_op_viaticos',scoped:true,folio:'VIA',
  estados:['Solicitada','Autorizada','Comprobada','Rechazada'],
  fields:[{k:'comisionado',l:'Comisionado(a)',t:'text',req:1},{k:'destino',l:'Destino',t:'text',req:1},{k:'ini',l:'Fecha inicio',t:'date'},{k:'fin',l:'Fecha fin',t:'date'},{k:'concepto',l:'Concepto / objeto',t:'text'},{k:'monto',l:'Monto estimado (MXN)',t:'num'}]},
 {id:'s6',icon:'🚗',title:'Comisión y traslado',key:'sigej_op_comision',scoped:true,folio:'COM',
  estados:['Programada','En curso','Concluida','Cancelada'],
  fields:[{k:'comisionado',l:'Comisionado(a)',t:'text',req:1},{k:'medio',l:'Medio de traslado',t:'select',o:['Vehículo oficial','Vehículo particular','Transporte público','Aéreo']},{k:'origen',l:'Origen',t:'text'},{k:'destino',l:'Destino',t:'text',req:1},{k:'fecha',l:'Fecha',t:'date'},{k:'motivo',l:'Motivo',t:'text'}]},
 {id:'s8',icon:'🧑‍⚖️',title:'Permisos, licencias e incidencias',key:'sigej_op_laboral',scoped:false,folio:'PL',estados:['—'],fields:[{k:'x',l:'—',t:'text'}]},
 {id:'s7',icon:'📚',title:'Biblioteca y préstamos',key:'sigej_op_biblioteca',scoped:false,folio:'BIB',
  estados:['Disponible','Prestado','Devuelto','Vencido'],
  fields:[{k:'material',l:'Material',t:'text',req:1},{k:'tipo',l:'Tipo',t:'select',o:['Libro','Revista','Expediente','Recurso digital']},{k:'solicitante',l:'Solicitante',t:'text'},{k:'prestamo',l:'Fecha préstamo',t:'date'},{k:'devol',l:'Fecha devolución',t:'date'}]}
];
var cur='s1';
function sub(id){for(var i=0;i<SUBS.length;i++)if(SUBS[i].id===(id||cur))return SUBS[i];return SUBS[0];}
function loadR(s){var a=J(s.key);return Array.isArray(a)?a:[];}
function saveR(s,a){localStorage.setItem(s.key,JSON.stringify(a));}
function blog(tipo,accion){try{var L=JSON.parse(localStorage.getItem('sigej_bitacora')||'[]');L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:PERFIL,modulo:'Módulo Operativo · '+sub().title,tipo:tipo,accion:String(accion||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);localStorage.setItem('sigej_bitacora',JSON.stringify(L));}catch(e){}if(window.__bitlog){try{window.__bitlog(tipo,accion);}catch(e){}}}
function canSee(s,r){if(!s.scoped)return true;if(isSuper()&&ambito()==='todo')return true;var a=myAdscr();if(!a)return true;return r.adscr===a;}
/* ===== render de un submódulo ===== */
function drawTabs(){el('tabbar').innerHTML=SUBS.map(function(s){return '<button class="tb'+(s.id===cur?' on':'')+'" onclick="go(\''+s.id+'\')">'+s.icon+' '+esc(s.title)+'</button>';}).join('');}
function go(id){cur=id;drawTabs();render();window.scrollTo(0,0);}
function fieldInput(f){var id='f_'+f.k;
 if(f.t==='select')return '<select id="'+id+'">'+f.o.map(function(x){return '<option>'+esc(x)+'</option>';}).join('')+'</select>';
 if(f.t==='ta')return '<textarea id="'+id+'" placeholder="'+esc(f.l)+'"></textarea>';
 var ty=f.t==='num'?'number':(f.t==='date'?'date':'text');
 return '<input id="'+id+'" type="'+ty+'" placeholder="'+esc(f.l)+'">';}
function render(){var s=sub();paintScope();
 if(s.id==='s8'){el('pane').innerHTML='<div class="note">🧑‍⚖️ <b>Permisos, Licencias, Incidencias y Descansos</b> (Compliance by Design · CCT). Como trabajador solo generas solicitudes; el Motor de Reglas valida antes de enviar. Las vacaciones no se solicitan (Calendario Vacacional Institucional).</div><iframe src="laboral_SIGEJ.html?embed=1" title="Permisos y Licencias" style="width:100%;height:80vh;border:1px solid var(--line);border-radius:12px;background:#fff"></iframe>';return;}
 if(s.id==='s7'){ /* Biblioteca: consulta y solicitud de préstamo (módulo dedicado embebido; alta/administración solo personal autorizado) */
  el('pane').innerHTML='<div class="note">📚 <b>Biblioteca Jurídica.</b> Como usuario general puedes <b>consultar el acervo</b> y <b>solicitar préstamos</b> (y ver si un ejemplar está prestado, a quién y de qué área). El alta de libros, la autorización de préstamos y las devoluciones son del personal autorizado de la Biblioteca.</div><iframe src="biblioteca_SIGEJ.html?embed=1" title="Biblioteca Jurídica" style="width:100%;height:80vh;border:1px solid var(--line);border-radius:12px;background:#fff"></iframe>';return;}
 var scopedNote=s.scoped?'<span class="bdg">🔒 alcance por adscripción</span>':'<span class="bdg" style="background:#e7f7ee;color:#128c4a">🌐 compartido</span>';
 var half=s.fields.length>4?'repeat(auto-fit,minmax(180px,1fr))':'repeat(auto-fit,minmax(200px,1fr))';
 var form='<div class="card alta"><input type="hidden" id="f_id"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><b style="color:#0a5c53">'+s.icon+' Nuevo registro · '+esc(s.title)+'</b>'+scopedNote+'</div>'+
  '<div class="grid" style="grid-template-columns:'+half+';margin-top:8px">'+s.fields.map(function(f){return '<div'+(f.t==='ta'?' style="grid-column:1/-1"':'')+'><label class="lb">'+esc(f.l)+(f.req?' *':'')+'</label>'+fieldInput(f)+'</div>';}).join('')+'</div>'+
  '<div style="margin-top:8px"><button class="bg" onclick="guardar()">💾 Guardar</button> <button class="bd" onclick="limpiar()">Limpiar</button> <span id="f_msg" style="font-size:12px;margin-left:8px"></span></div></div>';
 var filt='<div class="card filtros"><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">'+
  '<div><label class="lb">Buscar</label><input id="q" placeholder="texto…" oninput="render()"></div>'+
  '<div><label class="lb">Estado</label><select id="fe" onchange="render()"><option value="">Todos</option>'+s.estados.map(function(e){return '<option>'+esc(e)+'</option>';}).join('')+'</select></div>'+
  (s.scoped&&isSuper()&&ambito()==='todo'?'<div><label class="lb">Adscripción</label><select id="fa" onchange="render()"><option value="">Todas</option>'+ADSCR.map(function(a){return '<option>'+esc(a)+'</option>';}).join('')+'</select></div>':'')+
  '<div style="display:flex;align-items:end;gap:6px"><button class="b1 mini" onclick="expCSV()">⬇️ CSV</button><button class="bd mini" onclick="window.print()">🖨️</button></div>'+
  '</div></div>';
 el('pane').innerHTML='<div class="kpis" id="kpis"></div>'+form+filt+'<div id="list"></div>';
 // preserve prior filter values across re-render
 list();}
function visibleRows(){var s=sub();var all=loadR(s);var q=norm((el('q')||{}).value||''),fe=(el('fe')||{}).value||'',fa=(el('fa')||{}).value||'';
 var rows=all.filter(function(r){if(!canSee(s,r))return false;if(fe&&r.estado!==fe)return false;if(fa&&r.adscr!==fa)return false;
   if(q){var blob=norm(JSON.stringify(r.d||{})+' '+(r.folio||'')+' '+(r.adscr||'')+' '+(r.creadoPor||''));if(blob.indexOf(q)<0)return false;}return true;});
 rows.sort(function(a,b){return (b.ts||'').localeCompare(a.ts||'');});return rows;}
function list(){var s=sub();var rows=visibleRows();var all=loadR(s).filter(function(r){return canSee(s,r);});
 var byEst={};all.forEach(function(r){byEst[r.estado]=(byEst[r.estado]||0)+1;});
 var kp='<div class="kpi"><div class="n">'+rows.length+'</div><div class="l">En vista</div></div>'+
   '<div class="kpi"><div class="n">'+all.length+'</div><div class="l">'+(s.scoped?(isSuper()&&ambito()==='todo'?'Total (toda la Oficina)':'Total mi adscripción'):'Total compartido')+'</div></div>'+
   s.estados.slice(0,3).map(function(e){return '<div class="kpi"><div class="n">'+(byEst[e]||0)+'</div><div class="l">'+esc(e)+'</div></div>';}).join('');
 el('kpis').innerHTML=kp;
 el('list').innerHTML=rows.length?rows.map(function(r){return recHTML(s,r);}).join(''):'<div class="warn">Sin registros'+(s.scoped?' en tu adscripción':'')+'. Captura el primero arriba.</div>';}
function recHTML(s,r){var d=r.d||{};
 var body=s.fields.map(function(f){var v=d[f.k];if(v==null||v==='')return '';return '<b>'+esc(f.l)+':</b> '+esc(v);}).filter(Boolean).join(' &nbsp;·&nbsp; ');
 var seg=(r.seguimiento||[]).length?'<div style="margin-top:5px;font-size:11px;color:#475569">🧭 '+r.seguimiento.length+' nota(s) de seguimiento · última: '+esc((r.seguimiento[r.seguimiento.length-1]||{}).texto||'')+'</div>':'';
 var ofi=s.oficialia?(r.oficialiaFolio?'<span class="bdg" style="background:#e7f7ee;color:#128c4a">📨 En Oficialía: '+esc(r.oficialiaFolio)+'</span>':'<button class="bo mini" onclick="toOficialia(\''+r.id+'\')">📨 Registrar en Oficialía</button>'):'';
 return '<div class="rec"><div class="rh"><div><span class="rt">'+esc(r.folio)+'</span> <span class="bdg '+esc(r.estado)+'">'+esc(r.estado)+'</span> '+(s.scoped?'<span class="bdg adsc">'+esc(r.adscr||'—')+'</span>':'')+'<div class="meta">'+esc(r.ts)+' · por '+esc(r.creadoPor||'—')+'</div></div><div>'+ofi+'</div></div>'+
  '<div class="body">'+body+'</div>'+seg+
  '<div class="acts"><button class="bd mini" onclick="editar(\''+r.id+'\')">✏️ Editar</button><button class="bd mini" onclick="cambiarEstado(\''+r.id+'\')">🔁 Estado</button><button class="bd mini" onclick="segAdd(\''+r.id+'\')">🧭 Seguimiento</button><button class="bd mini" onclick="verTraza(\''+r.id+'\')">🧾 Trazabilidad</button><button class="bd mini" onclick="borrar(\''+r.id+'\')">🗑️</button></div></div>';}
/* ===== acciones ===== */
function nextFolio(s){var a=loadR(s);var y=new Date().getFullYear();return s.folio+'-'+y+'-'+String(a.length+1).padStart(4,'0');}
function guardar(){var s=sub();var d={};var falta='';
 s.fields.forEach(function(f){var v=(el('f_'+f.k)||{}).value;v=(v==null?'':String(v)).trim();if(f.req&&!v)falta=falta||f.l;d[f.k]=v;});
 if(falta){el('f_msg').style.color='#c0392b';el('f_msg').textContent='Falta: '+falta;return;}
 if(s.scoped&&!myAdscr()){el('f_msg').style.color='#c0392b';el('f_msg').textContent='Primero define tu adscripción (barra superior).';return;}
 var a=loadR(s);var id=el('f_id').value;
 if(id){for(var i=0;i<a.length;i++){if(a[i].id===id){a[i].d=d;(a[i].hist=a[i].hist||[]).push({ts:nowStr(),usuario:PERFIL,accion:'Edición'});break;}}blog('Acción','Edita '+s.title+' '+id);}
 else{var folio=nextFolio(s);var rec={id:'OP-'+Date.now().toString(36),folio:folio,d:d,estado:s.estados[0],adscr:s.scoped?myAdscr():(myAdscr()||'General'),creadoPor:PERFIL,ts:nowStr(),hist:[{ts:nowStr(),usuario:PERFIL,accion:'Alta ('+s.estados[0]+')'}],seguimiento:[]};a.push(rec);blog('Acción','Registra '+s.title+' '+folio);}
 saveR(s,a);el('f_msg').style.color='#128c4a';el('f_msg').textContent='✓ Guardado.';limpiar();list();}
function editar(id){var s=sub();var r=loadR(s).filter(function(x){return x.id===id;})[0];if(!r)return;el('f_id').value=id;s.fields.forEach(function(f){var e=el('f_'+f.k);if(e)e.value=(r.d||{})[f.k]||'';});window.scrollTo(0,0);}
function limpiar(){var s=sub();el('f_id').value='';s.fields.forEach(function(f){var e=el('f_'+f.k);if(e)e.value=(f.t==='select'?f.o[0]:'');});}
function cambiarEstado(id){var s=sub();var a=loadR(s);var r=null;a.forEach(function(x){if(x.id===id)r=x;});if(!r)return;
 var op=prompt('Nuevo estado ('+s.estados.join(' / ')+'):',r.estado);if(op===null)return;op=op.trim();if(s.estados.indexOf(op)<0){alert('Estado no válido.');return;}
 r.estado=op;(r.hist=r.hist||[]).push({ts:nowStr(),usuario:PERFIL,accion:'Estado → '+op});saveR(s,a);blog('Acción',s.title+' '+r.folio+' → '+op);list();}
function segAdd(id){var s=sub();var a=loadR(s);var r=null;a.forEach(function(x){if(x.id===id)r=x;});if(!r)return;
 var t=prompt('Nota de seguimiento:','');if(t===null||!t.trim())return;(r.seguimiento=r.seguimiento||[]).push({ts:nowStr(),usuario:PERFIL,texto:t.trim()});(r.hist=r.hist||[]).push({ts:nowStr(),usuario:PERFIL,accion:'Nota de seguimiento'});saveR(s,a);blog('Seguimiento',s.title+' '+r.folio);list();}
function verTraza(id){var s=sub();var r=loadR(s).filter(function(x){return x.id===id;})[0];if(!r)return;
 var h=(r.hist||[]).map(function(x){return '• '+x.ts+' — '+x.usuario+': '+x.accion;}).join('\n');
 var sg=(r.seguimiento||[]).map(function(x){return '• '+x.ts+' — '+x.usuario+': '+x.texto;}).join('\n');
 alert('🧾 Trazabilidad · '+r.folio+'\nAdscripción: '+(r.adscr||'—')+'\nEstado: '+r.estado+'\n\nHISTORIAL:\n'+(h||'—')+'\n\nSEGUIMIENTO:\n'+(sg||'—')+(r.oficialiaFolio?'\n\nRegistrado en Oficialía: '+r.oficialiaFolio:''));}
function borrar(id){var s=sub();if(!confirm('¿Eliminar este registro?'))return;saveR(s,loadR(s).filter(function(x){return x.id!==id;}));blog('Acción','Elimina registro '+s.title);list();}
/* Trazabilidad real hacia Oficialía de Partes (captura de oficios) — crea un oficio completo en sigej_oficios */
function toOficialia(id){var s=sub();var a=loadR(s);var r=null;a.forEach(function(x){if(x.id===id)r=x;});if(!r)return;
 if(r.oficialiaFolio){alert('Ya está registrado en Oficialía: '+r.oficialiaFolio);return;}
 if(!confirm('¿Registrar este oficio en Oficialía de Partes con trazabilidad? Se generará folio y sello.'))return;
 var d=r.d||{};var y=new Date().getFullYear();var OF=J('sigej_oficios')||[];var consec=OF.length+1;
 var folio='OF-'+String(consec).padStart(4,'0')+'/'+y;var verif='UDG-OF-'+Date.now().toString(36).toUpperCase();
 var o={folio:folio,verif:verif,serie:'OF',anio:y,consec:consec,via:d.tipo==='Externo'?'Externo':'Interno',tipo:'Oficio',demi:'Oficina de la Abogacía General',ddest:d.cargo||'',dest:d.dest||'',cargo:d.cargo||'',area:r.adscr||'',capt:PERFIL,resp:PERFIL,asunto:d.asunto||'',desc:d.desc||'',exp:[],prio:'Media',conf:'Pública',clas:'',obs:'Generado desde el Módulo Operativo ('+r.folio+')',kw:[],fecha:hoy(),hora:new Date().toTimeString().slice(0,5),sla:0,flimite:'',estatus:'Capturado',estHist:[{est:'Capturado',ts:nowStr(),usuario:PERFIL}],acuse:null,cc:[],turno:'',stubFolio:'',relaciones:[],docs:[],versiones:[],riesgos:[],traza:[{ts:nowStr(),accion:'Captura del oficio (Módulo Operativo)',usuario:PERFIL,nota:'Origen '+r.folio+' · sello '+verif}]};
 OF.push(o);localStorage.setItem('sigej_oficios',JSON.stringify(OF));
 r.oficialiaFolio=folio;(r.hist=r.hist||[]).push({ts:nowStr(),usuario:PERFIL,accion:'Registrado en Oficialía ('+folio+')'});saveR(s,a);
 blog('Acción','Oficio '+r.folio+' registrado en Oficialía como '+folio);
 alert('✅ Registrado en Oficialía de Partes\nFolio: '+folio+'\nSello: '+verif+'\nConsúltalo en Oficialía → Libro Electrónico.');list();}
function expCSV(){var s=sub();var rows=visibleRows();
 var cols=['Folio','Fecha','Estado','Adscripción','Creado por'].concat(s.fields.map(function(f){return f.l;}));
 var out=[cols].concat(rows.map(function(r){return [r.folio,r.ts,r.estado,r.adscr||'',r.creadoPor||''].concat(s.fields.map(function(f){return (r.d||{})[f.k]||'';}));}));
 var csv=out.map(function(rr){return rr.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');
 var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=s.key+'_'+hoy()+'.csv';a.click();}
/* init */
paintScope();drawTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"operativo_SIGEJ.html","w",encoding="utf-8").write(out)
print("operativo_SIGEJ.html OK -",len(out),"bytes | submódulos:",out.count("id:'s"))
