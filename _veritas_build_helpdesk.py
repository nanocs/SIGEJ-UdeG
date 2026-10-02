# -*- coding: utf-8 -*-
# Help Desk / ITSM (ITIL v4) para la Oficina de la Abogacía General — Service Desk, Incidentes, Solicitudes,
# Problemas, Cambios, CMDB/Inventario, Activos de software, Base de conocimiento, SLA, BI, Ciberseguridad,
# Soporte al Legal ERP (monitorea los módulos del sistema) y Centro de Mando del CIO. Cliente, localStorage.
import json
B="/Users/edithroque/Documents/CLAUDE/"
DATA={
 "corte":"2026-06-18",
 "tecnicos":["Mesa de servicio (N1)","Ing. Hernández — Redes (N2)","Ing. Ramírez — Sistemas (N2)","Lic. Gómez — M365 (N2)","Admin. Torres — Infraestructura (N3)","Proveedor externo (N4)"],
 "deps":["Oficina de la Abogacía General","Rectoría General","Secretaría General","CGADT","CUCEI","CUCEA","CUCS","CUCSH","CUAAD","CUCBA","CUCER","SEMS","CGTI","Coordinación de Personal"],
 "catInc":["Hardware","Software","Redes","Correo electrónico","Equipo de cómputo","Impresoras","Aplicaciones jurídicas","Bases de datos","Microsoft 365","SharePoint","Seguridad informática","Telefonía","Videoconferencia","Infraestructura","Accesos","Cuentas de usuario","Power BI","Sistema de gestión jurídica (SIGEJ)"],
 "catSol":["Alta de usuario","Baja de usuario","Cambio de permisos","Instalación de programa","Configuración de cuenta","Recuperación de contraseña","Solicitud de equipo","Solicitud de licencia","Solicitud de acceso","Configuración de VPN","Creación de buzón","Solicitud de respaldo","Recuperación de información"],
 "catChg":["Actualización","Migración","Implementación","Configuración","Cambio de infraestructura","Nuevo sistema"],
 "claseCI":["Equipo de cómputo","Laptop","Servidor","Impresora","Switch / Red","Teléfono IP","Licencia / Software","Base de datos","Aplicación","Activo tecnológico"],
 "swProd":["Microsoft 365","Adobe Creative Cloud","Antivirus / EDR","Sistema jurídico SIGEJ","Power BI","Herramienta de IA","Sistema operativo Windows","Sistema operativo Server","Otro"],
 "kbTipos":["Manual","Pregunta frecuente (FAQ)","Solución conocida","Procedimiento","Guía","Tutorial","Política","Configuración","Error común"],
 "secTipos":["Malware","Phishing","Acceso indebido","Pérdida de información","Vulnerabilidad","Fuga de datos","Ransomware","Otro"],
 "modulos":[
  {"n":"Oficialía de Partes","k":"sigej_oficialia","link":"oficialia_SIGEJ.html","ic":"📨"},
  {"n":"Control de Oficios","k":"sigej_oficios","link":"oficialia_SIGEJ.html","ic":"📋"},
  {"n":"Instrumentos Jurídicos","k":"sigej_instrumentos","link":"instrumentos_SIGEJ.html","ic":"📜"},
  {"n":"Litigio (altas locales)","k":"sigej_capturas","link":"contencioso_SIGEJ.html","ic":"⚔️"},
  {"n":"Patrimonio Intangible","k":"sigej_patrimonio","link":"patrimonio_SIGEJ.html","ic":"🧩"},
  {"n":"Asuntos Internacionales","k":"sigej_internacional","link":"internacional_SIGEJ.html","ic":"🌎"},
  {"n":"Normatividad","k":"sigej_normatividad","link":"normatividad_SIGEJ.html","ic":"📖"},
  {"n":"MASC","k":"sigej_masc","link":"contencioso_SIGEJ.html","ic":"🤝"},
  {"n":"Responsabilidades","k":"sigej_resp","link":"contencioso_SIGEJ.html","ic":"⚖️"},
  {"n":"Asesoría / Consultas","k":"sigej_asesoria","link":"contencioso_SIGEJ.html","ic":"💡"},
  {"n":"Proyectos","k":"sigej_proyectos","link":"contencioso_SIGEJ.html","ic":"📌"},
  {"n":"Transparencia (UTI)","k":"sigej_uti","link":"transparencia_general_SIGEJ.html","ic":"🔎"},
  {"n":"Bitácora del sistema","k":"sigej_bitacora","link":"transparencia_general_SIGEJ.html","ic":"🧾"}
 ]
}
# Competencias y roles jurídicos — movidos desde Instrumentos (gobernanza IAM del Legal ERP).
# Fuente única: catálogos generados por _veritas_build_instrumentos.py (sin duplicar a mano).
try:
    _cr=json.load(open(B+"instrumentos_catalogos.json",encoding="utf-8"))
    DATA["cr_areas"]=_cr.get("areas",{});DATA["cr_familias"]=_cr.get("familias",[])
    DATA["cr_roles"]=_cr.get("roles",[]);DATA["cr_raci"]=_cr.get("raci",[])
except Exception as _e:
    DATA["cr_areas"]={};DATA["cr_familias"]=[];DATA["cr_roles"]=[];DATA["cr_raci"]=[]
    print("AVISO: no se pudo leer instrumentos_catalogos.json ->",_e)
DATAJ=json.dumps(DATA,ensure_ascii=False)

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html" class="act">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''

