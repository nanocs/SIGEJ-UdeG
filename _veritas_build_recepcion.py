# -*- coding: utf-8 -*-
# OFICIALÍA DE PARTES · SUBMÓDULO DE RECEPCIÓN INTEGRAL (hub central de correspondencia jurídica del SIGEJ)
# Recepción → Registro → Digitalización/OCR → Clasificación → Turnado → Retorno (inmutable) → Trazabilidad → Acuse QR → Dashboard → Riesgos.
# Reglas: folio único, sin borrado (solo retorno/aclaración/cancelación con motivo), historial inalterable con sello (quién/cuándo).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Oficialía · Recepción'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','recepcion_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="recepcion_SIGEJ.html" class="act">📥 Recepción</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="alertas_centro_SIGEJ.html">🔔 Alertas</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Oficialía de Partes · Recepción</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--orange:#ea580c;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:15px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabbar{display:flex;gap:5px;flex-wrap:wrap;padding:12px 18px 0;max-width:1340px;margin:auto}
.tb{padding:9px 13px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px;color:#334155}
.tb.on{background:#0a4d8c;color:#fff;font-weight:700}
.wrap{max-width:1340px;margin:auto;padding:14px 18px 44px}
.ct{display:none}.ct.on{display:block}
.flow{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:12px}
.flow span{background:#fff;border:1px solid var(--line);border-radius:20px;padding:4px 10px;font-size:11px;color:#64748b}
.flow span b{color:#0a4d8c}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:12px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul2)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.y .n{color:var(--amber)}.kpi.g .n{color:var(--ok)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.card h3{margin:0 0 8px;font-size:14px;color:var(--azul)}
.grid{display:grid;gap:8px}
label.lb{font-size:11px;color:#64748b;display:block;margin-bottom:2px;font-weight:600}
.req{color:#c0392b}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px;background:#fff}
textarea{min-height:46px;resize:vertical}
fieldset{border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin:0 0 10px}
legend{font-size:11.5px;color:#0a4d8c;font-weight:700;padding:0 6px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:8px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bo{background:var(--orange);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bg{background:var(--ok);color:#fff;font-weight:700}.br{background:var(--red);color:#fff;font-weight:700}.mini{padding:5px 9px;font-size:11.5px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:7px 6px;vertical-align:top}
tr.rowc{cursor:pointer}tr.rowc:hover{background:#f8fbff}
.bdg{padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;white-space:nowrap;background:#eef2f7;color:#0a4d8c}
.st{padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;white-space:nowrap}
.st.v{background:#e7f7ee;color:#128c4a}.st.y{background:#fef3e2;color:#b45309}.st.r{background:#fdeaea;color:#c0392b}.st.b{background:#eef6ff;color:#0a4d8c}.st.g{background:#f1f5f9;color:#475569}
.u-Urgente{color:#c0392b;font-weight:700}.u-Alta{color:#ea580c;font-weight:700}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.warn{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.drawer{position:fixed;inset:0;background:rgba(8,20,38,.5);display:none;z-index:9000}
.drawer.on{display:block}
.panel{position:absolute;top:0;right:0;width:640px;max-width:96vw;height:100%;background:#fff;overflow:auto;padding:18px 20px;box-shadow:-8px 0 30px rgba(0,0,0,.3)}
.panel .x{position:absolute;top:12px;right:16px;cursor:pointer;font-size:18px;color:#64748b}
.tl{border-left:2px solid #cbd5e1;margin-left:6px;padding-left:14px}
.tl .ev{position:relative;padding:7px 0;font-size:12px}
.tl .ev:before{content:'';position:absolute;left:-21px;top:11px;width:9px;height:9px;border-radius:50%;background:#0a4d8c}
.tl .ev.ret:before{background:#c0392b}.tl .ev.tur:before{background:#ea580c}
.acuse{border:2px dashed #0a4d8c;border-radius:12px;padding:14px;display:flex;gap:14px;align-items:flex-start;background:#fff}
.acuse .q img{width:118px;height:118px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
@media print{.navbar,header,.tabbar,.flow,footer,.acts,.card.filtros{display:none!important}body{background:#fff}}
</style></head><body>
<header><h1>📥 Oficialía de Partes · Recepción y Correspondencia</h1><div class="s">Hub central del SIGEJ — punto único de entrada, registro, turnado, retorno y trazabilidad de la Abogacía General</div></header>
__NAV__
<div class="tabbar" id="tabbar"></div>
<div class="wrap">
 <div class="flow"><span>1 <b>Recibir</b></span><span>2 <b>Registrar</b></span><span>3 <b>Digitalizar</b></span><span>4 <b>Clasificar</b></span><span>5 <b>Turnar</b></span><span>6 <b>Revisar</b></span><span>7 <b>Retornar/Aceptar</b></span><span>8 <b>Atender</b></span><span>9 <b>Concluir</b></span><span>10 <b>Archivar</b></span></div>
 <div id="pane"></div>
</div>
<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwc"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function S(k,v){localStorage.setItem(k,JSON.stringify(v));}
function ec(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function nowT(){return new Date().toISOString().slice(0,16).replace('T',' ');}
function nowFull(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function today(){return new Date().toISOString().slice(0,10);}
function hora(){return new Date().toTimeString().slice(0,8);}
var PERFIL=localStorage.getItem('sigej_perfil')||'(perfil)';
var SES=J('sigej_sesion')||{};
/* ===== catálogos ===== */
var ADMIN=['Administrador','Sistemas','Jefe del Área de Sistemas'];
function isAdmin(){return ADMIN.indexOf(PERFIL)>=0;}
var RETORNO=['Administrador','Sistemas','Jefe del Área de Sistemas','Director','Coordinador Jurídico','Coordinador de Enlace con la Red','Coordinador de Normatividad','Jefe de Oficialía de Partes'];
function puedeRetornar(){return RETORNO.indexOf(PERFIL)>=0;}
var COORDS=['Abogacía General (Dirección)','Coordinación General Jurídica','Coordinación de Enlace con la Red','Coordinación de Normatividad'];
var UNIDADES=['Unidad de lo Contencioso','Unidad de Atención y Servicios Legales','Unidad de Patrimonio Intangible','Unidad de Asuntos Internacionales','Unidad de Instrumentos Jurídicos','Unidad de Capacitación, Investigación y Difusión','Unidad de Estatutos y Reglamentos','Unidad de Normatividad Administrativa','Unidad de Apoyo a Órganos Colegiados','Área Contable','Área de Personal','Área de Sistemas','Oficialía de Partes','Mensajería'];
var MODULOS=['contencioso_SIGEJ','instrumentos_SIGEJ','patrimonio_SIGEJ','internacional_SIGEJ','normatividad_SIGEJ','operativo_SIGEJ','serviciosocial_SIGEJ'];
var MEDIOS=['Físico / ventanilla','Correo electrónico','Mensajería','Plataforma','Escaneo','Carga digital'];
var URGENCIA=['Normal','Media','Alta','Urgente'];
var CONFID=['Pública','Reservada','Confidencial','Datos personales sensibles'];
var MEDIO_ACUSE=['Correo electrónico','Impreso','SIGEJ','WhatsApp'];
var ESTATUS=['Recibido','Digitalizado','Pendiente de clasificación','Turnado','Devuelto por error de turnado','Retornado a Oficialía','Reasignado','En revisión','En trámite','En firma','Atendido','Concluido','Archivado','Cancelado'];
function stColor(s){if(['Concluido','Atendido','Archivado'].indexOf(s)>=0)return 'v';if(['Devuelto por error de turnado','Cancelado'].indexOf(s)>=0)return 'r';if(['Retornado a Oficialía','Pendiente de clasificación','En firma'].indexOf(s)>=0)return 'y';if(s==='Recibido'||s==='Turnado'||s==='En revisión'||s==='En trámite'||s==='Reasignado')return 'b';return 'g';}
var TIPOS_DEF=['Demanda inicial','Promoción','Oficio','Requerimiento','Notificación','Acuerdo','Resolución','Sentencia','Emplazamiento','Citatorio','Informe','Convenio','Contrato','Dictamen','Consulta jurídica','Solicitud interna','Solicitud externa','Documentación complementaria','Acuse','Anexo','Correspondencia general'];
function tipos(){var t=J('sigej_tipos_doc');return Array.isArray(t)&&t.length?t:TIPOS_DEF;}
function seedTipos(){if(!J('sigej_tipos_doc'))S('sigej_tipos_doc',TIPOS_DEF.slice());}
seedTipos();
/* formularios dinámicos por tipo (III) */
var DIN={
 'Demanda inicial':[['autoridad','Autoridad'],['resimp','Resolución impugnada'],['actor','Actor'],['demandado','Demandado'],['tercero','Tercero interesado'],['materia','Materia'],['plazo','Plazo probable'],['docing','Documento que se ingresa']],
 'Promoción':[['exp','Expediente'],['organo','Órgano jurisdiccional'],['actor','Actor'],['demandado','Demandado'],['tercero','Tercero'],['docing','Documento que se ingresa'],['copias','Copias']],
 'Oficio':[['numofi','Número de oficio'],['depemi','Dependencia emisora'],['dest','Destinatario'],['cargo','Cargo'],['asu2','Asunto'],['ccc','Copias de conocimiento'],['expvinc','Expedientes vinculados']],
 'Convenio':[['tipoinst','Tipo de instrumento'],['depsol','Dependencia solicitante'],['contra','Contraparte'],['monto','Monto (si aplica)'],['vig','Vigencia'],['fuente','Fuente de financiamiento'],['anxtec','Anexos técnicos']],
 'Contrato':[['tipoinst','Tipo de instrumento'],['depsol','Dependencia solicitante'],['contra','Contraparte'],['monto','Monto (si aplica)'],['vig','Vigencia'],['fuente','Fuente de financiamiento'],['anxtec','Anexos técnicos']]
};
/* ===== datos ===== */
function REC(){var a=J('sigej_recepcion');return Array.isArray(a)?a:[];}
function saveREC(a){S('sigej_recepcion',a);}
function byId(id){return REC().filter(function(r){return r.id===id;})[0];}
function blog(t,a){try{var L=J('sigej_bitacora')||[];L.push({ts:nowFull(),perfil:PERFIL,modulo:'Oficialía · Recepción',tipo:t,accion:String(a||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);S('sigej_bitacora',L);}catch(e){}if(window.__bitlog){try{window.__bitlog(t,a);}catch(e){}}}
function tl(r,accion,obs,cls){(r.timeline=r.timeline||[]).push({ts:nowT(),usuario:PERFIL,accion:accion,modulo:'Recepción',obs:obs||'',cls:cls||''});}
function makeQR(text){try{var d=document.createElement('div');new QRCode(d,{text:String(text),width:118,height:118,correctLevel:QRCode.CorrectLevel.M});var c=d.querySelector('canvas');if(c)return c.toDataURL('image/png');var im=d.querySelector('img');return im?im.src:'';}catch(e){return '';}}
/* ===== XI DISTRIBUCIÓN / NOTIFICACIÓN AUTOMÁTICA (store persistente sigej_notificaciones; el módulo Notificaciones lo consume) ===== */
function notify(base,dests){var N=J('sigej_notificaciones')||[];var t=Date.now().toString(36);var n=0;
 dests.forEach(function(d,i){if(!d.para)return;n++;N.push({id:'NT-'+t+'-'+i,ts:nowT(),tipo:base.tipo,folio:base.folio,asunto:base.asunto||'',para:d.para,rol:d.rol||'',canal:d.canal||'SIGEJ',mensaje:base.mensaje||'',link:base.link||'recepcion_SIGEJ.html',leido:false,origen:'Oficialía · Recepción'});});
 if(N.length>4000)N=N.slice(-4000);S('sigej_notificaciones',N);return n;}
function distribuir(r,contexto){var d=r.destino||{};
 var ccc=(r.din&&r.din.ccc)?String(r.din.ccc).split(/[,;]+/).map(function(s){return s.trim();}).filter(Boolean):[];
 var dests=[{para:d.coordinacion,rol:'Área receptora',canal:'SIGEJ'},{para:d.unidad,rol:'Unidad/área',canal:'SIGEJ'},{para:d.abogado,rol:'Abogado asignado',canal:'SIGEJ'},{para:'Supervisor del área',rol:'Supervisor',canal:'SIGEJ'}];
 if(r.correoCopia)dests.push({para:r.correoCopia,rol:'Quien presenta',canal:'Correo'});
 ccc.forEach(function(c){dests.push({para:c,rol:'Copia de conocimiento',canal:'SIGEJ'});});
 var n=notify({tipo:contexto||'Recepción',folio:r.folio,asunto:r.asunto,mensaje:(contexto||'Documento')+' — '+r.tipoDoc+' turnado a '+(d.coordinacion||'—')+(d.abogado?' · Abg. '+d.abogado:''),link:'recepcion_SIGEJ.html'},dests);
 tl(r,'Notificación / distribución',(n)+' destinatario(s): '+(d.coordinacion||'—')+(d.abogado?' · Abg. '+d.abogado:'')+(r.correoCopia?' · correo a '+r.correoCopia:''));
 return n;}
/* ===== vinculación del turnado con CREACIÓN REAL DE EXPEDIENTE en el módulo destino ===== */
function crearDestino(modulo,r,a){try{
 if(modulo==='contencioso_SIGEJ'){var C=J('sigej_capturas')||[];var num=a.expediente||('EXP-REC-'+(C.length+1)+'/'+new Date().getFullYear());while(C.some(function(x){return x.num===num;}))num=num+'-'+Date.now().toString(36).slice(-2);
  C.push({num:num,materia_fina:(r.din&&r.din.materia)||r.tipoDoc,via:'',tipo_juicio:'',estado:'En trámite',dependencia:r.presenta.dependencia||'',centro:'',actor:(r.din&&r.din.actor)||'',demandado:(r.din&&r.din.demandado)||'Universidad de Guadalajara',autoridad:(r.din&&r.din.autoridad)||'',responsable:a.abogado||'Por asignar',sentido:'',monto:0,pasivo:0,anio:new Date().getFullYear(),fecha_inicio:r.fecha,observaciones:'Creado desde Oficialía · Recepción '+r.folio,pruebas:'',docs:[],agenda:[],score:20,nivel_riesgo:'Bajo',prioridad:(r.urgencia==='Urgente'?'Urgente':'Normal'),capturado:today(),origen:'Oficialía · Recepción',recepcionFolio:r.folio});
  S('sigej_capturas',C);return {folio:num,link:'contencioso_SIGEJ.html',label:'Expediente contencioso'};}
 if(modulo==='instrumentos_SIGEJ'){var I=J('sigej_instrumentos')||[];var yr=String(new Date().getFullYear());var folio='INSTR-'+yr+'-'+String(I.length+1).padStart(3,'0');
  I.push({folio:folio,fam:(r.tipoDoc==='Contrato'?'Contratos':'Convenios'),tipo:r.tipoDoc,area:'OAG',dep:(r.din&&r.din.depsol)||r.presenta.dependencia||'',contra:(r.din&&r.din.contra)||'',obj:r.asunto,monto:+(r.din&&r.din.monto)||0,fuente:(r.din&&r.din.fuente)||'',firma:'',ini:'',fin:(r.din&&r.din.vig)||'',estado:'Solicitud',resp:a.abogado||'Por asignar',oblig:[],movimientos:[{fecha:r.fecha,oficio:r.folio,area:'Oficialía de Partes',desc:'Ingreso por Oficialía · Recepción'}],versiones:[{v:1,autor:PERFIL,fecha:today(),nota:'Alta desde Oficialía · Recepción '+r.folio}],bitacora:[{ts:nowFull(),accion:'Alta desde Recepción',usuario:PERFIL}],score:20,nivel:'Bajo',origen:'Oficialía · Recepción',recepcionFolio:r.folio});
  S('sigej_instrumentos',I);return {folio:folio,link:'instrumentos_SIGEJ.html',label:'Instrumento jurídico'};}
 /* demás módulos → alta protegida en su propio store (aparece en su widget de Alta, inmutable) */
 var AL=J('sigej_altas')||[];var f2='ALT-'+new Date().getFullYear()+'-'+String(AL.length+1).padStart(4,'0');
 AL.push({id:'AL-'+Date.now().toString(36),folio:f2,tipo:'Expediente nuevo',modulo:modulo,titulo:r.asunto,detalle:'Turnado desde Oficialía · Recepción '+r.folio+' ('+r.tipoDoc+')',plazoTipo:'',plazoBase:'',fechaLimite:'',estado:'Abierto',capturadoPor:PERFIL,fechaCaptura:nowT(),hist:[{ts:nowT(),usuario:PERFIL,accion:'Alta desde Recepción '+r.folio}],seguimiento:[],subprocesos:[],anulado:null,origen:'Oficialía · Recepción',recepcionFolio:r.folio});
 S('sigej_altas',AL);return {folio:f2,link:modulo+'.html',label:'Expediente vinculado'};
}catch(e){return null;}}
/* ===== TABS ===== */
var TABS=[['t1','📥 Recepción'],['t2','📋 Bandeja / Libro'],['t3','📊 Dashboard'],['t4','⚠️ Matriz de riesgos'],['t6','↩️ Tablero de retornos'],['t5','⚙️ Catálogo de tipos']];
var cur='t1';
function drawTabs(){el('tabbar').innerHTML=TABS.map(function(t){return '<button class="tb'+(t[0]===cur?' on':'')+'" onclick="go(\''+t[0]+'\')">'+t[1]+'</button>';}).join('');}
function go(id){cur=id;drawTabs();render();window.scrollTo(0,0);}
function render(){if(cur==='t1')formRecepcion();else if(cur==='t2')bandeja();else if(cur==='t3')dashboard();else if(cur==='t4')riesgos();else if(cur==='t6')retornos();else if(cur==='t5')catalogo();}
/* ===== I-IV RECEPCIÓN (form dinámico) ===== */
function opt(a,sel){return a.map(function(x){return '<option'+(x===sel?' selected':'')+'>'+ec(x)+'</option>';}).join('');}
function formRecepcion(){var puede=['Secretaría General','Director','Coordinador General','Consulta'].indexOf(PERFIL)<0;
 if(!puede){el('pane').innerHTML='<div class="warn">Tu perfil es de consulta: puedes ver la Bandeja y el Dashboard, no registrar recepciones.</div>';return;}
 var g3='grid-template-columns:repeat(auto-fit,minmax(210px,1fr))';
 el('pane').innerHTML='<div class="card"><h3>📥 Recepción de documento · folio único, acuse, sello y QR</h3>'+
  '<input type="hidden" id="f_id">'+
  '<fieldset><legend>Recepción</legend><div class="grid" style="'+g3+'">'+
   '<div><label class="lb">Fecha de recepción</label><input id="f_fecha" type="date" value="'+today()+'"></div>'+
   '<div><label class="lb">Hora exacta</label><input id="f_hora" value="'+hora()+'" readonly></div>'+
   '<div><label class="lb">Medio de recepción <span class="req">*</span></label><select id="f_medio">'+opt(MEDIOS)+'</select></div>'+
   '<div><label class="lb">Tipo de documento <span class="req">*</span></label><select id="f_tipo" onchange="dinRender()">'+opt(tipos())+'</select></div>'+
   '<div><label class="lb">Nivel de urgencia</label><select id="f_urg">'+opt(URGENCIA)+'</select></div>'+
   '<div><label class="lb">Confidencialidad</label><select id="f_conf">'+opt(CONFID)+'</select></div>'+
  '</div></fieldset>'+
  '<fieldset><legend>Quién suscribe / presenta / recibe (IV)</legend><div class="grid" style="'+g3+'">'+
   '<div><label class="lb">Suscribe (escribe/firma) — nombre</label><input id="f_susn" placeholder="Nombre de quien suscribe"></div>'+
   '<div><label class="lb">Suscribe — cargo</label><input id="f_susc" placeholder="Cargo"></div>'+
   '<div><label class="lb">Presenta — nombre <span class="req">*</span></label><input id="f_pren" placeholder="Quien presenta el documento"></div>'+
   '<div><label class="lb">Presenta — cargo</label><input id="f_prec" placeholder="Cargo de quien presenta"></div>'+
   '<div><label class="lb">Dependencia / institución / procedencia <span class="req">*</span></label><input id="f_dep" placeholder="Área o institución de origen"></div>'+
   '<div><label class="lb">Recibe (Oficialía)</label><input id="f_recn" value="'+ec(SES.nombre||PERFIL)+'" readonly></div>'+
   '<div><label class="lb">Cargo/usuario de quien recibe</label><input id="f_recc" value="'+ec(PERFIL)+'" readonly></div>'+
  '</div></fieldset>'+
  '<fieldset><legend>Asunto y destino</legend><div class="grid" style="'+g3+'">'+
   '<div style="grid-column:1/-1"><label class="lb">Asunto <span class="req">*</span></label><input id="f_asu" placeholder="Asunto del documento"></div>'+
   '<div><label class="lb">Expediente relacionado</label><input id="f_exp" placeholder="Folio de expediente (si existe)"></div>'+
   '<div><label class="lb">Coordinación destinataria <span class="req">*</span></label><select id="f_coord">'+opt([''].concat(COORDS))+'</select></div>'+
   '<div><label class="lb">Unidad / área destinataria</label><select id="f_unidad">'+opt([''].concat(UNIDADES))+'</select></div>'+
   '<div><label class="lb">Abogado destinatario (si procede)</label><input id="f_abog" placeholder="Nombre del abogado"></div>'+
  '</div></fieldset>'+
  '<fieldset id="f_din"><legend>Datos específicos del tipo</legend><div class="grid" id="f_dinbox" style="'+g3+'"></div></fieldset>'+
  '<fieldset><legend>Anexos, acuse y digitalización</legend><div class="grid" style="'+g3+'">'+
   '<div><label class="lb">Número de anexos</label><input id="f_anx" type="number" min="0" value="0"></div>'+
   '<div style="grid-column:span 2"><label class="lb">Descripción de anexos</label><input id="f_anxd" placeholder="Detalle de anexos"></div>'+
   '<div><label class="lb">Medio de notificación para acuse</label><select id="f_macuse">'+opt(MEDIO_ACUSE)+'</select></div>'+
   '<div><label class="lb">Correo para copia del formato</label><input id="f_correo" placeholder="correo@dominio"></div>'+
   '<div><label class="lb">Documento digitalizado</label><input id="f_file" type="file"></div>'+
   '<div style="grid-column:1/-1"><label class="lb">Observaciones</label><textarea id="f_obs" placeholder="Observaciones"></textarea></div>'+
  '</div></fieldset>'+
  '<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center"><button class="bg" onclick="guardarRec()">💾 Registrar recepción (genera folio + acuse + QR)</button><button class="bd" onclick="ocrRec()">🔎 OCR / autollenado</button><button class="bd" onclick="formRecepcion()">Limpiar</button><span id="f_msg" style="font-size:12px;margin-left:6px"></span></div>'+
  '</div><div id="acuseBox"></div>';
 dinRender();}
function dinRender(){var t=el('f_tipo').value;var box=el('f_dinbox');var cfg=DIN[t];
 if(!cfg){el('f_din').style.display='none';box.innerHTML='';return;}
 el('f_din').style.display='';el('f_din').querySelector('legend').textContent='Datos específicos · '+t;
 box.innerHTML=cfg.map(function(f){return '<div><label class="lb">'+ec(f[1])+'</label><input id="d_'+f[0]+'" placeholder="'+ec(f[1])+'"></div>';}).join('');}
function guardarRec(){
 var req={f_medio:'Medio',f_tipo:'Tipo',f_pren:'Presenta (nombre)',f_dep:'Dependencia de procedencia',f_asu:'Asunto',f_coord:'Coordinación destinataria'};
 for(var k in req){var v=(el(k).value||'').trim();if(!v){el('f_msg').style.color='#c0392b';el('f_msg').textContent='Falta: '+req[k];return;}}
 var A=REC();var y=new Date().getFullYear();var folio='REC-'+y+'-'+String(A.length+1).padStart(5,'0');
 var verif='UDG-REC-'+Date.now().toString(36).toUpperCase();
 var din={};var t=el('f_tipo').value;if(DIN[t])DIN[t].forEach(function(f){var e=el('d_'+f[0]);if(e)din[f[0]]=e.value.trim();});
 var r={id:'RC-'+Date.now().toString(36),folio:folio,verif:verif,fecha:el('f_fecha').value||today(),hora:el('f_hora').value||hora(),
  suscribe:{nombre:el('f_susn').value.trim(),cargo:el('f_susc').value.trim()},
  presenta:{nombre:el('f_pren').value.trim(),cargo:el('f_prec').value.trim(),dependencia:el('f_dep').value.trim()},
  recibe:{nombre:SES.nombre||PERFIL,usuario:PERFIL},
  medioRecepcion:el('f_medio').value,tipoDoc:t,asunto:el('f_asu').value.trim(),expedienteRel:el('f_exp').value.trim(),
  destino:{coordinacion:el('f_coord').value,unidad:el('f_unidad').value,area:el('f_unidad').value,abogado:el('f_abog').value.trim()},
  anexosNum:+el('f_anx').value||0,anexosDesc:el('f_anxd').value.trim(),observaciones:el('f_obs').value.trim(),
  urgencia:el('f_urg').value,confidencialidad:el('f_conf').value,medioAcuse:el('f_macuse').value,correoCopia:el('f_correo').value.trim(),
  din:din,docs:[],estatus:'Recibido',capturadoPor:PERFIL,fechaCaptura:nowT(),turnos:[],timeline:[],cancelado:null};
 r.qr=makeQR(folio+'|'+verif);
 tl(r,'Recepción','Ingreso por '+r.medioRecepcion+' · presenta '+r.presenta.nombre);
 var f=el('f_file').files[0];
 var fin=function(){distribuir(r,'Recepción');A.push(r);saveREC(A);blog('Acción','Recepción registrada '+folio+' · '+t);el('f_msg').style.color='#128c4a';el('f_msg').textContent='✓ '+folio+' registrado y distribuido.';acuseBox(r);};
 if(f){if(f.size>1.9e6){alert('Máx 1.9 MB.');return;}var rd=new FileReader();rd.onload=function(){r.docs.push({nombre:f.name,tipo:f.type,data:rd.result,fecha:today(),por:PERFIL});r.timeline.push({ts:nowT(),usuario:PERFIL,accion:'Digitalización',modulo:'Recepción',obs:f.name});r.estatus='Digitalizado';fin();};rd.readAsDataURL(f);}else fin();}
function acuseBox(r){el('acuseBox').innerHTML='<div class="card"><h3>🧾 Acuse de recibo</h3>'+acuseHTML(r)+
  '<div style="margin-top:8px" class="acts"><button class="b1 mini" onclick="printAcuse(\''+r.id+'\')">🖨️ Imprimir / PDF</button><button class="bo mini" onclick="mailAcuse(\''+r.id+'\')">✉️ Enviar por correo</button><button class="bd mini" onclick="openRec(\''+r.id+'\')">📂 Abrir expediente</button></div></div>';}
function acuseHTML(r){return '<div class="acuse"><div class="q"><img src="'+(r.qr||'')+'" alt="QR"></div><div style="flex:1;font-size:12.5px;line-height:1.7">'+
  '<div style="font-weight:800;color:#00254a;font-size:14px">ACUSE DE RECIBO · Oficialía de Partes · UdeG</div>'+
  '<b>Folio:</b> '+ec(r.folio)+' &nbsp; <b>Sello:</b> '+ec(r.verif)+'<br>'+
  '<b>Fecha/hora:</b> '+ec(r.fecha)+' '+ec(r.hora)+'<br>'+
  '<b>Tipo:</b> '+ec(r.tipoDoc)+' &nbsp; <b>Asunto:</b> '+ec(r.asunto)+'<br>'+
  '<b>Presenta:</b> '+ec(r.presenta.nombre)+(r.presenta.dependencia?' ('+ec(r.presenta.dependencia)+')':'')+'<br>'+
  '<b>Recibe:</b> '+ec(r.recibe.nombre)+'<br>'+
  '<b>Turnado a:</b> '+ec(r.destino.coordinacion||'—')+(r.destino.unidad?' · '+ec(r.destino.unidad):'')+'<br>'+
  '<b>Anexos:</b> '+r.anexosNum+(r.anexosDesc?' — '+ec(r.anexosDesc):'')+'</div></div>'+
  '<div class="note" style="margin-top:8px">Documento con <b>sello digital</b> y <b>QR de verificación</b>. El acuse es inalterable; cualquier corrección se realiza por retorno o aclaración, nunca por eliminación (regla de negocio XVI).</div>';}
function printAcuse(id){var r=byId(id);if(!r)return;var w=window.open('','_blank');w.document.write('<html><head><title>Acuse '+ec(r.folio)+'</title><style>body{font-family:Segoe UI,system-ui,sans-serif;padding:24px;color:#0a1f3c}.acuse{border:2px dashed #0a4d8c;border-radius:12px;padding:16px;display:flex;gap:16px}img{width:130px;height:130px}.note{background:#eef6ff;border:1px solid #cfe0f5;border-radius:9px;padding:9px 12px;font-size:12px;margin-top:10px}</style></head><body>'+acuseHTML(r)+'<p style="font-size:11px;color:#64748b;margin-top:14px">Oficina de la Abogacía General · Universidad de Guadalajara · abogral@udg.mx</p></body></html>');w.document.close();w.focus();setTimeout(function(){w.print();},350);blog('Acción','Impresión de acuse '+r.folio);}
function mailAcuse(id){var r=byId(id);if(!r)return;var to=r.correoCopia||'';var s=encodeURIComponent('Acuse de recibo '+r.folio+' · Oficialía de Partes UdeG');var b=encodeURIComponent('ACUSE DE RECIBO · Oficialía de Partes · UdeG\n\nFolio: '+r.folio+'\nSello: '+r.verif+'\nFecha/hora: '+r.fecha+' '+r.hora+'\nTipo: '+r.tipoDoc+'\nAsunto: '+r.asunto+'\nPresenta: '+r.presenta.nombre+'\nRecibe: '+r.recibe.nombre+'\nTurnado a: '+(r.destino.coordinacion||'—')+'\nAnexos: '+r.anexosNum+'\n\nVerificable por QR/sello. Documento inalterable.');(r.timeline=r.timeline||[]).push({ts:nowT(),usuario:PERFIL,accion:'Acuse enviado por correo',modulo:'Recepción',obs:to});var A=REC();A.forEach(function(x){if(x.id===id)x.timeline=r.timeline;});saveREC(A);blog('Acción','Acuse '+r.folio+' enviado por correo');window.location.href='mailto:'+encodeURIComponent(to)+'?subject='+s+'&body='+b;}
/* OCR (X) — extracción por reglas (OCR de imagen real = backend) */
function ocrRec(){var t=prompt('Pega el texto del documento (escaneo/PDF). Se extraen datos por reglas y se llenan campos vacíos:','');if(t===null||!t.trim())return;
 function g(re){var m=t.match(re);return m?(m[1]||m[0]).trim():'';}
 var asu=g(/asunto\s*:?\s*([^\n\r]{4,140})/i);var num=g(/oficio\s*(?:n[uú]m(?:ero)?\.?)?\s*:?\s*([\w\/-]{2,20})/i);var dep=g(/(?:dependencia|procedencia|remitente)\s*:?\s*([^\n\r]{3,80})/i);var exp=g(/expediente\s*:?\s*([\w\/-]{2,25})/i);var corr=g(/[\w.+-]+@[\w-]+\.[\w.-]+/);
 if(asu&&!el('f_asu').value)el('f_asu').value=asu;
 if(dep&&!el('f_dep').value)el('f_dep').value=dep;
 if(exp&&!el('f_exp').value)el('f_exp').value=exp;
 if(corr&&!el('f_correo').value)el('f_correo').value=corr;
 if(/oficio/i.test(t)){el('f_tipo').value='Oficio';dinRender();if(num&&el('d_numofi'))el('d_numofi').value=num;}
 el('f_msg').style.color='#0a4d8c';el('f_msg').textContent='OCR: campos autollenados (revisa y completa).';}
/* ===== V TURNADO / VI RETORNO / VIII ESTATUS ===== */
function openRec(id){var r=byId(id);if(!r)return;el('drwc').innerHTML=drawer(r);el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
function drawer(r){var d=r.destino||{};
 var dinRows=Object.keys(r.din||{}).filter(function(k){return r.din[k];}).map(function(k){return '<b>'+ec(k)+':</b> '+ec(r.din[k]);}).join(' · ');
 var tls=(r.timeline||[]).map(function(e){return '<div class="ev '+(e.cls||'')+'"><b>'+ec(e.accion)+'</b> <span style="color:#94a3b8">'+ec(e.ts)+' · '+ec(e.usuario)+'</span>'+(e.obs?'<br><span style="color:#475569">'+ec(e.obs)+'</span>':'')+'</div>';}).join('');
 var turnos=(r.turnos||[]).map(function(x){var cls=x.accion==='Retorno'?'st r':(x.accion==='Reasignación'?'st y':'st b');return '<tr><td><span class="'+cls+'">'+ec(x.accion)+'</span></td><td style="font-size:11px">'+ec(x.ts)+'<br>'+ec(x.usuario)+'</td><td style="font-size:11px">'+ec((x.a&&(x.a.coordinacion||x.a.unidad||x.a.abogado||x.a.modulo||x.a.expediente))||'—')+'</td><td style="font-size:11px">'+ec(x.motivo||'')+'</td></tr>';}).join('');
 var acts='';var puede=['Secretaría General','Director','Coordinador General','Consulta'].indexOf(PERFIL)<0;
 if(puede)acts+='<button class="bo mini" onclick="turnarUI(\''+r.id+'\')">🎯 Turnar</button>';
 if(puedeRetornar())acts+=' <button class="br mini" onclick="retornarUI(\''+r.id+'\')">↩️ Retornar por error</button>';
 if(puede)acts+=' <button class="b1 mini" onclick="estatusUI(\''+r.id+'\')">🔁 Estatus</button> <button class="bd mini" onclick="docUp(\''+r.id+'\')">📎 Adjuntar</button>';
 acts+=' <button class="bd mini" onclick="printAcuse(\''+r.id+'\')">🧾 Acuse</button>';
 if(isAdmin())acts+=' <button class="br mini" onclick="cancelarUI(\''+r.id+'\')">🚫 Cancelar</button>';
 var ev=r.expedienteVinculado;
 var expBanner=ev?'<div class="note" style="background:#e7f7ee;border-color:#bfe6cf;color:#128c4a">🔗 <b>Expediente vinculado:</b> '+ec(ev.label||'Expediente')+' <b>'+ec(ev.folio)+'</b>'+(ev.link?' · <a href="'+ev.link+'" target="_blank" style="color:#0a5c53;font-weight:700">abrir módulo →</a>':'')+'</div>':'';
 var nots=(J('sigej_notificaciones')||[]).filter(function(x){return x.folio===r.folio;});
 var leidas=nots.filter(function(x){return x.leido;}).length;
 var distr='<div class="card"><h3>🔔 Distribución / notificaciones (XI) <button class="bo mini" style="float:right" onclick="distribuirManual(\''+r.id+'\')">✉️ Reenviar / correo</button></h3>'+(nots.length?'<div style="font-size:11px;color:#64748b;margin-bottom:4px">Lectura: <b>'+leidas+'/'+nots.length+'</b> destinatarios acusaron recibido en SIGEJ.</div><table><tr><th>Cuándo</th><th>Destinatario</th><th>Rol</th><th>Canal</th><th>Lectura</th></tr>'+nots.slice(-16).reverse().map(function(x){return '<tr><td style="font-size:11px">'+ec(x.ts)+'</td><td>'+ec(x.para)+'</td><td style="font-size:11px">'+ec(x.rol)+'</td><td><span class="bdg">'+ec(x.canal)+'</span></td><td style="font-size:11px">'+(x.leido?'<span class="st v">✓ leída</span> '+ec(x.leidoPor||'')+(x.leidoTs?' · '+ec(x.leidoTs):''):'<span class="st y">pendiente</span>')+'</td></tr>';}).join('')+'</table>':'<div style="color:#94a3b8;font-size:12px">Sin notificaciones registradas.</div>')+'<div class="note" style="margin-top:6px">Canal <b>SIGEJ</b> (bandeja de Notificaciones) con <b>acuse de lectura por destinatario</b>. <b>Correo</b> por enlace mailto. <b>Teams / app móvil</b> = fase backend.</div></div>';
 return '<h2 style="margin:0 0 2px;color:#00254a;font-size:17px">'+ec(r.folio)+' <span class="st '+stColor(r.estatus)+'">'+ec(r.estatus)+'</span></h2>'+
  '<div style="color:#64748b;font-size:12px;margin-bottom:10px">'+ec(r.tipoDoc)+' · <span class="u-'+ec(r.urgencia)+'">'+ec(r.urgencia)+'</span> · '+ec(r.confidencialidad)+'</div>'+
  '<div class="card"><b>Asunto:</b> '+ec(r.asunto)+'<br><b>Recepción:</b> '+ec(r.fecha)+' '+ec(r.hora)+' · '+ec(r.medioRecepcion)+'<br><b>Suscribe:</b> '+ec(r.suscribe.nombre||'—')+(r.suscribe.cargo?' ('+ec(r.suscribe.cargo)+')':'')+'<br><b>Presenta:</b> '+ec(r.presenta.nombre)+(r.presenta.dependencia?' · '+ec(r.presenta.dependencia):'')+'<br><b>Recibe:</b> '+ec(r.recibe.nombre)+'<br><b>Destino:</b> '+ec(d.coordinacion||'—')+(d.unidad?' · '+ec(d.unidad):'')+(d.abogado?' · Abg. '+ec(d.abogado):'')+'<br><b>Expediente:</b> '+ec(r.expedienteRel||'—')+'<br><b>Anexos:</b> '+r.anexosNum+(r.anexosDesc?' — '+ec(r.anexosDesc):'')+(dinRows?'<br><b>Específicos:</b> '+dinRows:'')+(r.observaciones?'<br><b>Obs.:</b> '+ec(r.observaciones):'')+'</div>'+expBanner+
  '<div class="acts" style="margin-bottom:10px">'+acts+'</div>'+
  (r.cancelado?'<div class="warn">🚫 <b>Cancelado</b> por '+ec(r.cancelado.por)+' · '+ec(r.cancelado.ts)+' — '+ec(r.cancelado.motivo)+'</div>':'')+
  (turnos?'<div class="card"><h3>🎯 Turnos y retornos (inalterable)</h3><table><tr><th>Acción</th><th>Cuándo/Quién</th><th>Destino</th><th>Motivo</th></tr>'+turnos+'</table></div>':'')+
  distr+
  '<div class="card"><h3>🧾 Línea de tiempo (VII)</h3><div class="tl">'+(tls||'<div class="ev">Sin eventos.</div>')+'</div></div>'+
  (r.docs&&r.docs.length?'<div class="card"><h3>📎 Documentos digitalizados</h3>'+r.docs.map(function(x){return '<a href="'+x.data+'" download="'+ec(x.nombre)+'" style="color:#0a4d8c">📄 '+ec(x.nombre)+'</a>';}).join('<br>')+'</div>':'');}
function reAbrir(id){openRec(id);}
function turnarUI(id){var r=byId(id);if(!r)return;
 var h='<h3 style="color:#00254a">🎯 Turnar '+ec(r.folio)+'</h3>'+
  '<label class="lb">Coordinación</label><select id="t_coord">'+opt([''].concat(COORDS),r.destino.coordinacion)+'</select>'+
  '<label class="lb">Unidad / área</label><select id="t_uni">'+opt([''].concat(UNIDADES),r.destino.unidad)+'</select>'+
  '<label class="lb">Abogado específico</label><input id="t_abg" value="'+ec(r.destino.abogado||'')+'">'+
  '<label class="lb">Módulo del SIGEJ</label><select id="t_mod">'+opt([''].concat(MODULOS))+'</select>'+
  '<label class="lb">Expediente (existente o nuevo)</label><input id="t_exp" placeholder="Folio de expediente">'+
  '<label class="lb">Prioridad</label><select id="t_prio">'+opt(URGENCIA)+'</select>'+
  '<label class="lb">Plazo interno (días)</label><input id="t_plazo" type="number" min="0" value="5">'+
  '<label class="lb">Motivo del turno</label><textarea id="t_mot"></textarea>'+
  '<div style="margin-top:8px"><button class="bo" onclick="turnarDo(\''+id+'\')">Confirmar turno</button> <button class="bd" onclick="openRec(\''+id+'\')">Cancelar</button></div>';
 el('drwc').innerHTML=h;}
function turnarDo(id){var A=REC();var r=A.filter(function(x){return x.id===id;})[0];if(!r)return;
 var a={coordinacion:el('t_coord').value,unidad:el('t_uni').value,area:el('t_uni').value,abogado:el('t_abg').value.trim(),modulo:el('t_mod').value,expediente:el('t_exp').value.trim()};
 if(!a.coordinacion&&!a.unidad&&!a.modulo&&!a.abogado){alert('Indica al menos un destino.');return;}
 var turno={ts:nowT(),usuario:PERFIL,accion:'Turnado',de:r.destino,a:a,motivo:el('t_mot').value.trim(),prioridad:el('t_prio').value,plazo:+el('t_plazo').value||0};
 r.turnos.push(turno);
 r.destino={coordinacion:a.coordinacion,unidad:a.unidad,area:a.area,abogado:a.abogado};r.estatus='Turnado';
 tl(r,'Turnado',(a.coordinacion||a.unidad||a.modulo||a.abogado)+(el('t_mot').value?' — '+el('t_mot').value:''),'tur');
 /* Vinculación: crear expediente real en el módulo destino (o vinculado si ya existe) */
 var creado=null;
 if(a.modulo){creado=crearDestino(a.modulo,r,a);if(creado){turno.expedienteCreado=creado.folio;turno.expedienteLink=creado.link;r.expedienteVinculado={folio:creado.folio,modulo:a.modulo,link:creado.link,label:creado.label};tl(r,'Expediente creado','('+creado.label+') '+creado.folio+' en '+a.modulo);blog('Acción','Recepción '+r.folio+' → crea '+creado.folio+' en '+a.modulo);}}
 else if(a.expediente){r.expedienteVinculado={folio:a.expediente,modulo:'',link:'',label:'Expediente existente'};tl(r,'Vinculación a expediente','Expediente existente '+a.expediente);}
 /* Distribución/notificación automática (XI) */
 distribuir(r,'Turnado');
 saveREC(A);blog('Acción','Turno '+r.folio+' → '+(a.coordinacion||a.unidad||a.modulo)+(creado?' · exp '+creado.folio:''));openRec(id);}
function retornarUI(id){if(!puedeRetornar()){alert('Solo Administrador, Help Desk, Director/Coordinador autorizado o Responsable de Oficialía pueden retornar.');return;}
 var r=byId(id);if(!r)return;var ultimo=(r.turnos||[]).slice(-1)[0]||{};
 var h='<h3 style="color:#c0392b">↩️ Retorno por error de canalización · '+ec(r.folio)+'</h3>'+
  '<div class="warn">El turno incorrecto <b>no se elimina</b>: se conserva como antecedente en la línea de tiempo (regla VI/XVI).</div>'+
  '<div class="card" style="font-size:12px"><b>Ingreso original:</b> '+ec(r.fecha)+' '+ec(r.hora)+'<br><b>Primer turno:</b> '+ec((r.turnos[0]&&r.turnos[0].ts)||'—')+'<br><b>Área/abogado actual:</b> '+ec(r.destino.coordinacion||'—')+' · '+ec(r.destino.unidad||'—')+' · '+ec(r.destino.abogado||'—')+'</div>'+
  '<label class="lb">Motivo del retorno <span class="req">*</span></label><textarea id="r_mot" placeholder="Por qué fue mal canalizado"></textarea>'+
  '<label class="lb">Nueva coordinación asignada</label><select id="r_coord">'+opt([''].concat(COORDS))+'</select>'+
  '<label class="lb">Nueva unidad / área</label><select id="r_uni">'+opt([''].concat(UNIDADES))+'</select>'+
  '<label class="lb">Nuevo abogado (si procede)</label><input id="r_abg">'+
  '<label class="lb">Destino del retorno</label><select id="r_dest"><option>Oficialía de Partes</option><option>Otra Coordinación</option><option>Otra Unidad</option><option>Otra Área</option><option>Otro abogado</option><option>Otro módulo</option></select>'+
  '<label class="lb">Observaciones</label><input id="r_obs">'+
  '<div style="margin-top:8px"><button class="br" onclick="retornarDo(\''+id+'\')">Confirmar retorno</button> <button class="bd" onclick="openRec(\''+id+'\')">Cancelar</button></div>';
 el('drwc').innerHTML=h;}
function retornarDo(id){var A=REC();var r=A.filter(function(x){return x.id===id;})[0];if(!r)return;
 var mot=(el('r_mot').value||'').trim();if(!mot){alert('El motivo del retorno es obligatorio (regla XVI.3).');return;}
 var destTipo=el('r_dest').value;var a={coordinacion:el('r_coord').value,unidad:el('r_uni').value,area:el('r_uni').value,abogado:el('r_abg').value.trim()};
 r.turnos.push({ts:nowT(),usuario:PERFIL,accion:'Retorno',de:r.destino,a:a,motivo:mot,destinoTipo:destTipo,obs:(el('r_obs').value||'').trim(),
   ingresoOriginal:r.fecha+' '+r.hora,primerTurno:(r.turnos[0]&&r.turnos[0].ts)||'',areaInicial:(r.turnos[0]&&r.turnos[0].a&&r.turnos[0].a.coordinacion)||r.destino.coordinacion,abogadoInicial:(r.turnos[0]&&r.turnos[0].a&&r.turnos[0].a.abogado)||r.destino.abogado});
 r.estatus=(destTipo==='Oficialía de Partes')?'Retornado a Oficialía':'Devuelto por error de turnado';
 if(a.coordinacion||a.unidad||a.abogado)r.destino={coordinacion:a.coordinacion,unidad:a.unidad,area:a.area,abogado:a.abogado};
 tl(r,'Retorno por error','→ '+destTipo+' — '+mot,'ret');
 saveREC(A);blog('Acción','Retorno '+r.folio+' — '+mot);openRec(id);}
function distribuirManual(id){var A=REC();var r=A.filter(function(x){return x.id===id;})[0];if(!r)return;var n=distribuir(r,'Redistribución');saveREC(A);blog('Acción','Redistribución '+r.folio);
 var d=r.destino||{};var to=r.correoCopia||'';var s=encodeURIComponent('Turnado '+r.folio+' · '+r.tipoDoc+' · Oficialía de Partes UdeG');var b=encodeURIComponent('Se turna el documento '+r.folio+' ('+r.tipoDoc+')\nAsunto: '+r.asunto+'\nÁrea receptora: '+(d.coordinacion||'—')+(d.unidad?' · '+d.unidad:'')+(d.abogado?'\nAbogado asignado: '+d.abogado:'')+(r.expedienteVinculado?'\nExpediente vinculado: '+r.expedienteVinculado.folio:'')+'\n\nOficina de la Abogacía General · UdeG · abogral@udg.mx');
 alert('🔔 Notificado a '+n+' destinatario(s) por SIGEJ. Se abrirá el correo para el envío externo (correo/Teams reales = backend).');window.location.href='mailto:'+encodeURIComponent(to)+'?subject='+s+'&body='+b;openRec(id);}
function estatusUI(id){var r=byId(id);if(!r)return;var h='<h3 style="color:#00254a">🔁 Cambiar estatus · '+ec(r.folio)+'</h3><label class="lb">Nuevo estatus</label><select id="s_new">'+opt(ESTATUS,r.estatus)+'</select><label class="lb">Observación</label><input id="s_obs"><div style="margin-top:8px"><button class="b1" onclick="estatusDo(\''+id+'\')">Aplicar</button> <button class="bd" onclick="openRec(\''+id+'\')">Cancelar</button></div>';el('drwc').innerHTML=h;}
function estatusDo(id){var A=REC();var r=A.filter(function(x){return x.id===id;})[0];if(!r)return;var ns=el('s_new').value;r.estatus=ns;tl(r,'Cambio de estatus → '+ns,(el('s_obs').value||'').trim());saveREC(A);blog('Acción',r.folio+' estatus → '+ns);openRec(id);}
function docUp(id){var inp=document.createElement('input');inp.type='file';inp.onchange=function(){var f=inp.files[0];if(!f)return;if(f.size>1.9e6){alert('Máx 1.9 MB.');return;}var rd=new FileReader();rd.onload=function(){var A=REC();var r=A.filter(function(x){return x.id===id;})[0];(r.docs=r.docs||[]).push({nombre:f.name,tipo:f.type,data:rd.result,fecha:today(),por:PERFIL});tl(r,'Carga de anexo',f.name);if(r.estatus==='Recibido')r.estatus='Digitalizado';saveREC(A);blog('Acción','Anexo en '+r.folio);openRec(id);};rd.readAsDataURL(f);};inp.click();}
function cancelarUI(id){if(!isAdmin())return;var m=prompt('Motivo de cancelación (no se elimina, queda cancelado y en bitácora):','');if(m===null||!m.trim())return;var A=REC();var r=A.filter(function(x){return x.id===id;})[0];r.cancelado={motivo:m.trim(),por:PERFIL,ts:nowT()};r.estatus='Cancelado';tl(r,'Cancelación',m.trim(),'ret');saveREC(A);blog('Acción','Cancela '+r.folio);openRec(id);}
/* ===== XIII BANDEJA + BÚSQUEDA + FILTROS ===== */
function bandeja(){var A=REC();
 el('pane').innerHTML='<div class="card filtros"><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">'+
  '<div><label class="lb">Buscar (folio, asunto, persona, OCR…)</label><input id="q" oninput="bandList()" placeholder="palabra clave"></div>'+
  '<div><label class="lb">Tipo</label><select id="fq_tipo" onchange="bandList()"><option value="">Todos</option>'+opt(tipos())+'</select></div>'+
  '<div><label class="lb">Estatus</label><select id="fq_est" onchange="bandList()"><option value="">Todos</option>'+opt(ESTATUS)+'</select></div>'+
  '<div><label class="lb">Coordinación</label><select id="fq_coord" onchange="bandList()"><option value="">Todas</option>'+opt(COORDS)+'</select></div>'+
  '<div><label class="lb">Prioridad</label><select id="fq_prio" onchange="bandList()"><option value="">Todas</option>'+opt(URGENCIA)+'</select></div>'+
  '<div><label class="lb">Especiales</label><select id="fq_flag" onchange="bandList()"><option value="">—</option><option value="ret">Retornados</option><option value="sinturno">Sin turnar</option><option value="urg">Urgentes sin atender</option></select></div>'+
  '<div style="display:flex;align-items:end;gap:6px"><button class="b1 mini" onclick="expCSV()">⬇️ CSV</button></div>'+
  '</div></div><div class="card" style="overflow:auto"><table><thead><tr><th>Folio</th><th>Fecha/hora</th><th>Tipo</th><th>Asunto</th><th>Presenta</th><th>Destino</th><th>Prioridad</th><th>Estatus</th></tr></thead><tbody id="bt"></tbody></table><div id="bcap" style="font-size:11px;color:#64748b;padding:6px"></div></div>';
 bandList();}
function bandFilter(){var A=REC();var q=norm((el('q')||{}).value||''),ft=(el('fq_tipo')||{}).value||'',fe=(el('fq_est')||{}).value||'',fc=(el('fq_coord')||{}).value||'',fp=(el('fq_prio')||{}).value||'',ff=(el('fq_flag')||{}).value||'';
 return A.filter(function(r){
   if(ft&&r.tipoDoc!==ft)return false;if(fe&&r.estatus!==fe)return false;if(fc&&r.destino.coordinacion!==fc)return false;if(fp&&r.urgencia!==fp)return false;
   if(ff==='ret'&&!(r.turnos||[]).some(function(x){return x.accion==='Retorno';}))return false;
   if(ff==='sinturno'&&(r.turnos||[]).some(function(x){return x.accion==='Turnado';}))return false;
   if(ff==='urg'&&!(r.urgencia==='Urgente'&&['Atendido','Concluido','Archivado'].indexOf(r.estatus)<0))return false;
   if(q){var blob=norm(r.folio+' '+r.asunto+' '+r.tipoDoc+' '+r.presenta.nombre+' '+(r.suscribe.nombre||'')+' '+r.recibe.nombre+' '+(r.destino.coordinacion||'')+' '+(r.destino.abogado||'')+' '+(r.expedienteRel||'')+' '+JSON.stringify(r.din||{}));if(blob.indexOf(q)<0)return false;}
   return true;}).sort(function(a,b){return (b.fechaCaptura||'').localeCompare(a.fechaCaptura||'');});}
function bandList(){var rows=bandFilter();
 el('bt').innerHTML=rows.length?rows.slice(0,300).map(function(r){var ret=(r.turnos||[]).some(function(x){return x.accion==='Retorno';});return '<tr class="rowc" onclick="openRec(\''+r.id+'\')"><td><b>'+ec(r.folio)+'</b>'+(ret?' <span class="st r">↩︎</span>':'')+'</td><td style="white-space:nowrap;font-size:11px">'+ec(r.fecha)+'<br>'+ec(r.hora)+'</td><td style="font-size:11.5px">'+ec(r.tipoDoc)+'</td><td>'+ec(r.asunto).slice(0,60)+'</td><td style="font-size:11.5px">'+ec(r.presenta.nombre)+'</td><td style="font-size:11px">'+ec(r.destino.coordinacion||'—')+(r.destino.abogado?'<br>Abg. '+ec(r.destino.abogado):'')+'</td><td><span class="u-'+ec(r.urgencia)+'">'+ec(r.urgencia)+'</span></td><td><span class="st '+stColor(r.estatus)+'">'+ec(r.estatus)+'</span></td></tr>';}).join(''):'<tr><td colspan="8" style="text-align:center;color:#64748b;padding:16px">Sin documentos con estos filtros.</td></tr>';
 el('bcap').textContent=rows.length+' documento(s)'+(rows.length>300?' (mostrando 300)':'')+'.';}
function expCSV(){var rows=bandFilter();var out=[['Folio','Fecha','Hora','Tipo','Asunto','Presenta','Dependencia','Recibe','Coordinacion','Abogado','Prioridad','Confidencialidad','Estatus','Anexos','Retornado']].concat(rows.map(function(r){return [r.folio,r.fecha,r.hora,r.tipoDoc,r.asunto,r.presenta.nombre,r.presenta.dependencia,r.recibe.nombre,r.destino.coordinacion,r.destino.abogado,r.urgencia,r.confidencialidad,r.estatus,r.anexosNum,(r.turnos||[]).some(function(x){return x.accion==='Retorno';})?'Sí':'No'];}));var csv=out.map(function(rr){return rr.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='recepcion_'+today()+'.csv';a.click();}
/* ===== XIV DASHBOARD ===== */
function dashboard(){var A=REC();var hoyD=today();
 var hoyN=A.filter(function(r){return r.fecha===hoyD;}).length;
 var ret=A.filter(function(r){return (r.turnos||[]).some(function(x){return x.accion==='Retorno';});}).length;
 var sinturno=A.filter(function(r){return !(r.turnos||[]).some(function(x){return x.accion==='Turnado';})&&['Cancelado','Archivado'].indexOf(r.estatus)<0;}).length;
 var urg=A.filter(function(r){return r.urgencia==='Urgente'&&['Atendido','Concluido','Archivado'].indexOf(r.estatus)<0;}).length;
 var pend=A.filter(function(r){return r.estatus==='Pendiente de clasificación'||r.estatus==='Recibido';}).length;
 var porTipo={},porArea={},porAbg={};A.forEach(function(r){porTipo[r.tipoDoc]=(porTipo[r.tipoDoc]||0)+1;var c=r.destino.coordinacion||'(sin asignar)';porArea[c]=(porArea[c]||0)+1;if(r.destino.abogado)porAbg[r.destino.abogado]=(porAbg[r.destino.abogado]||0)+1;});
 var tturno=[],tret=[];A.forEach(function(r){var rc=new Date((r.fechaCaptura||'').replace(' ','T'));var t1=(r.turnos||[]).filter(function(x){return x.accion==='Turnado';})[0];if(t1){var d=(new Date(t1.ts.replace(' ','T'))-rc)/36e5;if(d>=0)tturno.push(d);}var rr=(r.turnos||[]).filter(function(x){return x.accion==='Retorno';})[0];if(rr){var d2=(new Date(rr.ts.replace(' ','T'))-rc)/36e5;if(d2>=0)tret.push(d2);}});
 function avg(a){return a.length?(a.reduce(function(x,y){return x+y;},0)/a.length).toFixed(1):'—';}
 el('pane').innerHTML='<div class="kpis">'+
  '<div class="kpi"><div class="n">'+hoyN+'</div><div class="l">Recibidos hoy</div></div>'+
  '<div class="kpi"><div class="n">'+A.length+'</div><div class="l">Total histórico</div></div>'+
  '<div class="kpi '+(sinturno?'y':'')+'"><div class="n">'+sinturno+'</div><div class="l">Pendientes de turnar</div></div>'+
  '<div class="kpi '+(ret?'r':'')+'"><div class="n">'+ret+'</div><div class="l">Documentos retornados</div></div>'+
  '<div class="kpi '+(urg?'r':'')+'"><div class="n">'+urg+'</div><div class="l">Urgentes sin atender</div></div>'+
  '<div class="kpi"><div class="n">'+pend+'</div><div class="l">Pendientes de clasificación</div></div>'+
  '<div class="kpi"><div class="n">'+avg(tturno)+' h</div><div class="l">Tiempo prom. de turnado</div></div>'+
  '<div class="kpi"><div class="n">'+avg(tret)+' h</div><div class="l">Prom. recepción→retorno</div></div>'+
 '</div>'+
 '<div class="grid" style="grid-template-columns:1fr 1fr">'+dashTable('Documentos por tipo',porTipo)+dashTable('Documentos por área destinataria',porArea)+'</div>'+
 dashTable('Carga por abogado',porAbg);}
function dashTable(t,o){var k=Object.keys(o).sort(function(a,b){return o[b]-o[a];});return '<div class="card"><h3>'+ec(t)+'</h3>'+(k.length?'<table>'+k.slice(0,12).map(function(x){return '<tr><td>'+ec(x)+'</td><td style="text-align:right"><b>'+o[x]+'</b></td></tr>';}).join('')+'</table>':'<div style="color:#94a3b8;font-size:12px">Sin datos.</div>')+'</div>';}
/* ===== TABLERO DE RETORNOS (auditoría de canalización errónea recurrente) ===== */
function retornosData(){var A=REC();var RET=[];A.forEach(function(r){(r.turnos||[]).forEach(function(t){if(t.accion==='Retorno')RET.push({folio:r.folio,id:r.id,ts:t.ts,usuario:t.usuario||'—',tipoDoc:r.tipoDoc,areaInicial:t.areaInicial||(t.de&&t.de.coordinacion)||'—',abogadoInicial:t.abogadoInicial||(t.de&&t.de.abogado)||'—',nuevaArea:(t.a&&(t.a.coordinacion||t.a.unidad||t.a.abogado))||'—',motivo:t.motivo||'—'});});});RET.sort(function(a,b){return (b.ts||'').localeCompare(a.ts||'');});return RET;}
function dashTableRec(t,o){var k=Object.keys(o).sort(function(a,b){return o[b]-o[a];});return '<div class="card"><h3>'+ec(t)+'</h3>'+(k.length?'<table>'+k.slice(0,12).map(function(x){var rec=o[x]>=2;return '<tr><td>'+ec(x)+(rec?' <span class="st y">recurrente</span>':'')+'</td><td style="text-align:right"><b>'+o[x]+'</b></td></tr>';}).join('')+'</table>':'<div style="color:#94a3b8;font-size:12px">Sin datos.</div>')+'</div>';}
function retornos(){var A=REC();var RET=retornosData();
 var docsConRet=A.filter(function(r){return (r.turnos||[]).some(function(t){return t.accion==='Retorno';});}).length;
 var tasa=A.length?Math.round(docsConRet/A.length*100):0;
 function agg(key){var o={};RET.forEach(function(x){var k=x[key]||'—';o[k]=(o[k]||0)+1;});return o;}
 var porArea=agg('areaInicial'),porAbg=agg('abogadoInicial'),porMotivo=agg('motivo');
 var recArea=Object.keys(porArea).filter(function(k){return porArea[k]>=2&&k!=='—';});
 el('pane').innerHTML='<div class="note">↩️ Auditoría de <b>canalización errónea</b>: todo retorno conserva el turno incorrecto como antecedente (regla VI/XVI.4). Este tablero detecta patrones recurrentes por área y abogado para corregir criterios de turnado.</div>'+
  '<div class="kpis">'+
  '<div class="kpi r"><div class="n">'+RET.length+'</div><div class="l">Retornos totales</div></div>'+
  '<div class="kpi"><div class="n">'+docsConRet+'</div><div class="l">Documentos retornados</div></div>'+
  '<div class="kpi '+(tasa>15?'r':(tasa>5?'y':''))+'"><div class="n">'+tasa+'%</div><div class="l">Tasa de retorno</div></div>'+
  '<div class="kpi '+(recArea.length?'y':'')+'"><div class="n">'+recArea.length+'</div><div class="l">Áreas con retorno recurrente</div></div>'+
  '</div>'+
  (recArea.length?'<div class="warn">⚠️ Canalización errónea <b>recurrente</b> hacia: <b>'+recArea.map(ec).join('</b>, <b>')+'</b>. Revisar criterios de turnado y/o capacitación del área receptora.</div>':'')+
  '<div class="grid" style="grid-template-columns:1fr 1fr">'+dashTableRec('Retornos por área inicial (mal canalizada)',porArea)+dashTableRec('Retornos por abogado inicial',porAbg)+'</div>'+
  dashTableRec('Motivos de retorno más frecuentes',porMotivo)+
  '<div class="card" style="overflow:auto"><h3>Detalle de retornos <button class="b1 mini" style="float:right" onclick="expRetCSV()">⬇️ CSV</button></h3><table><thead><tr><th>Folio</th><th>Cuándo</th><th>Quién detecta</th><th>Área inicial</th><th>Reasignado a</th><th>Motivo</th></tr></thead><tbody>'+(RET.length?RET.slice(0,200).map(function(x){return '<tr class="rowc" onclick="openRec(\''+x.id+'\')"><td><b>'+ec(x.folio)+'</b></td><td style="font-size:11px">'+ec(x.ts)+'</td><td style="font-size:11px">'+ec(x.usuario)+'</td><td style="font-size:11px">'+ec(x.areaInicial)+(x.abogadoInicial&&x.abogadoInicial!=='—'?'<br>Abg. '+ec(x.abogadoInicial):'')+'</td><td style="font-size:11px">'+ec(x.nuevaArea)+'</td><td>'+ec(x.motivo)+'</td></tr>';}).join(''):'<tr><td colspan="6" style="text-align:center;color:#128c4a;padding:16px">Sin retornos registrados ✓</td></tr>')+'</tbody></table></div>';}
function expRetCSV(){var RET=retornosData();var out=[['Folio','Cuando','QuienDetecta','Tipo','AreaInicial','AbogadoInicial','ReasignadoA','Motivo']].concat(RET.map(function(x){return [x.folio,x.ts,x.usuario,x.tipoDoc,x.areaInicial,x.abogadoInicial,x.nuevaArea,x.motivo];}));var csv=out.map(function(rr){return rr.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='retornos_'+today()+'.csv';a.click();}
/* ===== XV MATRIZ DE RIESGOS ===== */
function riesgos(){var A=REC();
 var R=[
  ['Documentos no turnados',A.filter(function(r){return !(r.turnos||[]).some(function(x){return x.accion==='Turnado';})&&['Cancelado','Archivado'].indexOf(r.estatus)<0;})],
  ['Documentos urgentes sin atención',A.filter(function(r){return r.urgencia==='Urgente'&&['Atendido','Concluido','Archivado'].indexOf(r.estatus)<0;})],
  ['Expedientes sin abogado asignado',A.filter(function(r){return !r.destino.abogado&&['Cancelado','Archivado'].indexOf(r.estatus)<0;})],
  ['Documentos sin acuse impreso/enviado',A.filter(function(r){return !(r.timeline||[]).some(function(x){return /Acuse/.test(x.accion);});})],
  ['Turnos erróneos (con retorno)',A.filter(function(r){return (r.turnos||[]).some(function(x){return x.accion==='Retorno';});})],
  ['Posibles duplicados (mismo asunto+dependencia)',dupes(A)]
 ];
 el('pane').innerHTML='<div class="note">Matriz de detección temprana (XV). El riesgo de vencimiento de plazo se consolida en el <a href="alertas_centro_SIGEJ.html" style="color:#0a4d8c">Centro de Alertas</a>.</div>'+R.map(function(x){var arr=x[1];var col=arr.length?(x[0].indexOf('urgentes')>=0||x[0].indexOf('no turnados')>=0?'r':'y'):'g';return '<div class="card"><h3>'+ec(x[0])+' <span class="st '+col+'">'+arr.length+'</span></h3>'+(arr.length?'<table><tr><th>Folio</th><th>Asunto</th><th>Estatus</th></tr>'+arr.slice(0,10).map(function(r){return '<tr class="rowc" onclick="openRec(\''+r.id+'\')"><td>'+ec(r.folio)+'</td><td>'+ec(r.asunto).slice(0,50)+'</td><td><span class="st '+stColor(r.estatus)+'">'+ec(r.estatus)+'</span></td></tr>';}).join('')+'</table>'+(arr.length>10?'<div style="font-size:11px;color:#94a3b8;padding:4px">'+arr.length+' en total</div>':''):'<div style="color:#128c4a;font-size:12px">Sin hallazgos ✓</div>')+'</div>';}).join('');}
function dupes(A){var seen={},out=[];A.forEach(function(r){var k=norm(r.asunto+'|'+r.presenta.dependencia);if(seen[k])out.push(r);else seen[k]=1;});return out;}
/* ===== II/CATÁLOGO editable (Admin/HD) ===== */
function catalogo(){var t=tipos();var adm=isAdmin();
 el('pane').innerHTML='<div class="card"><h3>⚙️ Catálogo de tipos de documento</h3><div class="note">'+(adm?'Como <b>Administrador / Help Desk</b> puedes agregar o retirar tipos. Los tipos en uso no se eliminan del historial.':'Solo el <b>Administrador General o Help Desk autorizado</b> puede editar este catálogo.')+'</div>'+
  '<div style="display:flex;flex-wrap:wrap;gap:6px;margin:8px 0">'+t.map(function(x,i){return '<span class="bdg" style="padding:5px 10px">'+ec(x)+(adm?' <span style="cursor:pointer;color:#c0392b" onclick="delTipo('+i+')">✕</span>':'')+'</span>';}).join('')+'</div>'+
  (adm?'<div style="display:flex;gap:6px;max-width:420px"><input id="nt" placeholder="Nuevo tipo de documento"><button class="bg" onclick="addTipo()">＋ Agregar</button></div>':'')+'</div>';}
function addTipo(){if(!isAdmin())return;var v=(el('nt').value||'').trim();if(!v)return;var t=tipos();if(t.indexOf(v)<0){t.push(v);S('sigej_tipos_doc',t);blog('Acción','Alta tipo de documento: '+v);}catalogo();}
function delTipo(i){if(!isAdmin())return;var t=tipos();var v=t[i];if(!confirm('¿Retirar «'+v+'» del catálogo? (no afecta documentos ya registrados)'))return;t.splice(i,1);S('sigej_tipos_doc',t);blog('Acción','Retira tipo de documento: '+v);catalogo();}
/* init */
drawTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{background:#fff!important}.wrap{padding-top:6px!important}";document.head.appendChild(st);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"recepcion_SIGEJ.html","w",encoding="utf-8").write(out)
print("recepcion_SIGEJ.html OK -",len(out),"bytes | tipos:",out.count("Demanda inicial"),"| tabs:",out.count("['t"))
