# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/chat_data.json",encoding="utf-8"))
DATA=json.dumps(d,ensure_ascii=False)
NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html" class="act">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Chat Jurídico</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#f4f6f9;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:14px 24px}
header h1{margin:0;font-size:18px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{max-width:860px;margin:auto;padding:14px;display:flex;flex-direction:column;height:calc(100vh - 92px)}
.warn{background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:7px 11px;font-size:11px;color:#8a6d1a;margin-bottom:8px}
.chat{flex:1;overflow-y:auto;padding:6px 2px;display:flex;flex-direction:column;gap:10px}
.msg{max-width:80%;padding:10px 13px;border-radius:14px;font-size:13.5px;line-height:1.5}
.bot{background:#fff;border:1px solid var(--line);align-self:flex-start;border-bottom-left-radius:4px}
.user{background:var(--azul2);color:#fff;align-self:flex-end;border-bottom-right-radius:4px}
.msg b{color:inherit}.bot b{color:var(--azul)}
.msg table{width:100%;border-collapse:collapse;font-size:12px;margin-top:6px}
.msg th,.msg td{padding:4px 7px;text-align:left;border-bottom:1px solid var(--line)}.msg th{color:var(--mut)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.chip{background:#e6f0fb;color:var(--azul2);border:1px solid #cfe0f5;border-radius:14px;padding:5px 11px;font-size:11.5px;cursor:pointer}
.chip:hover{background:#d6e6f9}
.inbar{display:flex;gap:8px;padding-top:8px}
.inbar input{flex:1;padding:11px 13px;border:1px solid var(--line);border-radius:10px;font-size:14px}
.inbar button{padding:11px 18px;border:none;border-radius:10px;background:var(--teal);color:#fff;font-weight:600;cursor:pointer}
.src{font-size:10.5px;color:var(--mut);margin-top:5px}
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
<header><h1>💬 SIGEJ-UdeG · Chat Jurídico Institucional</h1><div class="s">Asistente de consulta sobre la base jurídica — Oficina de la Abogacía General</div></header>
__NAV__
<div class="wrap">
 <div class="warn">⚠️ Asistente <b>determinístico</b> (no IA generativa): responde con cifras reales de la base, sin inventar. Para temas no cubiertos lo dice. Corte de datos en el sistema.</div>
 <div class="chat" id="chat"></div>
 <div class="chips" id="chips"></div>
 <div class="inbar"><input id="q" placeholder="Pregunta… ej. ¿cuántos activos? · tasa de éxito · expediente 44/2003-S · alto riesgo" onkeydown="if(event.key=='Enter')send()"><button onclick="send()">Enviar</button></div>
</div>
<script>
const D=__DATA__;const K=D.kpi;
const norm=s=>(s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
function M(v){return '$'+Number(v).toLocaleString('es-MX');}
function tabla(rows,h1,h2){return '<table><tr><th>'+h1+'</th><th>'+h2+'</th></tr>'+rows.map(r=>`<tr><td>${r[0]}</td><td><b>${r[1]}</b></td></tr>`).join('')+'</table>';}
function topN(obj,n){return Object.entries(obj).sort((a,b)=>b[1]-a[1]).slice(0,n||8);}
function abogadoMatch(q){const qn=norm(q);return D.abogados.find(a=>{const w=norm(a.n).split(' ');return w.some(x=>x.length>3&&qn.includes(x));});}
const HOY=new Date(2026,5,18);
function diasRest(f){return Math.round((new Date(f+'T00:00:00')-HOY)/86400000);}
function getMasc(){try{const m=JSON.parse(localStorage.getItem('sigej_masc')||'null');if(m&&m.length)return m;}catch(e){}return D.masc||[];}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function venc90(a,k,dd){return a.filter(e=>{const d=diasRest(e[k]);return d!==null&&d>=0&&d<=(dd||90);}).length;}
function hiRisk(a){return a.filter(e=>e.nivel==='Alto'||e.nivel==='Crítico').length;}
function byKey(a,k){const o={};a.forEach(e=>{o[e[k]||'—']=(o[e[k]||'—']||0)+1;});return Object.entries(o);}
function ask(q){const n=norm(q);
 const mexp=q.match(/\d{1,4}\s*\/\s*\d{2,4}(?:-?[a-zA-Z]+)?/);
 if(mexp){const num=mexp[0].replace(/\s/g,'');const e=D.index[num];
  if(e)return `<b>Expediente ${num}</b><br>Materia: <b>${e.mat}</b> · Estado: <b>${e.est}</b> · Riesgo: <b>${e.niv}</b> (${e.sc}) · Año: ${e.an||'—'}<br>Responsable: <b>${e.resp}</b> · Dependencia: ${e.dep||'—'} · ${e.act?'Activo':'Concluido'}`;
  return `No localicé el expediente <b>${num}</b> en la base (${K.total} expedientes consolidados). Verifica el número.`;}
 if(/cuant|numero|total/.test(n)&&/activ/.test(n)||/^activ/.test(n))return `Hay <b>${K.activos}</b> expedientes <b>activos</b> de ${K.total} (criterio: estado ≠ CONCLUIDO). Concluidos: ${K.concluidos}.`;
 if(/conclu/.test(n))return `<b>${K.concluidos}</b> expedientes concluidos de ${K.total}.`;
 if(/tasa|exito|éxito|gana|pierd/.test(n))return `<b>Tasa de éxito procesal:</b> ${K.tasa_e}% (criterio estricto Fav/[Fav+Desf]) · ${K.tasa_a}% (criterio ampliado, incluye sobreseimientos y amparos negados a la contraparte).`;
 if(/alto riesgo|critico|crítico|riesgo alto/.test(n))return `<b>${K.alto}</b> asuntos de <b>alto riesgo</b> (${K.criticos} críticos). Top:`+tabla(D.alto_top.slice(0,8).map(x=>[x.num+' ('+x.mat+')',x.niv+' '+x.sc]),'Expediente','Riesgo')+'<div class="src">Score proxy explicable, orientativo.</div>';
 if(/materia/.test(n))return `<b>Expedientes por materia</b> (rama sustantiva):`+tabla(topN(D.materia),'Materia','N');
 if(/(por|cada|del) ?(año|anio)|litigiosidad.*año/.test(n)||/^año|^anio/.test(n))return `<b>Expedientes por año</b> (radicación):`+tabla(topN(D.anio,20),'Año','N');
 if(/depend|centro|cucs|cucea|conflicto/.test(n))return `<b>Dependencias con más litigiosidad:</b>`+tabla(topN(D.dep,10),'Dependencia','N');
 if(/pasivo|conting|reserva|cuanto debe|monto total/.test(n))return `<b>Pasivo contingente (piso documentado):</b> ${M(K.pasivo)} — solo expedientes con monto capturado. La cuantía real es mayor (la mayoría no tiene monto legible). Ver pestaña Provisión del dashboard.`;
 if(/atora|rezago|caduc|sin movim|parad|inactiv/.test(n))return `<b>${K.atora24}</b> expedientes activos sin movimiento registrado <b>> 24 meses</b> (riesgo de caducidad). Revisa la vista "Tiempos & Cuellos" del dashboard.`;
 if(/cuello|tiempo|duracion|duración|tarda|demora|lento/.test(n))return `Duración mediana de un juicio: <b>${K.dur} años</b>. El <b>cuello de botella</b> es la etapa <b>${K.cuello}</b> con ${K.cuello_d} días de mediana (el resto fluye en pocos días).`;
 if(/suspension|suspensión|suspens/.test(n))return `<b>${K.susp}</b> expedientes con <b>suspensión provisional concedida</b> (análisis documental, a confirmar caso por caso).`;
 if(/parcialidad/.test(n)){const ms=getMasc();let pend=[];ms.forEach(r=>(r.parcialidades||[]).forEach(p=>{if(!p.pagada){const d=diasRest(p.fecha);pend.push({exp:r.exp||r.id,nn:p.n,d:d});}}));
  if(!ms.some(r=>(r.parcialidades||[]).length))return `Aún no hay <b>parcialidades</b> capturadas con calendario de pago. Captúralas en el módulo 🤝 MASC (forma de pago: Parcialidades).`;
  const venc=pend.filter(x=>x.d<0),prox=pend.filter(x=>x.d>=0&&x.d<=30);pend.sort((a,b)=>a.d-b.d);
  return `Parcialidades pendientes: <b>${pend.length}</b> · <b>${venc.length}</b> vencidas · <b>${prox.length}</b> por vencer (≤30 días).`+(pend.length?tabla(pend.slice(0,8).map(x=>[x.exp+' · parc. '+x.nn,x.d<0?'venció hace '+(-x.d)+'d':'en '+x.d+'d']),'Convenio','Vencimiento'):'');}
 if(/masc|convenio|concili/.test(n)){const ms=getMasc();const monto=ms.reduce((s,x)=>s+(+x.monto||0),0);const byc={};ms.forEach(x=>{const c=x.cumplimiento||'—';byc[c]=(byc[c]||0)+1;});
  return `<b>${ms.length}</b> convenios/conciliaciones MASC (todos laborales en la base) · monto convenido <b>${M(monto)}</b>.`+tabla(Object.entries(byc),'Cumplimiento','N')+'<div class="src">No incluye desistimientos, caducidades ni sobreseimientos. Detalle en el módulo 🤝 MASC.</div>';}
 if(/carga|cuantos lleva|cartera|reparto/.test(n)){const a=abogadoMatch(q);if(a)return `<b>${a.n}</b> — ${a.act} activos de ${a.tot} totales · estatus: <b>${a.st}</b>.`;
  return `<b>Carga por abogado</b> (activos):`+tabla(D.abogados.slice().sort((x,y)=>y.act-x.act).slice(0,8).map(a=>[a.n.split(' ').slice(0,2).join(' ')+(a.st!=='Activo'?' ('+a.st+')':''),a.act]),'Abogado','Activos');}
 if(/baja|incapac|renunci|ya no esta|personal|plantilla/.test(n)){const ina=D.abogados.filter(a=>a.st!=='Activo');
  return `Personal no activo:`+tabla(ina.map(a=>[a.n.split(' ').slice(0,2).join(' '),a.st+' · '+a.act+' activos']),'Abogado','Estatus')+'<div class="src">Reasigna su cartera en el módulo 👤 Abogados.</div>';}
 if(/panorama|resumen|todo el sistema|todos los modulos|todos los módulos|institucional|cuantos asuntos|cuántos asuntos|por modulo|por módulo|ecosistema/.test(n)){
  const inst=J('sigej_instrumentos'),pat=J('sigej_patrimonio'),intl=J('sigej_internacional'),norm=J('sigej_normatividad'),proy=J('sigej_proyectos'),resp=J('sigej_resp'),ase=J('sigej_asesoria'),ms=getMasc();
  const rows=[['⚖️ Litigio / Contencioso',K.total],['📜 Instrumentos (CLM)',inst.length],['🧩 Patrimonio intangible',pat.length],['🌎 Asuntos internacionales',intl.length],['📖 Normatividad',norm.length],['📌 Proyectos',proy.length],['⚖️ Responsabilidades',resp.length],['💡 Asesoría',ase.length],['🤝 MASC',ms.length]];
  const tot=rows.reduce((s,r)=>s+(+r[1]||0),0);
  return `<b>Panorama institucional</b> — ${tot} asuntos/registros en todo el sistema:`+tabla(rows,'Módulo / área','N')+'<div class="src">Litigio embebido (corte oficial); el resto es lo capturado en cada módulo. Detalle y buscador global en 📊 Transparencia General.</div>';}
 if(/instrumento|contrato|^clm|legal erp/.test(n)){const a=J('sigej_instrumentos');
  if(!a.length)return 'Aún no hay <b>instrumentos jurídicos</b> (convenios/contratos, CLM) capturados. Captúralos en el módulo 📜 Instrumentos.';
  return `<b>${a.length}</b> instrumentos jurídicos (CLM) · <b>${hiRisk(a)}</b> de alto riesgo · <b>${venc90(a,'fin',90)}</b> por vencer (≤90 días).`+tabla(byKey(a,'fam'),'Familia','N')+'<div class="src">Detalle en el módulo 📜 Instrumentos.</div>';}
 if(/patrimonio|propiedad intelectual|marca|patente|derecho de autor|variedad vegetal|obtentor|software institucional|intangible/.test(n)){const a=J('sigej_patrimonio');
  if(!a.length)return 'Aún no hay <b>activos de patrimonio intangible</b> (marcas, patentes, obras, software…) capturados. Captúralos en el módulo 🧩 Patrimonio Intangible.';
  return `<b>${a.length}</b> activos de patrimonio intangible · <b>${venc90(a,'venc',180)}</b> con vigencia próxima (≤180d).`+tabla(byKey(a,'cat'),'Categoría','N');}
 if(/internacional|visa|migrat|migra|extranjer|movilidad|consul|pasaporte|convenio internacional/.test(n)){const a=J('sigej_internacional');
  if(!a.length)return 'Aún no hay <b>expedientes internacionales</b> (migración, movilidad, convenios internacionales, traducción) capturados. Captúralos en el módulo 🌎 Asuntos Internacionales.';
  return `<b>${a.length}</b> expedientes internacionales · <b>${venc90(a,'venc',180)}</b> con vigencia migratoria próxima (≤180d).`+tabla(byKey(a,'clase'),'Clase','N');}
 if(/normativ|reglamento|estatuto|reforma|dictamen|tecnica legislativa|técnica legislativa|cuadro comparativo/.test(n)){const a=J('sigej_normatividad');
  if(!a.length)return 'Aún no hay <b>expedientes normativos</b> (reformas, dictámenes, interpretaciones) capturados. Captúralos en el módulo 📖 Normatividad.';
  return `<b>${a.length}</b> expedientes normativos · <b>${hiRisk(a)}</b> de riesgo alto.`+tabla(byKey(a,'tipo'),'Tipo','N');}
 if(/proyecto/.test(n)){const a=J('sigej_proyectos');if(!a.length)return 'Aún no hay <b>proyectos</b> registrados. Captúralos en el módulo 📌 Proyectos.';
  const r=a.filter(e=>e.estado==='En riesgo').length;return `<b>${a.length}</b> proyectos · <b>${r}</b> en riesgo.`+tabla(byKey(a,'estado'),'Estado','N');}
 if(/responsabilidad|lgra|sancion|sanción|falta administrativa|prescrip/.test(n)){const a=J('sigej_resp');
  if(!a.length)return 'Aún no hay <b>procedimientos de responsabilidad administrativa</b> (marco LGRA) capturados. Captúralos en el módulo ⚖️ Responsabilidades.';
  return `<b>${a.length}</b> procedimientos de responsabilidad administrativa.`+tabla(byKey(a,'estado'),'Estado','N')+'<div class="src">Detalle y alerta de prescripción en ⚖️ Responsabilidades.</div>';}
 if(/asesoria|asesoría|consulta|opinion|opinión|dictamen juridico/.test(n)){const a=J('sigej_asesoria');
  if(!a.length)return 'Aún no hay <b>consultas/asesorías</b> capturadas. Regístralas en el módulo 💡 Asesoría.';
  return `<b>${a.length}</b> consultas/asesorías registradas.`+tabla(byKey(a,'estado'),'Estado','N');}
 const a=abogadoMatch(q);if(a)return `<b>${a.n}</b> lleva ${a.act} expedientes activos (${a.tot} totales) · estatus: <b>${a.st}</b>.`;
 if(/hola|buenas|saludos|ayuda|que puedes|qué puedes/.test(n))return `Soy tu asistente jurídico institucional. Integro <b>todo el sistema</b>:<br>• <b>Litigio</b>: activos, tasa de éxito, alto riesgo, materia/año/dependencia, pasivo, atorados, cuellos, suspensiones, carga por abogado, o un expediente por su número.<br>• <b>Otras áreas</b>: instrumentos (CLM), patrimonio intangible (marcas/patentes), asuntos internacionales (visas/migración), normatividad, proyectos, MASC, responsabilidades, asesoría.<br>• <b>Panorama institucional</b> (escribe «panorama» o «resumen»). ¿Qué necesitas?`;
 return `No tengo una respuesta determinística para eso. Cubro <b>todo el sistema</b>: litigio (activos, tasa, riesgo, materia, pasivo, atorados, cuellos, carga por abogado, expediente por número), <b>instrumentos, patrimonio, internacional, normatividad, proyectos, MASC, responsabilidades, asesoría</b> y un <b>panorama institucional</b>. Para análisis abierto, consúltame (Veritas) directamente.`;}
function add(html,cls){const c=document.getElementById('chat');const d=document.createElement('div');d.className='msg '+cls;d.innerHTML=html;c.appendChild(d);c.scrollTop=c.scrollHeight;}
function send(){const v=document.getElementById('q').value.trim();if(!v)return;add(v,'user');document.getElementById('q').value='';setTimeout(()=>add(ask(v),'bot'),120);}
const CHIPS=['Panorama institucional','¿Cuántos activos?','Tasa de éxito','Asuntos de alto riesgo','Carga por abogado','Instrumentos','Patrimonio / marcas','Asuntos internacionales','Normatividad','Proyectos','Convenios MASC','Parcialidades por vencer','Expediente 44/2003-S'];
document.getElementById('chips').innerHTML=CHIPS.map(c=>`<span class="chip" onclick="document.getElementById('q').value='${c}';send()">${c}</span>`).join('');
add('👋 Hola, soy el <b>Chat Jurídico Institucional</b> de SIGEJ-UdeG. Ahora integro <b>todo el sistema</b>: litigio ('+K.total+' expedientes) + instrumentos, patrimonio intangible, asuntos internacionales, normatividad, proyectos, MASC, responsabilidades y asesoría. Escribe «<b>panorama</b>» para un resumen institucional, o prueba un botón de abajo.','bot');
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
})();</script>
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
open("/Users/edithroque/Documents/CLAUDE/chat_SIGEJ.html","w",encoding="utf-8").write(TPL.replace("__DATA__",DATA).replace("__NAV__",NAV))
print("chat_SIGEJ.html OK")