SNIP=r"""<script>
/* SIGEJ — Control de acceso por perfil (capa de interfaz, sin backend) */
(function(){
 var SOLO=['SIGEJ_inicio','buscador_SIGEJ'];var JEFE=['SIGEJ_inicio','dashboard_SIGEJ','instrumentos_SIGEJ','patrimonio_SIGEJ','internacional_SIGEJ','normatividad_SIGEJ','contencioso_SIGEJ','buscador_SIGEJ','transparencia_general_SIGEJ','oficialia_SIGEJ','helpdesk_SIGEJ','administracion_SIGEJ','chat_SIGEJ','notificaciones_SIGEJ','alertas_centro_SIGEJ','recepcion_SIGEJ','biblioteca_SIGEJ','cumplimiento_SIGEJ','laboral_SIGEJ'];var ABOG=['SIGEJ_inicio','dashboard_SIGEJ','instrumentos_SIGEJ','patrimonio_SIGEJ','internacional_SIGEJ','normatividad_SIGEJ','contencioso_SIGEJ','buscador_SIGEJ','oficialia_SIGEJ','helpdesk_SIGEJ','chat_SIGEJ','notificaciones_SIGEJ','alertas_centro_SIGEJ','recepcion_SIGEJ','biblioteca_SIGEJ','cumplimiento_SIGEJ','laboral_SIGEJ'];var PERMS={'Administrador':null,'Abogado General':null,'Coordinador Jurídico':null,'Coordinador de Enlace con la Red':null,'Coordinador de Normatividad':null,'Secretaría General':SOLO,'Director':SOLO,'Coordinador General':SOLO,'Jefe de Unidad de lo Contencioso':JEFE,'Jefe de Unidad de Atención y Servicios Legales':JEFE,'Jefe de Unidad de Patrimonio Intangible':JEFE,'Jefe de Unidad de Asuntos Internacionales':JEFE,'Jefe de Unidad de Instrumentos Jurídicos':JEFE,'Jefe de Unidad de Capacitación, Investigación y Difusión':JEFE,'Jefe de Unidad de Estatutos y Reglamentos':JEFE,'Jefe de Unidad de Normatividad Administrativa':JEFE,'Jefe de Unidad de Apoyo a Órganos Colegiados':JEFE,'Jefe del Área Contable':JEFE,'Jefe del Área de Personal':JEFE,'Jefe del Área de Sistemas':JEFE,'Jefe de Oficialía de Partes':JEFE,'Jefe de Mensajería':JEFE,'Abogado':ABOG,'Analista':ABOG,'Asistente':ABOG,'Sistemas':null};
 var ROLES=Object.keys(PERMS);var perfil=localStorage.getItem('sigej_perfil');
 var pageKey=(location.pathname.split('/').pop()||'SIGEJ_inicio.html').replace('.html','')||'SIGEJ_inicio';
 function allowed(p){return PERMS[p]===null?null:PERMS[p];}
 function overlay(html){var d=document.createElement('div');d.style.cssText='position:fixed;inset:0;background:rgba(8,20,38,.78);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;font-family:Segoe UI,system-ui,sans-serif';d.innerHTML='<div style="background:#fff;border-radius:16px;max-width:440px;width:100%;padding:26px;box-shadow:0 12px 40px rgba(0,0,0,.4)">'+html+'</div>';document.body.appendChild(d);return d;}
 function pick(){var __G=[['Nivel 100 · Administración',['Administrador']],['Nivel 90 · Dirección superior',['Abogado General']],['Nivel 80 · Coordinaciones',['Coordinador Jurídico','Coordinador de Enlace con la Red','Coordinador de Normatividad']],['Nivel 70 · Secretaría y Dirección',['Secretaría General','Director','Coordinador General']],['Nivel 50 · Jefaturas de Unidad y Área',['Jefe de Unidad de lo Contencioso','Jefe de Unidad de Atención y Servicios Legales','Jefe de Unidad de Patrimonio Intangible','Jefe de Unidad de Asuntos Internacionales','Jefe de Unidad de Instrumentos Jurídicos','Jefe de Unidad de Capacitación, Investigación y Difusión','Jefe de Unidad de Estatutos y Reglamentos','Jefe de Unidad de Normatividad Administrativa','Jefe de Unidad de Apoyo a Órganos Colegiados','Jefe del Área Contable','Jefe del Área de Personal','Jefe del Área de Sistemas','Jefe de Oficialía de Partes','Jefe de Mensajería']],['Nivel 30 · Operativo jurídico',['Abogado','Analista']],['Nivel 10 · Apoyo',['Asistente']],['Nivel 1 · Sistemas',['Sistemas']]];var __u={};var opt=__G.map(function(g){var o=g[1].filter(function(r){return PERMS.hasOwnProperty(r);}).map(function(r){__u[r]=1;return '<option>'+r+'</option>';}).join('');return o?'<optgroup label="'+g[0]+'">'+o+'</optgroup>':'';}).join('');var __r=ROLES.filter(function(r){return !__u[r];}).map(function(r){return '<option>'+r+'</option>';}).join('');if(__r)opt+='<optgroup label="Otros">'+__r+'</optgroup>';
  var d=overlay('<h2 style="margin:0 0 4px;color:#00254a;font-size:19px">⚖️ SIGEJ-UdeG</h2><div style="color:#64748b;font-size:13px;margin-bottom:16px">Selecciona tu perfil para personalizar el acceso.</div><select id="__perf" style="width:100%;padding:10px;border:1px solid #e2e8f0;border-radius:8px;font-size:14px;margin:4px 0 16px">'+opt+'</select><button id="__ok" style="width:100%;padding:11px;border:none;border-radius:9px;background:#1f9d6b;color:#fff;font-weight:600;font-size:14px;cursor:pointer">Entrar</button><div style="font-size:10.5px;color:#94a3b8;margin-top:12px">Control de interfaz (prototipo). Seguridad real (MFA, backend) = fase de implementación.</div>');
  d.querySelector('#__ok').onclick=function(){localStorage.setItem('sigej_perfil',d.querySelector('#__perf').value);location.reload();};}
 function badge(){var b=document.createElement('div');b.style.cssText='position:fixed;right:12px;bottom:12px;z-index:9000;background:#00254a;color:#fff;border-radius:20px;padding:7px 13px;font-size:12px;box-shadow:0 3px 12px rgba(0,0,0,.3);font-family:Segoe UI,system-ui,sans-serif';
  var __HD=['Administrador','Sistemas','Jefe del Área de Sistemas'];var __ver=__HD.indexOf(perfil)>=0;b.innerHTML='👤 '+(__ver?perfil:'Sesión activa')+' <span style="opacity:.6">·</span> <span id="__chg" style="cursor:pointer;text-decoration:underline">salir</span>';document.body.appendChild(b);
  b.querySelector('#__chg').onclick=function(){localStorage.removeItem('sigej_perfil');localStorage.removeItem('sigej_sesion');location.replace('acceso_SIGEJ.html');};}
 function apply(){var allow=allowed(perfil);
  document.querySelectorAll('.navbar a').forEach(function(a){var k=(a.getAttribute('href')||'').replace('.html','');if(k==='SIGEJ_inicio'||!k)return;if(allow&&allow.indexOf(k)<0)a.style.display='none';});
  if(allow&&allow.indexOf(pageKey)<0&&pageKey!=='SIGEJ_inicio'){overlay('<h2 style="margin:0 0 6px;color:#c0392b">Acceso restringido</h2><div style="color:#475569;font-size:13px;margin-bottom:16px">El perfil <b>'+perfil+'</b> no tiene acceso a este módulo.</div><a href="SIGEJ_inicio.html" style="display:inline-block;padding:10px 16px;background:#0a4d8c;color:#fff;border-radius:8px;text-decoration:none;font-weight:600">← Volver al inicio</a> <button onclick="localStorage.removeItem(\'sigej_perfil\');location.reload()" style="margin-left:8px;padding:10px 14px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;cursor:pointer">Cambiar perfil</button>');return;}
  if(perfil==='Consulta'){document.querySelectorAll('button').forEach(function(b){var t=(b.textContent||'');if(/registrar|crear|guardar|asignar|resolver|cerrar|escalar|aprobar|eliminar|cargar demo/i.test(t)){b.disabled=true;b.style.opacity=.4;}});}
 }
 if(!perfil){if(!/[?&]embed=1/.test(location.search)){location.replace('acceso_SIGEJ.html');}return;}else{apply();badge();if(['Abogado General','Sistemas','Secretaría General','Director','Coordinador General'].indexOf(perfil)>=0){setTimeout(function(){document.querySelectorAll('button,.lk,.del').forEach(function(b){var t=(b.textContent||'')+(b.title||'');if(/guardar|registrar|crear|captur|recibir|turnar|elimina|borrar|baja|adjuntar|generar|autoriz|pagar|aplicar|asignar|cargar demo|resolver|escalar|aprobar|publicar|solicitar|despach|＋/i.test(t)){b.disabled=true;b.style.opacity=.45;b.title='Perfil de solo lectura / consulta';}});},450);}}
})();
</script><script>
/* SIGEJ — Bitácora de auditoría */
(function(){try{var perfil=localStorage.getItem('sigej_perfil')||'(sin perfil)';
 function blog(tipo,accion){try{var L=JSON.parse(localStorage.getItem('sigej_bitacora')||'[]');L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:perfil,modulo:'Help Desk / ITSM',tipo:tipo,accion:String(accion||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);localStorage.setItem('sigej_bitacora',JSON.stringify(L));}catch(e){}}
 window.__bitlog=blog;blog('Acceso','Ingreso al módulo');
 var RX=/registrar|crear|guardar|asignar|resolver|cerrar|escalar|aprobar|exportar|csv|cargar demo/i;
 document.addEventListener('click',function(ev){try{var el=ev.target&&ev.target.closest&&ev.target.closest('button,.lk');if(!el)return;var txt=(el.textContent||'').trim().replace(/\s+/g,' ');if(RX.test(txt)&&txt.length<70)blog('Acción',txt);}catch(e){}},true);
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
<title>SIGEJ-UdeG · Help Desk / ITSM</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--amber:#e08e0b;--ok:#1f9d6b;--ink:#0a1f3c;--mut:#64748b;--card:#ffffff;--card2:#f8fafc;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:radial-gradient(1200px 600px at 80% -10%,transparent,transparent),var(--bg);color:var(--ink)}
header{padding:14px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;border-bottom:1px solid var(--line)}
header h1{margin:0;font-size:18px}header .s{opacity:.8;font-size:12px;margin-top:3px}
.navbar{background:#06182c;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#475569;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.live{display:inline-flex;align-items:center;gap:6px;background:rgba(31,157,107,.15);color:#7ee0b4;border:1px solid rgba(31,157,107,.4);border-radius:20px;padding:5px 12px;font-size:12px}
.dot{width:8px;height:8px;border-radius:50%;background:#2ee08a;animation:p 1.5s infinite}@keyframes p{50%{opacity:.3}}
.tabbar{display:flex;flex-wrap:wrap;gap:6px;padding:14px 24px 0;max-width:1440px;margin:auto}
.tb{background:var(--card);color:#475569;border:1px solid var(--line);border-bottom:none;border-radius:11px 11px 0 0;padding:10px 15px;font-size:13px;font-weight:600;cursor:pointer}
.tb:hover{color:#fff}.tb.on{background:var(--azul2);color:#fff;border-color:var(--azul2)}
.wrap{padding:14px 24px 34px;max-width:1440px;margin:auto}
.tab{display:none}.tab.on{display:block}
.h{font-size:14px;color:#0a4d8c;font-weight:700;margin:16px 0 10px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:14px}
.kpi{background:linear-gradient(160deg,var(--card),var(--card2));border:1px solid var(--line);border-radius:13px;padding:14px}
.kpi .n{font-size:24px;font-weight:800}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.g .n{color:#7ee0b4}.kpi.r .n{color:#ff9b8d}.kpi.y .n{color:#ffce82}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:15px}
.card h3{margin:0 0 10px;font-size:13px;color:#0a4d8c}.card.s2{grid-column:span 2}
canvas{max-height:240px}
.f{display:inline-flex;flex-direction:column;gap:3px;margin:0 8px 9px 0}.f label{font-size:11px;color:var(--mut);font-weight:600}
.f input,.f select,.f textarea{padding:7px 8px;border:1px solid var(--line);border-radius:6px;font-size:12.5px;background:#f1f5fb;color:var(--ink);min-width:150px}
.f textarea{min-width:320px;min-height:44px}
button{padding:8px 13px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
.b1{background:var(--azul2)}.b3{background:var(--ok)}.bw{background:#2b579a}.bd{background:#33507a}.bg{background:var(--gold);color:#3a2c05}.mini{padding:4px 9px;font-size:11px}
.comp{background:#f1f5fb;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12px}.comp b{color:#0a4d8c}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px}.bar input,.bar select{padding:6px 8px;border:1px solid var(--line);border-radius:6px;font-size:12px;background:#f1f5fb;color:var(--ink)}
.it{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:12px;margin-bottom:9px;cursor:pointer}.it:hover{border-color:var(--teal)}
.it .t{font-weight:700;color:#0a4d8c;font-size:13px}.it .m{font-size:11px;color:var(--mut);margin-top:3px}
.chip{display:inline-block;background:#f1f5fb;border:1px solid var(--line);border-radius:9px;padding:2px 8px;font-size:10px;color:#475569;margin:1px}
.sem{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:4px}
.heat{width:100%;border-collapse:collapse;font-size:11.5px}.heat td,.heat th{padding:6px;text-align:center;border:2px solid var(--bg)}.heat th{color:var(--mut)}.heat td.lab{text-align:left;color:#0a4d8c}
table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:7px 8px;text-align:left;border-bottom:1px solid var(--line)}th{color:var(--mut)}
.rb{font-size:10px;padding:2px 8px;border-radius:9px;font-weight:600}.rb-Crítico{background:rgba(192,57,43,.25);color:#ff9b8d}.rb-Alto{background:rgba(234,88,12,.22);color:#ffb38f}.rb-Medio{background:rgba(224,142,11,.2);color:#ffce82}.rb-Bajo{background:rgba(31,157,107,.2);color:#8fe0d8}.rb-Indeterminado{background:rgba(143,166,196,.18);color:var(--mut)}
.tl{border-left:2px solid var(--line);margin-left:6px;padding-left:14px}
.tl .ev{position:relative;margin-bottom:7px;font-size:11.5px;color:#475569;line-height:1.4}
.tl .ev:before{content:'';position:absolute;left:-21px;top:4px;width:8px;height:8px;border-radius:50%;background:var(--teal);box-shadow:0 0 0 2px var(--bg)}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:26px;text-align:center;color:var(--mut);font-size:13px}
.warn{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:9px;padding:9px 12px;font-size:11.5px;color:#e8cf95;margin:8px 0}
a.dl{color:#7ee0b4}.lk{color:#7ee0b4;cursor:pointer}
.slabar{height:8px;border-radius:5px;background:#f1f5fb;overflow:hidden;margin-top:4px}.slabar > span{display:block;height:100%}
.drawer{position:fixed;inset:0;background:rgba(4,12,24,.72);display:none;align-items:center;justify-content:center;z-index:9000;padding:18px}
.drawer.on{display:flex}.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;max-width:960px;width:100%;max-height:90vh;overflow:auto;padding:20px}
.panel .x{float:right;cursor:pointer;color:var(--mut);font-size:20px}
footer{padding:14px 24px;color:#64748b;font-size:11px;text-align:center}
/* HDR-UNIF · encabezado institucional unificado SIGEJ-UdeG */
header{background:linear-gradient(120deg,#00254a 0%,#0a4d8c 100%)!important;color:#fff!important;border-bottom:none!important;padding:14px 24px!important}
header h1{margin:0!important;font-size:18px!important;font-weight:700!important;color:#fff!important;letter-spacing:.2px}
header .s,header .sub{opacity:.85!important;font-size:12px!important;margin-top:3px!important;color:#e6eefb!important}
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
<header><div><h1>🛠️ SIGEJ-UdeG · Help Desk &amp; ITSM — Service Desk de la Abogacía General</h1>
<div class="s">ITIL v4 · incidentes, solicitudes, problemas, cambios, CMDB, base de conocimiento, SLA, ciberseguridad y soporte al Legal ERP</div></div>
<div style="text-align:right"><span class="live"><span class="dot"></span>En vivo · <span id="upd"></span></span> <button class="b1 mini" onclick="reloadAll();compute()">↻ Actualizar</button></div></header>
__NAV__
<div class="tabbar">
 <button class="tb on" data-t="t1" onclick="tab('t1')">🎫 Mesa de ayuda</button>
 <button class="tb" data-t="t2" onclick="tab('t2')">🌐 Autoservicio</button>
 <button class="tb" data-t="t3" onclick="tab('t3')">🧩 CMDB / Inventario</button>
 <button class="tb" data-t="t4" onclick="tab('t4')">💿 Activos de software</button>
 <button class="tb" data-t="t5" onclick="tab('t5')">📚 Base de conocimiento</button>
 <button class="tb" data-t="t6" onclick="tab('t6')">⏱️ SLA y escalamiento</button>
 <button class="tb" data-t="t7" onclick="tab('t7')">🛰️ Tablero BI</button>
 <button class="tb" data-t="t8" onclick="tab('t8')">🩺 Soporte al Legal ERP</button>
 <button class="tb" data-t="t9" onclick="tab('t9')">🛡️ Ciberseguridad</button>
 <button class="tb" data-t="t10" onclick="tab('t10')">🎯 Centro de Mando (CIO)</button>
 <button class="tb" data-t="t11" onclick="tab('t11')">🔐 Usuarios y seguridad (IAM)</button>
 <button class="tb" data-t="t12" onclick="tab('t12')">🏛️ Competencias y roles</button>
</div>
<div class="wrap">
 <section id="t1" class="tab on">
  <div class="card"><h3>🎫 Registrar ticket (incidente · solicitud · problema · cambio)</h3>
   <div class="f"><label>Tipo</label><select id="i_tipo" onchange="catByTipo();idPrev()"></select></div>
   <div class="f"><label>Categoría</label><select id="i_cat"></select></div>
   <div class="f"><label>ID (consecutivo)</label><input id="i_id" readonly style="font-weight:700;color:#8fe0d8"></div>
   <div class="f" style="display:flex"><label>Asunto</label><input id="i_asunto"></div>
   <div class="f" style="display:flex"><label>Descripción</label><textarea id="i_desc"></textarea></div>
   <div class="f"><label>Solicitante</label><input id="i_sol"></div>
   <div class="f"><label>Dependencia</label><select id="i_dep"></select></div>
   <div class="f"><label>Impacto</label><select id="i_imp"><option>Alto</option><option selected>Medio</option><option>Bajo</option></select></div>
   <div class="f"><label>Urgencia</label><select id="i_urg"><option>Alta</option><option selected>Media</option><option>Baja</option></select></div>
   <div class="f"><label>Prioridad (auto)</label><input id="i_prio" readonly></div>
   <div class="f"><label>Técnico asignado</label><select id="i_tec"></select></div>
   <div style="margin-top:6px"><button class="b3" onclick="regTicket()">🎫 Crear ticket</button> <button class="bd mini" onclick="seedDemo()">⚙ Cargar datos de demostración</button> <span id="i_msg" style="font-size:12px;color:#7ee0b4;margin-left:8px"></span></div>
  </div>
  <div class="warn">⚠️ La <b>prioridad</b> se calcula con la matriz ITIL (impacto × urgencia); el <b>SLA</b> arranca al crear el ticket. La <b>clasificación con IA</b>, las <b>respuestas automáticas</b>, la <b>detección de recurrencias</b> y las <b>integraciones</b> (ServiceNow, Jira, M365, Active Directory, Power BI, correo) = fase de implementación con backend.</div>
  <div class="bar" style="margin-top:12px"><input id="q" placeholder="Buscar (id, asunto, solicitante, técnico, categoría)…" oninput="renderList()" style="min-width:260px">
   <select id="fTipo" onchange="renderList()"><option value="">Todo tipo</option><option>Incidente</option><option>Solicitud</option><option>Problema</option><option>Cambio</option></select>
   <select id="fEst" onchange="renderList()"><option value="">Todo estado</option></select>
   <select id="fPrio" onchange="renderList()"><option value="">Toda prioridad</option><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
   <button class="bd mini" onclick="exportCSV()">⬇ CSV</button><span id="cnt" style="font-size:12px;color:#64748b"></span></div>
  <div id="lista"></div>
 </section>

 <section id="t2" class="tab">
  <div class="grid">
   <div class="card"><h3>🌐 Reportar incidencia / solicitar servicio</h3>
    <div class="f"><label>Tipo</label><select id="p_tipo"><option>Incidente</option><option>Solicitud</option></select></div>
    <div class="f" style="display:flex"><label>¿Qué necesitas?</label><input id="p_asunto"></div>
    <div class="f" style="display:flex"><label>Detalle</label><textarea id="p_desc"></textarea></div>
    <div class="f"><label>Tu nombre</label><input id="p_sol"></div>
    <div class="f"><label>Dependencia</label><select id="p_dep"></select></div>
    <div style="margin-top:6px"><button class="b3" onclick="portalReport()">📨 Enviar</button> <span id="p_msg" style="font-size:12px;color:#7ee0b4"></span></div>
   </div>
   <div class="card"><h3>🔎 Soluciones conocidas (autoservicio)</h3>
    <div class="bar"><input id="p_kb" placeholder="Busca en la base de conocimiento…" oninput="portalKB()" style="min-width:200px"></div>
    <div id="p_kbList" style="font-size:12px"></div>
   </div>
  </div>
  <div class="h">📋 Mis tickets (por solicitante)</div>
  <div class="bar"><input id="p_mine" placeholder="Escribe tu nombre para ver tus tickets…" oninput="portalMine()" style="min-width:240px"></div>
  <div id="p_mineList"></div>
 </section>

 <section id="t3" class="tab">
  <div class="card"><h3>🧩 Alta de elemento de configuración (CMDB) / inventario</h3>
   <div class="f"><label>Clase de CI</label><select id="c_clase"></select></div>
   <div class="f"><label>Marca</label><input id="c_marca"></div>
   <div class="f"><label>Modelo</label><input id="c_modelo"></div>
   <div class="f"><label>N.º de serie</label><input id="c_serie"></div>
   <div class="f"><label>Etiqueta patrimonial</label><input id="c_etiq"></div>
   <div class="f"><label>Responsable</label><input id="c_resp"></div>
   <div class="f"><label>Dependencia</label><select id="c_dep"></select></div>
   <div class="f"><label>Ubicación</label><input id="c_ubic"></div>
   <div class="f"><label>Estado</label><select id="c_estado"><option>Operativo</option><option>En reparación</option><option>En resguardo</option><option>Baja</option></select></div>
   <div class="f"><label>Garantía hasta</label><input id="c_gar" type="date"></div>
   <div class="f"><label>Fecha de adquisición</label><input id="c_adq" type="date"></div>
   <div style="margin-top:6px"><button class="b3" onclick="regCI()">＋ Registrar activo</button> <span id="c_msg" style="font-size:12px;color:#7ee0b4"></span></div>
  </div>
  <div class="kpis" id="cmdbKpis"></div>
  <div class="bar"><input id="cq" placeholder="Buscar activo (marca, serie, etiqueta, responsable, dependencia)…" oninput="renderCMDB()" style="min-width:280px"><select id="cfClase" onchange="renderCMDB()"><option value="">Toda clase</option></select><button class="bd mini" onclick="exportCMDB()">⬇ CSV</button></div>
  <div id="cmdbList"></div>
 </section>

 <section id="t4" class="tab">
  <div class="card"><h3>💿 Alta de licencia / activo de software</h3>
   <div class="f"><label>Producto</label><select id="s_prod"></select></div>
   <div class="f"><label>Tipo</label><select id="s_tipo"><option>Licencia perpetua</option><option>Suscripción</option><option>Open source</option></select></div>
   <div class="f"><label>Cantidad (asientos)</label><input id="s_cant" type="number"></div>
   <div class="f"><label>Costo anual (MXN)</label><input id="s_costo" type="number"></div>
   <div class="f"><label>Vigencia hasta</label><input id="s_vig" type="date"></div>
   <div class="f"><label>Uso (%)</label><input id="s_uso" type="number" min="0" max="100"></div>
   <div style="margin-top:6px"><button class="b3" onclick="regSW()">＋ Registrar software</button> <span id="s_msg" style="font-size:12px;color:#7ee0b4"></span></div>
  </div>
  <div class="kpis" id="swKpis"></div>
  <div class="h">Licencias y vigencias</div>
  <div id="swList"></div>
 </section>

 <section id="t5" class="tab">
  <div class="card"><h3>📚 Nuevo artículo de conocimiento</h3>
   <div class="f"><label>Tipo</label><select id="k_tipo"></select></div>
   <div class="f"><label>Categoría</label><input id="k_cat" list="l_cat"><datalist id="l_cat"></datalist></div>
   <div class="f" style="display:flex"><label>Título</label><input id="k_tit"></div>
   <div class="f" style="display:flex"><label>Contenido / solución</label><textarea id="k_cont"></textarea></div>
   <div class="f"><label>Etiquetas (coma)</label><input id="k_tags"></div>
   <div style="margin-top:6px"><button class="b3" onclick="regKB()">＋ Publicar artículo</button> <span id="k_msg" style="font-size:12px;color:#7ee0b4"></span></div>
  </div>
  <div class="bar"><input id="kq" placeholder="Buscar en la base de conocimiento (título, contenido, etiqueta)…" oninput="renderKB()" style="min-width:300px"></div>
  <div id="kbList"></div>
  <div class="warn">La <b>búsqueda semántica con IA</b> y la <b>recomendación automática de artículos</b> = fase backend. Aquí la búsqueda es por palabras clave sobre lo capturado.</div>
 </section>

 <section id="t6" class="tab">
  <div class="h">⏱️ Acuerdos de Nivel de Servicio (SLA) — tiempos objetivo</div>
  <div class="card"><table id="slaTable"></table></div>
  <div class="h">🪜 Matriz de escalamiento</div>
  <div class="card"><table id="escTable"></table></div>
  <div class="h">⛔ Incumplimientos de SLA (vigentes)</div>
  <div id="breachList"></div>
 </section>

 <section id="t7" class="tab">
  <div class="kpis" id="biKpis"></div>
  <div class="grid">
   <div class="card"><h3>Tickets por categoría</h3><canvas id="cCat"></canvas></div>
   <div class="card"><h3>Por tipo</h3><canvas id="cTipo"></canvas></div>
   <div class="card"><h3>Por prioridad</h3><canvas id="cPrio"></canvas></div>
   <div class="card"><h3>Por estado</h3><canvas id="cEst"></canvas></div>
   <div class="card"><h3>Productividad por técnico</h3><canvas id="cTec"></canvas></div>
   <div class="card"><h3>Tendencia de tickets (por día)</h3><canvas id="cDia"></canvas></div>
  </div>
 </section>

 <section id="t8" class="tab">
  <div class="kpis" id="erpKpis"></div>
  <div class="h">🩺 Salud y disponibilidad de datos de los módulos del Legal ERP</div>
  <div class="card" style="overflow:auto"><table id="erpTable"></table></div>
  <div class="h">🕑 Actividad reciente del ecosistema (bitácora)</div>
  <div id="erpAct"></div>
  <div class="warn">La «salud» refleja la <b>disponibilidad de datos</b> de cada módulo (registros y última actividad en la bitácora). El <b>monitoreo activo</b> (uptime, latencia, APM, alertas de servicio) y la supervisión de <b>OCR/IA/firma/SharePoint/M365</b> = fase de implementación con backend.</div>
 </section>

 <section id="t9" class="tab">
  <div class="card"><h3>🛡️ Registrar incidente de seguridad</h3>
   <div class="f"><label>Tipo</label><select id="x_tipo"></select></div>
   <div class="f"><label>Severidad</label><select id="x_sev"><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select></div>
   <div class="f" style="display:flex"><label>Descripción</label><textarea id="x_desc"></textarea></div>
   <div class="f"><label>Activo / sistema afectado</label><input id="x_act"></div>
   <div class="f"><label>Acción / contención</label><input id="x_acc"></div>
   <div style="margin-top:6px"><button class="b3" onclick="regSec()">＋ Registrar incidente</button> <span id="x_msg" style="font-size:12px;color:#7ee0b4"></span></div>
  </div>
  <div class="kpis" id="secKpis"></div>
  <div class="h">Incidentes de seguridad</div><div id="secList"></div>
 </section>

 <section id="t10" class="tab">
  <div class="kpis" id="cioKpis"></div>
  <div class="grid">
   <div class="card s2"><h3>🩺 Salud del ecosistema tecnológico</h3><div id="cioSalud"></div></div>
   <div class="card"><h3>Cumplimiento de SLA</h3><canvas id="cioSla"></canvas></div>
   <div class="card"><h3>Tickets críticos abiertos</h3><div id="cioCrit"></div></div>
   <div class="card"><h3>Licencias por vencer (≤90 días)</h3><div id="cioLic"></div></div>
   <div class="card"><h3>Incidentes de seguridad abiertos</h3><div id="cioSec"></div></div>
   <div class="card s2"><h3>🏗️ Especificación técnica del SIGEJ (backend, seguridad e integraciones)</h3><div style="font-size:12.5px;color:#334155;line-height:1.6;margin-top:4px">Documento de arquitectura para el Área de Sistemas: modelo de datos (módulos → tablas), IAM real (SSO + 2FA + RBAC/ABAC), integraciones priorizadas (SIIAU, Firma-e, PNT, Power BI…), IA/OCR y plan de migración por fases.</div><div style="margin-top:8px"><a class="b1 mini" style="text-decoration:none;display:inline-block;padding:8px 14px;border-radius:8px" href="arquitectura_SIGEJ.html">📄 Abrir especificación técnica →</a></div></div>
  </div>
 </section>
 <section id="t11" class="tab">
  <div id="iamNav" style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px">
   <button class="b1 mini" onclick="iamGo('usuarios')">👤 Usuarios</button>
   <button class="bd mini" onclick="iamGo('exp')">📁 Expedientes y reasignación</button>
   <button class="bd mini" onclick="iamGo('cupos')">🎚️ Cupos por módulo</button>
   <button class="bd mini" onclick="iamGo('lic')">🪪 Licencias</button>
   <button class="bd mini" onclick="iamGo('cap')">📊 Capacidad</button>
   <button class="bd mini" onclick="iamGo('seg')">🔒 Seguridad</button>
   <button class="bd mini" onclick="iamGo('audit')">🧾 Auditoría</button>
  </div>
  <div id="iamBody"></div>
 </section>
 <section id="t12" class="tab">
  <div class="card" style="background:#eef6ff;border:1px solid #cfe0f5;font-size:12.5px;color:#0a4d8c;margin-bottom:12px">🏛️ <b>Competencias y roles jurídicos</b> — matriz de área responsable, jerarquía de roles y RACI para la elaboración de instrumentos jurídicos. Gobernanza IAM del Legal ERP (movido aquí desde el módulo de Instrumentos). Fuente de datos: catálogos de Instrumentos Jurídicos.</div>
  <div class="grid">
   <div class="card s2"><h3>Matriz de competencias por área responsable</h3><div id="compMatriz"></div></div>
   <div class="card"><h3>Jerarquía y roles (niveles)</h3><div id="rolesBox"></div></div>
   <div class="card"><h3>Matriz RACI</h3><div id="raciBox"></div></div>
  </div>
 </section>
</div>
<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;let CH={};
function el(id){return document.getElementById(id);}
function val(id){return (el(id).value||'').trim();}
function pad(n){return (n<10?'0':'')+n;}
function nowTs(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function todayISO(){return new Date().toISOString().slice(0,10);}
function nowYear(){return String(new Date().getFullYear());}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function setK(k,a){localStorage.setItem(k,JSON.stringify(a));}
function money(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function rb(n){return n?'<span class="rb rb-'+n+'">'+n+'</span>':'';}
function hoursTo(ts){if(!ts)return null;return Math.round((new Date(ts.replace(' ','T'))-new Date())/36e5);}
function hoursSince(ts){if(!ts)return null;return (new Date()-new Date(ts.replace(' ','T')))/36e5;}
/* stores */
let TK=J('sigej_helpdesk'),CI=J('sigej_hd_cmdb'),SW=J('sigej_hd_sw'),KB=J('sigej_hd_kb'),SEC=J('sigej_hd_sec');
function saveTK(){setK('sigej_helpdesk',TK);}function saveCI(){setK('sigej_hd_cmdb',CI);}function saveSW(){setK('sigej_hd_sw',SW);}function saveKB(){setK('sigej_hd_kb',KB);}function saveSEC(){setK('sigej_hd_sec',SEC);}
function reloadAll(){TK=J('sigej_helpdesk');CI=J('sigej_hd_cmdb');SW=J('sigej_hd_sw');KB=J('sigej_hd_kb');SEC=J('sigej_hd_sec');}
/* catálogos config */
const SLA={'Crítico':{resp:1,sol:4},'Alto':{resp:4,sol:8},'Medio':{resp:8,sol:24},'Bajo':{resp:24,sol:72}};
const ESC=[['Nivel 1','Soporte básico — Mesa de servicio'],['Nivel 2','Especialistas (redes, sistemas, M365)'],['Nivel 3','Administradores de infraestructura'],['Nivel 4','Proveedores externos'],['Nivel 5','Fabricantes']];
const EST_TKT=['Nuevo','Asignado','En proceso','En espera','Resuelto','Cerrado','Cancelado'];
const EST_PRB=['Identificado','En análisis','Causa raíz','Solución conocida','Cerrado'];
const EST_CHG=['Solicitado','En evaluación','Aprobado','Programado','Implementado','Cerrado','Rechazado'];
function estList(t){return t==='Problema'?EST_PRB:t==='Cambio'?EST_CHG:EST_TKT;}
const CERR=['Cerrado','Cancelado','Rechazado'];
function abierto(t){return CERR.indexOf(t.estado)<0;}
function resuelto(t){return ['Resuelto','Cerrado','Implementado','Solución conocida'].indexOf(t.estado)>=0;}
const PRIOM={'Alto|Alta':'Crítico','Alto|Media':'Alto','Alto|Baja':'Medio','Medio|Alta':'Alto','Medio|Media':'Medio','Medio|Baja':'Bajo','Bajo|Alta':'Medio','Bajo|Media':'Bajo','Bajo|Baja':'Bajo'};
function prioFrom(imp,urg){return PRIOM[imp+'|'+urg]||'Medio';}
const PREF={'Incidente':'INC','Solicitud':'REQ','Problema':'PRB','Cambio':'CHG'};
/* fill selects */
function fillSel(id,arr,ph){const e=el(id);if(!e)return;e.innerHTML=(ph?'<option value="">'+ph+'</option>':'')+arr.map(x=>'<option>'+x+'</option>').join('');}
function catByTipo(){const t=val('i_tipo');const map={'Incidente':D.catInc,'Solicitud':D.catSol,'Problema':D.catInc,'Cambio':D.catChg};fillSel('i_cat',map[t]||D.catInc);}
function idPrev(){const t=val('i_tipo');const pre=PREF[t]||'TKT';const y=nowYear();const n=TK.filter(x=>x.id&&x.id.indexOf(pre+'-'+y)===0).length+1;el('i_id').value=pre+'-'+y+'-'+String(n).padStart(4,'0');}
function autoPrio(){el('i_prio').value=prioFrom(val('i_imp'),val('i_urg'));}
function initForms(){fillSel('i_tipo',['Incidente','Solicitud','Problema','Cambio']);catByTipo();fillSel('i_dep',D.deps);fillSel('i_tec',['— sin asignar —'].concat(D.tecnicos));fillSel('p_dep',D.deps);
 fillSel('c_clase',D.claseCI);fillSel('cfClase',D.claseCI,'Toda clase');fillSel('c_dep',D.deps);fillSel('s_prod',D.swProd);fillSel('k_tipo',D.kbTipos);fillSel('x_tipo',D.secTipos);
 el('i_imp').onchange=autoPrio;el('i_urg').onchange=autoPrio;autoPrio();idPrev();el('i_sol').value=localStorage.getItem('sigej_perfil')||'';}
/* tabs */
function tab(id){document.querySelectorAll('.tab').forEach(s=>s.classList.toggle('on',s.id===id));document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 if(id==='t1')renderList();if(id==='t3'){renderCMDB();}if(id==='t4')renderSW();if(id==='t5')renderKB();if(id==='t6')renderSLA();if(id==='t7')renderBI();if(id==='t8')renderERP();if(id==='t9')renderSEC();if(id==='t10')renderCIO();if(id==='t11')renderIAM();if(id==='t12')renderComp();}
function renderComp(){
 var A=D.cr_areas||{},F=D.cr_familias||[],R=D.cr_roles||[],RA=D.cr_raci||[];
 document.getElementById('compMatriz').innerHTML='<table><tr><th>Área</th><th>Responsable de</th><th>Revisor</th><th>Autoridad</th><th>Fuente</th></tr>'+
  Object.keys(A).map(function(ac){var a=A[ac];var fams=F.filter(function(f){return f.area===ac;}).map(function(f){return f.fam;}).join(', ');return '<tr><td><b>'+ac+'</b><br><span style="font-size:11px;color:#64748b">'+a.nombre+'</span></td><td>'+fams+'</td><td>'+a.revisor+'</td><td>'+a.autoridad+'</td><td><a href="'+a.fuente+'" target="_blank" style="color:#0a4d8c">ver</a></td></tr>';}).join('')+'</table>';
 document.getElementById('rolesBox').innerHTML=R.map(function(r){return '<div style="display:flex;justify-content:space-between;padding:6px 2px;border-bottom:1px solid var(--line);font-size:12.5px"><span>Nivel '+r[0]+'</span><b>'+r[1]+'</b></div>';}).join('');
 document.getElementById('raciBox').innerHTML=RA.map(function(r){return '<div style="padding:6px 2px;border-bottom:1px solid var(--line);font-size:12px"><b style="color:#0a4d8c">'+r[0]+'</b> — '+r[1]+'</div>';}).join('');
}
function logT(o,acc){o.traza.push({ts:nowTs(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:acc});}
/* ====== tickets ====== */
function regTicket(){if(!val('i_asunto')){el('i_msg').style.color='#ff9b8d';el('i_msg').textContent='Indica el asunto.';return;}
 const t=val('i_tipo');const prio=prioFrom(val('i_imp'),val('i_urg'));const created=nowTs();const sl=SLA[prio]||SLA['Medio'];
 const vR=new Date(Date.now()+sl.resp*36e5).toISOString().slice(0,19).replace('T',' ');
 const vS=new Date(Date.now()+sl.sol*36e5).toISOString().slice(0,19).replace('T',' ');
 const tec=val('i_tec');const asg=tec&&tec.indexOf('sin asignar')<0;
 const o={id:val('i_id'),tipo:t,cat:val('i_cat'),asunto:val('i_asunto'),desc:val('i_desc'),sol:val('i_sol'),dep:val('i_dep'),imp:val('i_imp'),urg:val('i_urg'),prio:prio,tec:asg?tec:'',estado:asg?'Asignado':estList(t)[0],nivelEsc:1,creado:created,venceResp:vR,venceSol:vS,sla:prio,ci:'',solucion:'',calif:0,aprob:[],causa:'',traza:[{ts:created,usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Ticket creado'+(asg?' y asignado a '+tec:'')}]};
 TK.push(o);saveTK();if(window.__bitlog)__bitlog('Acción','Crear ticket '+o.id);
 ['i_asunto','i_desc'].forEach(id=>el(id).value='');idPrev();el('i_msg').style.color='#7ee0b4';el('i_msg').textContent='✓ '+o.id+' creado ('+prio+').';renderList();compute();}
function idxTK(id){return TK.findIndex(x=>x.id===id);}
function slaState(t){if(resuelto(t))return {c:'#1f9d6b',txt:'En SLA'};const h=hoursTo(t.venceSol);if(h===null)return {c:'#64748b',txt:'—'};if(h<0)return {c:'#c0392b',txt:'Vencido '+(-h)+'h'};if(h<=2)return {c:'#ea580c',txt:'Vence en '+h+'h'};if(h<=8)return {c:'#e08e0b',txt:'En '+h+'h'};return {c:'#1f9d6b',txt:'En '+h+'h'};}
function renderList(){const q=(val('q')||'').toLowerCase();const ft=val('fTipo'),fe=val('fEst'),fp=val('fPrio');
 const ests=Array.from(new Set(TK.map(e=>e.estado)));const se=el('fEst');if(se&&se.options.length-1!==ests.length){const cur=se.value;se.innerHTML='<option value="">Todo estado</option>'+ests.map(e=>'<option>'+e+'</option>').join('');se.value=cur;}
 let arr=TK.filter(e=>(!ft||e.tipo===ft)&&(!fe||e.estado===fe)&&(!fp||e.prio===fp));
 if(q)arr=arr.filter(e=>(e.id+' '+e.asunto+' '+e.sol+' '+(e.tec||'')+' '+e.cat).toLowerCase().indexOf(q)>=0);
 el('cnt').textContent=arr.length+' de '+TK.length;
 const box=el('lista');
 if(!TK.length){box.innerHTML='<div class="empty">📭 Sin tickets. Crea el primero arriba o pulsa <b>⚙ Cargar datos de demostración</b> para ver el tablero con ejemplos.</div>';return;}
 box.innerHTML=arr.sort((a,b)=>b.creado.localeCompare(a.creado)).map(e=>{const i=TK.indexOf(e);const s=slaState(e);const ico={'Incidente':'🔧','Solicitud':'📦','Problema':'🧪','Cambio':'🔁'}[e.tipo]||'🎫';
  return '<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><span class="t">'+ico+' '+e.id+' · '+e.asunto+'</span><span>'+rb(e.prio)+' <span class="chip">'+e.tipo+'</span> <span class="chip">'+e.estado+'</span> <span class="sem" style="background:'+s.c+'"></span><span style="font-size:11px;color:'+s.c+'">'+s.txt+'</span></span></div><div class="m">'+e.cat+' · '+(e.sol||'—')+' · '+(e.dep||'—')+(e.tec?' · 👷 '+e.tec:' · sin asignar')+'</div></div>';}).join('')||'<div class="empty" style="padding:14px">Sin coincidencias.</div>';}
function ficha(i){const t=TK[i];if(!t){closeDrw();return;}const s=slaState(t);const ests=estList(t.tipo);
 const estBtns=ests.map(e=>'<button class="bd mini" style="'+(e===t.estado?'background:#0a4d8c':'')+'" onclick="setEstado('+i+',\''+e+'\')">'+e+'</button>').join(' ');
 const traza=t.traza.map(x=>'<div class="ev">'+x.ts+' · '+x.usuario+' — '+x.accion+'</div>').join('');
 const aprob=(t.aprob||[]).length?(t.aprob||[]).map(a=>'<span class="chip">'+a+'</span>').join(' '):'<span style="color:#64748b;font-size:12px">Sin aprobaciones.</span>';
 const rH=hoursTo(t.venceResp),sH=hoursTo(t.venceSol);
 el('drwBody').innerHTML='<h2 style="margin:0 0 4px;color:#0a4d8c">'+t.id+' · '+t.asunto+'</h2>'+
  '<div style="margin:4px 0 10px">'+rb(t.prio)+' <span class="chip">'+t.tipo+'</span> <span class="chip">'+t.cat+'</span> <span class="chip">'+t.estado+'</span> <span class="chip">N'+t.nivelEsc+'</span></div>'+
  '<div class="comp"><b>📇 Datos</b><br>Solicitante: '+(t.sol||'—')+' · Dependencia: '+(t.dep||'—')+'<br>Impacto: '+t.imp+' · Urgencia: '+t.urg+' · Creado: '+t.creado+'<br>Técnico: '+(t.tec||'sin asignar')+(t.desc?'<br>Descripción: '+t.desc:'')+'</div>'+
  '<div class="comp"><b>⏱️ SLA ('+t.sla+')</b> <span class="sem" style="background:'+s.c+'"></span><span style="color:'+s.c+'">'+s.txt+'</span><br><span style="font-size:11px;color:#64748b">Respuesta objetivo: '+SLA[t.sla].resp+'h ('+(rH===null?'—':rH<0?'vencida':rH+'h')+') · Solución objetivo: '+SLA[t.sla].sol+'h ('+(sH===null?'—':sH<0?'vencida':sH+'h')+')</span></div>'+
  '<div class="comp"><b>🔄 Estado / flujo</b><div style="margin-top:6px;display:flex;flex-wrap:wrap;gap:4px">'+estBtns+'</div></div>'+
  '<div class="comp"><b>👷 Asignación y escalamiento</b><div style="margin-top:6px"><div class="f"><label>Técnico</label><select id="d_tec"><option value="">— sin asignar —</option>'+D.tecnicos.map(x=>'<option'+(x===t.tec?' selected':'')+'>'+x+'</option>').join('')+'</select></div> <button class="b1 mini" onclick="asignar('+i+')">Asignar</button> <button class="bg mini" onclick="escalar('+i+')">⏫ Escalar (N'+t.nivelEsc+'→N'+Math.min(5,t.nivelEsc+1)+')</button></div></div>'+
  '<div class="comp"><b>🧩 CI relacionado (CMDB)</b><div style="margin-top:6px"><div class="f"><label>Activo</label><select id="d_ci"><option value="">— ninguno —</option>'+CI.map(c=>'<option'+(c.id===t.ci?' selected':'')+'>'+c.id+' · '+c.clase+' '+(c.marca||'')+'</option>').join('')+'</select></div> <button class="bd mini" onclick="linkCI('+i+')">Vincular</button></div></div>'+
  (t.tipo==='Cambio'?'<div class="comp"><b>🔁 Gestión de cambio</b> <span class="chip">riesgo: '+(t.riesgo||'—')+'</span><div style="margin-top:6px">Aprobaciones: '+aprob+' <button class="bd mini" onclick="aprobar('+i+')">＋ Aprobación</button> <button class="bd mini" onclick="setRiesgo('+i+')">Riesgo/impacto</button></div></div>':'')+
  (t.tipo==='Problema'?'<div class="comp"><b>🧪 Gestión de problema</b><div style="margin-top:6px">Causa raíz: '+(t.causa||'<span style=\'color:#64748b\'>por determinar</span>')+' <button class="bd mini" onclick="setCausa('+i+')">Definir causa raíz</button></div></div>':'')+
  '<div class="comp"><b>✅ Solución</b><div style="margin-top:6px">'+(t.solucion?t.solucion:'<span style="color:#64748b">Sin solución registrada.</span>')+' <button class="bd mini" onclick="setSolucion('+i+')">Registrar solución</button> <button class="bg mini" onclick="aKB('+i+')">📚 Pasar a base de conocimiento</button></div></div>'+
  '<div class="comp"><b>⭐ Calificación de la atención</b><div style="margin-top:6px">'+[1,2,3,4,5].map(n=>'<span class="lk" style="font-size:18px" onclick="calificar('+i+','+n+')">'+(n<=(t.calif||0)?'★':'☆')+'</span>').join('')+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad (auditoría)</b><div class="tl" style="margin-top:6px">'+traza+'</div></div>'+
  '<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="b3 mini" onclick="setEstado('+i+',\''+(t.tipo==='Cambio'?'Implementado':'Resuelto')+'\')">✔ Resolver</button> <button class="bd mini" onclick="setEstado('+i+',\'Cerrado\')">🔒 Cerrar</button> <button class="bw mini" onclick="docExp('+i+')">📎 Expediente electrónico</button> <button class="bd" onclick="closeDrw()">Cerrar ventana</button></div>';
 el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
el('drw').onclick=function(ev){if(ev.target.id==='drw')closeDrw();};
function setEstado(i,e){const t=TK[i];t.estado=e;logT(t,'Estado → '+e);if(resuelto(t)&&!t.resuelto)t.resuelto=nowTs();saveTK();if(window.__bitlog)__bitlog('Acción','Ticket '+t.id+' → '+e);ficha(i);compute();}
function asignar(i){const t=TK[i];t.tec=val('d_tec');if(t.tec&&(t.estado==='Nuevo'||t.estado==='Identificado'||t.estado==='Solicitado'))t.estado='Asignado';logT(t,'Asignado a '+(t.tec||'sin asignar'));saveTK();ficha(i);compute();}
function escalar(i){const t=TK[i];t.nivelEsc=Math.min(5,(t.nivelEsc||1)+1);logT(t,'Escalado a Nivel '+t.nivelEsc);saveTK();if(window.__bitlog)__bitlog('Acción','Escalar '+t.id+' a N'+t.nivelEsc);ficha(i);}
function linkCI(i){const t=TK[i];const v=val('d_ci');t.ci=v?v.split(' · ')[0]:'';logT(t,'CI vinculado: '+(t.ci||'ninguno'));saveTK();ficha(i);}
function aprobar(i){const t=TK[i];const a=prompt('Aprobado por (nombre/rol):','');if(!a)return;t.aprob.push(a);logT(t,'Aprobación: '+a);if(t.estado==='En evaluación')t.estado='Aprobado';saveTK();ficha(i);}
function setRiesgo(i){const t=TK[i];const r=prompt('Riesgo del cambio (Crítico/Alto/Medio/Bajo):',t.riesgo||'Medio');if(r===null)return;t.riesgo=r;const im=prompt('Impacto del cambio:',t.impactoChg||'Medio');t.impactoChg=im||'';logT(t,'Riesgo/impacto del cambio: '+r);saveTK();ficha(i);}
function setCausa(i){const t=TK[i];const c=prompt('Causa raíz identificada:',t.causa||'');if(c===null)return;t.causa=c;if(t.estado==='En análisis')t.estado='Causa raíz';logT(t,'Causa raíz definida');saveTK();ficha(i);}
function setSolucion(i){const t=TK[i];const s=prompt('Solución aplicada:',t.solucion||'');if(s===null)return;t.solucion=s;logT(t,'Solución registrada');saveTK();ficha(i);}
function calificar(i,n){const t=TK[i];t.calif=n;logT(t,'Calificación: '+n+'/5');saveTK();ficha(i);}
function aKB(i){const t=TK[i];if(!t.solucion){alert('Primero registra la solución.');return;}KB.push({id:'KB-'+nowYear()+'-'+String(KB.length+1).padStart(4,'0'),tipo:'Solución conocida',cat:t.cat,tit:t.asunto,cont:t.solucion,tags:[t.cat,t.tipo],fecha:todayISO(),autor:localStorage.getItem('sigej_perfil')||'(perfil)',desde:t.id});saveKB();logT(t,'Solución publicada en base de conocimiento');saveTK();alert('✓ Artículo creado en la base de conocimiento.');ficha(i);}
function exportCSV(){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';const cab=['id','tipo','categoria','asunto','solicitante','dependencia','prioridad','estado','tecnico','nivel_esc','creado','vence_solucion','sla','calificacion'];
 const rows=TK.map(t=>[t.id,t.tipo,t.cat,t.asunto,t.sol,t.dep,t.prio,t.estado,t.tec,'N'+t.nivelEsc,t.creado,t.venceSol,t.sla,t.calif].map(esc).join(','));
 dl('helpdesk_tickets.csv',cab.join(',')+'\n'+rows.join('\n'),'text/csv');}
function dl(name,txt,type){const b=new Blob(['﻿'+txt],{type:type});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;a.click();}
/* ====== portal autoservicio ====== */
function portalReport(){if(!val('p_asunto')){el('p_msg').style.color='#ff9b8d';el('p_msg').textContent='Describe tu necesidad.';return;}
 const t=val('p_tipo');const pre=PREF[t];const y=nowYear();const n=TK.filter(x=>x.id&&x.id.indexOf(pre+'-'+y)===0).length+1;const id=pre+'-'+y+'-'+String(n).padStart(4,'0');const created=nowTs();const prio='Medio';const sl=SLA[prio];
 TK.push({id:id,tipo:t,cat:t==='Incidente'?'Sin clasificar':'Solicitud de servicio',asunto:val('p_asunto'),desc:val('p_desc'),sol:val('p_sol'),dep:val('p_dep'),imp:'Medio',urg:'Media',prio:prio,tec:'',estado:'Nuevo',nivelEsc:1,creado:created,venceResp:new Date(Date.now()+sl.resp*36e5).toISOString().slice(0,19).replace('T',' '),venceSol:new Date(Date.now()+sl.sol*36e5).toISOString().slice(0,19).replace('T',' '),sla:prio,ci:'',solucion:'',calif:0,aprob:[],causa:'',traza:[{ts:created,usuario:val('p_sol')||'(autoservicio)',accion:'Reportado por autoservicio'}]});
 saveTK();el('p_msg').style.color='#7ee0b4';el('p_msg').textContent='✓ Registrado: '+id;el('p_asunto').value='';el('p_desc').value='';portalMine();compute();}
function portalKB(){const q=(val('p_kb')||'').toLowerCase();const arr=KB.filter(a=>!q||(a.tit+' '+a.cont+' '+(a.tags||[]).join(' ')).toLowerCase().indexOf(q)>=0).slice(0,8);
 el('p_kbList').innerHTML=KB.length?(arr.length?arr.map(a=>'<div style="border-bottom:1px solid var(--line);padding:6px 0"><b style="color:#0a4d8c">'+a.tit+'</b> <span class="chip">'+a.tipo+'</span><br><span style="color:#475569">'+(a.cont||'').slice(0,120)+'</span></div>').join(''):'<div style="color:#64748b">Sin coincidencias.</div>'):'<div style="color:#64748b">Base de conocimiento vacía.</div>';}
function portalMine(){const q=(val('p_mine')||'').toLowerCase();if(!q){el('p_mineList').innerHTML='<div class="empty" style="padding:14px">Escribe tu nombre para ver tus tickets.</div>';return;}
 const arr=TK.filter(t=>(t.sol||'').toLowerCase().indexOf(q)>=0);el('p_mineList').innerHTML=arr.length?arr.map(t=>{const i=TK.indexOf(t);const s=slaState(t);return '<div class="it" onclick="ficha('+i+')"><div class="t">'+t.id+' · '+t.asunto+'</div><div class="m">'+t.tipo+' · '+t.estado+' · <span style="color:'+s.c+'">'+s.txt+'</span></div></div>';}).join(''):'<div class="empty" style="padding:14px">Sin tickets para «'+q+'».</div>';}
/* ====== CMDB ====== */
function regCI(){if(!val('c_marca')&&!val('c_modelo')){el('c_msg').style.color='#ff9b8d';el('c_msg').textContent='Indica marca o modelo.';return;}
 const id='CI-'+nowYear()+'-'+String(CI.length+1).padStart(4,'0');
 CI.push({id:id,clase:val('c_clase'),marca:val('c_marca'),modelo:val('c_modelo'),serie:val('c_serie'),etiq:val('c_etiq'),resp:val('c_resp'),dep:val('c_dep'),ubic:val('c_ubic'),estado:val('c_estado'),gar:val('c_gar'),adq:val('c_adq'),fecha:todayISO()});
 saveCI();if(window.__bitlog)__bitlog('Acción','Registrar activo CMDB '+id);['c_marca','c_modelo','c_serie','c_etiq','c_resp','c_ubic'].forEach(x=>el(x).value='');el('c_msg').style.color='#7ee0b4';el('c_msg').textContent='✓ '+id+' registrado.';renderCMDB();}
function renderCMDB(){const q=(val('cq')||'').toLowerCase();const fc=val('cfClase');
 const op=CI.filter(c=>c.estado==='Operativo').length,gar=CI.filter(c=>{const d=c.gar?Math.round((new Date(c.gar)-new Date())/864e5):null;return d!==null&&d<0;}).length;
 el('cmdbKpis').innerHTML=[['',CI.length,'Activos (CIs)',''],['',op,'Operativos','g'],['',CI.filter(c=>c.estado==='En reparación').length,'En reparación','y'],['',gar,'Garantía vencida','r'],['',new Set(CI.map(c=>c.dep)).size,'Dependencias','']].map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 let arr=CI.filter(c=>(!fc||c.clase===fc)&&(!q||(c.id+' '+c.marca+' '+c.modelo+' '+c.serie+' '+c.etiq+' '+c.resp+' '+c.dep).toLowerCase().indexOf(q)>=0));
 el('cmdbList').innerHTML=CI.length?(arr.length?'<div class="card" style="overflow:auto"><table><tr><th>ID</th><th>Clase</th><th>Marca/Modelo</th><th>Serie</th><th>Etiqueta</th><th>Responsable</th><th>Dependencia</th><th>Estado</th><th>Garantía</th></tr>'+arr.map(c=>{const d=c.gar?Math.round((new Date(c.gar)-new Date())/864e5):null;const gc=d===null?'':d<0?'color:#ff9b8d':d<=90?'color:#ffce82':'';return '<tr><td>'+c.id+'</td><td>'+c.clase+'</td><td>'+(c.marca||'')+' '+(c.modelo||'')+'</td><td>'+(c.serie||'—')+'</td><td>'+(c.etiq||'—')+'</td><td>'+(c.resp||'—')+'</td><td>'+(c.dep||'—')+'</td><td>'+c.estado+'</td><td style="'+gc+'">'+(c.gar||'—')+'</td></tr>';}).join('')+'</table></div>':'<div class="empty">Sin coincidencias.</div>'):'<div class="empty">📭 CMDB vacía. Registra el primer activo o carga datos de demostración.</div>';}
function exportCMDB(){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';const cab=['id','clase','marca','modelo','serie','etiqueta','responsable','dependencia','ubicacion','estado','garantia','adquisicion'];
 const rows=CI.map(c=>[c.id,c.clase,c.marca,c.modelo,c.serie,c.etiq,c.resp,c.dep,c.ubic,c.estado,c.gar,c.adq].map(esc).join(','));dl('cmdb_inventario.csv',cab.join(',')+'\n'+rows.join('\n'),'text/csv');}
/* ====== software ====== */
function regSW(){if(!val('s_prod')){return;}SW.push({id:'SW-'+nowYear()+'-'+String(SW.length+1).padStart(4,'0'),prod:val('s_prod'),tipo:val('s_tipo'),cant:+val('s_cant')||0,costo:+val('s_costo')||0,vig:val('s_vig'),uso:+val('s_uso')||0,fecha:todayISO()});saveSW();el('s_msg').style.color='#7ee0b4';el('s_msg').textContent='✓ registrado.';renderSW();}
function renderSW(){const venc=SW.filter(s=>{const d=s.vig?Math.round((new Date(s.vig)-new Date())/864e5):null;return d!==null&&d>=0&&d<=90;}).length;const costo=SW.reduce((a,s)=>a+(s.costo||0),0);
 el('swKpis').innerHTML=[['',SW.length,'Productos','',],['',SW.reduce((a,s)=>a+(s.cant||0),0),'Asientos/licencias',''],['',money(costo),'Costo anual',''],['',venc,'Por vencer ≤90d','y']].map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('swList').innerHTML=SW.length?'<div class="card" style="overflow:auto"><table><tr><th>Producto</th><th>Tipo</th><th>Asientos</th><th>Costo anual</th><th>Vigencia</th><th>Uso</th></tr>'+SW.map(s=>{const d=s.vig?Math.round((new Date(s.vig)-new Date())/864e5):null;const vc=d===null?'':d<0?'color:#ff9b8d':d<=90?'color:#ffce82':'';return '<tr><td>'+s.prod+'</td><td>'+s.tipo+'</td><td>'+s.cant+'</td><td>'+money(s.costo)+'</td><td style="'+vc+'">'+(s.vig||'—')+(d!==null&&d<0?' (vencida)':d!==null&&d<=90?' ('+d+'d)':'')+'</td><td>'+(s.uso||0)+'%</td></tr>';}).join('')+'</table></div>':'<div class="empty">📭 Sin licencias registradas.</div>';}
/* ====== base de conocimiento ====== */
function regKB(){if(!val('k_tit')){el('k_msg').style.color='#ff9b8d';el('k_msg').textContent='Indica el título.';return;}
 KB.push({id:'KB-'+nowYear()+'-'+String(KB.length+1).padStart(4,'0'),tipo:val('k_tipo'),cat:val('k_cat'),tit:val('k_tit'),cont:val('k_cont'),tags:val('k_tags').split(',').map(x=>x.trim()).filter(Boolean),fecha:todayISO(),autor:localStorage.getItem('sigej_perfil')||'(perfil)'});
 saveKB();el('k_msg').style.color='#7ee0b4';el('k_msg').textContent='✓ publicado.';['k_tit','k_cont','k_tags'].forEach(x=>el(x).value='');renderKB();}
function renderKB(){const q=(val('kq')||'').toLowerCase();const cats=Array.from(new Set(KB.map(a=>a.cat).filter(Boolean)));el('l_cat').innerHTML=cats.map(c=>'<option>'+c+'</option>').join('');
 let arr=KB.filter(a=>!q||(a.tit+' '+a.cont+' '+(a.tags||[]).join(' ')+' '+a.cat).toLowerCase().indexOf(q)>=0);
 el('kbList').innerHTML=KB.length?(arr.length?arr.map(a=>'<div class="card" style="margin-bottom:8px"><div style="display:flex;justify-content:space-between"><b style="color:#0a4d8c">'+a.tit+'</b><span class="chip">'+a.tipo+'</span></div><div style="font-size:12px;color:#475569;margin-top:5px">'+(a.cont||'').slice(0,260)+'</div><div style="margin-top:5px">'+(a.tags||[]).map(t=>'<span class="chip">'+t+'</span>').join(' ')+' <span style="font-size:10px;color:#64748b">· '+(a.cat||'')+' · '+a.fecha+(a.desde?' · desde '+a.desde:'')+'</span></div></div>').join(''):'<div class="empty">Sin coincidencias.</div>'):'<div class="empty">📭 Base de conocimiento vacía. Publica el primer artículo.</div>';}
/* ====== SLA y escalamiento ====== */
function renderSLA(){el('slaTable').innerHTML='<tr><th>Nivel de prioridad</th><th>Tiempo de respuesta</th><th>Tiempo de solución</th></tr>'+Object.keys(SLA).map(k=>'<tr><td>'+rb(k)+'</td><td>'+SLA[k].resp+' h</td><td>'+SLA[k].sol+' h</td></tr>').join('');
 el('escTable').innerHTML='<tr><th>Nivel</th><th>Atiende</th><th>Tickets en este nivel</th></tr>'+ESC.map((e,i)=>'<tr><td><b>'+e[0]+'</b></td><td>'+e[1]+'</td><td>'+TK.filter(t=>t.nivelEsc===i+1).length+'</td></tr>').join('');
 const br=TK.filter(t=>!resuelto(t)&&hoursTo(t.venceSol)!==null&&hoursTo(t.venceSol)<8).sort((a,b)=>hoursTo(a.venceSol)-hoursTo(b.venceSol));
 el('breachList').innerHTML=br.length?br.map(t=>{const i=TK.indexOf(t);const s=slaState(t);return '<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between"><span class="t"><span class="sem" style="background:'+s.c+'"></span>'+t.id+' · '+t.asunto+'</span><span style="color:'+s.c+';font-weight:700">'+s.txt+'</span></div><div class="m">'+t.prio+' · '+t.estado+' · '+(t.tec||'sin asignar')+' · N'+t.nivelEsc+'</div></div>';}).join(''):'<div class="empty">✓ Sin incumplimientos de SLA próximos.</div>';}
/* ====== BI ====== */
const PAL=['#1aa39a','#0a4d8c','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#16a085','#5d6d7e','#9d174d'];
function cnt(arr,key){const o={};arr.forEach(e=>{const v=(typeof key==='function'?key(e):e[key])||'(s/d)';o[v]=(o[v]||0)+1;});return o;}
function chart(id,type,labels,data,opts){if(!window.Chart)return;if(CH[id])CH[id].destroy();const ctx=el(id);if(!ctx)return;
 CH[id]=new Chart(ctx,{type:type,data:{labels:labels,datasets:[{data:data,backgroundColor:opts&&opts.multi?PAL:(opts&&opts.color||'#1aa39a'),borderColor:opts&&opts.line?'#1aa39a':undefined,fill:false}]},options:{indexAxis:opts&&opts.horiz?'y':'x',plugins:{legend:{display:!!(opts&&opts.legend),position:'right',labels:{color:'#0a4d8c',font:{size:9}}}},scales:type==='doughnut'?{}:{x:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}},y:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}}}}});}
function avgHours(filterFn,fromKey,toKey){const a=TK.filter(filterFn).map(t=>{const f=t[fromKey],to=t[toKey];if(!f||!to)return null;return (new Date(to.replace(' ','T'))-new Date(f.replace(' ','T')))/36e5;}).filter(x=>x!==null&&x>=0);return a.length?Math.round(a.reduce((x,y)=>x+y,0)/a.length):0;}
function renderBI(){const abi=TK.filter(abierto).length,cer=TK.filter(t=>!abierto(t)).length;
 const venc=TK.filter(t=>!resuelto(t)&&hoursTo(t.venceSol)!==null&&hoursTo(t.venceSol)<0).length;
 const cerrados=TK.filter(t=>!abierto(t));const cumpl=cerrados.length?Math.round(100*cerrados.filter(t=>{const r=t.resuelto||t.creado;return new Date(r.replace(' ','T'))<=new Date((t.venceSol||r).replace(' ','T'));}).length/cerrados.length):0;
 const tAtt=avgHours(t=>t.tec,'creado','venceResp');
 const K=[['',TK.length,'Tickets totales',''],['',abi,'Abiertos','y'],['',cer,'Cerrados','g'],['',venc,'Vencidos SLA','r'],['',cumpl+'%','Cumplimiento SLA',cumpl>=85?'g':cumpl>=60?'y':'r'],['',TK.filter(t=>!t.tec&&abierto(t)).length,'Backlog sin asignar','y'],['',new Set(TK.map(t=>t.tec).filter(Boolean)).size,'Técnicos activos','']];
 el('biKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 if(TK.length){const c=cnt(TK,'cat');const ce=Object.entries(c).sort((a,b)=>b[1]-a[1]).slice(0,10);chart('cCat','bar',ce.map(x=>x[0]),ce.map(x=>x[1]),{horiz:true,color:'#0a4d8c'});
  const tp=cnt(TK,'tipo');chart('cTipo','doughnut',Object.keys(tp),Object.values(tp),{multi:true,legend:true});
  const pr=cnt(TK,'prio');chart('cPrio','doughnut',Object.keys(pr),Object.values(pr),{multi:true,legend:true});
  const es=cnt(TK,'estado');chart('cEst','bar',Object.keys(es),Object.values(es),{horiz:true,color:'#d4a32c'});
  const te=cnt(TK.filter(t=>t.tec),'tec');const tee=Object.entries(te).sort((a,b)=>b[1]-a[1]).slice(0,8);chart('cTec','bar',tee.map(x=>x[0].split(' ')[0]+' '+(x[0].split(' ')[1]||'')),tee.map(x=>x[1]),{horiz:true,color:'#1aa39a'});
  const di=cnt(TK,t=>(t.creado||'').slice(0,10));const dk=Object.keys(di).sort();chart('cDia','line',dk,dk.map(k=>di[k]),{line:true,color:'#7e57c2'});
 }else{['cCat','cTipo','cPrio','cEst','cTec','cDia'].forEach(id=>{if(CH[id])CH[id].destroy();});}}
/* ====== Soporte al Legal ERP ====== */
function renderERP(){const bit=J('sigej_bitacora');
 let totalReg=0;const rows=D.modulos.map(m=>{const n=J(m.k).length;totalReg+=n;
  const last=bit.filter(b=>(b.modulo||'').toLowerCase().indexOf(m.n.split(' ')[0].toLowerCase())>=0).slice(-1)[0];
  const estado=n>0?'🟢 Operativo':'🟡 Sin datos aún';
  return '<tr><td>'+m.ic+' <b>'+m.n+'</b></td><td>'+n+'</td><td>'+estado+'</td><td style="font-size:11px;color:#64748b">'+(last?last.ts:'—')+'</td><td><a class="lk" href="'+m.link+'">abrir ↗</a></td></tr>';}).join('');
 el('erpKpis').innerHTML=[['',D.modulos.length,'Módulos monitoreados',''],['',totalReg,'Registros del ecosistema',''],['',bit.length,'Acciones en bitácora',''],['',D.modulos.filter(m=>J(m.k).length>0).length,'Con datos','g']].map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('erpTable').innerHTML='<tr><th>Módulo</th><th>Registros</th><th>Estado</th><th>Última actividad</th><th></th></tr>'+rows;
 el('erpAct').innerHTML=bit.length?bit.slice(-12).reverse().map(b=>'<div class="it"><div class="t">'+(b.modulo||'—')+' · '+(b.tipo||'')+'</div><div class="m">'+b.ts+' · '+(b.perfil||'')+' — '+(b.accion||'')+'</div></div>').join(''):'<div class="empty">Sin actividad registrada aún.</div>';}
/* ====== ciberseguridad ====== */
function regSec(){if(!val('x_desc')){el('x_msg').style.color='#ff9b8d';el('x_msg').textContent='Describe el incidente.';return;}
 SEC.push({id:'SEC-'+nowYear()+'-'+String(SEC.length+1).padStart(4,'0'),tipo:val('x_tipo'),sev:val('x_sev'),desc:val('x_desc'),act:val('x_act'),acc:val('x_acc'),estado:'Abierto',fecha:nowTs()});saveSEC();if(window.__bitlog)__bitlog('Acción','Incidente de seguridad '+val('x_tipo'));el('x_desc').value='';el('x_act').value='';el('x_acc').value='';el('x_msg').style.color='#7ee0b4';el('x_msg').textContent='✓ registrado.';renderSEC();}
function secCerrar(i){SEC[i].estado=SEC[i].estado==='Abierto'?'Contenido':'Cerrado';saveSEC();renderSEC();}
function renderSEC(){const ab=SEC.filter(s=>s.estado==='Abierto').length,cr=SEC.filter(s=>s.sev==='Crítico'&&s.estado!=='Cerrado').length;
 el('secKpis').innerHTML=[['',SEC.length,'Incidentes',''],['',ab,'Abiertos','r'],['',cr,'Críticos activos','r'],['',SEC.filter(s=>s.estado==='Cerrado').length,'Cerrados','g']].map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('secList').innerHTML=SEC.length?SEC.slice().reverse().map(s=>{const i=SEC.indexOf(s);return '<div class="it"><div style="display:flex;justify-content:space-between"><span class="t">'+s.id+' · '+s.tipo+'</span><span>'+rb(s.sev)+' <span class="chip">'+s.estado+'</span></span></div><div class="m">'+(s.desc||'').slice(0,90)+(s.act?' · activo: '+s.act:'')+(s.acc?' · acción: '+s.acc:'')+' · '+s.fecha+' <span class="lk" onclick="event.stopPropagation();secCerrar('+i+')">avanzar estado</span></div></div>';}).join(''):'<div class="empty">✓ Sin incidentes de seguridad registrados.</div>';}
/* ====== Centro de Mando CIO ====== */
function renderCIO(){const abi=TK.filter(abierto).length;const cerrados=TK.filter(t=>!abierto(t));const cumpl=cerrados.length?Math.round(100*cerrados.filter(t=>{const r=t.resuelto||t.creado;return new Date(r.replace(' ','T'))<=new Date((t.venceSol||r).replace(' ','T'));}).length/cerrados.length):0;
 const crit=TK.filter(t=>t.prio==='Crítico'&&abierto(t));const venc=TK.filter(t=>!resuelto(t)&&hoursTo(t.venceSol)!==null&&hoursTo(t.venceSol)<0).length;
 const lic=SW.filter(s=>{const d=s.vig?Math.round((new Date(s.vig)-new Date())/864e5):null;return d!==null&&d>=0&&d<=90;});const secAb=SEC.filter(s=>s.estado!=='Cerrado');
 el('cioKpis').innerHTML=[['',abi,'Tickets abiertos','y'],['',crit.length,'Críticos abiertos','r'],['',venc,'SLA vencidos','r'],['',cumpl+'%','Cumplimiento SLA',cumpl>=85?'g':'y'],['',CI.length,'Activos (CMDB)',''],['',secAb.length,'Seguridad abiertos',secAb.length?'r':'g']].map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 let totalReg=0;D.modulos.forEach(m=>totalReg+=J(m.k).length);
 const salud=D.modulos.map(m=>{const n=J(m.k).length;return '<span class="chip" style="border-color:'+(n>0?'#1f9d6b':'#33507a')+'">'+(n>0?'🟢':'⚪')+' '+m.n+' ('+n+')</span>';}).join(' ');
 el('cioSalud').innerHTML='<div style="font-size:12px;color:#475569;margin-bottom:6px">'+D.modulos.filter(m=>J(m.k).length>0).length+' de '+D.modulos.length+' módulos con datos · '+totalReg+' registros en el ecosistema.</div>'+salud;
 chart('cioSla','doughnut',['Cumplido','Incumplido'],[cumpl,100-cumpl],{multi:true,legend:true});
 el('cioCrit').innerHTML=crit.length?crit.map(t=>{const i=TK.indexOf(t);return '<div class="it" onclick="ficha('+i+')"><div class="t">'+t.id+' · '+t.asunto+'</div><div class="m">'+t.estado+' · '+(t.tec||'sin asignar')+'</div></div>';}).join(''):'<div class="empty">Sin tickets críticos abiertos.</div>';
 el('cioLic').innerHTML=lic.length?lic.map(s=>{const d=Math.round((new Date(s.vig)-new Date())/864e5);return '<div class="it"><div class="t">'+s.prod+'</div><div class="m">vence en '+d+'d · '+money(s.costo)+'</div></div>';}).join(''):'<div class="empty">Sin licencias por vencer.</div>';
 el('cioSec').innerHTML=secAb.length?secAb.map(s=>'<div class="it"><div class="t">'+s.tipo+' '+rb(s.sev)+'</div><div class="m">'+(s.desc||'').slice(0,70)+' · '+s.estado+'</div></div>').join(''):'<div class="empty">Sin incidentes de seguridad abiertos.</div>';}
/* ====== demo ====== */
function seedDemo(){if(!confirm('Cargar un conjunto de datos de DEMOSTRACIÓN (tickets, activos, licencias, conocimiento, seguridad)? Se añade a lo existente.'))return;
 const now=Date.now();function ts(hAgo){return new Date(now-hAgo*36e5).toISOString().slice(0,19).replace('T',' ');}
 function mk(id,tipo,cat,asunto,sol,dep,imp,urg,estado,tec,hAgo,sol2){const prio=prioFrom(imp,urg);const sl=SLA[prio];const cr=ts(hAgo);const o={id:id,tipo:tipo,cat:cat,asunto:asunto,desc:'(demo) '+asunto,sol:sol,dep:dep,imp:imp,urg:urg,prio:prio,tec:tec,estado:estado,nivelEsc:1,creado:cr,venceResp:new Date(new Date(cr.replace(' ','T')).getTime()+sl.resp*36e5).toISOString().slice(0,19).replace('T',' '),venceSol:new Date(new Date(cr.replace(' ','T')).getTime()+sl.sol*36e5).toISOString().slice(0,19).replace('T',' '),sla:prio,ci:'',solucion:sol2||'',calif:estado==='Cerrado'?5:0,aprob:[],causa:'',traza:[{ts:cr,usuario:'demo',accion:'Ticket creado (demo)'}]};if(['Resuelto','Cerrado'].indexOf(estado)>=0)o.resuelto=ts(Math.max(0,hAgo-2));return o;}
 TK.push(mk('INC-'+nowYear()+'-9001','Incidente','Correo electrónico','No puedo enviar correo institucional','Lic. Vega','CUCEI','Alto','Alta','En proceso',D.tecnicos[3],6));
 TK.push(mk('INC-'+nowYear()+'-9002','Incidente','Impresoras','Impresora no responde en piso 3','Mtra. Ruiz','Oficina de la Abogacía General','Medio','Media','Asignado',D.tecnicos[0],30));
 TK.push(mk('REQ-'+nowYear()+'-9003','Solicitud','Alta de usuario','Alta de cuenta para nuevo abogado','RH','Oficina de la Abogacía General','Medio','Baja','Cerrado',D.tecnicos[1],72,'Cuenta creada en Active Directory y M365.'));
 TK.push(mk('INC-'+nowYear()+'-9004','Incidente','Sistema de gestión jurídica (SIGEJ)','Lentitud al abrir el tablero','Abog. Soto','CUCEA','Alto','Alta','Nuevo','',2));
 TK.push(mk('CHG-'+nowYear()+'-9005','Cambio','Actualización','Actualizar versión del SIGEJ a 2.4','CGTI','CGTI','Medio','Media','En evaluación','',48));
 TK.push(mk('PRB-'+nowYear()+'-9006','Problema','Redes','Caídas intermitentes de VPN','Soporte','CGTI','Alto','Media','En análisis',D.tecnicos[1],120));
 saveTK();
 CI.push({id:'CI-'+nowYear()+'-9001',clase:'Laptop',marca:'Dell',modelo:'Latitude 5440',serie:'DL5440-001',etiq:'UDG-AG-1201',resp:'Abog. Soto',dep:'Oficina de la Abogacía General',ubic:'Dirección',estado:'Operativo',gar:new Date(now+120*864e5).toISOString().slice(0,10),adq:'2024-02-15',fecha:todayISO()});
 CI.push({id:'CI-'+nowYear()+'-9002',clase:'Servidor',marca:'HPE',modelo:'ProLiant DL360',serie:'HP360-007',etiq:'UDG-AG-SRV07',resp:'CGTI',dep:'CGTI',ubic:'Site principal',estado:'Operativo',gar:new Date(now+30*864e5).toISOString().slice(0,10),adq:'2022-09-01',fecha:todayISO()});
 CI.push({id:'CI-'+nowYear()+'-9003',clase:'Impresora',marca:'HP',modelo:'LaserJet M428',serie:'HPM428-014',etiq:'UDG-AG-IMP14',resp:'Mesa de servicio',dep:'Oficina de la Abogacía General',ubic:'Piso 3',estado:'En reparación',gar:new Date(now-20*864e5).toISOString().slice(0,10),adq:'2021-05-10',fecha:todayISO()});
 saveCI();
 SW.push({id:'SW-'+nowYear()+'-9001',prod:'Microsoft 365',tipo:'Suscripción',cant:45,costo:180000,vig:new Date(now+60*864e5).toISOString().slice(0,10),uso:88,fecha:todayISO()});
 SW.push({id:'SW-'+nowYear()+'-9002',prod:'Antivirus / EDR',tipo:'Suscripción',cant:60,costo:54000,vig:new Date(now+25*864e5).toISOString().slice(0,10),uso:95,fecha:todayISO()});
 SW.push({id:'SW-'+nowYear()+'-9003',prod:'Power BI',tipo:'Suscripción',cant:10,costo:36000,vig:new Date(now+300*864e5).toISOString().slice(0,10),uso:70,fecha:todayISO()});
 saveSW();
 KB.push({id:'KB-'+nowYear()+'-9001',tipo:'Solución conocida',cat:'Correo electrónico',tit:'Outlook no envía: revisar conexión y perfil',cont:'1) Verificar conexión. 2) Reiniciar Outlook. 3) Reparar perfil en Panel de control > Correo. 4) Revisar buzón lleno.',tags:['outlook','correo','m365'],fecha:todayISO(),autor:'demo'});
 KB.push({id:'KB-'+nowYear()+'-9002',tipo:'Procedimiento',cat:'Accesos',tit:'Recuperación de contraseña institucional',cont:'Solicitar por autoservicio; validar identidad; restablecer en Active Directory; forzar cambio en primer inicio.',tags:['contraseña','accesos','ad'],fecha:todayISO(),autor:'demo'});
 saveKB();
 SEC.push({id:'SEC-'+nowYear()+'-9001',tipo:'Phishing',sev:'Alto',desc:'Campaña de correo suplantando a Rectoría solicitando credenciales.',act:'Correo institucional',acc:'Bloqueo de remitente y aviso a usuarios.',estado:'Contenido',fecha:ts(40)});
 saveSEC();
 el('i_msg').style.color='#7ee0b4';el('i_msg').textContent='✓ Datos de demostración cargados.';renderList();compute();alert('✓ Demo cargada: 6 tickets, 3 activos, 3 licencias, 2 artículos y 1 incidente de seguridad.');}
/* ====== init ====== */
function compute(){reloadAll();renderList();const t=new Date();el('upd').textContent='actualizado '+pad(t.getHours())+':'+pad(t.getMinutes())+':'+pad(t.getSeconds());}
window.addEventListener('storage',()=>{reloadAll();compute();});
window.addEventListener('focus',()=>{reloadAll();});
initForms();renderList();
const _t=new Date();el('upd').textContent='actualizado '+pad(_t.getHours())+':'+pad(_t.getMinutes())+':'+pad(_t.getSeconds());
</script>
<script>
/* Expediente electrónico — adjuntar archivos por categoría documental */
const DCATS=['Captura de pantalla','Evidencia','Orden de servicio','Reporte','Manual / guía','Otro'];let __DOCREF=null;
function __rec(ref){return (typeof ref==='number')?TK[ref]:TK.find(function(x){return x.id===ref;});}
function docExp(ref){var rec=__rec(ref);if(!rec)return;if(!rec.docs)rec.docs=[];
 var ov=document.getElementById('__docov')||document.createElement('div');ov.id='__docov';ov.style.cssText='position:fixed;inset:0;background:rgba(10,31,60,.5);display:flex;align-items:center;justify-content:center;z-index:99998;padding:18px';
 var co=DCATS.map(function(c){return '<option>'+c+'</option>';}).join('');
 var ls=rec.docs.length?rec.docs.map(function(x,k){return '<div style="font-size:12px;color:#334155;padding:4px 0;border-bottom:1px solid #eef2f7">\ud83d\udcce <b>'+(x.cat||'')+'</b> \u00b7 '+x.nombre+' \u00b7 '+(x.fecha||'')+' <a href="'+x.data+'" download="'+x.nombre+'">descargar</a> \u00b7 <span style="color:#0a4d8c;cursor:pointer;text-decoration:underline" onclick="docVerR(\''+(rec.id!=null?rec.id:ref)+'\','+k+')">\ud83d\udc41 ver</span></div>';}).join(''):'<div style="color:#64748b;font-size:12px">Sin documentos en el expediente.</div>';
 ov.innerHTML='<div style="background:#fff;border-radius:14px;max-width:640px;width:100%;max-height:85vh;overflow:auto;padding:20px"><span style="float:right;cursor:pointer;color:#64748b;font-size:20px" onclick="document.getElementById(\'__docov\').remove()">\u2715</span><h3 style="margin:0 0 4px;color:#0a4d8c">\ud83d\udcce Expediente electr\u00f3nico</h3><div style="font-size:12px;color:#64748b;margin-bottom:10px">'+((rec.folio||rec.exp||rec.id||rec.nombre||'')+' \u00b7 '+(rec.tipo||rec.asunto||rec.clasif||''))+'</div><div style="display:flex;gap:6px;align-items:center;margin-bottom:10px;flex-wrap:wrap"><select id="__doccat" style="padding:6px 8px;border:1px solid #cbd5e1;border-radius:6px;font-size:12px">'+co+'</select><button onclick="docPick(\''+(rec.id!=null?rec.id:ref)+'\')" style="padding:6px 11px;border:none;border-radius:7px;background:#0a4d8c;color:#fff;font-size:12px;font-weight:600;cursor:pointer">\ud83d\udcce Adjuntar archivo</button> <button onclick="docOCR(\''+(rec.id!=null?rec.id:ref)+'\')" style="padding:6px 11px;border:none;border-radius:7px;background:#d4a32c;color:#3a2c05;font-size:12px;font-weight:600;cursor:pointer">🔎 OCR / extraer datos</button></div>'+ls+'<div style="font-size:10.5px;color:#94a3b8;margin-top:10px">Conforma el expediente electr\u00f3nico del registro \u00b7 PDF/imagen/Word \u22641.8 MB (prototipo en este equipo).</div></div>';
 if(!ov.parentNode)document.body.appendChild(ov);}
function docPick(ref){__DOCREF=ref;var c=document.getElementById('__doccat');window.__dcat=c?c.value:(DCATS[0]||'Documento');var inp=document.getElementById('__docfile');if(!inp){inp=document.createElement('input');inp.type='file';inp.id='__docfile';inp.style.display='none';inp.onchange=docOn;document.body.appendChild(inp);}inp.value='';inp.click();}
function docOn(){var f=this.files[0];if(!f||__DOCREF==null)return;if(f.size>1.8e6){alert('M\u00e1ximo 1.8 MB por archivo.');return;}var rec=__rec(__DOCREF);if(!rec)return;if(!rec.docs)rec.docs=[];var r=new FileReader();r.onload=function(){rec.docs.push({nombre:f.name,tipo:f.type,cat:window.__dcat||'Documento',data:r.result,fecha:new Date().toISOString().slice(0,10)});try{saveTK();}catch(e){}if(window.__bitlog)__bitlog('Acci\u00f3n','Adjuntar documento al expediente ('+(window.__dcat||'')+')');docExp(__DOCREF);try{renderList();}catch(e){}};r.readAsDataURL(f);}
function docVerR(ref,k){var rec=__rec(ref);var x=rec.docs[k];var w=window.open('','_blank');if(!w)return;if(/image/.test(x.tipo))w.document.write('<img src="'+x.data+'" style="max-width:100%">');else if(/pdf/.test(x.tipo))w.document.write('<iframe src="'+x.data+'" style="border:0;width:100%;height:100vh"></iframe>');else w.document.write('<a href="'+x.data+'" download="'+x.nombre+'">Descargar '+x.nombre+'</a>');}
function docOCR(ref){var rec=__rec(ref);if(!rec)return;var t=prompt('Pega el texto del documento (escaneo/PDF). El OCR de imagen es fase backend; aquí se extraen datos por reglas y se llenan campos:','');if(t===null||!t.trim())return;var folio=(t.match(/\b\d{1,5}\s*\/\s*\d{2,4}(?:-[A-Za-z]+)?\b/)||[''])[0].replace(/\s/g,'');var fecha=(t.match(/\b\d{4}-\d{2}-\d{2}\b/)||t.match(/\b\d{1,2}\/\d{1,2}\/\d{4}\b/)||[''])[0];var monto=(t.match(/\$\s?[\d,]+(?:\.\d{2})?/)||[''])[0];var am=t.match(/asunto\s*:?\s*([^\n\r]+)/i);var asunto=am?am[1].trim():t.replace(/\s+/g,' ').trim().slice(0,120);rec.ocr={folio:folio,fecha:fecha,monto:monto};var cs=['asunto','obj','objeto','descripcion','desc','nota','observaciones','titulo','tit'];for(var ci=0;ci<cs.length;ci++){if(cs[ci] in rec){if(!rec[cs[ci]])rec[cs[ci]]=asunto;break;}}if(!rec.docs)rec.docs=[];rec.docs.push({nombre:'Texto OCR (reglas).txt',tipo:'text/plain',cat:'OCR / extracción',data:'data:text/plain;base64,'+btoa(unescape(encodeURIComponent(t.slice(0,5000)))),fecha:new Date().toISOString().slice(0,10)});try{saveTK();}catch(e){}if(window.__bitlog)__bitlog('Acción','OCR/extracción al expediente');alert('Extraído por reglas — Folio: '+(folio||'—')+' · Fecha: '+(fecha||'—')+(monto?' · Monto: '+monto:'')+'. Texto guardado en el expediente; se llenó el asunto si estaba vacío. (OCR de imagen real = fase backend.)');docExp(ref);try{renderList();}catch(e){}}
/* ================= Submódulo: Administración Central de Usuarios y Seguridad (IAM · RBAC/ABAC) ================= */
function iel(i){return document.getElementById(i);}
function ival(i){var e=iel(i);return e?(e.value||'').trim():'';}
function ichk(i){var e=iel(i);return !!(e&&e.checked);}
function iL(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function iLO(k,d){try{return JSON.parse(localStorage.getItem(k)||d);}catch(e){return JSON.parse(d);}}
function iS(k,v){localStorage.setItem(k,JSON.stringify(v));}
function iesc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function iuid(){return 'U'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function inow(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function ihoy(){return new Date().toISOString().slice(0,10);}
var IAM_ADMIN=['Administrador','Sistemas','Jefe del Área de Sistemas'];
function iamPerfil(){return localStorage.getItem('sigej_perfil')||'(perfil)';}
function iamIsAdmin(){return IAM_ADMIN.indexOf(iamPerfil())>=0;}
function iamGuardW(){if(iamIsAdmin())return true;alert('🔒 Acción restringida: solo el Administrador General del SIGEJ o el Administrador del Help Desk pueden administrar usuarios, permisos y cupos (segregación de funciones).');return false;}
var IAM_ROLES=['Administrador','Abogado General','Coordinador Jurídico','Coordinador de Enlace con la Red','Coordinador de Normatividad','Secretaría General','Director','Coordinador General','Jefe de Unidad de lo Contencioso','Jefe de Unidad de Atención y Servicios Legales','Jefe de Unidad de Patrimonio Intangible','Jefe de Unidad de Asuntos Internacionales','Jefe de Unidad de Instrumentos Jurídicos','Jefe de Unidad de Capacitación, Investigación y Difusión','Jefe de Unidad de Estatutos y Reglamentos','Jefe de Unidad de Normatividad Administrativa','Jefe de Unidad de Apoyo a Órganos Colegiados','Jefe del Área Contable','Jefe del Área de Personal','Jefe del Área de Sistemas','Jefe de Oficialía de Partes','Jefe de Mensajería','Abogado','Abogado de Centro Universitario','Abogado de Dependencia UdeG','Analista','Asistente','Sistemas'];
var IAM_TIPOS=['Interno OAG','Administrativo','Abogado','Coordinador','Director','Secretaría','Oficialía de Partes','Mensajería','Chofer','Help Desk','Becario','Servicio social','Temporal','Externo autorizado'];
var IAM_COORD=['— selecciona —','Abogacía General','Coordinación de lo Contencioso','Coordinación de Enlace con la Red','Coordinación de Normatividad','Secretaría General'];
var IAM_MODS=[['contencioso','Asuntos Contenciosos',45],['instrumentos','Instrumentos Jurídicos',18],['patrimonio','Patrimonio Intangible',8],['internacional','Asuntos Internacionales',12],['normatividad','Normatividad Universitaria',10],['oficialia','Oficialía de Partes',12],['administracion','Administración OAG',10],['desarrollo','Conocimiento y Desarrollo',10],['transparencia','Transparencia General',8],['helpdesk','Help Desk',5],['buscador','Buscador Global',160],['notificaciones','Notificaciones',160]];
function iamModName(k){for(var i=0;i<IAM_MODS.length;i++)if(IAM_MODS[i][0]===k)return IAM_MODS[i][1];return k;}
var IAM_PRIV=[['consultar','Consultar'],['crear','Crear'],['capturar','Capturar'],['modificar','Modificar'],['autorizar','Autorizar'],['firmar','Firmar'],['descargar','Descargar'],['exportar','Exportar'],['imprimir','Imprimir'],['compartir','Compartir'],['eliminar','Eliminar (baja lógica)'],['verConfid','Ver confidenciales'],['verDatosP','Ver datos personales'],['verReportes','Ver reportes'],['verDash','Ver dashboards'],['adminUsr','Administrar usuarios'],['configSis','Configurar sistema']];
var IAM_EXPROL=['Abogado responsable','Abogado auxiliar','Supervisor','Coordinador','Director'];
function iamPreset(rol){var p={};IAM_PRIV.forEach(function(x){p[x[0]]=false;});
 if(/Administrador|^Sistemas$/.test(rol)){IAM_PRIV.forEach(function(x){p[x[0]]=true;});return p;}
 p.consultar=true;p.verReportes=true;
 if(/Abogado$|Analista/.test(rol)){p.crear=p.capturar=p.modificar=p.descargar=p.imprimir=p.compartir=p.eliminar=true;}
 if(/Asistente/.test(rol)){p.capturar=p.descargar=p.imprimir=true;}
 if(/Coordinador|Director|Secretaría General|Abogado General|Jefe/.test(rol)){p.crear=p.modificar=p.autorizar=p.firmar=p.descargar=p.exportar=p.imprimir=p.verDash=p.verConfid=true;}
 if(/Jefe del Área de Sistemas/.test(rol)){p.adminUsr=true;p.configSis=true;}
 return p;}
function iamSeed(){
 if(!localStorage.getItem('sigej_iam_cupos')){var c={};IAM_MODS.forEach(function(m){c[m[0]]=m[2];});c.__total=170;iS('sigej_iam_cupos',c);}
 if(!localStorage.getItem('sigej_iam_seg'))iS('sigej_iam_seg',{f2a:true,minlen:12,expira:90,intentos:5,inactividad:15,ip:false,horario:false,ubic:false,dispositivos:true});
 if(!localStorage.getItem('sigej_iam_lic'))iS('sigej_iam_lic',{total:170,temporales:10,prueba:5,externos:15});
 if(!localStorage.getItem('sigej_usuarios')){iS('sigej_usuarios',[
  {id:iuid(),nombre:'Edith Roque Huerta',numEmp:'CU-1001',rol:'Administrador',tipo:'Interno OAG',cargo:'Administradora General SIGEJ',coord:'Abogacía General',unidad:'Dirección',area:'Dirección',correo:'eroque@udg.mx',estado:'Activo',usuario:'eroque',f2a:true,fAlta:'2026-01-15',mods:IAM_MODS.map(function(m){return m[0];}),perm:iamPreset('Administrador'),exps:[],lic:'LIC-0001',passSet:true},
  {id:iuid(),nombre:'Juan Pérez López',numEmp:'CU-1042',rol:'Abogado',tipo:'Abogado',cargo:'Abogado Laboral',coord:'Coordinación de lo Contencioso',unidad:'Unidad de lo Contencioso',area:'Laboral',correo:'jperez@udg.mx',estado:'Activo',usuario:'jperez',f2a:false,fAlta:'2026-02-01',mods:['contencioso','notificaciones','buscador'],perm:iamPreset('Abogado'),exps:[],lic:'LIC-0002',passSet:true},
  {id:iuid(),nombre:'María Gómez Ruiz',numEmp:'CU-1099',rol:'Jefe del Área de Sistemas',tipo:'Help Desk',cargo:'Administrador del Help Desk',coord:'Secretaría General',unidad:'Área de Sistemas',area:'Sistemas',correo:'mgomez@udg.mx',estado:'Activo',usuario:'mgomez',f2a:true,fAlta:'2026-01-20',mods:['helpdesk','buscador','notificaciones'],perm:iamPreset('Jefe del Área de Sistemas'),exps:[],lic:'LIC-0003',passSet:true}
 ]);}
}
function iamAudit(afectado,accion,antes,despues,justif){var A=iL('sigej_usuarios_audit');
 A.push({ts:inow(),admin:iamPerfil(),afectado:afectado||'',accion:accion,antes:antes==null?'':String(antes),despues:despues==null?'':String(despues),justif:justif||'',navegador:(navigator.userAgent||'').slice(0,90),equipo:(navigator.platform||'—'),ip:'(se resuelve en backend)'});
 iS('sigej_usuarios_audit',A);if(window.__bitlog)__bitlog('Seguridad',accion+(afectado?' · '+afectado:''));}
var IAMV='usuarios';
function iamGo(v){IAMV=v;[].forEach.call(document.querySelectorAll('#iamNav button'),function(b){b.className='bd mini';});var idx={usuarios:0,exp:1,cupos:2,lic:3,cap:4,seg:5,audit:6}[v];var bt=document.querySelectorAll('#iamNav button')[idx];if(bt)bt.className='b1 mini';renderIAM();}
function renderIAM(){iamSeed();var b=iel('iamBody');if(!b)return;
 var banner=iamIsAdmin()?'<div style="background:#e6f6ee;border:1px solid #bfe6cf;color:#15803d;border-radius:9px;padding:9px 13px;font-size:12px;margin-bottom:12px">🔓 Sesión con privilegios de administración («'+iesc(iamPerfil())+'»). Toda acción queda en la bitácora de auditoría inalterable.</div>':'<div style="background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:11px 14px;font-size:12.5px;margin-bottom:12px">🔒 <b>Acceso restringido.</b> La administración de usuarios, roles, permisos y cupos es <b>exclusiva</b> del Administrador General del SIGEJ y del Administrador del Help Desk. Tu perfil («'+iesc(iamPerfil())+'») puede <b>consultar</b> pero no modificar (segregación de funciones, Art. II).</div>';
 if(IAMV==='usuarios')b.innerHTML=banner+vUsuarios();
 else if(IAMV==='exp')b.innerHTML=banner+vExp();
 else if(IAMV==='cupos')b.innerHTML=banner+vCupos();
 else if(IAMV==='lic')b.innerHTML=banner+vLic();
 else if(IAMV==='cap'){b.innerHTML=banner+vCap();vCapChart();}
 else if(IAMV==='seg')b.innerHTML=banner+vSeg();
 else b.innerHTML=banner+vAudit();
}
function iamModsChecks(sel){return IAM_MODS.map(function(m){return '<label style="display:inline-flex;align-items:center;gap:4px;font-size:11.5px;margin:2px 10px 2px 0"><input type="checkbox" id="iam_mod_'+m[0]+'"'+((sel&&sel.indexOf(m[0])>=0)?' checked':'')+'> '+m[1]+'</label>';}).join('');}
function iamMatrixChecks(p){return IAM_PRIV.map(function(x){return '<label style="display:inline-flex;align-items:center;gap:4px;font-size:11.5px;margin:2px 10px 2px 0"><input type="checkbox" id="iam_priv_'+x[0]+'"'+((p&&p[x[0]])?' checked':'')+'> '+x[1]+'</label>';}).join('');}
function iamFillPreset(){var p=iamPreset(ival('u_rol'));IAM_PRIV.forEach(function(x){var e=iel('iam_priv_'+x[0]);if(e)e.checked=!!p[x[0]];});}
function iamFormHTML(){
 function fld(id,lab,ty){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+lab+'</label><input id="'+id+'"'+(ty?' type="'+ty+'"':'')+' style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px;font-size:13px"></div>';}
 function sel(id,lab,arr,ev){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+lab+'</label><select id="'+id+'"'+(ev?' onchange="'+ev+'"':'')+' style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px;font-size:13px">'+arr.map(function(x){return '<option>'+x+'</option>';}).join('')+'</select></div>';}
 var g='display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px';
 var h='<div style="font-weight:700;color:#0a4d8c;margin:12px 0 4px;font-size:13px">';
 return h+'📇 Datos generales</div><div style="'+g+'">'+fld('u_nombre','Nombre completo *')+fld('u_numEmp','Número de empleado')+fld('u_codU','Código universitario')+fld('u_curp','CURP')+fld('u_rfc','RFC')+fld('u_cargo','Cargo')+fld('u_categoria','Categoría')+fld('u_correo','Correo institucional')+fld('u_correoAlt','Correo alterno')+fld('u_tel','Teléfono')+fld('u_ext','Extensión')+'</div>'+
  h+'🏛️ Adscripción (obligatoria · Art. IV)</div><div style="'+g+'">'+sel('u_coord','Coordinación *',IAM_COORD)+fld('u_unidad','Unidad *')+fld('u_area','Área *')+fld('u_depto','Departamento')+fld('u_dependencia','Dependencia universitaria')+fld('u_centroU','Centro Universitario')+fld('u_sistema','Sistema')+fld('u_jefe','Jefe inmediato')+fld('u_super','Supervisor')+fld('u_coordinador','Coordinador')+'</div>'+
  h+'👤 Rol y tipo</div><div style="'+g+'">'+sel('u_rol','Rol (plantilla de permisos) *',IAM_ROLES,'iamFillPreset()')+sel('u_tipo','Tipo de usuario',IAM_TIPOS)+'</div>'+
  h+'🧩 Módulos autorizados (Art. V) — solo estos aparecerán en su menú</div><div style="padding:4px 0">'+iamModsChecks([])+'</div>'+
  h+'🔑 Matriz de privilegios (Art. VIII) — se prellena por rol; ajusta finamente</div><div style="padding:4px 0" id="u_matrix">'+iamMatrixChecks(iamPreset('Abogado'))+'</div>'+
  h+'⚙️ Configuración y seguridad</div><div style="'+g+'">'+fld('u_usuario','Usuario (login)')+fld('u_pass','Contraseña','password')+fld('u_fAlta','Fecha de alta','date')+'<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">Doble factor (2FA)</label><label style="font-size:12.5px"><input type="checkbox" id="u_f2a" checked> Exigir 2FA</label></div></div>'+
  '<div style="font-size:11px;color:#8a6d1a;background:#fff8e6;border:1px solid #e7c66b;border-radius:8px;padding:8px 10px;margin:8px 0">🔐 La contraseña se <b>cifra y almacena en el backend</b> (hash + salt); aquí no se guarda en claro. 2FA, caducidad y políticas se <b>aplican en el servidor</b>.</div>'+
  '<div style="margin-top:8px"><button class="b3" onclick="iamSaveUser()">＋ Crear usuario</button></div>';
}
function vUsuarios(){var U=iL('sigej_usuarios');var q=(ival('u_q')||'').toLowerCase();
 var act=U.filter(function(u){return u.estado==='Activo';}).length,sus=U.filter(function(u){return /Suspendido|Bloqueado/.test(u.estado);}).length,baja=U.filter(function(u){return u.estado==='Baja lógica';}).length;
 var kpi='<div class="kpis" style="margin-bottom:12px"><div class="kpi"><div class="n">'+U.length+'</div><div class="l">Usuarios</div></div><div class="kpi g"><div class="n">'+act+'</div><div class="l">Activos</div></div><div class="kpi y"><div class="n">'+sus+'</div><div class="l">Suspendidos/Bloqueados</div></div><div class="kpi r"><div class="n">'+baja+'</div><div class="l">Baja lógica</div></div></div>';
 var form=iamIsAdmin()?('<div class="card"><h3 style="cursor:pointer;margin:0" onclick="var f=iel(\'uForm\');f.style.display=(f.style.display===\'none\')?\'block\':\'none\'">➕ Alta de usuario — clic para abrir/cerrar</h3><div id="uForm" style="display:none">'+iamFormHTML()+'</div></div>'):'';
 var rows=U.map(function(u,i){return {u:u,i:i};}).filter(function(o){return !q||JSON.stringify(o.u).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:10px 0"><input id="u_q" value="'+iesc(ival('u_q'))+'" placeholder="🔎 Buscar usuario (nombre, cargo, adscripción, rol)…" oninput="renderIAM()" style="width:100%;padding:8px 10px;border:1px solid #d9e2ec;border-radius:8px"></div>';
 tbl+='<table style="width:100%;border-collapse:collapse;font-size:12.5px"><tr style="text-align:left;color:#64748b"><th style="padding:6px">Usuario</th><th>Cargo / Rol</th><th>Adscripción</th><th>Módulos</th><th>Estado</th></tr>';
 tbl+=rows.length?rows.map(function(o){var u=o.u;var c=u.estado==='Activo'?'#15803d':/Suspendido|Bloqueado/.test(u.estado)?'#b45309':u.estado==='Baja lógica'?'#c0392b':'#64748b';return '<tr style="cursor:pointer;border-top:1px solid #eef2f7" onclick="iamFicha('+o.i+')"><td style="padding:6px"><b>'+iesc(u.nombre)+'</b><br><span style="color:#64748b;font-size:11px">'+iesc(u.usuario||'—')+' · '+iesc(u.numEmp||'')+'</span></td><td>'+iesc(u.cargo||'')+'<br><span style="color:#64748b;font-size:11px">'+iesc(u.rol||'')+'</span></td><td style="font-size:11px">'+iesc(u.coord||'')+'<br>'+iesc(u.unidad||'')+' · '+iesc(u.area||'')+'</td><td style="font-size:11px">'+(u.mods||[]).length+'</td><td><span style="color:'+c+';font-weight:700">'+iesc(u.estado||'')+'</span></td></tr>';}).join(''):'<tr><td colspan="5" style="padding:16px;text-align:center;color:#64748b">Sin usuarios.</td></tr>';
 tbl+='</table>';return kpi+form+tbl;
}
function iamSaveUser(){if(!iamGuardW())return;
 var nombre=ival('u_nombre');if(!nombre){alert('El nombre completo es obligatorio.');return;}
 var coord=ival('u_coord'),unidad=ival('u_unidad'),area=ival('u_area');
 if(!coord||coord==='— selecciona —'||!unidad||!area){alert('Adscripción obligatoria: Coordinación, Unidad y Área (Art. IV). No pueden existir usuarios sin adscripción.');return;}
 var mods=IAM_MODS.filter(function(m){return ichk('iam_mod_'+m[0]);}).map(function(m){return m[0];});
 if(!mods.length){alert('Asigna al menos un módulo autorizado (Art. IV/V).');return;}
 var cupos=iLO('sigej_iam_cupos','{}');var U=iL('sigej_usuarios');
 var totalAct=U.filter(function(u){return u.estado==='Activo';}).length;
 if(cupos.__total&&totalAct>=cupos.__total){alert('⛔ Se alcanzó el límite de usuarios activos del sistema ('+cupos.__total+'). No se puede crear (Regla XVIII). Amplía la capacidad en «Cupos».');return;}
 var over=mods.filter(function(mk){var lim=cupos[mk];if(!lim)return false;var a=U.filter(function(u){return u.estado==='Activo'&&(u.mods||[]).indexOf(mk)>=0;}).length;return a>=lim;});
 if(over.length){alert('⛔ Cupo lleno en: '+over.map(iamModName).join(', ')+'. No se puede asignar (Regla XV/XVIII). Amplía el cupo en «Cupos por módulo».');return;}
 var perm={};IAM_PRIV.forEach(function(x){perm[x[0]]=ichk('iam_priv_'+x[0]);});
 var u={id:iuid(),nombre:nombre,numEmp:ival('u_numEmp'),codU:ival('u_codU'),curp:ival('u_curp'),rfc:ival('u_rfc'),cargo:ival('u_cargo'),categoria:ival('u_categoria'),correo:ival('u_correo'),correoAlt:ival('u_correoAlt'),tel:ival('u_tel'),ext:ival('u_ext'),coord:coord,unidad:unidad,area:area,depto:ival('u_depto'),dependencia:ival('u_dependencia'),centroU:ival('u_centroU'),sistema:ival('u_sistema'),jefeInm:ival('u_jefe'),supervisor:ival('u_super'),coordinador:ival('u_coordinador'),usuario:ival('u_usuario'),passSet:ival('u_pass')?true:false,f2a:ichk('u_f2a'),rol:ival('u_rol'),tipo:ival('u_tipo'),mods:mods,perm:perm,estado:'Activo',fAlta:ival('u_fAlta')||ihoy(),fUltMod:ihoy(),fUltAcceso:'',exps:[],lic:'LIC-'+String(U.length+1).padStart(4,'0'),creadoPor:iamPerfil()};
 U.push(u);iS('sigej_usuarios',U);
 iamAudit(nombre,'Alta de usuario ('+u.rol+')','',nombre+' · '+mods.length+' módulos · '+coord,'Alta inicial');
 alert('✓ Usuario «'+nombre+'» creado y licencia '+u.lic+' asignada.');renderIAM();
}
function iamFicha(i){var U=iL('sigej_usuarios');var u=U[i];if(!u)return;var adm=iamIsAdmin();
 var perm=IAM_PRIV.filter(function(x){return u.perm&&u.perm[x[0]];}).map(function(x){return '<span style="display:inline-block;background:#e6f0fb;color:#0a4d8c;border-radius:11px;padding:1px 8px;font-size:10.5px;margin:1px">'+x[1]+'</span>';}).join('')||'—';
 var mods=(u.mods||[]).map(function(mk){return '<span style="display:inline-block;background:#eef2f7;border:1px solid #dbe3ec;border-radius:11px;padding:1px 8px;font-size:10.5px;margin:1px">'+iamModName(mk)+'</span>';}).join('')||'—';
 var exps=(u.exps||[]).length?(u.exps||[]).map(function(e){return '<div style="font-size:11.5px">📁 '+iesc(e.folio)+' — '+iesc(e.rol)+'</div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin expedientes asignados.</span>';
 var acc=adm?('<div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:10px">'+
   '<button class="bd mini" onclick="iamSetEstado('+i+',\'Suspendido\')">⏸ Suspender</button><button class="bd mini" onclick="iamSetEstado('+i+',\'Activo\')">▶ Reactivar</button><button class="bd mini" onclick="iamSetEstado('+i+',\'Bloqueado\')">🔒 Bloquear</button><button class="bd mini" onclick="iamSetEstado('+i+',\'Baja lógica\')">🗑 Baja lógica</button>'+
   '<button class="bd mini" onclick="iamReset('+i+')">🔑 Restablecer contraseña</button><button class="bd mini" onclick="iamCorreo('+i+')">✉️ Cambiar correo</button><button class="bd mini" onclick="iamAdscrip('+i+')">🏛️ Cambiar adscripción</button><button class="bd mini" onclick="iamSesion('+i+')">🚪 Cerrar sesión remota</button></div>'):'<div style="color:#64748b;font-size:12px;margin-top:8px">Solo lectura (perfil sin privilegios de administración).</div>';
 iel('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+iesc(u.nombre)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+iesc(u.cargo||'')+' · '+iesc(u.rol||'')+' · <b style="color:'+(u.estado==='Activo'?'#15803d':'#c0392b')+'">'+iesc(u.estado)+'</b></div>'+
  '<div style="background:#f8fafc;border:1px solid #eef2f7;border-radius:9px;padding:10px;font-size:12.5px;line-height:1.7"><b>Usuario:</b> '+iesc(u.usuario||'—')+' · <b>Emp:</b> '+iesc(u.numEmp||'—')+' · <b>Lic:</b> '+iesc(u.lic||'—')+'<br><b>CURP:</b> '+iesc(u.curp||'—')+' · <b>RFC:</b> '+iesc(u.rfc||'—')+'<br><b>Correo:</b> '+iesc(u.correo||'—')+'<br><b>Adscripción:</b> '+iesc(u.coord||'')+' · '+iesc(u.unidad||'')+' · '+iesc(u.area||'')+'<br><b>2FA:</b> '+(u.f2a?'sí':'no')+' · <b>Alta:</b> '+iesc(u.fAlta||'—')+' · <b>Últ. mod.:</b> '+iesc(u.fUltMod||'—')+'</div>'+
  '<div style="margin-top:8px"><b style="font-size:12px">🧩 Módulos autorizados</b><div style="margin-top:4px">'+mods+'</div></div>'+
  '<div style="margin-top:8px"><b style="font-size:12px">🔑 Privilegios</b><div style="margin-top:4px">'+perm+'</div></div>'+
  '<div style="margin-top:8px"><b style="font-size:12px">📁 Expedientes</b><div style="margin-top:4px">'+exps+'</div></div>'+
  acc+'<div style="margin-top:10px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 iel('drw').classList.add('on');
}
function iamSetEstado(i,est){if(!iamGuardW())return;var U=iL('sigej_usuarios');var u=U[i];if(!u)return;if(u.estado===est){alert('El usuario ya está en «'+est+'».');return;}
 var j=prompt('Justificación del cambio de estado a «'+est+'» (obligatoria, Art. XII):','');if(j===null)return;var antes=u.estado;u.estado=est;u.fUltMod=ihoy();iS('sigej_usuarios',U);
 iamAudit(u.nombre,'Cambio de estado',antes,est,j||'—');
 if(/Baja|Suspendido/.test(est))iamAudit(u.nombre,'Licencia liberada automáticamente ('+est+')',u.lic,'disponible','Recuperación automática (Art. XVI)');
 iamFicha(i);
}
function iamReset(i){if(!iamGuardW())return;var U=iL('sigej_usuarios');var u=U[i];var j=prompt('Motivo del restablecimiento de contraseña de '+u.nombre+':','');if(j===null)return;u.fUltMod=ihoy();iS('sigej_usuarios',U);iamAudit(u.nombre,'Restablecimiento de contraseña','','(enlace enviado)',j||'—');alert('🔑 Se generó un enlace de restablecimiento (envío por el backend). Registrado en auditoría.');}
function iamCorreo(i){if(!iamGuardW())return;var U=iL('sigej_usuarios');var u=U[i];var nc=prompt('Nuevo correo institucional (actual: '+(u.correo||'—')+'):',u.correo||'');if(nc===null||!nc.trim())return;var antes=u.correo;u.correo=nc.trim();u.fUltMod=ihoy();iS('sigej_usuarios',U);iamAudit(u.nombre,'Cambio de correo',antes,u.correo,'Solicitud de cambio');iamFicha(i);}
function iamAdscrip(i){if(!iamGuardW())return;var U=iL('sigej_usuarios');var u=U[i];var co=prompt('Coordinación:',u.coord||'');if(co===null)return;var un=prompt('Unidad:',u.unidad||'');if(un===null)return;var ar=prompt('Área:',u.area||'');if(ar===null)return;var antes=u.coord+' / '+u.unidad+' / '+u.area;u.coord=co.trim()||u.coord;u.unidad=un.trim()||u.unidad;u.area=ar.trim()||u.area;u.fUltMod=ihoy();iS('sigej_usuarios',U);iamAudit(u.nombre,'Cambio de adscripción',antes,u.coord+' / '+u.unidad+' / '+u.area,'Reubicación institucional');iamAudit(u.nombre,'Licencia revisada por cambio de adscripción',u.lic,u.lic,'Art. XVI');iamFicha(i);}
function iamSesion(i){if(!iamGuardW())return;var U=iL('sigej_usuarios');var u=U[i];iamAudit(u.nombre,'Cierre remoto de sesión','activa','cerrada','Control de sesiones (Art. XI)');alert('🚪 Sesión(es) de '+u.nombre+' marcada(s) para cierre remoto (ejecuta el backend). Registrado en auditoría.');}
function vExp(){var U=iL('sigej_usuarios').filter(function(u){return u.estado==='Activo';});var AS=iL('sigej_exp_asig');var RE=iL('sigej_exp_reasig');
 var uopt=U.map(function(u){return '<option value="'+u.id+'">'+iesc(u.nombre)+' ('+iesc(u.rol)+')</option>';}).join('');
 var f=iamIsAdmin()?('<div class="card"><h3 style="margin:0 0 6px">📁 Asignar expediente (Art. VI)</h3><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:8px"><div><label style="font-size:11px;color:#64748b">Expediente / folio</label><input id="ax_exp" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px"></div><div><label style="font-size:11px;color:#64748b">Usuario</label><select id="ax_usr" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px">'+uopt+'</select></div><div><label style="font-size:11px;color:#64748b">Rol en el expediente</label><select id="ax_rol" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px">'+IAM_EXPROL.map(function(x){return '<option>'+x+'</option>';}).join('')+'</select></div></div><div style="margin-top:8px"><button class="b3" onclick="iamAsignarExp()">＋ Asignar</button></div></div>'+
  '<div class="card"><h3 style="margin:0 0 6px">🔁 Reasignar expediente (Art. VII · nunca borra historial)</h3><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:8px"><div><label style="font-size:11px;color:#64748b">Expediente / folio</label><input id="rx_exp" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px"></div><div><label style="font-size:11px;color:#64748b">Nuevo abogado</label><select id="rx_usr" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px">'+uopt+'</select></div><div><label style="font-size:11px;color:#64748b">Autorizó</label><input id="rx_aut" placeholder="Quién autorizó" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px"></div></div><div style="margin-top:6px"><input id="rx_mot" placeholder="Motivo de la reasignación" style="width:100%;padding:7px 9px;border:1px solid #d9e2ec;border-radius:7px"></div><div style="margin-top:8px"><button class="b1" onclick="iamReasignar()">🔁 Reasignar</button></div></div>'):'';
 var tA='<div class="card"><h3 style="margin:0 0 6px">Asignaciones vigentes</h3>'+(AS.length?'<table style="width:100%;font-size:12px;border-collapse:collapse"><tr style="text-align:left;color:#64748b"><th style="padding:5px">Expediente</th><th>Usuario</th><th>Rol</th><th>Fecha</th></tr>'+AS.map(function(a){return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px">'+iesc(a.folio)+'</td><td>'+iesc(a.usuario)+'</td><td>'+iesc(a.rol)+'</td><td>'+iesc(a.fecha)+'</td></tr>';}).join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin asignaciones.</div>')+'</div>';
 var tR='<div class="card"><h3 style="margin:0 0 6px">🧾 Historial de reasignaciones (inalterable)</h3>'+(RE.length?RE.map(function(r){return '<div style="border-left:3px solid #0a4d8c;padding:6px 10px;margin:6px 0;background:#f8fafc;font-size:12px"><b>'+iesc(r.folio)+'</b>: '+iesc(r.anterior)+' → <b>'+iesc(r.nuevo)+'</b><br><span style="color:#64748b">'+iesc(r.fecha)+' '+iesc(r.hora)+' · autorizó: '+iesc(r.autorizo||'—')+' · realizó: '+iesc(r.realizo)+' · motivo: '+iesc(r.motivo||'—')+'</span></div>';}).join(''):'<div style="color:#64748b;font-size:12px">Sin reasignaciones.</div>')+'</div>';
 return f+tA+tR;
}
function iamAsignarExp(){if(!iamGuardW())return;var exp=ival('ax_exp');if(!exp){alert('Indica el expediente.');return;}var U=iL('sigej_usuarios');var u=U.filter(function(x){return x.id===ival('ax_usr');})[0];if(!u)return;var rol=ival('ax_rol');var AS=iL('sigej_exp_asig');AS.push({folio:exp,usuario:u.nombre,uid:u.id,rol:rol,fecha:ihoy(),por:iamPerfil()});iS('sigej_exp_asig',AS);u.exps=u.exps||[];u.exps.push({folio:exp,rol:rol});iS('sigej_usuarios',U);iamAudit(u.nombre,'Asignación de expediente '+exp+' ('+rol+')','',exp,'Asignación');alert('✓ Expediente '+exp+' asignado a '+u.nombre+' ('+rol+').');renderIAM();}
function iamReasignar(){if(!iamGuardW())return;var exp=ival('rx_exp');if(!exp){alert('Indica el expediente.');return;}var U=iL('sigej_usuarios');var nu=U.filter(function(x){return x.id===ival('rx_usr');})[0];if(!nu)return;var AS=iL('sigej_exp_asig');var prev=AS.filter(function(a){return a.folio===exp&&/responsable/i.test(a.rol);}).slice(-1)[0];var anterior=prev?prev.usuario:'(sin responsable previo)';var mot=ival('rx_mot');var RE=iL('sigej_exp_reasig');RE.push({folio:exp,anterior:anterior,nuevo:nu.nombre,fecha:ihoy(),hora:inow().slice(11,16),autorizo:ival('rx_aut'),realizo:iamPerfil(),motivo:mot,doc:'',obs:''});iS('sigej_exp_reasig',RE);AS.push({folio:exp,usuario:nu.nombre,uid:nu.id,rol:'Abogado responsable',fecha:ihoy(),por:iamPerfil()});iS('sigej_exp_asig',AS);iamAudit(nu.nombre,'Reasignación de expediente '+exp,anterior,nu.nombre,mot||'—');alert('🔁 Expediente '+exp+' reasignado a '+nu.nombre+'. Historial conservado (Art. VII).');renderIAM();}
function vCupos(){var cupos=iLO('sigej_iam_cupos','{}');var U=iL('sigej_usuarios');var dis=!iamIsAdmin();
 var rows=IAM_MODS.map(function(m){var act=U.filter(function(u){return u.estado==='Activo'&&(u.mods||[]).indexOf(m[0])>=0;}).length;var lim=cupos[m[0]]||0;var disp=lim-act;var pct=lim?Math.round(100*act/lim):0;var c=pct>=100?'#c0392b':pct>=90?'#e08e0b':pct>=80?'#d4a32c':'#15803d';return '<tr style="border-top:1px solid #eef2f7"><td style="padding:6px">'+m[1]+'</td><td><input id="cup_'+m[0]+'" type="number" min="0" value="'+lim+'"'+(dis?' disabled':'')+' style="width:80px;padding:5px;border:1px solid #d9e2ec;border-radius:6px"></td><td>'+act+'</td><td style="color:'+(disp<0?'#c0392b':'#15803d')+';font-weight:700">'+disp+'</td><td style="color:'+c+';font-weight:700">'+pct+'%</td></tr>';}).join('');
 return '<div class="card"><h3 style="margin:0 0 6px">🎚️ Cupos de usuarios por módulo (Art. XV) — límites independientes</h3>'+
  '<div style="display:flex;gap:10px;align-items:center;margin-bottom:8px;flex-wrap:wrap"><label style="font-size:12.5px">Límite total del sistema:</label><input id="cup_total" type="number" min="0" value="'+(cupos.__total||0)+'"'+(dis?' disabled':'')+' style="width:90px;padding:6px;border:1px solid #d9e2ec;border-radius:6px"> <span style="font-size:12px;color:#64748b">(120 trabajadores + abogados comisionados, ~2 por Centro Universitario)</span></div>'+
  '<table style="width:100%;font-size:12.5px;border-collapse:collapse"><tr style="text-align:left;color:#64748b"><th style="padding:6px">Módulo</th><th>Autorizados</th><th>Activos</th><th>Disponibles</th><th>Ocupación</th></tr>'+rows+'</table>'+
  (dis?'<div style="color:#64748b;font-size:12px;margin-top:8px">Solo el Administrador puede modificar cupos (Regla XVIII).</div>':'<div style="margin-top:10px"><button class="b3" onclick="iamSaveCupos()">💾 Guardar cupos</button></div>')+'</div>';
}
function iamSaveCupos(){if(!iamGuardW())return;var cupos=iLO('sigej_iam_cupos','{}');var antes=JSON.stringify(cupos);cupos.__total=+ival('cup_total')||0;IAM_MODS.forEach(function(m){cupos[m[0]]=+ival('cup_'+m[0])||0;});iS('sigej_iam_cupos',cupos);var j=prompt('Motivo/autorización del ajuste de cupos (Regla XVIII):','');iamAudit('(sistema)','Modificación de cupos de usuarios',antes,JSON.stringify(cupos),j||'—');alert('💾 Cupos actualizados y registrados en auditoría.');renderIAM();}
function vLic(){var lic=iLO('sigej_iam_lic','{}');var U=iL('sigej_usuarios');var enUso=U.filter(function(u){return u.estado==='Activo';}).length;var susp=U.filter(function(u){return /Suspendido|Bloqueado/.test(u.estado);}).length;var disp=(lic.total||0)-enUso;var ext=U.filter(function(u){return u.tipo==='Externo autorizado';}).length;var temp=U.filter(function(u){return u.tipo==='Temporal';}).length;var dis=!iamIsAdmin();
 function f(id,lab,v){return '<div><label style="font-size:11px;color:#64748b;display:block">'+lab+'</label><input id="'+id+'" type="number" min="0" value="'+(v||0)+'"'+(dis?' disabled':'')+' style="width:100%;padding:7px;border:1px solid #d9e2ec;border-radius:6px"></div>';}
 return '<div class="kpis" style="margin-bottom:12px"><div class="kpi"><div class="n">'+(lic.total||0)+'</div><div class="l">Licencias contratadas</div></div><div class="kpi y"><div class="n">'+enUso+'</div><div class="l">En uso</div></div><div class="kpi g"><div class="n">'+disp+'</div><div class="l">Disponibles</div></div><div class="kpi r"><div class="n">'+susp+'</div><div class="l">Suspendidas (recuperables)</div></div></div>'+
  '<div class="card"><h3 style="margin:0 0 6px">🪪 Administración de licencias y cupos (Art. XVI)</h3><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px">'+f('lic_total','Total contratadas',lic.total)+f('lic_temp','Temporales',lic.temporales)+f('lic_prueba','De prueba',lic.prueba)+f('lic_ext','Para externos',lic.externos)+'</div>'+
  '<div style="font-size:12px;color:#475569;margin-top:8px">En uso por externos: <b>'+ext+'</b> · temporales activas: <b>'+temp+'</b>. La licencia se <b>recupera automáticamente</b> al dar de baja, suspender o cambiar de adscripción al usuario (Art. XVI).</div>'+
  (dis?'':'<div style="margin-top:10px"><button class="b3" onclick="iamSaveLic()">💾 Guardar licencias</button></div>')+'</div>';
}
function iamSaveLic(){if(!iamGuardW())return;var lic=iLO('sigej_iam_lic','{}');var antes=JSON.stringify(lic);lic.total=+ival('lic_total')||0;lic.temporales=+ival('lic_temp')||0;lic.prueba=+ival('lic_prueba')||0;lic.externos=+ival('lic_ext')||0;iS('sigej_iam_lic',lic);var j=prompt('Motivo/autorización del ajuste de licencias:','');iamAudit('(sistema)','Modificación de licencias',antes,JSON.stringify(lic),j||'—');alert('💾 Licencias actualizadas y auditadas.');renderIAM();}
function vCap(){var cupos=iLO('sigej_iam_cupos','{}');var lic=iLO('sigej_iam_lic','{}');var U=iL('sigej_usuarios');
 var act=U.filter(function(u){return u.estado==='Activo';}).length,sus=U.filter(function(u){return /Suspendido|Bloqueado/.test(u.estado);}).length;
 var interno=U.filter(function(u){return u.tipo!=='Externo autorizado';}).length,externo=U.length-interno;
 var alerts=[];var bars=IAM_MODS.map(function(m){var a=U.filter(function(u){return u.estado==='Activo'&&(u.mods||[]).indexOf(m[0])>=0;}).length;var lim=cupos[m[0]]||0;var pct=lim?Math.round(100*a/lim):0;var c=pct>=100?'#c0392b':pct>=90?'#e08e0b':pct>=80?'#d4a32c':'#1aa39a';if(pct>=80)alerts.push(m[1]+' '+pct+'%');return '<div style="margin:5px 0"><div style="display:flex;justify-content:space-between;font-size:11.5px"><span>'+m[1]+'</span><span style="color:'+c+';font-weight:700">'+a+'/'+lim+' ('+pct+'%)</span></div><div style="height:9px;background:#eef2f7;border-radius:6px;overflow:hidden"><div style="height:100%;width:'+Math.min(100,pct)+'%;background:'+c+'"></div></div></div>';}).join('');
 var kp='<div class="kpis" style="margin-bottom:12px"><div class="kpi"><div class="n">'+(cupos.__total||0)+'</div><div class="l">Autorizados (sistema)</div></div><div class="kpi g"><div class="n">'+act+'</div><div class="l">Activos</div></div><div class="kpi y"><div class="n">'+sus+'</div><div class="l">Suspendidos</div></div><div class="kpi"><div class="n">'+((lic.total||0)-act)+'</div><div class="l">Licencias disponibles</div></div><div class="kpi"><div class="n">'+interno+' / '+externo+'</div><div class="l">Internos / externos</div></div></div>';
 var al=alerts.length?'<div style="background:#fef3e2;border:1px solid #e7c66b;color:#b45309;border-radius:9px;padding:10px 13px;font-size:12.5px;margin-bottom:10px">⚠️ <b>Alertas de capacidad (≥80%):</b> '+alerts.join(' · ')+' — planifica ampliación antes de agotar cupos (Art. XVII).</div>':'';
 var proj='<div style="background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:10px 13px;font-size:12.5px;margin-top:10px">📈 <b>Proyección (heurística):</b> con '+act+' usuarios activos de '+(cupos.__total||0)+' autorizados ('+(cupos.__total?Math.round(100*act/cupos.__total):0)+'% de ocupación), '+((lic.total||0)-act)+' licencias libres. La tendencia de crecimiento y la proyección de nuevas licencias requeridas se calculan con el histórico en el backend/Power BI.</div>';
 return kp+al+'<div class="card"><h3 style="margin:0 0 6px">📊 Ocupación por módulo (Art. XVII)</h3>'+bars+'</div><div class="card"><h3 style="margin:0 0 6px">Usuarios por módulo</h3><canvas id="iamCapCh" height="120"></canvas></div>'+proj;
}
function vCapChart(){try{var U=iL('sigej_usuarios');var labels=IAM_MODS.map(function(m){return m[1];});var data=IAM_MODS.map(function(m){return U.filter(function(u){return u.estado==='Activo'&&(u.mods||[]).indexOf(m[0])>=0;}).length;});if(window.__iamCh)window.__iamCh.destroy();var c=iel('iamCapCh');if(c&&window.Chart)window.__iamCh=new Chart(c,{type:'bar',data:{labels:labels,datasets:[{data:data,backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}}
function vSeg(){var s=iLO('sigej_iam_seg','{}');var dis=!iamIsAdmin();function d(){return dis?' disabled':'';}
 function chk(id,lab,v){return '<label style="display:block;font-size:12.5px;margin:4px 0"><input type="checkbox" id="'+id+'"'+(v?' checked':'')+d()+'> '+lab+'</label>';}
 function num(id,lab,v){return '<div><label style="font-size:11px;color:#64748b;display:block">'+lab+'</label><input id="'+id+'" type="number" min="0" value="'+(v||0)+'"'+d()+' style="width:100%;padding:7px;border:1px solid #d9e2ec;border-radius:6px"></div>';}
 return '<div class="card"><h3 style="margin:0 0 6px">🔒 Control de seguridad (Art. XIII)</h3><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:8px">'+num('sg_min','Longitud mínima de contraseña',s.minlen)+num('sg_exp','Caducidad de contraseña (días)',s.expira)+num('sg_int','Bloqueo tras N intentos fallidos',s.intentos)+num('sg_ina','Cierre por inactividad (min)',s.inactividad)+'</div><div style="margin-top:8px">'+chk('sg_f2a','Exigir doble factor (2FA)',s.f2a)+chk('sg_ip','Restricción por IP',s.ip)+chk('sg_hor','Restricción por horario',s.horario)+chk('sg_ubi','Restricción por ubicación',s.ubic)+chk('sg_disp','Registro de dispositivos autorizados',s.dispositivos)+'</div>'+
  '<div style="font-size:11.5px;color:#8a6d1a;background:#fff8e6;border:1px solid #e7c66b;border-radius:8px;padding:8px 10px;margin:8px 0">🛡️ Estas políticas se <b>aplican en el backend</b> (2FA real, hashing, bloqueo por intentos, cierre por inactividad, geo/IP/horario, registro de dispositivos). Aquí se definen y auditan los parámetros.</div>'+
  (dis?'':'<div><button class="b3" onclick="iamSaveSeg()">💾 Guardar políticas</button></div>')+'</div>';
}
function iamSaveSeg(){if(!iamGuardW())return;var s=iLO('sigej_iam_seg','{}');var antes=JSON.stringify(s);s.minlen=+ival('sg_min')||0;s.expira=+ival('sg_exp')||0;s.intentos=+ival('sg_int')||0;s.inactividad=+ival('sg_ina')||0;s.f2a=ichk('sg_f2a');s.ip=ichk('sg_ip');s.horario=ichk('sg_hor');s.ubic=ichk('sg_ubi');s.dispositivos=ichk('sg_disp');iS('sigej_iam_seg',s);iamAudit('(sistema)','Modificación de políticas de seguridad',antes,JSON.stringify(s),'Ajuste de seguridad');alert('💾 Políticas guardadas y auditadas.');renderIAM();}
function vAudit(){if(!iamIsAdmin())return '<div style="color:#64748b;font-size:13px;padding:14px">La bitácora de auditoría solo es accesible para el Administrador General, el Administrador del Help Desk o un auditor autorizado (Art. XI).</div>';
 var A=iL('sigej_usuarios_audit').slice().reverse();var q=(ival('au_q')||'').toLowerCase();var rows=A.filter(function(r){return !q||JSON.stringify(r).toLowerCase().indexOf(q)>=0;}).slice(0,300);
 return '<div style="margin-bottom:8px"><input id="au_q" value="'+iesc(ival('au_q'))+'" placeholder="🔎 Filtrar auditoría (usuario, acción, admin)…" oninput="renderIAM()" style="width:100%;padding:8px;border:1px solid #d9e2ec;border-radius:8px"></div>'+
  '<div style="font-size:11.5px;color:#64748b;margin-bottom:6px">'+A.length+' registro(s) · bitácora <b>inalterable</b> (solo lectura, sin edición ni borrado · Art. XII). La dirección IP se resuelve en el backend.</div>'+
  '<table style="width:100%;font-size:11.5px;border-collapse:collapse"><tr style="text-align:left;color:#64748b"><th style="padding:5px">Fecha/hora</th><th>Admin</th><th>Acción</th><th>Afectado</th><th>Antes → Después</th><th>Justificación</th></tr>'+
  (rows.length?rows.map(function(r){return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px;white-space:nowrap">'+iesc(r.ts)+'</td><td>'+iesc(r.admin)+'</td><td>'+iesc(r.accion)+'</td><td>'+iesc(r.afectado)+'</td><td style="font-size:10.5px;color:#475569">'+iesc((r.antes||'—').slice(0,30))+' → '+iesc((r.despues||'—').slice(0,30))+'</td><td style="font-size:10.5px">'+iesc(r.justif||'—')+'</td></tr>';}).join(''):'<tr><td colspan="6" style="padding:14px;text-align:center;color:#64748b">Sin registros de auditoría.</td></tr>')+'</table>';
}

</script>
__SNIP__
</body></html>"""
html=TPL.replace("__DATA__",DATAJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"helpdesk_SIGEJ.html","w",encoding="utf-8").write(html)
print("helpdesk_SIGEJ.html OK -",len(html),"bytes | técnicos",len(DATA["tecnicos"]),"| catInc",len(DATA["catInc"]),"| módulos monitoreados",len(DATA["modulos"]))
