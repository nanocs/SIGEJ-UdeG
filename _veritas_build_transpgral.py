# -*- coding: utf-8 -*-
# Transparencia General — buscador global institucional sobre TODOS los módulos/áreas + estadísticas, matrices y reportes.
import json
B="/Users/edithroque/Documents/CLAUDE/"
co=json.load(open(B+"comando_data.json",encoding="utf-8"))
DATA={"corte":co.get("corte","2026-06-18"),"exp":co["exp"]}
DATAJ=json.dumps(DATA,ensure_ascii=False)

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html" class="act">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''

SNIP=r"""<script>
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
 }
 if(!perfil){if(!/[?&]embed=1/.test(location.search)){location.replace('acceso_SIGEJ.html');}return;}else{apply();badge();if(['Abogado General','Sistemas','Secretaría General','Director','Coordinador General'].indexOf(perfil)>=0){setTimeout(function(){document.querySelectorAll('button,.lk,.del').forEach(function(b){var t=(b.textContent||'')+(b.title||'');if(/guardar|registrar|crear|captur|recibir|turnar|elimina|borrar|baja|adjuntar|generar|autoriz|pagar|aplicar|asignar|cargar demo|resolver|escalar|aprobar|publicar|solicitar|despach|＋/i.test(t)){b.disabled=true;b.style.opacity=.45;b.title='Perfil de solo lectura / consulta';}});},450);}}
})();
</script><script>
/* SIGEJ — Bitácora de auditoría (registro de interfaz, sin backend) */
(function(){try{
 var perfil=localStorage.getItem('sigej_perfil')||'(sin perfil)';
 function blog(tipo,accion){try{var L=JSON.parse(localStorage.getItem('sigej_bitacora')||'[]');L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:perfil,modulo:'Transparencia General',tipo:tipo,accion:String(accion||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);localStorage.setItem('sigej_bitacora',JSON.stringify(L));}catch(e){}}
 window.__bitlog=blog;blog('Acceso','Ingreso al módulo');
 var RX=/exportar|word|csv|descargar|reporte/i;
 document.addEventListener('click',function(ev){try{var el=ev.target&&ev.target.closest&&ev.target.closest('button');if(!el)return;var txt=(el.textContent||'').trim();if(RX.test(txt)&&txt.length<70)blog('Acción',txt);}catch(e){}},true);
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
})();</script><script>
/* OCR universal por reglas · rellena formularios de captura desde texto pegado (SIGEJ). El OCR de imagen es fase backend. */
(function(){try{
if(/[?&]embed=1/.test(location.search))return;
var pk=(location.pathname.split('/').pop()||'x').replace('.html','')||'x';
if(/^(index|acceso_SIGEJ|seguimiento_SIGEJ)$/.test(pk))return;
if(!document.body)return;
function hasForm(){return document.querySelector('input[type=date]')||document.querySelectorAll('.f').length>2||document.querySelector('textarea');}
var b=document.createElement('div');b.textContent='🔎 OCR';
b.style.cssText='position:fixed;left:16px;bottom:16px;background:#7a5a1f;color:#fff;padding:9px 14px;border-radius:22px;font:600 12.5px system-ui,sans-serif;cursor:pointer;z-index:99996;box-shadow:0 4px 14px rgba(0,0,0,.25)';
document.body.appendChild(b);
function upd(){b.style.display=hasForm()?'block':'none';}upd();setTimeout(upd,1200);
b.onclick=function(){
 var t=prompt('Pega el TEXTO del documento escaneado/PDF. Se extraen datos por reglas (folio, fecha, monto, correo, teléfono, CURP/RFC, asunto…) y se llenan los campos vacíos del formulario. (El OCR de imagen real es fase backend.)','');
 if(t===null||!t.trim())return;
 var folio=(t.match(/\b\d{1,6}\s*\/\s*\d{2,4}(?:-[A-Za-z]+)?\b/)||[''])[0].replace(/\s/g,'');
 var fecha=(t.match(/\b\d{4}-\d{2}-\d{2}\b/)||[''])[0];
 if(!fecha){var md=t.match(/\b(\d{1,2})\/(\d{1,2})\/(\d{4})\b/);if(md)fecha=md[3]+'-'+('0'+md[2]).slice(-2)+'-'+('0'+md[1]).slice(-2);}
 var monto=((t.match(/\$\s?[\d,]+(?:\.\d{2})?/)||[''])[0]||'').replace(/[^\d.]/g,'');
 var correo=(t.match(/[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}/)||[''])[0];
 var tel=(t.match(/\b(?:\+?52[\s-]?)?(?:\(?\d{2,3}\)?[\s-]?)?\d{3}[\s-]?\d{4}\b/)||[''])[0];
 var curp=(t.match(/\b[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]{2}\b/i)||[''])[0];
 var rfc=(t.match(/\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b/i)||[''])[0];
 var STOPKW='asunto|objeto|nombre|contacto|firmante|responsable|solicitante|prestador|correo|e-?mail|tel|celular|extensi|monto|importe|valor|costo|fecha|vigencia|apertura|folio|oficio|expediente|clave|rfc|curp|dependencia|contraparte|instituci|entidad|remite|cargo|puesto|domicilio|direcci';
 function grab(label){var re=new RegExp('(?:'+label+')\\s*:?\\s*([^\\r\\n]{3,180}?)(?=\\s*(?:'+STOPKW+')\\s*:|[\\r\\n]|$)','i');var m=t.match(re);return m?m[1].trim().replace(/[·,;:.\s]+$/,''):'';}
 var asunto=grab('asunto|objeto');
 var nombre=grab('nombre|firmante|solicitante|prestador');
 var dep=grab('dependencia|contraparte|instituci[oó]n|entidad|remite');
 var map=[['folio|oficio|no\\.|n[uú]mero|expediente|clave',folio],['fecha|vigencia|apertura|inicio|t[eé]rmino|venc|recep',fecha],['monto|importe|valor|costo|precio|cuant',monto],['correo|e-?mail|\\bmail\\b',correo],['tel|celular|extensi',tel],['curp',curp],['rfc',rfc],['nombre|contacto|firmante|responsable|solicitante|prestador',nombre],['dependencia|contraparte|instituci|entidad|remite|solicitant',dep],['objeto|asunto|descripci|observaci|\\btema\\b|hechos|concepto|resumen',asunto]];
 var campos=document.querySelectorAll('input:not([type=hidden]):not([type=file]):not([type=checkbox]):not([type=radio]),textarea');var n=0;
 for(var i=0;i<campos.length;i++){var c=campos[i];if(c.value&&c.value.trim())continue;var lab='';var fdiv=c.closest('.f');if(fdiv){var l=fdiv.querySelector('label');if(l)lab=l.textContent;}var desc=((c.id||'')+' '+(c.placeholder||'')+' '+lab).toLowerCase();
   for(var k=0;k<map.length;k++){if(!map[k][1])continue;if(new RegExp(map[k][0]).test(desc)){if(c.type==='date'&&!/^\d{4}-\d{2}-\d{2}$/.test(map[k][1]))continue;c.value=map[k][1];c.dispatchEvent(new Event('input',{bubbles:true}));n++;break;}}}
 alert('OCR por reglas — extraído: '+[folio&&'folio '+folio,fecha&&'fecha '+fecha,monto&&'monto '+monto,correo&&'correo',tel&&'tel',asunto&&'asunto'].filter(Boolean).join(' · ')+'. Se llenaron '+n+' campo(s) vacío(s). Revisa y completa lo demás. (OCR de imagen real = fase backend.)');
 if(window.__bitlog)__bitlog('OCR','Extracción por reglas y llenado de formulario ('+n+' campos)');
};
}catch(e){}})();
</script>
<script>
/* Seguimiento universal · notas de abogados y auxiliares por modulo (SIGEJ) */
(function(){try{
if(/[?&]embed=1/.test(location.search))return;
var pk=(location.pathname.split('/').pop()||'x').replace('.html','')||'x';
if(/^(index|acceso_SIGEJ|seguimiento_SIGEJ|solicitud_convenios_SIGEJ)$/.test(pk))return;
if(!document.body)return;
function AA(){try{return JSON.parse(localStorage.getItem('sigej_seguimiento')||'{}');}catch(e){return {};}}
function NN(){var a=AA();return a[pk]||[];}
function ec(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
var b=document.createElement('div');b.textContent='📝 Seguimiento';
b.style.cssText='position:fixed;right:16px;bottom:16px;background:#0a4d8c;color:#fff;padding:9px 14px;border-radius:22px;font:600 12.5px system-ui,sans-serif;cursor:pointer;z-index:99997;box-shadow:0 4px 14px rgba(0,0,0,.25)';
var p=document.createElement('div');
p.style.cssText='position:fixed;right:16px;bottom:58px;width:340px;max-width:92vw;max-height:70vh;background:#fff;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 12px 34px rgba(0,0,0,.28);z-index:99998;display:none;flex-direction:column;overflow:hidden';
p.innerHTML='<div style="background:#0a4d8c;color:#fff;padding:9px 12px;font:700 13px system-ui,sans-serif;display:flex;justify-content:space-between;align-items:center"><span>📝 Seguimiento del módulo</span><span id="__sgx" style="cursor:pointer;font-size:16px">✕</span></div><div id="__sgl" style="overflow:auto;padding:8px 11px;font:12px system-ui,sans-serif;color:#334155;flex:1;min-height:80px"></div><div style="padding:8px 10px;border-top:1px solid #e2e8f0"><textarea id="__sgt" rows="2" placeholder="Escribe una nota de seguimiento…" style="width:100%;box-sizing:border-box;font:12.5px system-ui,sans-serif;padding:7px;border:1px solid #cbd5e1;border-radius:8px;resize:vertical"></textarea><button id="__sga" style="margin-top:6px;background:#1f9d6b;color:#fff;border:none;border-radius:8px;padding:7px 12px;font:600 12px system-ui,sans-serif;cursor:pointer">＋ Agregar nota</button></div>';
document.body.appendChild(b);document.body.appendChild(p);
function draw(){var n=NN();document.getElementById('__sgl').innerHTML=n.length?n.slice().reverse().map(function(x){return '<div style="border-bottom:1px solid #eef2f7;padding:5px 0"><b style="color:#0a4d8c">'+ec(x.perfil)+'</b> <span style="color:#94a3b8;font-size:10.5px">'+ec(x.ts)+'</span><br>'+ec(x.texto).replace(/\n/g,'<br>')+'</div>';}).join(''):'<div style="color:#94a3b8">Sin notas de seguimiento aún. Escribe la primera.</div>';}
b.onclick=function(){var o=p.style.display!=='none';p.style.display=o?'none':'flex';if(!o)draw();};
document.getElementById('__sgx').onclick=function(){p.style.display='none';};
document.getElementById('__sga').onclick=function(){var t=(document.getElementById('__sgt').value||'').trim();if(!t)return;var a=AA();a[pk]=a[pk]||[];a[pk].push({ts:new Date().toISOString().slice(0,16).replace('T',' '),perfil:localStorage.getItem('sigej_perfil')||'(perfil)',texto:t});localStorage.setItem('sigej_seguimiento',JSON.stringify(a));document.getElementById('__sgt').value='';draw();if(window.__bitlog)__bitlog('Seguimiento','Nota de seguimiento');};
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
/* ALTA PROTEGIDA universal · SIGEJ — alta inmutable con sello de captura, seguimiento, trámites/procesos y plazo normativo.
   Inmutabilidad y firma real (WORM/hash/firma-e) son fase backend; aquí se garantiza en la interfaz: no hay borrado, solo anulación con motivo y bitácora. */
(function(){try{
if(/[?&]embed=1/.test(location.search))return;
var pk=(location.pathname.split('/').pop()||'x').replace('.html','')||'x';
if(/^(index|acceso_SIGEJ|seguimiento_SIGEJ|solicitud_convenios_SIGEJ|alertas_centro_SIGEJ|SIGEJ_inicio)$/.test(pk))return;
if(!document.body)return;
var PF=localStorage.getItem('sigej_perfil')||'(perfil)';
var RO=['Secretaría General','Director','Coordinador General','Consulta'];
var puedeCapturar=RO.indexOf(PF)<0;
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function Sv(k,v){localStorage.setItem(k,JSON.stringify(v));}
function ec(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function nowT(){return new Date().toISOString().slice(0,16).replace('T',' ');}
function today(){return new Date().toISOString().slice(0,10);}
function addDays(iso,n,base){var t=new Date(iso+'T00:00:00');if(base==='naturales'){t.setDate(t.getDate()+(n||0));return t.toISOString().slice(0,10);}var c=0;while(c<(n||0)){t.setDate(t.getDate()+1);var w=t.getDay();if(w!==0&&w!==6)c++;}return t.toISOString().slice(0,10);}
/* catálogo SLA — lo administra Help Desk en el Centro de Alertas; si no existe, se siembra por defecto (operacional, editable) */
function seedCat(){if(J('sigej_sla_catalogo').length)return;Sv('sigej_sla_catalogo',[
 {id:'sla1',tipo:'Respuesta a oficio urgente',dias:1,base:'habiles',ambito:'Interno',fundamento:'Plazo interno de la Oficina (configurable por Help Desk)',rec:[0],activo:true},
 {id:'sla2',tipo:'Respuesta a oficio ordinario',dias:5,base:'habiles',ambito:'Interno',fundamento:'Plazo interno de la Oficina (configurable por Help Desk)',rec:[2,0],activo:true},
 {id:'sla3',tipo:'Requerimiento de autoridad',dias:3,base:'habiles',ambito:'Federal',fundamento:'Conforme al término señalado en el requerimiento y la ley aplicable (capturar fundamento)',rec:[1,0],activo:true},
 {id:'sla4',tipo:'Contestacion / tramite administrativo',dias:10,base:'habiles',ambito:'Estatal',fundamento:'Ley del Procedimiento Administrativo del Estado de Jalisco y sus Municipios (capturar artículo aplicable)',rec:[3,1,0],activo:true},
 {id:'sla5',tipo:'Solicitud de informacion / transparencia',dias:8,base:'habiles',ambito:'Estatal',fundamento:'Ley de Transparencia y Acceso a la Información Pública del Estado de Jalisco (capturar artículo)',rec:[3,1],activo:true},
 {id:'sla6',tipo:'Requisicion de papeleria',dias:5,base:'naturales',ambito:'Interno',fundamento:'Plazo interno (configurable)',rec:[1],activo:true},
 {id:'sla7',tipo:'Viaticos / comprobacion',dias:10,base:'naturales',ambito:'Interno',fundamento:'Normatividad de la UdeG en materia de viáticos (capturar fundamento)',rec:[3,1],activo:true}
]);}
seedCat();
function ALL(){return J('sigej_altas');}
function mine(){return ALL().filter(function(x){return x.modulo===pk;});}
function blog(t,a){try{var L=J('sigej_bitacora');L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:PF,modulo:pk,tipo:t,accion:String(a||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);Sv('sigej_bitacora',L);}catch(e){}if(window.__bitlog){try{window.__bitlog(t,a);}catch(e){}}}
var b=document.createElement('div');b.textContent='➕ Alta protegida';
b.style.cssText='position:fixed;right:16px;bottom:58px;background:#1a6d64;color:#fff;padding:9px 14px;border-radius:22px;font:600 12.5px system-ui,sans-serif;cursor:pointer;z-index:99995;box-shadow:0 4px 14px rgba(0,0,0,.25)';
var p=document.createElement('div');
p.style.cssText='position:fixed;right:16px;bottom:104px;width:390px;max-width:94vw;max-height:78vh;background:#fff;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 12px 34px rgba(0,0,0,.3);z-index:99996;display:none;flex-direction:column;overflow:hidden';
document.body.appendChild(b);document.body.appendChild(p);
function catOpts(){var c=J('sigej_sla_catalogo').filter(function(x){return x.activo!==false;});return '<option value="">— Sin plazo —</option>'+c.map(function(x){return '<option value="'+x.id+'">'+ec(x.tipo)+' · '+x.dias+' d '+x.base+' ('+ec(x.ambito)+')</option>';}).join('');}
function head(){return '<div style="background:#1a6d64;color:#fff;padding:9px 12px;font:700 13px system-ui,sans-serif;display:flex;justify-content:space-between;align-items:center"><span>➕ Alta protegida · '+ec(pk)+'</span><span id="__alx" style="cursor:pointer;font-size:16px">✕</span></div>';}
function form(){if(!puedeCapturar)return '<div style="padding:12px;color:#8a6d1a;background:#fff8e6;font:12px system-ui,sans-serif">Tu perfil es de solo lectura/consulta: puedes ver las altas, no capturar.</div>';
 return '<div style="padding:10px 12px;border-bottom:1px solid #e2e8f0;font:12px system-ui,sans-serif">'+
 '<div style="display:flex;gap:6px;flex-wrap:wrap"><select id="__altipo" style="flex:1;min-width:150px;padding:7px;border:1px solid #cbd5e1;border-radius:8px"><option>Documento nuevo</option><option>Expediente nuevo</option><option>Trámite nuevo</option><option>Proceso nuevo</option></select>'+
 '<select id="__alplazo" style="flex:1;min-width:150px;padding:7px;border:1px solid #cbd5e1;border-radius:8px">'+catOpts()+'</select></div>'+
 '<input id="__altit" placeholder="Título / identificación *" style="width:100%;box-sizing:border-box;margin-top:6px;padding:7px;border:1px solid #cbd5e1;border-radius:8px">'+
 '<textarea id="__aldet" rows="2" placeholder="Detalle / descripción" style="width:100%;box-sizing:border-box;margin-top:6px;padding:7px;border:1px solid #cbd5e1;border-radius:8px;resize:vertical"></textarea>'+
 '<button id="__alsave" style="margin-top:6px;background:#1f9d6b;color:#fff;border:none;border-radius:8px;padding:8px 12px;font:600 12px system-ui,sans-serif;cursor:pointer">💾 Guardar (con sello de captura)</button> <span id="__almsg" style="font:11px system-ui,sans-serif;margin-left:6px"></span></div>';}
function plazoBadge(a){if(!a.fechaLimite)return '';var d=Math.round((new Date(a.fechaLimite+'T00:00:00')-new Date(today()+'T00:00:00'))/864e5);var col=d<0?'#c0392b':(d<=2?'#e08e0b':'#128c4a');var txt=d<0?('vencido hace '+(-d)+' d'):(d===0?'vence hoy':'vence en '+d+' d');return '<span style="background:'+col+';color:#fff;border-radius:10px;padding:1px 7px;font-size:9.5px">⏰ '+txt+'</span>';}
function draw(){var rows=mine().slice().reverse();
 p.querySelector('#__allist').innerHTML=rows.length?rows.map(function(a){var an=a.anulado;
  return '<div style="border-bottom:1px solid #eef2f7;padding:7px 0'+(an?';opacity:.6':'')+'">'+
   '<div><b style="color:#0a4d8c">'+ec(a.folio)+'</b> · '+ec(a.tipo)+' '+(an?'<span style="background:#fdeaea;color:#c0392b;border-radius:10px;padding:1px 7px;font-size:9.5px">ANULADA</span>':plazoBadge(a))+'</div>'+
   '<div style="font-size:12px;color:#334155">'+ec(a.titulo)+'</div>'+
   '<div style="font-size:10px;color:#94a3b8">🖊️ '+ec(a.capturadoPor)+' · '+ec(a.fechaCaptura)+(a.fechaLimite?' · límite '+a.fechaLimite:'')+((a.seguimiento||[]).length?' · 🧭 '+a.seguimiento.length:'')+((a.subprocesos||[]).length?' · ➕ '+a.subprocesos.length:'')+'</div>'+
   (an?'<div style="font-size:10px;color:#c0392b">Anulada por '+ec(an.por)+' · '+ec(an.ts)+' — '+ec(an.motivo)+'</div>':
     (puedeCapturar?'<div style="margin-top:4px;display:flex;gap:4px;flex-wrap:wrap"><button onclick="window.__alSeg(\''+a.id+'\')" style="font-size:10.5px;border:1px solid #cfe0f5;background:#eef6ff;color:#0a4d8c;border-radius:7px;padding:3px 7px;cursor:pointer">🧭 Seguimiento</button><button onclick="window.__alSub(\''+a.id+'\')" style="font-size:10.5px;border:1px solid #cfe0f5;background:#eef6ff;color:#0a4d8c;border-radius:7px;padding:3px 7px;cursor:pointer">➕ Trámite/Proceso</button><button onclick="window.__alTraza(\''+a.id+'\')" style="font-size:10.5px;border:1px solid #e2e8f0;background:#f8fafc;color:#334155;border-radius:7px;padding:3px 7px;cursor:pointer">🧾 Traza</button><button onclick="window.__alAnu(\''+a.id+'\')" style="font-size:10.5px;border:1px solid #e7a0a0;background:#fdeaea;color:#c0392b;border-radius:7px;padding:3px 7px;cursor:pointer">🚫 Anular</button></div>':''))+
  '</div>';
 }).join(''):'<div style="color:#94a3b8;font:12px system-ui,sans-serif;padding:6px">Sin altas en este módulo. Captura la primera (queda con sello y no podrá borrarse).</div>';}
function render(){p.innerHTML=head()+form()+'<div id="__allist" style="overflow:auto;padding:8px 12px;font:12px system-ui,sans-serif;flex:1;min-height:90px"></div><div style="padding:7px 12px;border-top:1px solid #e2e8f0;font:10.5px system-ui,sans-serif;color:#64748b">🔒 Registro inmutable: una vez guardado no se borra; solo se anula con motivo. Todo queda en la bitácora de auditoría.</div>';
 p.querySelector('#__alx').onclick=function(){p.style.display='none';};
 var sv=p.querySelector('#__alsave');if(sv)sv.onclick=save;draw();}
function save(){var tit=(p.querySelector('#__altit').value||'').trim();if(!tit){p.querySelector('#__almsg').style.color='#c0392b';p.querySelector('#__almsg').textContent='Falta el título.';return;}
 var tipo=p.querySelector('#__altipo').value;var plz=p.querySelector('#__alplazo').value;var det=(p.querySelector('#__aldet').value||'').trim();
 var A=ALL();var y=new Date().getFullYear();var folio='ALT-'+y+'-'+String(A.length+1).padStart(4,'0');
 var fl='',pt='',pb='';if(plz){var c=J('sigej_sla_catalogo').filter(function(x){return x.id===plz;})[0];if(c){pt=c.tipo;pb=c.base;fl=addDays(today(),c.dias,c.base);}}
 var rec={id:'AL-'+Date.now().toString(36),folio:folio,tipo:tipo,modulo:pk,titulo:tit,detalle:det,plazoTipo:pt,plazoBase:pb,fechaLimite:fl,estado:'Abierto',capturadoPor:PF,fechaCaptura:nowT(),hist:[{ts:nowT(),usuario:PF,accion:'Alta ('+tipo+')'}],seguimiento:[],subprocesos:[],anulado:null};
 A.push(rec);Sv('sigej_altas',A);blog('Acción','Alta protegida '+folio+' · '+tipo+' · '+tit);
 p.querySelector('#__altit').value='';p.querySelector('#__aldet').value='';p.querySelector('#__almsg').style.color='#128c4a';p.querySelector('#__almsg').textContent='✓ '+folio+' guardada con sello.';draw();}
window.__alSeg=function(id){var t=prompt('Nota de seguimiento:','');if(t===null||!t.trim())return;var A=ALL();A.forEach(function(a){if(a.id===id){(a.seguimiento=a.seguimiento||[]).push({ts:nowT(),usuario:PF,texto:t.trim()});(a.hist=a.hist||[]).push({ts:nowT(),usuario:PF,accion:'Seguimiento'});}});Sv('sigej_altas',A);blog('Seguimiento','Seguimiento en alta '+id);draw();};
window.__alSub=function(id){var k=prompt('Nuevo (escribe: Trámite  o  Proceso):','Trámite');if(k===null)return;var tp=/proceso/i.test(k)?'Proceso':'Trámite';var t=prompt('Descripción del '+tp+':','');if(t===null||!t.trim())return;var A=ALL();A.forEach(function(a){if(a.id===id){(a.subprocesos=a.subprocesos||[]).push({ts:nowT(),usuario:PF,tipo:tp,texto:t.trim()});(a.hist=a.hist||[]).push({ts:nowT(),usuario:PF,accion:'Agrega '+tp});}});Sv('sigej_altas',A);blog('Acción','Nuevo '+tp+' en alta '+id);draw();};
window.__alAnu=function(id){var m=prompt('Motivo de ANULACIÓN (la información NO se borra; queda anulada y en bitácora):','');if(m===null||!m.trim())return;var A=ALL();A.forEach(function(a){if(a.id===id){a.anulado={motivo:m.trim(),por:PF,ts:nowT()};a.estado='Anulado';(a.hist=a.hist||[]).push({ts:nowT(),usuario:PF,accion:'Anulación: '+m.trim()});}});Sv('sigej_altas',A);blog('Acción','Anula alta '+id);draw();};
window.__alTraza=function(id){var a=ALL().filter(function(x){return x.id===id;})[0];if(!a)return;var h=(a.hist||[]).map(function(x){return '• '+x.ts+' — '+x.usuario+': '+x.accion;}).join('\n');var sg=(a.seguimiento||[]).map(function(x){return '• '+x.ts+' — '+x.usuario+': '+x.texto;}).join('\n');var sp=(a.subprocesos||[]).map(function(x){return '• '+x.ts+' — '+x.usuario+' ['+x.tipo+']: '+x.texto;}).join('\n');alert('🧾 Trazabilidad · '+a.folio+'\nCaptura: '+a.capturadoPor+' · '+a.fechaCaptura+'\nPlazo: '+(a.plazoTipo||'—')+(a.fechaLimite?' (límite '+a.fechaLimite+')':'')+'\n\nHISTORIAL:\n'+(h||'—')+'\n\nSEGUIMIENTO:\n'+(sg||'—')+'\n\nTRÁMITES/PROCESOS:\n'+(sp||'—'));};
b.onclick=function(){var o=p.style.display!=='none';if(o){p.style.display='none';}else{render();p.style.display='flex';}};
}catch(e){}})();
</script>"""

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Transparencia General</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--card:#ffffff;--card2:#f8fafc;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:radial-gradient(1200px 600px at 80% -10%,transparent,transparent),var(--bg);color:var(--ink)}
header{padding:14px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;border-bottom:1px solid var(--line)}
header h1{margin:0;font-size:18px}header .s{opacity:.8;font-size:12px;margin-top:3px}
.navbar{background:#06182c;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#475569;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.live{display:inline-flex;align-items:center;gap:6px;background:rgba(31,157,107,.15);color:#7ee0b4;border:1px solid rgba(31,157,107,.4);border-radius:20px;padding:5px 12px;font-size:12px}
.dot{width:8px;height:8px;border-radius:50%;background:#2ee08a;animation:p 1.5s infinite}@keyframes p{50%{opacity:.3}}
.tabbar{display:flex;flex-wrap:wrap;gap:6px;padding:14px 24px 0;max-width:1440px;margin:auto}
.tb{background:var(--card);color:#475569;border:1px solid var(--line);border-bottom:none;border-radius:11px 11px 0 0;padding:10px 16px;font-size:13px;font-weight:600;cursor:pointer}
.tb:hover{color:#fff}.tb.on{background:var(--azul2);color:#fff;border-color:var(--azul2)}
.wrap{padding:14px 24px 36px;max-width:1440px;margin:auto}
.tab{display:none}.tab.on{display:block}
.h{font-size:14px;color:#0a4d8c;font-weight:700;margin:16px 0 10px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:14px}
.kpi{background:linear-gradient(160deg,var(--card),var(--card2));border:1px solid var(--line);border-radius:13px;padding:14px}
.kpi .n{font-size:24px;font-weight:800}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.g .n{color:#7ee0b4}.kpi.r .n{color:#ff9b8d}.kpi.y .n{color:#ffce82}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:15px}
.card h3{margin:0 0 10px;font-size:13px;color:#0a4d8c}.card.s2{grid-column:span 2}
canvas{max-height:250px}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px}.bar input,.bar select{padding:7px 9px;border:1px solid var(--line);border-radius:7px;font-size:12.5px;background:#f1f5fb;color:var(--ink)}
button{padding:8px 13px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
.b1{background:var(--azul2)}.b3{background:var(--ok,#1f9d6b)}.bw{background:#2b579a}.bd{background:#33507a}.mini{padding:5px 10px;font-size:11px}
.it{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:7px}
.it .t{font-weight:700;color:#0a4d8c;font-size:12.5px}.it .m{font-size:11px;color:var(--mut);margin-top:2px}
table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:7px 8px;text-align:left;border-bottom:1px solid var(--line)}th{color:var(--mut)}
.heat{width:100%;border-collapse:collapse;font-size:11.5px}.heat td,.heat th{padding:6px;text-align:center;border:2px solid var(--bg)}.heat th{color:var(--mut)}.heat td.lab{text-align:left;color:#0a4d8c}
.chip{display:inline-block;background:#f1f5fb;border:1px solid var(--line);border-radius:9px;padding:2px 8px;font-size:10px;color:#475569;margin:1px}
.rb{font-size:10px;padding:2px 8px;border-radius:9px;font-weight:600}.rb-Crítico{background:rgba(192,57,43,.25);color:#ff9b8d}.rb-Alto{background:rgba(234,88,12,.22);color:#ffb38f}.rb-Medio{background:rgba(224,142,11,.2);color:#ffce82}.rb-Bajo{background:rgba(31,157,107,.2);color:#8fe0d8}
a.lk{color:#7ee0b4;text-decoration:none}
.note{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:9px;padding:9px 12px;font-size:11.5px;color:#e8cf95;margin:8px 0}
iframe{width:100%;height:82vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7}
footer{padding:14px 24px;color:#64748b;font-size:11px;text-align:center}
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
<header><div><h1>📊 SIGEJ-UdeG · Transparencia General — Rendición de cuentas institucional</h1>
<div class="s">Buscador global sobre todos los módulos y áreas · estadísticas · matrices · reportes · solicitudes de transparencia (UTI)</div></div>
<div style="text-align:right"><span class="live"><span class="dot"></span>En vivo · <span id="upd"></span></span> <button class="b1 mini" onclick="loadAll();render();">↻ Actualizar</button></div></header>
__NAV__
<div class="tabbar">
 <button class="tb on" data-t="t1" onclick="tab('t1')">🔍 Buscador global</button>
 <button class="tb" data-t="t2" onclick="tab('t2')">📊 Estadísticas</button>
 <button class="tb" data-t="t3" onclick="tab('t3')">🧮 Matrices</button>
 <button class="tb" data-t="t4" onclick="tab('t4')">📑 Reportes consolidados</button>
 <button class="tb" data-t="t7" onclick="tab('t7')">📑 Reportes en 2 pasos</button>
 <button class="tb" data-t="t5" onclick="tab('t5')">🔎 Solicitudes UTI</button>
 <button class="tb" data-t="t8" onclick="tab('t8')">🧾 Bitácora de auditoría</button>
 <button class="tb" data-t="t6" onclick="tab('t6')">ℹ️ Cobertura</button>
 <button class="tb" data-t="t9" onclick="tab('t9')">📋 Obligaciones Art. 8 y 14 Bis (jurídicas)</button>
 <button class="tb" data-t="t10" onclick="tab('t10')">📅 Agenda pública del Titular</button>
</div>
<div class="wrap">
 <section id="t1" class="tab on">
  <div class="bar">
   <input id="q" placeholder="Buscar en TODO el sistema (folio, asunto, responsable, dependencia, materia…)" oninput="renderBuscador()" style="min-width:340px">
   <select id="fMod" onchange="renderBuscador()"><option value="">Todos los módulos</option></select>
   <select id="fAnio" onchange="renderBuscador()"><option value="">Todo año</option></select>
   <select id="fNiv" onchange="renderBuscador()"><option value="">Todo riesgo</option><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
   <button class="bd mini" onclick="exportBuscador()">⬇ CSV resultados</button>
   <span id="cnt" style="font-size:12px;color:#64748b"></span>
  </div>
  <div id="lista"></div>
 </section>
 <section id="t2" class="tab">
  <div class="kpis" id="stKpis"></div>
  <div class="grid">
   <div class="card s2"><h3>Registros por módulo / área</h3><canvas id="cMod"></canvas></div>
   <div class="card"><h3>Por nivel de riesgo</h3><canvas id="cNiv"></canvas></div>
   <div class="card"><h3>Por año</h3><canvas id="cAnio"></canvas></div>
  </div>
 </section>
 <section id="t3" class="tab">
  <div class="h">🧮 Matriz módulo × nivel de riesgo</div><div class="card"><table class="heat" id="mxNiv"></table><div style="margin-top:8px"><button class="bd mini" onclick="exportMatriz('niv')">⬇ CSV</button></div></div>
  <div class="h">🧮 Matriz módulo × año</div><div class="card" style="overflow:auto"><table class="heat" id="mxAnio"></table><div style="margin-top:8px"><button class="bd mini" onclick="exportMatriz('anio')">⬇ CSV</button></div></div>
 </section>
 <section id="t4" class="tab">
  <div class="card"><h3>📑 Generación de reportes institucionales</h3>
   <div style="font-size:12px;color:#c7d6ea;margin-bottom:10px">Genera reportes de transparencia y rendición de cuentas consolidados de todo el sistema.</div>
   <div style="display:flex;gap:8px;flex-wrap:wrap">
    <button class="bw" onclick="reporteConsolidadoWord()">📄 Reporte consolidado institucional (Word)</button>
    <button class="b3" onclick="exportTodo()">⬇ Base completa (CSV)</button>
   </div>
   <div class="h">Reporte por módulo / área</div>
   <div class="bar"><select id="rMod"></select> <button class="b1 mini" onclick="reporteModuloWord()">📄 Reporte del módulo (Word)</button> <button class="bd mini" onclick="reporteModuloCSV()">⬇ CSV del módulo</button></div>
   <div id="rPrev"></div>
  </div>
 </section>
 <section id="t5" class="tab">
  <div class="note">🔎 <b>Solicitudes de transparencia (UTI)</b> integradas: registro por folio, materia, cuantía y oficio de respuesta en Word. Es el módulo de transparencia operativo, embebido aquí.</div>
  <iframe id="utiFrame" data-src="transparencia_SIGEJ.html?embed=1" title="Solicitudes UTI"></iframe>
 </section>
 <section id="t7" class="tab">
  <div class="note">📑 <b>Reportes en 2 pasos</b> integrados: el generador de reportes por pasos vive aquí, en Transparencia General. Comparte los datos de todo el sistema.</div>
  <iframe id="repFrame" data-src="reportes_SIGEJ.html?embed=1" title="Reportes en 2 pasos"></iframe>
 </section>
 <section id="t8" class="tab">
  <div class="note">🧾 <b>Bitácora de auditoría</b> integrada: registro de accesos y acciones de interfaz de todo el sistema, para rendición de cuentas. Es de solo lectura.</div>
  <iframe id="bitFrame" data-src="bitacora_SIGEJ.html?embed=1" title="Bitácora de auditoría"></iframe>
 </section>
 <section id="t6" class="tab">
  <div class="card"><h3>ℹ️ Cobertura — fuentes integradas</h3><div id="cobBox"></div>
   <div class="note" style="margin-top:10px">El <b>texto consolidado</b>, la <b>búsqueda semántica</b>, el <b>OCR</b> y la publicación automática en la <b>Plataforma Nacional de Transparencia (PNT)</b> son fase backend. Aquí la búsqueda es por palabras clave sobre los campos capturados en cada módulo. Distingue dato capturado de derivado.</div></div>
 </section>
 <section id="t9" class="tab">
  <div id="oblBody"></div>
 </section>
 <section id="t10" class="tab">
  <div class="card"><h3>📅 Agenda pública de la persona titular de la Abogacía General</h3>
   <div class="note" style="margin:6px 0">Publicación proactiva de la agenda del titular. Se difunden únicamente las actividades marcadas como <b>públicas</b>; los datos personales de terceros y la información reservada no se muestran. Fuente única compartida con el Centro Ejecutivo.</div>
   <iframe id="agPubFrame" data-src="agenda_titular_SIGEJ.html?embed=1&amp;pub=1" title="Agenda pública del Titular" style="width:100%;height:78vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe>
  </div>
 </section>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const HOY=new Date(2026,5,18);let CH={};let ALL=[];
function el(id){return document.getElementById(id);}
/* ===== Obligaciones de transparencia — Art. 8 y 14-Bis (Ley de Transparencia del Edo. de Jalisco y sus Municipios). Texto conforme a la ley; se identifican las fracciones JURÍDICAS / con implicación jurídica ===== */
var ART8=[
 {fr:'I',nat:'Jurídica',d:'Información necesaria para el ejercicio del derecho a la información: Ley General, esta Ley y su Reglamento; reglamento interno de información pública; lineamientos del Instituto; <b>actas y resoluciones del Comité de Transparencia</b>; índice de expedientes reservados; manual y formato de solicitud; estadística de solicitudes.'},
 {fr:'II',nat:'Jurídica',d:'<b>Marco jurídico aplicable</b> al y por el sujeto obligado: Constituciones Federal y Estatal; tratados internacionales; leyes federales y estatales; reglamentos federales, estatales y municipales; decretos, acuerdos, criterios, políticas y demás normas jurídicas generales.',src:{mod:'Normatividad Universitaria',link:'normatividad_SIGEJ.html',store:'sigej_normatividad',lab:'normas/dictámenes'}},
 {fr:'III',nat:'Administrativa',d:'Información sobre la planeación del desarrollo (PND, programas federales, PED, programas estatales y regionales, evaluaciones).'},
 {fr:'IV',nat:'Administrativa',d:'Información sobre la planeación estratégica gubernamental aplicable.'},
 {fr:'V',nat:'Mixta',d:'Información financiera, patrimonial y administrativa.',sub:['a) Partidas del PEF/PEE y clasificador por objeto del gasto (últimos 3 años)','b) Ingresos extraordinarios (origen, responsables, destino)','c) Presupuesto de egresos anual','d) Convocatorias a concursos para cargos públicos y resultados','e) Organigrama y plantilla (base/confianza/vacantes)','f) Remuneraciones mensuales por puesto','g) Nóminas completas','h) Jubilados y pensionados y montos','i) Estados financieros mensuales','j) Gastos de comunicación social'],src:{mod:'Administración OAG',link:'administracion_SIGEJ.html',store:'sigej_adm_contable',lab:'movimientos contables'}},
 {fr:'VI',nat:'Mixta',d:'Información sobre la gestión pública (funciones, servicios, obras, programas, políticas y <b>convenios, contratos, concesiones, licencias y permisos</b>).',sub:['a) Funciones públicas (fundamento legal, descripción, recursos)','b) Servicios públicos','c) Obras públicas (últimos 3 años)','d) Programas sociales','e) Políticas públicas','f) <b>Los convenios, contratos y demás instrumentos jurídicos suscritos</b> (últimos 3 años)','g) Concesiones, licencias, permisos y autorizaciones'],srcs:[{mod:'Instrumentos Jurídicos (CLM)',link:'instrumentos_SIGEJ.html',store:'sigej_instrumentos',lab:'convenios/contratos',inc:'inciso f)'},{mod:'Patrimonio Inmobiliario',link:'patrimonial_SIGEJ.html',store:'sigej_contratos_inm',lab:'comodatos/concesiones',inc:'inciso g)'},{mod:'Sostenibilidad',link:'sostenibilidad_SIGEJ.html',store:'sigej_sost_cert',lab:'permisos/licencias amb.',inc:'inciso g)'},{mod:'Hospitales y Salud',link:'hospitales_SIGEJ.html',store:'sigej_hosp_est',lab:'licencias sanitarias',inc:'inciso g)'},{mod:'Patrimonio Intangible',link:'patrimonio_SIGEJ.html',store:'sigej_patrimonio',lab:'registros/licencias PI',inc:'inciso g)'}]},
 {fr:'VII',nat:'Jurídica',d:'<b>Versiones públicas de las resoluciones y laudos</b> que emitan los sujetos obligados (procedimientos y juicios).',src:{mod:'Asuntos Contenciosos / MASC',link:'contencioso_SIGEJ.html',exp:true,lab:'resoluciones/laudos'}},
 {fr:'VIII',nat:'Administrativa',d:'Mecanismos e instrumentos de participación ciudadana.'},
 {fr:'IX',nat:'Administrativa',d:'Información pública ordinaria, proactiva o focalizada.'},
 {fr:'X',nat:'Jurídica',d:'<b>Condiciones generales de trabajo, contratos o convenios</b> que regulen las relaciones laborales del personal de base y de confianza.',src:{mod:'Administración → Personal',link:'administracion_SIGEJ.html',store:'sigej_adm_personal',lab:'movimientos de personal'}},
 {fr:'XI',nat:'Administrativa',d:'Estudios financiados con recursos públicos.'},
 {fr:'XII',nat:'Administrativa',d:'Ingresos recibidos por cualquier concepto y responsables de recibirlos, administrarlos y ejercerlos.'},
 {fr:'XIII',nat:'Jurídica',d:'<b>Catálogo de disposición y guía de archivo documental</b> (Ley de Archivos).',src:{mod:'Oficialía de Partes',link:'oficialia_SIGEJ.html',store:'sigej_oficios',lab:'oficios/documentos'}},
 {fr:'XIV',nat:'Administrativa',d:'La demás información pública a que obliguen las disposiciones federales y la Ley General.'}
];
var ART14B=[
 {fr:'I',nat:'Jurídica',d:'La obligatoria para todos los sujetos obligados (remite al Art. 8).'},
 {fr:'II',nat:'Administrativa',d:'Planes y programas de estudio (áreas de conocimiento, perfil profesional, duración, asignaturas y créditos).'},
 {fr:'III',nat:'Jurídica',d:'<b>Toda la información relacionada con sus procedimientos administrativos.</b>',src:{mod:'Responsabilidades (Contencioso)',link:'contencioso_SIGEJ.html',store:'sigej_resp',lab:'procedimientos'}},
 {fr:'IV',nat:'Administrativa',d:'Remuneración de los profesores, incluyendo estímulos al desempeño, nivel y monto.'},
 {fr:'V',nat:'Mixta',d:'Lista de profesores con licencia o en año sabático.'},
 {fr:'VI',nat:'Mixta',d:'Listado de becas y apoyos, así como los procedimientos y requisitos para obtenerlos.'},
 {fr:'VII',nat:'Jurídica',d:'<b>Convocatorias de los concursos de oposición.</b>'},
 {fr:'VIII',nat:'Jurídica',d:'<b>Información relativa a los procesos de selección de los consejos</b> (órganos colegiados / CGU).',src:{mod:'Normatividad → Órganos colegiados (CGU)',link:'normatividad_SIGEJ.html',store:'sigej_normatividad',lab:'asuntos normativos/CGU'}},
 {fr:'IX',nat:'Administrativa',d:'Resultado de las evaluaciones del cuerpo docente.'},
 {fr:'X',nat:'Jurídica',d:'<b>Listado de instituciones incorporadas y requisitos de incorporación</b> de estudios.',src:{mod:'Programas Académicos',link:'programas_SIGEJ.html',store:'sigej_programas',lab:'programas/incorporaciones'}},
 {fr:'XI',nat:'Jurídica',d:'<b>Información respecto a las empresas u organismos para-universitarios.</b>'}
];
var OBLEST=['Pendiente','En proceso','Publicada','No aplica'];
var OBLSOLOJUR=true;
function oblStore(){try{return JSON.parse(localStorage.getItem('sigej_transp_oblig')||'{}');}catch(e){return {};}}
function oblSet(k,f,v){var s=oblStore();s[k]=s[k]||{};s[k][f]=v;localStorage.setItem('sigej_transp_oblig',JSON.stringify(s));if(f==='estado'&&window.__bitlog)__bitlog('Transparencia','Obligación '+k+' → '+v);renderObl();}
function oblGet(k){return oblStore()[k]||{};}
function oblCount(src){if(!src)return 0;try{if(src.exp){var e=(D.exp||[]).filter(function(x){return /Sentencia|Laudo|Amparo|Ejecut|Conclu|Resoluci/.test((x.est||''));}).length;return e+J('sigej_masc').length;}return J(src.store).length;}catch(e){return 0;}}
function natClass(n){return n==='Jurídica'?'g':n==='Mixta'?'y':'n';}
function oblExtra(x){var h='';
 if(x.sub){h+='<details style="margin-top:4px"><summary style="cursor:pointer;font-size:11px;color:#0a4d8c">▸ Incisos ('+x.sub.length+')</summary><ul style="margin:4px 0 0 15px;padding:0;font-size:11px;color:#475569;line-height:1.5">'+x.sub.map(function(s){return '<li>'+s+'</li>';}).join('')+'</ul></details>';}
 var srcs=x.srcs||(x.src?[x.src]:[]);
 if(srcs.length)h+='<div style="margin-top:5px;font-size:10.5px;color:#64748b">🔗 Fuente(s) en SIGEJ:</div>';
 srcs.forEach(function(s){h+='<div style="margin-top:3px;font-size:11px"><span style="background:#e6f0fb;color:#0a4d8c;border:1px solid #cfe0f5;border-radius:12px;padding:2px 8px"><b>'+s.mod+'</b>'+(s.inc?' ('+s.inc+')':'')+' · '+oblCount(s)+' '+s.lab+'</span> <a href="'+s.link+'" style="color:#0a4d8c;font-weight:600">abrir →</a></div>';});
 return h;}
function oblToggle(){OBLSOLOJUR=!OBLSOLOJUR;renderObl();}
function oblTabla(art,arr,pref){var rows=arr.filter(function(x){return !OBLSOLOJUR||x.nat==='Jurídica'||x.nat==='Mixta';});
 return '<table style="width:100%;border-collapse:collapse;font-size:12px"><tr style="text-align:left;color:#64748b"><th style="padding:6px;border-bottom:2px solid #e2e8f0">Fr.</th><th style="border-bottom:2px solid #e2e8f0">Contenido (conforme a la Ley)</th><th style="border-bottom:2px solid #e2e8f0">Naturaleza</th><th style="border-bottom:2px solid #e2e8f0">Responsable</th><th style="border-bottom:2px solid #e2e8f0">Publicación</th></tr>'+
  rows.map(function(x){var k=pref+'-'+x.fr;var g=oblGet(k);var c=g.estado==='Publicada'?'#15803d':g.estado==='No aplica'?'#64748b':g.estado==='En proceso'?'#b45309':'#c0392b';
   var sel='<select onchange="oblSet(\''+k+'\',\'estado\',this.value)" style="padding:4px;border:1px solid #e2e8f0;border-radius:6px;font-size:11px;color:'+c+';font-weight:700">'+OBLEST.map(function(e){return '<option'+(e===(g.estado||'Pendiente')?' selected':'')+'>'+e+'</option>';}).join('')+'</select>';
   var resp='<input value="'+((g.resp||'').replace(/"/g,'&quot;'))+'" onchange="oblSet(\''+k+'\',\'resp\',this.value)" placeholder="área" style="width:110px;padding:4px;border:1px solid #e2e8f0;border-radius:6px;font-size:11px">';
   return '<tr style="border-bottom:1px solid #f1f5f9"><td style="padding:6px;font-weight:700;color:#0a4d8c">'+x.fr+'</td><td style="font-size:11.5px;line-height:1.5">'+x.d+oblExtra(x)+'</td><td><span class="qc" style="background:'+(x.nat==='Jurídica'?'#e6f6ee;color:#15803d':x.nat==='Mixta'?'#fef3e2;color:#b45309':'#eef2f7;color:#475569')+';cursor:default">'+x.nat+'</span></td><td>'+resp+'</td><td>'+sel+'</td></tr>';}).join('')+'</table>';}
function oblStrip(s){return (s||'').replace(/<[^>]+>/g,'');}
function oblRows(soloJurMix){var out=[];[['Art. 8',ART8,'A8'],['Art. 14-Bis',ART14B,'A14B']].forEach(function(p){p[1].forEach(function(x){if(soloJurMix&&x.nat==='Administrativa')return;var g=oblGet(p[2]+'-'+x.fr);var srcs=x.srcs||(x.src?[x.src]:[]);var fu=srcs.map(function(s){return s.mod+'('+oblCount(s)+' '+s.lab+')';}).join('; ');out.push({art:p[0],fr:x.fr,nat:x.nat,cont:oblStrip(x.d),fuente:fu,resp:g.resp||'',estado:g.estado||'Pendiente'});});});return out;}
function oblResumen(){var scope=[];[['A8',ART8],['A14B',ART14B]].forEach(function(p){p[1].forEach(function(x){if(x.nat!=='Administrativa')scope.push(p[0]+'-'+x.fr);});});
 var by={Pendiente:0,'En proceso':0,Publicada:0,'No aplica':0};scope.forEach(function(k){by[oblGet(k).estado||'Pendiente']++;});
 var n=scope.length;var pct=n?Math.round(100*by.Publicada/n):0;
 var seg=[['Publicada',by.Publicada,'#1f9d6b'],['En proceso',by['En proceso'],'#e08e0b'],['Pendiente',by.Pendiente,'#c0392b'],['No aplica',by['No aplica'],'#94a3b8']];
 var bar=seg.map(function(s){var w=n?100*s[1]/n:0;return w>0?'<div title="'+s[0]+': '+s[1]+'" style="width:'+w+'%;background:'+s[2]+'"></div>':'';}).join('');
 var leg=seg.map(function(s){return '<span style="font-size:11px;margin-right:12px"><span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:'+s[2]+'"></span> '+s[0]+' '+s[1]+'</span>';}).join('');
 return '<div class="card"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;align-items:center"><b style="color:#0a4d8c">📄 Reporte de cumplimiento (fracciones jurídicas y mixtas)</b><div><button class="qc" onclick="oblCSV()" style="cursor:pointer">⬇️ CSV</button> <button class="qc" onclick="oblWord()" style="cursor:pointer">📄 Word</button></div></div><div style="margin:8px 0 4px;font-size:12.5px">Avance de publicación: <b>'+pct+'%</b> ('+by.Publicada+' de '+n+' fracciones)</div><div style="display:flex;height:14px;border-radius:7px;overflow:hidden;background:#eef2f7">'+bar+'</div><div style="margin-top:6px">'+leg+'</div></div>';}
function oblCSV(){var r=oblRows(false);var rows=[['Articulo','Fraccion','Naturaleza','Contenido','FuentesSIGEJ','Responsable','EstadoPublicacion']].concat(r.map(function(x){return [x.art,x.fr,x.nat,x.cont,x.fuente,x.resp,x.estado];}));
 var csv=rows.map(function(rr){return rr.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='cumplimiento_transparencia_art8_14bis.csv';a.click();}
function oblWord(){var r=oblRows(true);var pub=r.filter(function(x){return x.estado==='Publicada';}).length;var pend=r.filter(function(x){return x.estado==='Pendiente';}).length;var proc=r.filter(function(x){return x.estado==='En proceso';}).length;
 var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria;font-size:11pt"><div style="text-align:center"><h2>UNIVERSIDAD DE GUADALAJARA · Oficina de la Abogacía General</h2><h3>Reporte de cumplimiento de obligaciones de transparencia<br>Artículos 8° y 14-Bis — Ley de Transparencia y Acceso a la Información Pública del Estado de Jalisco y sus Municipios</h3><p>(Fracciones con naturaleza jurídica o mixta que competen a la Abogacía General)</p></div><p><b>Resumen:</b> '+r.length+' fracciones · Publicadas: '+pub+' · En proceso: '+proc+' · Pendientes: '+pend+' · Avance: '+(r.length?Math.round(100*pub/r.length):0)+'%.</p><table border="1" cellpadding="4" style="border-collapse:collapse;width:100%;font-size:9pt"><tr style="background:#eef2f7"><th>Art.</th><th>Fr.</th><th>Naturaleza</th><th>Contenido</th><th>Fuente(s) en SIGEJ</th><th>Responsable</th><th>Estado</th></tr>'+r.map(function(x){return '<tr><td>'+x.art+'</td><td>'+x.fr+'</td><td>'+x.nat+'</td><td>'+x.cont+'</td><td>'+(x.fuente||'—')+'</td><td>'+(x.resp||'—')+'</td><td>'+x.estado+'</td></tr>';}).join('')+'</table><p style="font-size:8pt;color:#555;margin-top:10px">Texto conforme a la Ley vigente. La clasificación de naturaleza es de apoyo para asignar responsabilidad; no altera la obligación legal de publicar. La publicación en la Plataforma Nacional de Transparencia y su verificación son fase de implementación (backend). Documento generado por SIGEJ-UdeG.</p></body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Reporte_Cumplimiento_Art8_14Bis.doc';a.click();}
function renderObl(){var jur8=ART8.filter(function(x){return x.nat==='Jurídica';}).length,jur14=ART14B.filter(function(x){return x.nat==='Jurídica';}).length;
 var s=oblStore();var pub=0,tot=0;ART8.concat(ART14B).forEach(function(x,i){});
 [['A8',ART8],['A14B',ART14B]].forEach(function(p){p[1].forEach(function(x){if(x.nat==='Jurídica'){tot++;if((oblGet(p[0]+'-'+x.fr).estado)==='Publicada')pub++;}});});
 var kp='<div class="kpis" style="margin-bottom:12px"><div class="kpi"><div class="n">'+(jur8+jur14)+'</div><div class="l">Fracciones jurídicas identificadas</div></div><div class="kpi g"><div class="n">'+pub+'</div><div class="l">Publicadas (jurídicas)</div></div><div class="kpi y"><div class="n">'+(tot-pub)+'</div><div class="l">Pendientes (jurídicas)</div></div><div class="kpi"><div class="n">Art. 8 · 14-Bis</div><div class="l">Ley de Transparencia Jalisco</div></div></div>';
 el('oblBody').innerHTML='<h2 style="margin:0 0 4px;color:#00254a">📋 Obligaciones de transparencia — Art. 8 y 14-Bis</h2>'+
  '<p style="color:#64748b;font-size:12.5px;margin:0 0 10px">Información fundamental conforme a la <b>Ley de Transparencia y Acceso a la Información Pública del Estado de Jalisco y sus Municipios</b>. El <b>Art. 14-Bis aplica específicamente a las universidades públicas con autonomía</b> (UdeG). Se identifican y dan seguimiento a las fracciones <b>jurídicas o con implicación jurídica</b> que competen a la Oficina de la Abogacía General.</p>'+
  '<div style="display:flex;gap:8px;align-items:center;margin-bottom:10px"><button class="qc" onclick="oblToggle()" style="cursor:pointer">'+(OBLSOLOJUR?'👁️ Ver todas las fracciones':'⚖️ Ver solo jurídicas/mixtas')+'</button><span style="font-size:11.5px;color:#64748b">Filtro actual: '+(OBLSOLOJUR?'jurídicas y mixtas':'todas')+'</span></div>'+kp+oblResumen()+
  '<div class="card"><h3 style="color:#0a4d8c;margin:0 0 6px">Artículo 8° — Información fundamental GENERAL (aplica a todos los sujetos obligados, incluida la UdeG)</h3>'+oblTabla('Art. 8',ART8,'A8')+'</div>'+
  '<div class="card"><h3 style="color:#0a4d8c;margin:0 0 6px">Artículo 14-Bis — Información fundamental · UNIVERSIDADES PÚBLICAS CON AUTONOMÍA (UdeG)</h3>'+oblTabla('Art. 14-Bis',ART14B,'A14B')+'</div>'+
  '<div class="note">📌 Texto conforme a la Ley vigente (documento oficial proporcionado). La naturaleza «Jurídica/Mixta/Administrativa» es una clasificación de apoyo para asignar responsabilidad a la Abogacía General; no altera la obligación legal de publicar. La publicación en la <b>PNT/portal</b> y su verificación son fase backend. El estado y responsable capturados se guardan y quedan en la bitácora.</div>';
}
function val(id){return (el(id).value||'').trim();}
function pad(n){return (n<10?'0':'')+n;}
function rb(n){return n?'<span class="rb rb-'+n+'">'+n+'</span>':'';}
const PAL=['#1aa39a','#0a4d8c','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#16a085','#5d6d7e','#9d174d','#0e7490','#b91c1c','#6d28d9'];
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function loadAll(){const A=[];
 function push(mod,ic,arr,m){(arr||[]).forEach(function(e){try{var r=m(e);if(r){r.mod=mod;r.ic=ic;r.txt=(r.txt||'').toLowerCase();A.push(r);}}catch(x){}});}
 push('Litigio / Contencioso','⚖️',D.exp,e=>({folio:e.num,tit:(e.mat||'')+(e.via?' · '+e.via:''),est:e.est,resp:e.resp,anio:e.an?String(e.an):'',niv:e.niv,link:'modulo_expedientes_SIGEJ.html',txt:[e.num,e.mat,e.dep,e.resp,e.est,e.centro].join(' ')}));
 push('Instrumentos','📜',J('sigej_instrumentos'),e=>({folio:e.folio,tit:e.tipo+(e.obj?' · '+e.obj:''),est:e.estado,resp:e.resp,anio:(e.firma||e.ini||'').slice(0,4),niv:e.nivel,link:'instrumentos_SIGEJ.html',txt:[e.folio,e.tipo,e.obj,e.dep,e.contra,e.resp].join(' ')}));
 push('Patrimonio intangible','🧩',J('sigej_patrimonio'),e=>({folio:e.folio,tit:e.titulo||e.tipo,est:e.estado,resp:e.resp,anio:(e.sol||'').slice(0,4),niv:e.nivel,link:'patrimonio_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.cu,e.autor].join(' ')}));
 push('Asuntos internacionales','🌎',J('sigej_internacional'),e=>({folio:e.folio,tit:e.titulo,est:e.estado,resp:e.resp||'',anio:(e.ini||'').slice(0,4),niv:e.nivel,link:'internacional_SIGEJ.html',txt:[e.folio,e.titulo,e.pais,e.cu,e.dep,e.resp].join(' ')}));
 push('Normatividad','📖',J('sigej_normatividad'),e=>({folio:e.folio,tit:e.tipo+(e.norma?' · '+e.norma:''),est:e.estado,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:e.nivel,link:'normatividad_SIGEJ.html',txt:[e.folio,e.tipo,e.norma,e.objeto,e.materia,e.resp].join(' ')}));
 push('Repositorio normativo','📚',J('sigej_norma_repo'),e=>({folio:e.nom,tit:e.nom,est:e.est,resp:'',anio:(e.fecha||'').slice(0,4),niv:'',link:'normatividad_SIGEJ.html',txt:[e.nom,e.jer,e.mat,e.aut].join(' ')}));
 push('MASC','🤝',J('sigej_masc'),e=>({folio:e.exp||e.num||e.id||'MASC',tit:(e.tipo||'Convenio')+(e.actor?' · '+e.actor:''),est:e.cumplimiento||e.estado,resp:e.responsable,anio:(e.fecha||'').slice(0,4),niv:'',link:'masc_SIGEJ.html',txt:[e.exp,e.tipo,e.actor,e.demandado,e.responsable].join(' ')}));
 push('Responsabilidades (LGRA)','⚖️',J('sigej_resp'),e=>({folio:e.folio||e.id,tit:e.clasif||e.falta||'Procedimiento',est:e.estado,resp:e.responsable,anio:(e.finicio||'').slice(0,4),niv:'',link:'resp_SIGEJ.html',txt:[e.folio,e.clasif,e.autoridad,e.estado].join(' ')}));
 push('Resp. universitarias','🏛️',J('sigej_norma_resp'),e=>({folio:'RU',tit:(e.suj||'')+' · '+(e.falta||''),est:e.etapa,resp:'',anio:(e.fecha||'').slice(0,4),niv:'',link:'normatividad_SIGEJ.html',txt:[e.suj,e.falta,e.etapa,e.dep,e.nota].join(' ')}));
 push('Desincorporación de bienes','🏷️',J('sigej_norma_bienes'),e=>({folio:e.tipo||'Bien',tit:e.desc,est:e.est,resp:'',anio:'',niv:'',link:'normatividad_SIGEJ.html',txt:[e.tipo,e.acc,e.desc,e.dep].join(' ')}));
 push('Asesoría / consultas','💡',J('sigej_asesoria'),e=>({folio:e.folio||e.id,tit:e.asunto||e.tipo||'Consulta',est:e.estado,resp:e.responsable||e.abogado,anio:(e.fecha||'').slice(0,4),niv:'',link:'asesoria_SIGEJ.html',txt:[e.folio,e.asunto,e.tipo,e.dependencia].join(' ')}));
 push('Proyectos','📌',J('sigej_proyectos'),e=>({folio:e.id,tit:e.nombre,est:e.estado,resp:e.resp,anio:(e.ini||'').slice(0,4),niv:'',link:'proyectos_SIGEJ.html',txt:[e.nombre,e.tipo,e.dep,e.resp].join(' ')}));
 push('Solicitudes UTI','🔎',J('sigej_uti'),e=>({folio:e.folio,tit:(e.texto||'Solicitud').slice(0,50),est:e.estado||'Registrada',resp:e.responsable,anio:(e.fecha||e.fsol||'').slice(0,4),niv:'',link:'transparencia_SIGEJ.html',txt:[e.folio,e.texto,e.materia,e.respuesta].join(' ')}));
 push('Oficios (Control)','📋',J('sigej_oficios'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.asunto?' · '+e.asunto:''),est:e.estatus,resp:e.resp,anio:e.anio||(e.fecha||'').slice(0,4),niv:'',link:'oficialia_SIGEJ.html',txt:[e.folio,e.tipo,e.asunto,e.demi,e.ddest,e.dest,(e.kw||[]).join(' '),(e.exp||[]).join(' '),e.estatus].join(' ')}));
 push('Help Desk (tickets)','🛠️',J('sigej_helpdesk'),e=>({folio:e.id,tit:(e.tipo||'')+(e.asunto?' · '+e.asunto:''),est:e.estado,resp:e.tec,anio:(e.creado||'').slice(0,4),niv:e.prio,link:'helpdesk_SIGEJ.html',txt:[e.id,e.tipo,e.cat,e.asunto,e.sol,e.dep,e.tec,e.estado].join(' ')}));
 push('Administración · Contable','💵',J('sigej_adm_contable'),e=>({folio:e.id,tit:(e.tipo||'')+(e.concepto?' · '+e.concepto:''),est:e.estado,resp:e.por,anio:(e.fecha||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.tipo,e.concepto,e.benef,e.part,e.exp,e.estado].join(' ')}));
 push('Administración · Bienes','🏷️',J('sigej_adm_bienes'),e=>({folio:e.id,tit:e.desc,est:e.estado,resp:e.resg,anio:(e.adq||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.desc,e.marca,e.modelo,e.etiq,e.serie,e.resg,e.estado,e.motivo].join(' ')}));
 push('Administración · Personal','👥',J('sigej_adm_personal'),e=>({folio:e.id,tit:(e.tipo||'')+(e.nombre?' · '+e.nombre:''),est:e.estado,resp:e.nombre,anio:(e.fecha||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.tipo,e.nombre,e.puesto,e.contr,e.area,e.estado].join(' ')}));
 push('Logística · Comisiones','🚐',J('sigej_log_comisiones'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.destino?' · '+e.destino:''),est:e.estado,resp:e.chofer||e.abog,anio:(e.fecha||'').slice(0,4),niv:e.prio,link:'oficialia_SIGEJ.html',txt:[e.folio,e.tipo,e.destino,e.sol,e.abog,e.chofer,e.vehiculo,e.exp,e.area,e.estado].join(' ')}));
 push('Actuaciones externas','🚶',J('sigej_actuaciones'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.sub?' · '+e.sub:''),est:e.estado,resp:e.abog,anio:(e.fecha||'').slice(0,4),niv:'',link:'contencioso_SIGEJ.html',txt:[e.folio,e.tipo,e.sub,e.exp,e.org,e.juz,e.of,e.obj,e.abog,e.mat,e.estado].join(' ')}));
 push('Viáticos / Comisiones','🧳',J('sigej_adm_viaticos'),e=>({folio:e.folio,tit:(e.comis||'')+(e.obj?' · '+e.obj:''),est:e.estado,resp:e.abog||e.comis,anio:(e.fecha||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.folio,e.comis,e.obj,e.dest,e.drec,e.exp,e.abog,e.estado].join(' ')}));
 push('Conocimiento · Biblioteca','📚',J('sigej_biblioteca'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.autor?' · '+e.autor:''),est:e.estado,resp:e.autor,anio:e.anio||'',niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.autor,e.materia,e.isbn,e.tipo].join(' ')}));
 push('Capacitación','🎓',J('sigej_capacitacion'),e=>({folio:e.folio,tit:(e.tema||'')+(e.clase?' · '+e.clase:''),est:e.estado,resp:e.instructor,anio:(e.fsol||e.fprog||'').slice(0,4),niv:e.prioridad,link:'desarrollo_SIGEJ.html',txt:[e.folio,e.tema,e.clase,e.dep,e.instructor,e.estado].join(' ')}));
 push('Investigación jurídica','🔬',J('sigej_invest'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.autor,anio:(e.fecha||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.autor,e.materia,e.pub].join(' ')}));
 push('Difusión / Conocimiento','📣',J('sigej_difusion'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.resp,anio:(e.fpub||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.canal].join(' ')}));
 push('Observatorio jurídico','🛰️',J('sigej_observatorio'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.fuente?' · '+e.fuente:''),est:e.prioridad,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:e.prioridad,link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.fuente,e.materia].join(' ')}));
 push('Editorial / Conocimiento','📖',J('sigej_editorial'),e=>({folio:e.folio,tit:(e.titulo||'')+(e.tipo?' · '+e.tipo:''),est:e.estado,resp:e.autor,anio:(e.fecha||'').slice(0,4),niv:'',link:'desarrollo_SIGEJ.html',txt:[e.folio,e.titulo,e.tipo,e.autor,e.isbn,e.doi].join(' ')}));
 push('Almacén · Papelería','📦',J('sigej_adm_papeleria'),e=>({folio:e.id,tit:(e.nom||'')+(e.cat?' · '+e.cat:''),est:'',resp:e.prov,anio:(e.alta||'').slice(0,4),niv:'',link:'administracion_SIGEJ.html',txt:[e.id,e.nom,e.cat,e.prov].join(' ')}));
 push('Servicio social · Convenios','🤝',J('sigej_serviciosocial'),e=>({folio:e.folio,tit:(e.dependencia||'')+(e.objeto?' · '+e.objeto:''),est:e.estado,resp:e.resp,anio:(e.fin||'').slice(0,4),niv:'',link:'serviciosocial_SIGEJ.html',txt:[e.folio,e.dependencia,e.sector,e.objeto,e.cu,e.tipo,e.seguro].join(' ')}));
 push('Derechos Humanos (recomendaciones)','🕊️',J('sigej_derechoshumanos'),e=>({folio:e.folio,tit:(e.tipo||'')+' · '+(e.organismo||'').split(' — ')[0]+(e.derecho?' · '+e.derecho:''),est:e.estado,resp:e.resp,anio:(e.fRecep||'').slice(0,4),niv:'',link:'contencioso_SIGEJ.html',txt:[e.folio,e.organismo,e.tipo,e.numero,e.derecho,e.area,e.hechos].join(' ')}));
 push('Investigación (gobierno)','🔬',J('sigej_inv_investigadores'),e=>({folio:e.folio,tit:(e.nombre||'')+(e.snii&&e.snii!=='No'?' · '+e.snii:''),est:e.prodep,resp:e.nombre,anio:(e.fAlta||'').slice(0,4),niv:'',link:'gobinv_SIGEJ.html',txt:[e.folio,e.nombre,e.cu,e.area,e.snii,e.ca,e.lgac].join(' ')}));
 push('Laboratorios','🧪',J('sigej_lab'),e=>({folio:e.folio,tit:(e.nombre||'')+(e.bsl?' · '+e.bsl:''),est:e.estado,resp:e.respTecnico,anio:(e.fVenc||'').slice(0,4),niv:'',link:'laboratorios_SIGEJ.html',txt:[e.folio,e.nombre,e.cu,e.tipo,e.bsl,e.respTecnico,e.licencia].join(' ')}));
 push('Derecho Deportivo','🏅',J('sigej_deportivo'),e=>({folio:e.folio,tit:(e.tipo||'')+(e.entidad?' · '+e.entidad:''),est:e.estado,resp:e.resp,anio:(e.fecha||'').slice(0,4),niv:'',link:'deportivo_SIGEJ.html',txt:[e.folio,e.tipo,e.ambito,e.entidad,e.organismo,e.derecho,e.hechos,e.resp].join(' ')}));
 ALL=A;return A;}
function modList(){return Array.from(new Set(ALL.map(r=>r.mod)));}
function tab(id){document.querySelectorAll('.tab').forEach(s=>s.classList.toggle('on',s.id===id));
 document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 if(id==='t1')renderBuscador();if(id==='t2')renderStats();if(id==='t3')renderMatrices();if(id==='t4')renderRep();if(id==='t6')renderCob();if(id==='t9')renderObl();
 if(id==='t5'){var fr=el('utiFrame');if(fr&&!fr.src)fr.src=fr.dataset.src;}
 if(id==='t7'){var rf=el('repFrame');if(rf&&!rf.src)rf.src=rf.dataset.src;}
 if(id==='t8'){var bf=el('bitFrame');if(bf&&!bf.src)bf.src=bf.dataset.src;}
 if(id==='t10'){var af=el('agPubFrame');if(af&&!af.src)af.src=af.dataset.src;}}
function chart(id,type,labels,data,opts){if(!window.Chart)return;if(CH[id])CH[id].destroy();const ctx=el(id);if(!ctx)return;
 CH[id]=new Chart(ctx,{type:type,data:{labels:labels,datasets:[{data:data,backgroundColor:opts&&opts.multi?PAL:(opts&&opts.color||'#1aa39a')}]},
  options:{indexAxis:opts&&opts.horiz?'y':'x',plugins:{legend:{display:!!(opts&&opts.legend),position:'right',labels:{color:'#0a4d8c',font:{size:9}}}},
   scales:type==='doughnut'?{}:{x:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}},y:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}}}}});}
function cnt(arr,key){const o={};arr.forEach(e=>{const v=(e[key]||'(s/d)');o[v]=(o[v]||0)+1;});return o;}
/* t1 buscador */
function fillFilters(){const fm=el('fMod');const mc=fm.value;fm.innerHTML='<option value="">Todos los módulos</option>'+modList().map(m=>'<option'+(m===mc?' selected':'')+'>'+m+'</option>').join('');
 const ys=Array.from(new Set(ALL.map(r=>r.anio).filter(Boolean))).sort().reverse();const fy=el('fAnio');const yc=fy.value;fy.innerHTML='<option value="">Todo año</option>'+ys.map(y=>'<option'+(y==yc?' selected':'')+'>'+y+'</option>').join('');
 const rm=el('rMod');if(rm)rm.innerHTML=modList().map(m=>'<option>'+m+'</option>').join('');}
function filtered(){const q=(val('q')||'').toLowerCase();const fm=val('fMod'),fy=val('fAnio'),fn=val('fNiv');
 return ALL.filter(r=>(!fm||r.mod===fm)&&(!fy||String(r.anio)===fy)&&(!fn||r.niv===fn)&&(!q||r.txt.indexOf(q)>=0));}
function renderBuscador(){const arr=filtered();el('cnt').textContent=arr.length+' de '+ALL.length+' registros';
 const box=el('lista');const show=arr.slice(0,400);
 box.innerHTML=arr.length?show.map(r=>'<div class="it"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><span class="t">'+(r.folio||'—')+' · '+(r.tit||'').slice(0,70)+'</span><span><span class="chip">'+r.ic+' '+r.mod+'</span>'+(r.niv?' '+rb(r.niv):'')+'</span></div><div class="m">'+(r.est?'estado: '+r.est:'')+(r.resp?' · '+r.resp:'')+(r.anio?' · '+r.anio:'')+' · <a class="lk" href="'+r.link+'">abrir módulo →</a></div></div>').join('')+(arr.length>400?'<div style="color:#64748b;font-size:11px;padding:6px">Mostrando 400 de '+arr.length+'. Afina la búsqueda o exporta el CSV completo.</div>':''):'<div class="note">Sin coincidencias. Recuerda que el buscador cubre todo lo capturado en cada módulo; algunos arrancan vacíos.</div>';
 const t=new Date();el('upd').textContent='actualizado '+pad(t.getHours())+':'+pad(t.getMinutes())+':'+pad(t.getSeconds());}
function exportBuscador(){csv(filtered(),'transparencia_busqueda.csv');}
function csv(arr,name){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const cab=['modulo','folio','titulo','estado','responsable','anio','nivel'];
 const rows=arr.map(r=>[r.mod,r.folio,r.tit,r.est,r.resp,r.anio,r.niv].map(esc).join(','));
 const b=new Blob(['﻿'+cab.join(',')+'\n'+rows.join('\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;a.click();}
function exportTodo(){csv(ALL,'transparencia_base_completa.csv');}
/* t2 estadísticas */
function renderStats(){const porMod=cnt(ALL,'mod');const conDatos=Object.keys(porMod).length;
 const niv=ALL.filter(r=>r.niv).length;const hi=ALL.filter(r=>r.niv==='Alto'||r.niv==='Crítico').length;
 const K=[['',ALL.length,'Registros (todo el sistema)',''],['',conDatos,'Módulos con datos','y'],['',hi,'Riesgo alto','r'],['',new Set(ALL.map(r=>r.resp).filter(Boolean)).size,'Responsables','']];
 el('stKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 const pm=Object.entries(porMod).sort((a,b)=>b[1]-a[1]);chart('cMod','bar',pm.map(x=>x[0].split(' ')[0]),pm.map(x=>x[1]),{horiz:true,color:'#0a4d8c'});
 const nv={};['Crítico','Alto','Medio','Bajo'].forEach(n=>nv[n]=ALL.filter(r=>r.niv===n).length);chart('cNiv','doughnut',Object.keys(nv),Object.values(nv),{multi:true,legend:true});
 const an=cnt(ALL.filter(r=>r.anio),'anio');const ak=Object.keys(an).sort();chart('cAnio','bar',ak,ak.map(k=>an[k]),{color:'#1aa39a'});}
/* t3 matrices */
function mkey(r,k){return r[k]==null?'':String(r[k]).trim();}
function matriz(rowKey){const mods=modList();const cols=Array.from(new Set(ALL.map(r=>mkey(r,rowKey)).filter(Boolean))).sort();
 if(rowKey==='niv'){cols.length=0;['Crítico','Alto','Medio','Bajo'].forEach(c=>cols.push(c));}
 const cell={};mods.forEach(m=>{cell[m]={};cols.forEach(c=>cell[m][c]=0);});let mx=1;
 ALL.forEach(r=>{const c=mkey(r,rowKey);if(c&&cell[r.mod]&&cell[r.mod][c]!==undefined){cell[r.mod][c]++;mx=Math.max(mx,cell[r.mod][c]);}});
 return {mods:mods,cols:cols,cell:cell,mx:mx};}
function renderMatrices(){
 const n=matriz('niv');el('mxNiv').innerHTML='<tr><th class="lab">Módulo \\ Nivel</th>'+n.cols.map(c=>'<th>'+c+'</th>').join('')+'<th>Total</th></tr>'+
  n.mods.map(m=>{let tot=0;return '<tr><td class="lab">'+m+'</td>'+n.cols.map(c=>{const v=n.cell[m][c];tot+=v;const a=v/n.mx;const col=c==='Crítico'?'192,57,43':c==='Alto'?'234,88,12':c==='Medio'?'224,142,11':'31,157,107';return '<td style="background:rgba('+col+','+(v?0.15+a*0.7:0.04)+');color:#fff">'+v+'</td>';}).join('')+'<td><b>'+tot+'</b></td></tr>';}).join('');
 const y=matriz('anio');el('mxAnio').innerHTML='<tr><th class="lab">Módulo \\ Año</th>'+y.cols.map(c=>'<th>'+c+'</th>').join('')+'<th>Total</th></tr>'+
  y.mods.map(m=>{let tot=0;return '<tr><td class="lab">'+m+'</td>'+y.cols.map(c=>{const v=y.cell[m][c];tot+=v;const a=v/y.mx;return '<td style="background:rgba(26,163,154,'+(v?0.12+a*0.7:0.04)+');color:#fff">'+v+'</td>';}).join('')+'<td><b>'+tot+'</b></td></tr>';}).join('');}
function exportMatriz(t){const M=matriz(t==='niv'?'niv':'anio');const esc=v=>'"'+String(v).replace(/"/g,'""')+'"';
 let rows=['modulo,'+M.cols.map(esc).join(',')+',total'];
 M.mods.forEach(m=>{let tot=0;const r=M.cols.map(c=>{tot+=M.cell[m][c];return M.cell[m][c];});rows.push(esc(m)+','+r.join(',')+','+tot);});
 const b=new Blob(['﻿'+rows.join('\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='matriz_'+t+'.csv';a.click();}
/* t4 reportes */
function renderRep(){fillFilters();const porMod=cnt(ALL,'mod');
 el('rPrev').innerHTML='<table><tr><th>Módulo / área</th><th>Registros</th><th>Riesgo alto</th><th>Responsables</th></tr>'+modList().map(m=>{const rs=ALL.filter(r=>r.mod===m);return '<tr><td>'+(rs[0]?rs[0].ic:'')+' '+m+'</td><td><b>'+rs.length+'</b></td><td>'+rs.filter(r=>r.niv==='Alto'||r.niv==='Crítico').length+'</td><td>'+new Set(rs.map(r=>r.resp).filter(Boolean)).size+'</td></tr>';}).join('')+'</table>';}
function W(body){return '<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';}
function dl(html,name){const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;a.click();}
function reporteConsolidadoWord(){const mods=modList();
 let tbl='<table border="1" cellpadding="6" style="border-collapse:collapse;width:100%;font-size:10pt"><tr><th>Módulo / área</th><th>Registros</th><th>Riesgo alto</th><th>Responsables</th></tr>';
 mods.forEach(m=>{const rs=ALL.filter(r=>r.mod===m);tbl+='<tr><td>'+m+'</td><td>'+rs.length+'</td><td>'+rs.filter(r=>r.niv==='Alto'||r.niv==='Crítico').length+'</td><td>'+new Set(rs.map(r=>r.resp).filter(Boolean)).size+'</td></tr>';});
 tbl+='<tr><td><b>TOTAL</b></td><td><b>'+ALL.length+'</b></td><td><b>'+ALL.filter(r=>r.niv==='Alto'||r.niv==='Crítico').length+'</b></td><td>—</td></tr></table>';
 const body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Transparencia y Rendición de Cuentas</div>'+
  '<h2>REPORTE CONSOLIDADO INSTITUCIONAL</h2><p style="font-size:11pt">Corte: '+D.corte+' · Total de registros del sistema: '+ALL.length+' · Módulos con datos: '+mods.length+'.</p>'+tbl+
  '<p style="font-size:9pt;color:#666">Generado por el SIGEJ-UdeG (prototipo). Cifras derivadas de lo capturado en cada módulo; distingue dato capturado de proxy. PNT/OCR/semántica = fase backend.</p>';
 dl(W(body),'Reporte_consolidado_transparencia.doc');}
function reporteModuloCSV(){const m=val('rMod');csv(ALL.filter(r=>r.mod===m),'reporte_'+m.replace(/[^a-zA-Z]/g,'_')+'.csv');}
function reporteModuloWord(){const m=val('rMod');const rs=ALL.filter(r=>r.mod===m);
 let tbl='<table border="1" cellpadding="5" style="border-collapse:collapse;width:100%;font-size:9pt"><tr><th>Folio</th><th>Asunto</th><th>Estado</th><th>Responsable</th><th>Año</th></tr>';
 rs.slice(0,300).forEach(r=>{tbl+='<tr><td>'+(r.folio||'')+'</td><td>'+(r.tit||'')+'</td><td>'+(r.est||'')+'</td><td>'+(r.resp||'')+'</td><td>'+(r.anio||'')+'</td></tr>';});tbl+='</table>';
 const body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Transparencia · '+m+'</div><h2>REPORTE — '+m+'</h2><p style="font-size:11pt">Registros: '+rs.length+'</p>'+tbl;
 dl(W(body),'Reporte_'+m.replace(/[^a-zA-Z]/g,'_')+'.doc');}
/* t6 cobertura */
function renderCob(){const porMod=cnt(ALL,'mod');
 el('cobBox').innerHTML='<table><tr><th>Fuente / módulo</th><th>Registros</th></tr>'+modList().map(m=>{const rs=ALL.filter(r=>r.mod===m);return '<tr><td>'+(rs[0]?rs[0].ic:'')+' '+m+'</td><td><b>'+rs.length+'</b></td></tr>';}).join('')+'<tr><td><b>TOTAL</b></td><td><b>'+ALL.length+'</b></td></tr></table>';}
/* init */
window.addEventListener('storage',()=>{loadAll();if(el('t1').classList.contains('on'))renderBuscador();});
window.addEventListener('focus',()=>{loadAll();});
loadAll();fillFilters();renderBuscador();
</script>
__SNIP__
</body></html>"""
html=TPL.replace("__DATA__",DATAJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"transparencia_general_SIGEJ.html","w",encoding="utf-8").write(html)
print("transparencia_general_SIGEJ.html OK -",len(html),"bytes | exp embebidos:",len(DATA["exp"]))
