# -*- coding: utf-8 -*-
# Módulo de Asuntos Internacionales (Global Mobility / Immigration / International Agreements / Translation)
# Unidad de Asuntos Internacionales · OAG UdeG — Art. 221 RIAG-UdeG (texto a confirmar en fuente oficial).
# Arranca vacío (catálogos). Acceso: equipo jurídico. Sin backend (prototipo cliente).
import json
B="/Users/edithroque/Documents/CLAUDE/"

CLASES=[
 {"clase":"Migración (persona extranjera)","ic":"🛂","sub":["Investigador","Profesor visitante","Conferencista","Artista","Deportista","Técnico","Administrativo","Becario","Estudiante","Personal de organismo internacional"]},
 {"clase":"Movilidad de personal UdeG","ic":"✈️","sub":["Congreso","Seminario","Estancia de investigación","Sabático","Misión institucional","Programa de intercambio","Delegación"]},
 {"clase":"Convenio internacional","ic":"🤝","sub":["Convenio general de cooperación","Convenio específico","Intercambio de estudiantes","Intercambio de académicos","Doble titulación","Cotutela","Investigación conjunta","Red internacional","Movilidad","Programa multilateral"]},
 {"clase":"Traducción jurídica","ic":"🌐","sub":["Traducción oficial","Traducción certificada","Dictamen terminológico","Glosario institucional"]},
 {"clase":"Trámite consular / aduanal","ic":"📦","sub":["Apostilla","Legalización","Certificación","Importación temporal","Exportación","Equipo científico","Material biológico","Obra de arte"]},
 {"clase":"Derecho internacional privado","ic":"⚖️","sub":["Exhorto internacional","Carta rogatoria","Reconocimiento de sentencia extranjera","Ley aplicable","Contratación internacional","Arbitraje internacional"]},
]
FLUJOS={
 "Condición de estancia (INM)":["Solicitud","Integración documental","Carta de invitación","Cita ante INM","Trámite ante INM","Resolución","Tarjeta de residencia","Control de vigencia"],
 "Visa (consulado)":["Solicitud","Carta de invitación","Cita consular","Entrevista","Resolución","Emisión de visa","Registro"],
 "Prórroga / cambio de condición":["Solicitud","Documentación","Trámite ante INM","Resolución","Actualización"],
 "Regularización migratoria":["Solicitud","Integración documental","Trámite ante INM","Resolución","Tarjeta de residencia"],
 "Movilidad saliente":["Planeación","Pasaporte / visa","Seguro de viaje","Autorización institucional","Comisión / viaje","Informe de comisión"],
 "Convenio internacional":["Propuesta","Revisión jurídica","Traducción","Validación","Firma","Seguimiento","Prórroga / Terminación"],
 "Traducción jurídica":["Solicitud","Asignación","Traducción","Revisión terminológica","Certificación","Entrega"],
 "Trámite consular / aduanal":["Solicitud","Documentación","Trámite (SAT/Aduanas/Consulado)","Certificación","Entrega"],
 "Genérico":["Solicitud","Revisión","Trámite","Resolución","Archivo"],
}
CLASE_TRAMITE={"Migración (persona extranjera)":"Condición de estancia (INM)","Movilidad de personal UdeG":"Movilidad saliente","Convenio internacional":"Convenio internacional","Traducción jurídica":"Traducción jurídica","Trámite consular / aduanal":"Trámite consular / aduanal"}
CONDICIONES=["Visitante sin permiso para actividades remuneradas","Visitante con permiso para actividades remuneradas","Residente temporal","Residente temporal estudiante","Residente permanente","Visitante por razones humanitarias","Refugiado / protección complementaria","No aplica"]
VISAS=["(no aplica)","B-1 (negocios)","B-2 (turista)","F-1 (estudiante)","J-1 (intercambio)","H-1B (trabajo especializado)","TN (TMEC)","O-1 (habilidad extraordinaria)","P (artistas/deportistas)","Schengen","Reino Unido","Canadá (visitante/estudio/trabajo)","Visa mexicana de residencia"]
PAISES=["México","Estados Unidos","Canadá","España","Francia","Alemania","Italia","Reino Unido","Portugal","Países Bajos","Bélgica","Suiza","China","Japón","Corea del Sur","India","Brasil","Argentina","Chile","Colombia","Perú","Cuba","Australia","Rusia","Sudáfrica","Marruecos","Egipto","Emiratos Árabes Unidos","Turquía","Polonia","Suecia","Noruega","Finlandia","Irlanda","Austria","Grecia","Israel","Nueva Zelanda"]
IDIOMAS=["Inglés","Francés","Alemán","Italiano","Portugués","Chino","Japonés","Árabe","Español"]
CU=["CUAAD","CUCBA","CUCEA","CUCEI","CUCS","CUCSH","CUValles","CUNorte","CUSur","CUCiénega","CUCosta","CUCSur","CULagos","CUTonalá","SEMS","UDG Virtual","Rectoría General","Coordinación General de Cooperación e Internacionalización","Coordinación de Investigación","Institutos y Centros de Investigación"]
RIESGOS_CAT=["Migratorio","Consular","Geopolítico","Sanitario","Reputacional","Cumplimiento","Aduanal"]
ORGANISMOS=[["ONU","Naciones Unidas"],["UNESCO","Educación, ciencia y cultura"],["OEA","Organización de los Estados Americanos"],["Banco Mundial","Financiamiento al desarrollo"],["BID","Banco Interamericano de Desarrollo"],["OCDE","Cooperación y desarrollo económico"],["Unión Europea","Erasmus+ / Horizonte"],["Fulbright","Intercambio académico EE. UU."],["DAAD","Intercambio académico Alemania"],["Erasmus+","Movilidad europea"],["NIH","Salud · EE. UU."],["NSF","Ciencia · EE. UU."]]
FUENTES=["Recursos propios UdeG","SECIHTI","CONAHCYT","SEP","Fulbright","DAAD","Erasmus+","NIH","NSF","Unión Europea","Banco Mundial","BID","Organismo internacional","Mixto","No aplica"]
MARCO=[
 "Constitución Política de los Estados Unidos Mexicanos","Ley de Migración","Reglamento de la Ley de Migración",
 "Ley sobre Refugiados, Protección Complementaria y Asilo Político","Lineamientos y criterios administrativos del Instituto Nacional de Migración (INM)",
 "Acuerdos de la Secretaría de Gobernación","Tratados internacionales ratificados por México (La Haya, Convención de Viena sobre Relaciones Consulares/Diplomáticas, UNIDROIT)"]
ART221=("Art. 221 del Reglamento Interior de la Administración General de la UdeG — Unidad de Asuntos Internacionales. "
 "Ámbito (síntesis funcional, a confirmar el texto literal en la fuente oficial abogaciageneral.udg.mx): asesoría y gestión de los asuntos internacionales de la Universidad — "
 "movilidad global de personal y visitantes extranjeros, derecho migratorio mexicano e internacional, convenios internacionales, trámites consulares y aduanales, y traducción jurídica. "
 "⚠ El texto exacto del artículo debe verificarse en la fuente oficial antes de cualquier uso formal.")

DATA={"corte":"2026-06-18","clases":CLASES,"flujos":FLUJOS,"clase_tramite":CLASE_TRAMITE,"condiciones":CONDICIONES,
 "visas":VISAS,"paises":PAISES,"idiomas":IDIOMAS,"cu":CU,"riesgos_cat":RIESGOS_CAT,"organismos":ORGANISMOS,"fuentes":FUENTES,"marco":MARCO,"art221":ART221}
DATAJ=json.dumps(DATA,ensure_ascii=False)

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html" class="act">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''

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
  if(perfil==='Consulta'){
   document.querySelectorAll('button').forEach(function(b){var t=(b.textContent||'')+ (b.title||'');if(/guardar|registrar|eliminar|adjuntar|avanzar|agregar|enviar/i.test(t)){b.disabled=true;b.style.opacity=.4;b.title='Perfil Consulta: solo lectura';}});
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
 window.__bitlog=blog;blog('Acceso','Ingreso al módulo');
 var RX=/guardar|registrar|exportar|eliminar|adjuntar|avanzar|agregar|word|csv|descargar/i;
 document.addEventListener('click',function(ev){try{var el=ev.target&&ev.target.closest&&ev.target.closest('button,.lk,.del');if(!el)return;var txt=(el.textContent||'').trim().replace(/\s+/g,' ');if(RX.test(txt)&&txt.length<70)blog('Acción',txt);}catch(e){}},true);
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
<title>SIGEJ-UdeG · Asuntos Internacionales</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--amber:#e08e0b;--orange:#ea580c;--ok:#1f9d6b;--ink:#0a1f3c;--mut:#64748b;--card:#ffffff;--card2:#f8fafc;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:radial-gradient(1200px 600px at 80% -10%,transparent,transparent),var(--bg);color:var(--ink)}
header{padding:14px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;border-bottom:1px solid var(--line)}
header h1{margin:0;font-size:18px}header .s{opacity:.8;font-size:12px;margin-top:3px}
.navbar{background:#06182c;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#475569;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.live{display:inline-flex;align-items:center;gap:6px;background:rgba(31,157,107,.15);color:#7ee0b4;border:1px solid rgba(31,157,107,.4);border-radius:20px;padding:5px 12px;font-size:12px}
.dot{width:8px;height:8px;border-radius:50%;background:#2ee08a;animation:p 1.5s infinite}@keyframes p{50%{opacity:.3}}
.tabbar{display:flex;flex-wrap:wrap;gap:6px;padding:14px 24px 0;max-width:1440px;margin:auto}
.tb{background:var(--card);color:#475569;border:1px solid var(--line);border-bottom:none;border-radius:11px 11px 0 0;padding:10px 14px;font-size:12.5px;font-weight:600;cursor:pointer}
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
.buckets{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:9px}
.bk{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px;text-align:center}
.bk .n{font-size:21px;font-weight:800}.bk .l{font-size:10.5px;color:var(--mut)}
.bk.b1 .n{color:#c0392b}.bk.b2 .n{color:#ea580c}.bk.b3 .n{color:#e08e0b}
table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:7px 8px;text-align:left;border-bottom:1px solid var(--line)}th{color:var(--mut)}
.rb{font-size:10px;padding:2px 8px;border-radius:9px;font-weight:600}
.rb-Crítico{background:rgba(192,57,43,.25);color:#ff9b8d}.rb-Alto{background:rgba(234,88,12,.22);color:#ffb38f}.rb-Medio{background:rgba(224,142,11,.2);color:#ffce82}.rb-Bajo{background:rgba(31,157,107,.2);color:#8fe0d8}.rb-Indeterminado{background:rgba(143,166,196,.18);color:var(--mut)}
.f{display:inline-flex;flex-direction:column;gap:3px;margin:0 8px 9px 0}.f label{font-size:11px;color:var(--mut);font-weight:600}
.f input,.f select,.f textarea{padding:7px 8px;border:1px solid var(--line);border-radius:6px;font-size:12.5px;background:#f1f5fb;color:var(--ink);min-width:150px}
.f textarea{min-width:320px;min-height:46px}
button{padding:8px 13px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
.b1{background:var(--azul2)}.b3{background:var(--ok)}.bw{background:#2b579a}.bd{background:#33507a}.mini{padding:4px 9px;font-size:11px}
.comp{background:#f1f5fb;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12px}.comp b{color:#0a4d8c}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px}.bar input,.bar select{padding:6px 8px;border:1px solid var(--line);border-radius:6px;font-size:12px;background:#f1f5fb;color:var(--ink)}
.it{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:12px;margin-bottom:9px;cursor:pointer}.it:hover{border-color:var(--teal)}
.it .t{font-weight:700;color:#0a4d8c;font-size:13px}.it .m{font-size:11px;color:var(--mut);margin-top:3px}
.pipe{display:flex;gap:3px;overflow-x:auto;padding:6px 0}
.st{flex:0 0 auto;min-width:104px;background:var(--card2);border:1px solid var(--line);border-top:3px solid #33507a;border-radius:7px;padding:6px;font-size:10px;color:#0a4d8c}
.st.done{border-top-color:#1f9d6b}.st.cur{border-top-color:#0a4d8c;box-shadow:0 0 0 2px #0a4d8c}
.chip{display:inline-block;background:#f1f5fb;border:1px solid var(--line);border-radius:9px;padding:2px 8px;font-size:10px;color:#475569;margin:1px}
.heat{width:100%;border-collapse:collapse;font-size:11.5px}.heat td,.heat th{padding:6px;text-align:center;border:2px solid var(--bg)}.heat th{color:var(--mut)}.heat td.lab{text-align:left;color:#0a4d8c}
.drawer{position:fixed;inset:0;background:rgba(4,12,24,.72);display:none;align-items:center;justify-content:center;z-index:9000;padding:18px}
.drawer.on{display:flex}.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;max-width:920px;width:100%;max-height:88vh;overflow:auto;padding:20px}
.panel .x{float:right;cursor:pointer;color:var(--mut);font-size:20px}
.warn{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:9px;padding:9px 12px;font-size:11.5px;color:#e8cf95;margin:8px 0}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:26px;text-align:center;color:var(--mut);font-size:13px}
a.dl{color:#7ee0b4}.lk{color:#7ee0b4;cursor:pointer}
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
<header><div><h1>🌎 SIGEJ-UdeG · Asuntos Internacionales — Unidad de Asuntos Internacionales · OAG</h1>
<div class="s">Global Mobility · derecho migratorio MX e internacional · convenios internacionales · traducción jurídica · Art. 221 RIAG-UdeG</div></div>
<div style="text-align:right"><span class="live"><span class="dot"></span>En vivo · <span id="upd"></span></span> <button class="b1 mini" onclick="compute()">↻ Actualizar</button></div></header>
__NAV__
<div class="tabbar">
 <button class="tb on" data-t="t1" onclick="tab('t1')">🛰️ Tablero (BI)</button>
 <button class="tb" data-t="t2" onclick="tab('t2')">➕ Alta de expediente</button>
 <button class="tb" data-t="t3" onclick="tab('t3')">📁 Expedientes</button>
 <button class="tb" data-t="t4" onclick="tab('t4')">⏳ Vigencias migratorias</button>
 <button class="tb" data-t="t5" onclick="tab('t5')">✈️ Movilidad UdeG</button>
 <button class="tb" data-t="t6" onclick="tab('t6')">🤝 Convenios internacionales</button>
 <button class="tb" data-t="t7" onclick="tab('t7')">🌐 Traducción jurídica</button>
 <button class="tb" data-t="t8" onclick="tab('t8')">⚠️ Riesgo internacional</button>
 <button class="tb" data-t="t9" onclick="tab('t9')">🧠 Conocimiento</button>
 <button class="tb" data-t="t11" onclick="tab('t11')">🎓 Movilidad estudiantil/académica</button>
 <button class="tb" data-t="t10" onclick="tab('t10')">🏛️ Marco y organismos</button>
</div>
<div class="wrap">
 <section id="t1" class="tab on">
  <div class="kpis" id="ceKpis"></div>
  <div class="h">⏳ Vigencias migratorias próximas (180/90/60/30/15 días)</div><div class="buckets" id="ceBuckets"></div>
  <div class="grid" style="margin-top:14px">
   <div class="card"><h3>Por clase de asunto</h3><canvas id="cClase"></canvas></div>
   <div class="card"><h3>Por condición migratoria</h3><canvas id="cCond"></canvas></div>
   <div class="card s2"><h3>Por país / nacionalidad (top)</h3><canvas id="cPais"></canvas></div>
   <div class="card"><h3>Por estado del trámite</h3><canvas id="cEst"></canvas></div>
   <div class="card"><h3>Movilidad por Centro Universitario</h3><canvas id="cCU"></canvas></div>
   <div class="card s2"><h3>🗺️ Mapa de internacionalización — por Centro Universitario</h3><div id="ceMapa"></div></div>
  </div>
 </section>

 <section id="t2" class="tab">
  <div class="card"><h3>Alta de expediente internacional</h3>
   <div class="f"><label>Clase de asunto</label><select id="i_clase" onchange="claseChange()"></select></div>
   <div class="f"><label>Subtipo</label><select id="i_sub"></select></div>
   <div class="f"><label>Trámite (flujo)</label><select id="i_tramite"></select></div>
   <div class="f" style="display:flex"><label>Nombre / título del asunto</label><textarea id="i_titulo" style="min-height:38px"></textarea></div>
   <div class="f"><label>País / nacionalidad</label><select id="i_pais"></select></div>
   <div class="f"><label>Pasaporte</label><input id="i_pasaporte"></div>
   <div class="f"><label>CURP (si aplica)</label><input id="i_curp"></div>
   <div class="f"><label>Condición migratoria</label><select id="i_cond"></select></div>
   <div class="f"><label>Tipo de visa</label><select id="i_visa"></select></div>
   <div class="f"><label>Centro Universitario</label><select id="i_cu"></select></div>
   <div class="f"><label>Dependencia</label><input id="i_dep"></div>
   <div class="f"><label>Programa académico</label><input id="i_prog"></div>
   <div class="f"><label>Abogado(a) responsable</label><input id="i_resp"></div>
   <div class="f"><label>Convenio asociado</label><input id="i_conv"></div>
   <div class="f"><label>Idioma (traducción)</label><select id="i_idioma"></select></div>
   <div class="f"><label>Fuente de financiamiento</label><select id="i_fuente"></select></div>
   <div class="f"><label>Seguro (póliza/cobertura)</label><input id="i_seguro"></div>
   <div class="f"><label>Inicio</label><input id="i_ini" type="date"></div>
   <div class="f"><label>Vencimiento (visa/estancia/convenio)</label><input id="i_venc" type="date"></div>
   <div style="margin-top:6px"><button class="b3" onclick="saveExp()">＋ Registrar expediente</button> <span id="i_msg" style="font-size:12px;color:#7ee0b4;margin-left:8px"></span></div>
  </div>
  <div class="warn">⚠️ Captura local (prototipo). <b>IA jurídica</b> (cartas de invitación, verificación de requisitos migratorios, comparación de normativas, traducción), <b>OCR</b>, <b>búsqueda semántica</b>, integración con <b>INM / consulados / USCIS / SAT-Aduanas</b> y <b>memorias de traducción</b> automáticas = fase de implementación con backend.</div>
 </section>

 <section id="t3" class="tab">
  <div class="bar">
   <input id="q" placeholder="Buscar (folio, nombre, país, dependencia, programa)…" oninput="renderList()" style="min-width:240px">
   <select id="fClase" onchange="renderList()"><option value="">Toda clase</option></select>
   <select id="fPais" onchange="renderList()"><option value="">Todo país</option></select>
   <select id="fRiesgo" onchange="renderList()"><option value="">Todo riesgo</option><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
   <button class="bd mini" onclick="exportCSV()">⬇ CSV</button><span id="listCnt" style="font-size:12px;color:#64748b"></span>
  </div>
  <div id="lista"></div>
 </section>

 <section id="t4" class="tab">
  <div class="h">⏳ Matriz de vigencias migratorias (visa / condición de estancia / convenio)</div>
  <div class="buckets" id="vigBuckets"></div>
  <div class="bar" style="margin-top:12px"><select id="fVig" onchange="renderVig()"><option value="">Todo</option><option value="venc">Vencidos</option><option value="15">≤ 15 días</option><option value="30">≤ 30 días</option><option value="60">≤ 60 días</option><option value="90">≤ 90 días</option><option value="180">≤ 180 días</option></select></div>
  <div id="vigLista"></div>
  <div class="warn">Notificaciones automáticas (correo/app/push) a 180/90/60/30/15 días = fase backend. La analítica predictiva de negativa/vencimiento usa un score proxy explicable (días a vencimiento + riesgos marcados + condición).</div>
 </section>

 <section id="t5" class="tab">
  <div class="kpis" id="movKpis"></div>
  <div class="h">✈️ Movilidad internacional del personal UdeG (congresos, estancias, sabáticos, misiones)</div>
  <div id="movLista"></div>
 </section>

 <section id="t6" class="tab">
  <div class="kpis" id="convKpis"></div>
  <div class="h">🤝 Convenios internacionales</div>
  <div id="convLista"></div>
 </section>

 <section id="t7" class="tab">
  <div class="kpis" id="tradKpis"></div>
  <div class="h">🌐 Traducciones jurídicas</div>
  <div id="tradLista"></div>
  <div class="card" style="margin-top:12px"><h3>🗂️ Banco terminológico institucional</h3>
   <div class="f"><label>Idioma</label><select id="g_idioma"></select></div>
   <div class="f"><label>Término (origen)</label><input id="g_src"></div>
   <div class="f"><label>Equivalente (destino)</label><input id="g_dst"></div>
   <div class="f"><label>Nota / contexto</label><input id="g_nota" style="min-width:220px"></div>
   <div><button class="b3" onclick="saveTerm()">＋ Agregar término</button></div>
   <div id="glosList" style="margin-top:10px"></div></div>
 </section>

 <section id="t8" class="tab">
  <div class="h">🗺️ Matriz de riesgo internacional</div>
  <div class="card"><table class="heat" id="riskHeat"></table>
   <div style="font-size:11px;color:#64748b;margin-top:8px">Categorías: migratorio, consular, geopolítico, sanitario, reputacional, cumplimiento, aduanal. Registra riesgos por expediente desde su ficha; el nivel agregado usa score proxy explicable.</div></div>
  <div class="h">Expedientes por nivel de riesgo</div><div id="riskList"></div>
 </section>

 <section id="t9" class="tab">
  <div class="card"><h3>🧠 Centro de Conocimiento Internacional</h3>
   <div class="f"><label>Categoría</label><select id="k_cat"><option>Tratado internacional</option><option>Convención (La Haya / Viena)</option><option>Criterio INM</option><option>Criterio USCIS / Depto. de Estado</option><option>Manual consular</option><option>Guía institucional</option><option>Derecho comparado</option><option>Jurisprudencia</option><option>Glosario jurídico</option></select></div>
   <div class="f"><label>Título</label><input id="k_tit" style="min-width:260px"></div>
   <div class="f" style="display:flex"><label>Contenido / referencia</label><textarea id="k_txt"></textarea></div>
   <div><button class="b3" onclick="saveKB()">＋ Registrar</button></div>
  </div>
  <div class="card" style="margin-top:12px"><h3>📚 Marco jurídico aplicable</h3><div id="marcoBox"></div></div>
  <div class="bar" style="margin-top:12px"><input id="qkb" placeholder="Buscar conocimiento…" oninput="renderKB()" style="min-width:240px"></div>
  <div id="kbList"></div>
 </section>

 <section id="t10" class="tab">
  <div class="card"><h3>🏛️ Fundamento — Art. 221 RIAG-UdeG</h3><div id="art221" style="font-size:12.5px;color:#c7d6ea;line-height:1.6"></div></div>
  <div class="grid" style="margin-top:12px">
   <div class="card"><h3>🌍 Organismos internacionales</h3><div id="orgBox"></div></div>
   <div class="card"><h3>🤖 IA, dashboards y backend (hoja de ruta)</h3><div style="font-size:12px;color:#c7d6ea;line-height:1.7">🔹 <b>IA jurídica</b>: cartas de invitación, opiniones, verificación de requisitos migratorios, comparación de normativas, traducción automática, listas de verificación.<br>🔹 <b>Integraciones</b>: INM, consulados, USCIS, Departamento de Estado, SAT-Aduanas.<br>🔹 <b>Traducción</b>: memorias de traducción y repositorio multilingüe.<br>🔹 <b>Observatorio</b>: indicadores QS / THE / ANUIES / SECIHTI de movilidad e internacionalización.<br><span style="color:#e8cf95">Todo lo anterior es fase de implementación con backend e integraciones.</span></div></div>
  </div>
 </section>
 <section id="t11" class="tab">
  <div class="kpis" id="mestKpis"></div>
  <div class="h">🎓 Movilidad estudiantil y académica (intercambio · entrantes / salientes · doble titulación)</div>
  <div id="mestBody"></div>
 </section>
</div>
<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div></div>
<input type="file" id="fileIn" style="display:none">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const HOY=new Date(2026,5,18);let CH={};let FILEIDX=null;
let A=JSON.parse(localStorage.getItem('sigej_internacional')||'[]');
let KB=JSON.parse(localStorage.getItem('sigej_int_kb')||'[]');
let GL=JSON.parse(localStorage.getItem('sigej_int_glosario')||'[]');
function saveA(){localStorage.setItem('sigej_internacional',JSON.stringify(A));}
function saveKBs(){localStorage.setItem('sigej_int_kb',JSON.stringify(KB));}
function saveGL(){localStorage.setItem('sigej_int_glosario',JSON.stringify(GL));}
function el(id){return document.getElementById(id);}
function val(id){return (el(id).value||'').trim();}
function pad(n){return (n<10?'0':'')+n;}
function nowStr(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function hoyStr(){return HOY.toISOString().slice(0,10);}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-HOY)/864e5);}
function nivel(s){return s>70?'Crítico':s>=50?'Alto':s>=28?'Medio':s>0?'Bajo':'Indeterminado';}
function scoreOf(e){let s=0;const d=dr(e.venc);
 if(d!==null){s+= d<0?60:d<=15?50:d<=30?40:d<=60?28:d<=90?18:d<=180?10:2;}
 const rs=(e.riesgos||[]);if(rs.some(r=>r.nivel==='Crítico'))s+=25;else if(rs.some(r=>r.nivel==='Alto'))s+=15;else if(rs.length)s+=6;
 if((e.clase||'').match(/Migración/))s+=8;
 return Math.min(100,Math.round(s));}
function tab(id){document.querySelectorAll('.tab').forEach(s=>s.classList.toggle('on',s.id===id));
 document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 if(id==='t1')setTimeout(compute,20);if(id==='t3')renderList();if(id==='t4')renderVig();if(id==='t5')renderMov();if(id==='t6')renderConv();if(id==='t7')renderTrad();if(id==='t8')renderRiesgo();if(id==='t9')renderKB();if(id==='t10')renderMarco();if(id==='t11')renderMovEst();}
/* ===== Submódulo: Movilidad estudiantil y académica (intercambio internacional) ===== */
function MEST(){try{return JSON.parse(localStorage.getItem('sigej_int_movilidad')||'[]');}catch(e){return [];}}
function mestSave(x){localStorage.setItem('sigej_int_movilidad',JSON.stringify(x));}
function mv(id){var e=el(id);return e?(e.value||'').trim():'';}
function mesc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function muid(){return 'mov'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function mnow(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function mhoy(){return new Date().toISOString().slice(0,10);}
function mdr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(mhoy()+'T00:00:00'))/864e5);}
function mopt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
function mnotif(t,f){try{var N=JSON.parse(localStorage.getItem('sigej_notificaciones')||'[]');N.push({ts:mnow(),area:'Movilidad estudiantil/académica',texto:t,folio:f||'',modulo:'Asuntos Internacionales',leida:false});localStorage.setItem('sigej_notificaciones',JSON.stringify(N));}catch(e){}}
var MESTTIPO=['Estudiante saliente (outgoing)','Estudiante entrante (incoming)','Académico saliente','Académico entrante','Estancia de investigación','Doble titulación','Práctica / servicio social internacional'];
var MESTNIV=['Bachillerato','Licenciatura','Especialidad','Maestría','Doctorado','Posdoctorado'];
var MESTVISA=['No requiere','Visa de estudiante','Visa de visitante','Residente temporal estudiante','En trámite','Otorgada','Rechazada'];
var MESTSEG=['Gastos médicos internacionales','Seguro de viaje','Cobertura de la institución destino','Sin cobertura / por definir'];
var MESTEST=['Solicitud','En revisión','Aprobada','En curso','Concluida','Cancelada'];
var MESTCU=['CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUCostaSur','CUSur','CUCiénega','CUAltos','CULagos','CUNorte','CUValles','CUTonalá','SEMS','UDGVirtual','Coord. Gral. Cooperación e Internacionalización'];
function mestSeed(){if(localStorage.getItem('sigej_int_movilidad'))return;mestSave([
 {id:muid(),folio:'MOV-2026-001',nombre:'María Fernández',tipo:'Estudiante saliente (outgoing)',nivel:'Licenciatura',cu:'CUCEA',institucion:'Universidad de Salamanca',pais:'España',convenio:'CONV-INT (Erasmus+)',ini:'2026-09-01',fin:'2027-01-31',visaTipo:'Visa de estudiante',visaEst:'Otorgada',seguro:'Gastos médicos internacionales',respons:'Carta compromiso firmada',creditos:'Reconocimiento de 30 créditos',estado:'Aprobada',docs:[],traza:[{ts:mnow(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:muid(),folio:'MOV-2026-002',nombre:'John Smith',tipo:'Estudiante entrante (incoming)',nivel:'Maestría',cu:'CUCEI',institucion:'University of Texas',pais:'Estados Unidos',convenio:'CONV-INT',ini:'2026-08-15',fin:'2026-12-15',visaTipo:'Residente temporal estudiante',visaEst:'En trámite',seguro:'Sin cobertura / por definir',respons:'',creditos:'',estado:'En curso',docs:[],traza:[{ts:mnow(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:muid(),folio:'MOV-2026-003',nombre:'Dra. Ana Ruiz',tipo:'Académico saliente',nivel:'Doctorado',cu:'CUCS',institucion:'Sorbonne Université',pais:'Francia',convenio:'CONV-INT',ini:'2026-10-01',fin:'2027-03-31',visaTipo:'Visa de visitante',visaEst:'Otorgada',seguro:'Seguro de viaje',respons:'Estancia de investigación',creditos:'',estado:'Aprobada',docs:[],traza:[{ts:mnow(),usuario:'Sistema',accion:'Alta (demo)'}]}
]);}
function mestSinSeg(x){return /Sin cobertura|definir/.test(x.seguro||'');}
function renderMovEst(){mestSeed();var A=MEST();var q=(mv('mestq')||'').toLowerCase();
 var sal=A.filter(function(x){return /saliente/i.test(x.tipo);}).length,ent=A.filter(function(x){return /entrante/i.test(x.tipo);}).length;
 var curso=A.filter(function(x){return x.estado==='En curso';}).length;
 var sinSeg=A.filter(function(x){return /En curso|Aprobada/.test(x.estado)&&mestSinSeg(x);}).length;
 var venc=A.filter(function(x){var d=mdr(x.fin);return /En curso|Aprobada/.test(x.estado)&&d!==null&&d<=30;}).length;
 var K=[['',A.length,'Movilidades',''],['',sal,'Salientes','g'],['',ent,'Entrantes',''],['',curso,'En curso','y'],['',sinSeg,'Sin seguro (riesgo)','r']];
 el('mestKpis').innerHTML=K.map(function(k){return '<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>';}).join('');
 var al='';var ri=[];if(sinSeg)ri.push(sinSeg+' movilidad(es) en curso/aprobadas SIN seguro de gastos médicos internacionales');if(venc)ri.push(venc+' por concluir/renovar visa (≤30d)');
 if(ri.length)al='<div style="background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px">🚨 <b>Riesgo:</b> '+ri.join(' · ')+'.</div>';
 function f(id,l,ty){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+l+'</label><input id="'+id+'"'+(ty?' type="'+ty+'"':'')+' style="width:100%;padding:7px 9px;border:1px solid #e2e8f0;border-radius:7px;font-size:13px"></div>';}
 function s(id,l,a){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+l+'</label><select id="'+id+'" style="width:100%;padding:7px 9px;border:1px solid #e2e8f0;border-radius:7px;font-size:13px">'+mopt(a,'')+'</select></div>';}
 var g='display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px';
 var form='<div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:10px;overflow:hidden;background:#fff"><div onclick="var d=el(\'mestForm\');d.style.display=d.style.display===\'none\'?\'block\':\'none\'" style="background:#f8fafc;padding:10px 13px;font-weight:700;color:#0a4d8c;cursor:pointer;font-size:13px">➕ Registrar movilidad — clic para abrir/cerrar</div><div id="mestForm" style="display:none;padding:12px">'+
  '<div style="'+g+'">'+f('m_nom','Estudiante / académico *')+s('m_tipo','Tipo',MESTTIPO)+s('m_niv','Nivel',MESTNIV)+s('m_cu','CU / dependencia',MESTCU)+f('m_inst','Institución extranjera')+f('m_pais','País')+f('m_conv','Convenio marco vinculado')+f('m_ini','Inicio','date')+f('m_fin','Fin','date')+s('m_visat','Tipo de visa',MESTVISA)+s('m_visae','Estatus de visa',MESTVISA)+s('m_seg','Seguro / cobertura',MESTSEG)+s('m_est','Estado',MESTEST)+f('m_cred','Reconocimiento de créditos')+f('m_resp','Carta compromiso / responsabilidad')+'</div>'+
  '<div style="margin-top:8px"><button onclick="mestAdd()" style="border:none;border-radius:8px;padding:9px 14px;background:#1f9d6b;color:#fff;font-weight:700;cursor:pointer">＋ Registrar</button> <span id="m_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var rows=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var lista='<div style="margin:6px 0"><input id="mestq" value="'+mesc(mv('mestq'))+'" placeholder="🔎 Buscar (nombre, institución, país, convenio)…" oninput="renderMovEst()" style="width:100%;padding:8px;border:1px solid #e2e8f0;border-radius:8px"></div>'+
  (rows.length?rows.map(function(o){var x=o.x;var d=mdr(x.fin);return '<div class="it" onclick="mestFicha('+o.i+')"><div class="t">'+mesc(x.folio)+' · '+mesc(x.nombre)+' <span style="font-weight:400;color:#64748b">('+mesc(x.tipo)+')</span></div><div class="m">'+mesc(x.institucion||'')+' · '+mesc(x.pais||'—')+' · '+mesc(x.cu||'')+' · '+mesc(x.ini||'—')+'→'+mesc(x.fin||'—')+' · '+mesc(x.estado)+(mestSinSeg(x)?' · <span style="color:#c0392b;font-weight:700">SIN seguro</span>':' · seguro ✓')+(d!==null&&d<=30&&/En curso|Aprobada/.test(x.estado)?' · <span style="color:#b45309">'+(d<0?'concluida':d+'d')+'</span>':'')+'</div></div>';}).join(''):'<div class="empty">Sin movilidades registradas.</div>');
 el('mestBody').innerHTML=al+form+lista;
}
function mestAdd(){if(!mv('m_nom')){el('m_msg').style.color='#c0392b';el('m_msg').textContent='Indica el nombre.';return;}
 var A=MEST();var folio='MOV-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 var x={id:muid(),folio:folio,nombre:mv('m_nom'),tipo:mv('m_tipo'),nivel:mv('m_niv'),cu:mv('m_cu'),institucion:mv('m_inst'),pais:mv('m_pais'),convenio:mv('m_conv'),ini:mv('m_ini'),fin:mv('m_fin'),visaTipo:mv('m_visat'),visaEst:mv('m_visae'),seguro:mv('m_seg'),respons:mv('m_resp'),creditos:mv('m_cred'),estado:mv('m_est'),docs:[],traza:[{ts:mnow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Alta de movilidad'}]};
 A.push(x);mestSave(A);if(window.__bitlog)__bitlog('Movilidad estudiantil/académica','Alta '+folio+' · '+mv('m_nom'));
 if(mestSinSeg(x))mnotif('Movilidad de '+mv('m_nom')+' SIN seguro de gastos médicos internacionales',folio);
 el('m_msg').style.color='#1f9d6b';el('m_msg').textContent='✓ '+folio+' registrada.';renderMovEst();}
function mestFicha(i){var A=MEST();var x=A[i];if(!x)return;
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+mesc(d.cat||'Doc')+' · '+mesc(d.nombre)+' <a href="'+d.data+'" download="'+mesc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos (carta de aceptación, seguro, visa, convenio).</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+mesc(t.usuario)+' — '+mesc(t.accion)+'</div>';}).join('');
 function box(t,b,bd){return '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6'+(bd?';border-left:4px solid '+bd:'')+'"><b>'+t+'</b><br>'+b+'</div>';}
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+mesc(x.nombre)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+mesc(x.folio)+' · '+mesc(x.tipo)+' · '+mesc(x.estado)+'</div>'+
  box('🎓 Movilidad','Nivel: '+mesc(x.nivel||'—')+' · CU: '+mesc(x.cu||'—')+'<br>Institución: '+mesc(x.institucion||'—')+' ('+mesc(x.pais||'—')+')<br>Periodo: '+mesc(x.ini||'—')+' → '+mesc(x.fin||'—')+'<br>Convenio marco: '+mesc(x.convenio||'—')+'<br>Reconocimiento de créditos: '+mesc(x.creditos||'—'))+
  box('🛂 Visa / condición de estancia','Tipo: '+mesc(x.visaTipo||'—')+' · Estatus: '+mesc(x.visaEst||'—'))+
  box('🛡️ Seguro y responsabilidad','Cobertura: '+mesc(x.seguro||'—')+'<br>Carta compromiso: '+mesc(x.respons||'—'),(mestSinSeg(x)?'#c0392b':'#1f9d6b'))+
  '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0"><b>Estado</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+['En revisión','Aprobada','En curso','Concluida','Cancelada'].map(function(e){return '<button onclick="mestSetEstado('+i+',\''+e+'\')" style="border:none;border-radius:7px;padding:5px 9px;background:#e2e8f0;font-size:11px;cursor:pointer">'+e+'</button>';}).join('')+'</div></div>'+
  '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0"><b>🗂️ Expediente</b> <button onclick="mestAdj('+i+')" style="border:none;border-radius:7px;padding:5px 9px;background:#e2e8f0;font-size:11px;cursor:pointer">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button onclick="mestWord('+i+')" style="border:none;border-radius:7px;padding:7px 12px;background:#d4a32c;color:#3a2c05;font-weight:700;cursor:pointer">📄 Ficha (Word)</button> <button onclick="closeDrw()" style="border:none;border-radius:7px;padding:7px 12px;background:#e2e8f0;cursor:pointer">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function mestSetEstado(i,e){var A=MEST();var x=A[i];if(x.estado===e)return;x.estado=e;x.traza.push({ts:mnow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Estado → '+e});mestSave(A);if(window.__bitlog)__bitlog('Movilidad estudiantil/académica',x.folio+' → '+e);if(/En curso/.test(e)&&mestSinSeg(x))mnotif('Movilidad '+x.nombre+' EN CURSO sin seguro de gastos médicos internacionales',x.folio);mestFicha(i);}
function mestAdj(i){el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Carta de aceptación / Póliza de seguro / Visa / Convenio / Carta compromiso / Otro):','Carta de aceptación')||'Documento';var r=new FileReader();r.onload=function(){var A=MEST();A[i].docs=A[i].docs||[];A[i].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:mhoy()});A[i].traza.push({ts:mnow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Adjuntó '+cat+': '+f.name});mestSave(A);mestFicha(i);};r.readAsDataURL(f);};el('fileIn').click();}
function mestWord(i){var x=MEST()[i];var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Ficha de movilidad internacional — '+mesc(x.folio)+'</h3><p><b>Nombre:</b> '+mesc(x.nombre)+'<br><b>Tipo/Nivel:</b> '+mesc(x.tipo)+' / '+mesc(x.nivel)+' · <b>CU:</b> '+mesc(x.cu)+'<br><b>Institución:</b> '+mesc(x.institucion)+' ('+mesc(x.pais)+')<br><b>Periodo:</b> '+mesc(x.ini)+' a '+mesc(x.fin)+'<br><b>Convenio marco:</b> '+mesc(x.convenio)+'</p><p><b>Visa:</b> '+mesc(x.visaTipo)+' — '+mesc(x.visaEst)+'<br><b>Seguro:</b> '+mesc(x.seguro)+'<br><b>Reconocimiento de créditos:</b> '+mesc(x.creditos)+'<br><b>Carta compromiso:</b> '+mesc(x.respons)+'<br><b>Estado:</b> '+mesc(x.estado)+'</p></body></html>';var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Movilidad_'+x.folio+'.doc';a.click();}
function rb(n){return '<span class="rb rb-'+n+'">'+n+'</span>';}
/* catálogos */
function fill(id,arr,ph){const e=el(id);if(!e)return;e.innerHTML=(ph?'<option value="">'+ph+'</option>':'')+arr.map(x=>'<option>'+x+'</option>').join('');}
fill('i_clase',D.clases.map(c=>c.clase));fill('i_pais',D.paises);fill('i_cond',D.condiciones);fill('i_visa',D.visas);fill('i_cu',D.cu);fill('i_idioma',['(no aplica)'].concat(D.idiomas));fill('i_fuente',D.fuentes);
fill('fClase',D.clases.map(c=>c.clase),'Toda clase');fill('fPais',D.paises,'Todo país');fill('g_idioma',D.idiomas);
function claseChange(){const c=D.clases.find(x=>x.clase===val('i_clase'));fill('i_sub',c?c.sub:[]);const tr=D.clase_tramite[val('i_clase')]||'Genérico';fill('i_tramite',Object.keys(D.flujos));el('i_tramite').value=tr;}
claseChange();
/* alta */
function saveExp(){if(!val('i_titulo')){el('i_msg').style.color='#ff9b8d';el('i_msg').textContent='Indica el nombre/título.';return;}
 const tram=val('i_tramite');const flujo=(D.flujos[tram]||D.flujos['Genérico']).slice();
 const yr=(val('i_ini')||'2026').slice(0,4);const folio='INT-'+yr+'-'+String(A.length+1).padStart(3,'0');
 const o={folio:folio,clase:val('i_clase'),sub:val('i_sub'),tramite:tram,flujo:flujo,etapaIdx:0,estado:flujo[0],
  titulo:val('i_titulo'),pais:val('i_pais'),pasaporte:val('i_pasaporte'),curp:val('i_curp'),cond:val('i_cond'),
  visa:(val('i_visa')&&val('i_visa')!=='(no aplica)')?val('i_visa'):'',cu:val('i_cu'),dep:val('i_dep'),prog:val('i_prog'),conv:val('i_conv'),
  idioma:(val('i_idioma')&&val('i_idioma')!=='(no aplica)')?val('i_idioma'):'',fuente:val('i_fuente'),seguro:val('i_seguro'),resp:val('i_resp'),
  ini:val('i_ini'),venc:val('i_venc'),riesgos:[],traducciones:[],cartas:[],evidencias:[],
  versiones:[{v:1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:hoyStr(),nota:'Alta del expediente'}],
  bitacora:[{ts:nowStr(),accion:'Alta',usuario:localStorage.getItem('sigej_perfil')||'(perfil)'}]};
 o.score=scoreOf(o);o.nivel=nivel(o.score);A.push(o);saveA();
 if(window.__bitlog)__bitlog('Acción','Registrar expediente internacional '+folio);
 ['i_titulo','i_pasaporte','i_curp','i_dep','i_prog','i_conv','i_seguro','i_resp','i_ini','i_venc'].forEach(id=>el(id).value='');
 el('i_msg').style.color='#7ee0b4';el('i_msg').textContent='✓ '+folio+' registrado.';compute();}
/* t1 BI */
function cnt(arr,key){const o={};arr.forEach(e=>{const v=(typeof key==='function'?key(e):e[key])||'(s/d)';o[v]=(o[v]||0)+1;});return o;}
const PAL=['#1aa39a','#0a4d8c','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#16a085','#5d6d7e','#9d174d'];
function chart(id,type,labels,data,opts){if(!window.Chart)return;if(CH[id])CH[id].destroy();const ctx=el(id);if(!ctx)return;
 CH[id]=new Chart(ctx,{type:type,data:{labels:labels,datasets:[{data:data,backgroundColor:opts&&opts.multi?PAL:(opts&&opts.color||'#1aa39a')}]},
  options:{indexAxis:opts&&opts.horiz?'y':'x',plugins:{legend:{display:!!(opts&&opts.legend),position:'right',labels:{color:'#0a4d8c',font:{size:9}}}},
   scales:type==='doughnut'?{}:{x:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}},y:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}}}}});}
function compute(){A.forEach(e=>{e.score=scoreOf(e);e.nivel=nivel(e.score);});saveA();
 const mig=A.filter(e=>/Migración/.test(e.clase));const conv=A.filter(e=>/Convenio/.test(e.clase)).length;const trad=A.filter(e=>/Traducción/.test(e.clase)).length;const mov=A.filter(e=>/Movilidad/.test(e.clase)).length;
 const vig=A.filter(e=>{const d=dr(e.venc);return d!==null&&d>=0&&d<=180;}).length;
 const K=[['',A.length,'Expedientes',''],['',mig.length,'Personas extranjeras',''],['',mov,'Movilidad UdeG',''],['',conv,'Convenios int.',''],
  ['',vig,'Vigencias ≤180d','y'],['',trad,'Traducciones',''],['',A.filter(e=>e.nivel==='Crítico'||e.nivel==='Alto').length,'Riesgo alto','r'],['',new Set(A.map(e=>e.pais).filter(Boolean)).size,'Países','']];
 el('ceKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 const bdef=[[15,'≤ 15 días','b1'],[30,'≤ 30 días','b1'],[60,'≤ 60 días','b2'],[90,'≤ 90 días','b3'],[180,'≤ 180 días','b3']];
 const venc=A.filter(e=>{const d=dr(e.venc);return d!==null&&d<0;}).length;
 el('ceBuckets').innerHTML='<div class="bk b1"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div>'+
  bdef.map(b=>{const n=A.filter(e=>{const d=dr(e.venc);return d!==null&&d>=0&&d<=b[0];}).length;return '<div class="bk '+b[2]+'"><div class="n">'+n+'</div><div class="l">'+b[1]+'</div></div>';}).join('');
 if(A.length){const cl=cnt(A,'clase');chart('cClase','doughnut',Object.keys(cl),Object.values(cl),{multi:true,legend:true});
  const co=cnt(mig,'cond');chart('cCond','bar',Object.keys(co),Object.values(co),{horiz:true,color:'#1aa39a'});
  const pa=cnt(A.filter(e=>e.pais),'pais');const pe=Object.entries(pa).sort((a,b)=>b[1]-a[1]).slice(0,10);chart('cPais','bar',pe.map(x=>x[0]),pe.map(x=>x[1]),{color:'#0a4d8c'});
  const es=cnt(A,'estado');chart('cEst','bar',Object.keys(es),Object.values(es),{horiz:true,color:'#7e57c2'});
  const cu=cnt(A.filter(e=>e.cu),'cu');const ce=Object.entries(cu).sort((a,b)=>b[1]-a[1]).slice(0,10);chart('cCU','bar',ce.map(x=>x[0]),ce.map(x=>x[1]),{color:'#d4a32c'});
  const cus=Array.from(new Set(A.map(e=>e.cu).filter(Boolean)));
  el('ceMapa').innerHTML='<table><tr><th>Centro Universitario</th><th>Expedientes</th><th>Extranjeros</th><th>Movilidad</th><th>Convenios</th><th>Riesgo alto</th></tr>'+
   cus.map(c=>{const m=A.filter(e=>e.cu===c);return '<tr><td>'+c+'</td><td><b>'+m.length+'</b></td><td>'+m.filter(e=>/Migración/.test(e.clase)).length+'</td><td>'+m.filter(e=>/Movilidad/.test(e.clase)).length+'</td><td>'+m.filter(e=>/Convenio/.test(e.clase)).length+'</td><td>'+m.filter(e=>e.nivel==='Crítico'||e.nivel==='Alto').length+'</td></tr>';}).join('')+'</table>';
 } else {['cClase','cCond','cPais','cEst','cCU'].forEach(id=>{if(CH[id])CH[id].destroy();});el('ceMapa').innerHTML='<div class="empty" style="padding:14px">Aún no hay expedientes. Registra el primero en <b>➕ Alta de expediente</b>.</div>';}
 const t=new Date();el('upd').textContent='actualizado '+pad(t.getHours())+':'+pad(t.getMinutes())+':'+pad(t.getSeconds());}
/* t3 lista + ficha */
function renderList(){const q=(val('q')||'').toLowerCase();const fc=val('fClase'),fp=val('fPais'),fr=val('fRiesgo');
 let arr=A.filter(e=>(!fc||e.clase===fc)&&(!fp||e.pais===fp)&&(!fr||e.nivel===fr));
 if(q)arr=arr.filter(e=>(e.folio+' '+e.titulo+' '+(e.pais||'')+' '+(e.dep||'')+' '+(e.prog||'')).toLowerCase().indexOf(q)>=0);
 el('listCnt').textContent=arr.length+' de '+A.length;
 const box=el('lista');
 if(!A.length){box.innerHTML='<div class="empty">📭 Sin expedientes.<br>Registra el primero en <b>➕ Alta de expediente</b>. El módulo arranca vacío para no contener datos no verificados.</div>';return;}
 box.innerHTML=arr.map(e=>{const i=A.indexOf(e);const d=dr(e.venc);
  return '<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><span class="t">'+e.folio+' · '+e.titulo+'</span><span>'+rb(e.nivel)+' <span class="chip">'+e.estado+'</span></span></div><div class="m">'+e.clase+' · '+(e.pais||'—')+(e.cond?' · '+e.cond:'')+(e.visa?' · '+e.visa:'')+' · '+(e.cu||'—')+(d!==null?' · vence '+(d<0?'hace '+(-d)+'d':'en '+d+'d'):'')+'</div></div>';}).join('')||'<div class="empty" style="padding:14px">Sin coincidencias.</div>';}
function pipe(e){return '<div class="pipe">'+e.flujo.map((s,k)=>'<div class="st '+(k<e.etapaIdx?'done':k===e.etapaIdx?'cur':'')+'">'+s+'</div>').join('')+'</div>';}
function ficha(i){const e=A[i];const d=dr(e.venc);
 const ries=(e.riesgos||[]).length?'<table><tr><th>Categoría</th><th>Nivel</th><th>Nota</th></tr>'+(e.riesgos||[]).map((r,k)=>'<tr><td>'+r.cat+'</td><td>'+rb(r.nivel)+'</td><td>'+(r.nota||'')+' <span class="lk" onclick="delRiesgo('+i+','+k+')">✕</span></td></tr>').join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin riesgos registrados.</div>';
 const trd=(e.traducciones||[]).length?(e.traducciones||[]).map(t=>'<div style="font-size:11.5px;color:#475569">🌐 '+(t.idioma||'')+' · '+(t.doc||'')+' · '+(t.estado||'')+'</div>').join(''):'<div style="color:#64748b;font-size:12px">Sin traducciones.</div>';
 const ev=(e.evidencias||[]).length?(e.evidencias||[]).map(x=>'<div style="font-size:11.5px;color:#475569">📎 '+x.nombre+' · '+x.fecha+' <a class="dl" href="'+x.data+'" download="'+x.nombre+'">descargar</a></div>').join(''):'<div style="color:#64748b;font-size:12px">Sin evidencias.</div>';
 const ver=e.versiones.map(v=>'<div style="font-size:11.5px;color:#475569">v'+v.v+' · '+v.fecha+' · '+v.autor+' — '+v.nota+'</div>').join('');
 const bit=e.bitacora.slice(-6).map(b=>'<div style="font-size:11.5px;color:#475569">'+b.ts+' · '+b.usuario+' — '+b.accion+'</div>').join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 4px;color:#0a4d8c">'+e.folio+' · '+e.titulo+'</h2>'+
  '<div style="margin:4px 0 10px">'+rb(e.nivel)+' <span class="chip">'+e.clase+'</span> <span class="chip">'+(e.sub||'')+'</span> <span class="chip">'+e.estado+'</span></div>'+
  '<div class="comp"><b>Expediente internacional</b><br>País/nacionalidad: <b>'+(e.pais||'—')+'</b> · Pasaporte: '+(e.pasaporte||'—')+(e.curp?' · CURP: '+e.curp:'')+'<br>Condición migratoria: <b>'+(e.cond||'—')+'</b>'+(e.visa?' · Visa: '+e.visa:'')+'<br>CU: '+(e.cu||'—')+' · Dependencia: '+(e.dep||'—')+(e.prog?' · Programa: '+e.prog:'')+(e.resp?'<br>Abogado(a) responsable: <b>'+e.resp+'</b>':'')+(e.conv?'<br>Convenio asociado: '+e.conv:'')+'<br>Fuente: '+(e.fuente||'—')+(e.seguro?' · Seguro: '+e.seguro:'')+'<br>Trámite: '+e.tramite+'<br>Vigencia: '+(e.ini||'—')+' → '+(e.venc||'—')+(d!==null?' ('+(d<0?'vencido hace '+(-d)+'d':'vence en '+d+'d')+')':'')+'</div>'+
  '<div class="comp"><b>🔄 Flujo del trámite (BPMN)</b>'+pipe(e)+'<div style="margin-top:6px"><button class="bd mini" onclick="retroEtapa('+i+')">← Etapa anterior</button> <button class="b3 mini" onclick="avanzaEtapa('+i+')">Avanzar etapa →</button></div></div>'+
  '<div class="comp"><b>⚠️ Riesgos</b> <button class="bd mini" onclick="addRiesgo('+i+')">＋ Agregar</button><div style="margin-top:6px">'+ries+'</div></div>'+
  '<div class="comp"><b>🌐 Traducciones / cartas</b> <button class="bd mini" onclick="addTrad('+i+')">＋ Traducción</button> <button class="bd mini" onclick="cartaWord('+i+')">📄 Carta de invitación (Word)</button><div style="margin-top:6px">'+trd+'</div></div>'+
  '<div class="comp"><b>📎 Evidencias / soporte</b> <button class="bd mini" onclick="pickFile('+i+')">Subir</button><div style="margin-top:6px">'+ev+'</div></div>'+
  '<div class="comp"><b>🗂️ Versiones</b><div style="margin-top:6px">'+ver+'</div></div>'+
  '<div class="comp"><b>🧾 Bitácora</b><div style="margin-top:6px">'+bit+'</div></div>'+
  '<div class="comp" style="border-left:4px solid #0a4d8c"><b>📝 Seguimiento (notas del equipo)</b><div style="margin-top:4px">'+((e.seguimiento||[]).length?(e.seguimiento||[]).slice().reverse().map(function(s){return '<div style="font-size:11.5px;color:#334155;border-bottom:1px solid #eef2f7;padding:4px 0"><b style="color:#0a4d8c">'+(s.usuario||'')+'</b> <span style="color:#94a3b8;font-size:10px">'+(s.ts||'')+'</span><br>'+String(s.texto||'').replace(/</g,"&lt;")+'</div>';}).join(''):'<span style="color:#94a3b8;font-size:12px">Sin notas.</span>')+'</div><div style="margin-top:6px"><textarea id="xseg_'+i+'" rows="2" placeholder="Nota de seguimiento del asunto…" style="width:100%;padding:7px;border:1px solid var(--line);border-radius:8px"></textarea><button class="b3 mini" style="margin-top:5px" onclick="addSegInt('+i+')">＋ Agregar nota</button></div></div>'+
  '<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="bw" onclick="fichaWord('+i+')">📄 Ficha (Word)</button><button class="bd" onclick="closeDrw()">Cerrar</button> <button class="bd" style="background:#5a2330" onclick="delExp('+i+')">🗑 Eliminar</button></div>';
 el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
function addSegInt(i){var e=A[i];var el2=document.getElementById('xseg_'+i);var t=el2?el2.value.trim():'';if(!t){alert('Escribe la nota.');return;}e.seguimiento=e.seguimiento||[];e.seguimiento.push({ts:nowStr(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',texto:t});saveA();ficha(i);}
el('drw').onclick=ev=>{if(ev.target.id==='drw')closeDrw();};
function logIt(e,a){e.bitacora.push({ts:nowStr(),accion:a,usuario:localStorage.getItem('sigej_perfil')||'(perfil)'});}
function logV(e,n){e.versiones.push({v:e.versiones.length+1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:hoyStr(),nota:n});}
function avanzaEtapa(i){const e=A[i];if(e.etapaIdx<e.flujo.length-1){e.etapaIdx++;e.estado=e.flujo[e.etapaIdx];logIt(e,'Avance de trámite → '+e.estado);logV(e,'Etapa: '+e.estado);e.score=scoreOf(e);e.nivel=nivel(e.score);saveA();ficha(i);compute();renderList();}}
function retroEtapa(i){const e=A[i];if(e.etapaIdx>0){e.etapaIdx--;e.estado=e.flujo[e.etapaIdx];logIt(e,'Retroceso → '+e.estado);saveA();ficha(i);compute();}}
function addRiesgo(i){const e=A[i];const cat=prompt('Categoría ('+D.riesgos_cat.join(' / ')+'):','Migratorio');if(!cat)return;const niv=prompt('Nivel (Crítico/Alto/Medio/Bajo):','Medio')||'Medio';const nota=prompt('Nota:','')||'';
 e.riesgos.push({cat:cat,nivel:niv,nota:nota});logIt(e,'Riesgo: '+cat+' '+niv);e.score=scoreOf(e);e.nivel=nivel(e.score);saveA();ficha(i);compute();}
function delRiesgo(i,k){A[i].riesgos.splice(k,1);A[i].score=scoreOf(A[i]);A[i].nivel=nivel(A[i].score);saveA();ficha(i);compute();}
function addTrad(i){const e=A[i];const idioma=prompt('Idioma ('+D.idiomas.join('/')+'):','Inglés');if(!idioma)return;const doc=prompt('Documento:','')||'';const est=prompt('Estado (Solicitada/En proceso/Certificada/Entregada):','Solicitada')||'Solicitada';
 e.traducciones.push({idioma:idioma,doc:doc,estado:est});logIt(e,'Traducción '+idioma);saveA();ficha(i);compute();}
function pickFile(i){FILEIDX=i;el('fileIn').value='';el('fileIn').click();}
el('fileIn').onchange=function(){const f=this.files[0];if(!f||FILEIDX===null)return;if(f.size>1.5e6){alert('Máx 1.5 MB.');return;}
 const r=new FileReader();r.onload=()=>{const e=A[FILEIDX];e.evidencias=e.evidencias||[];e.evidencias.push({nombre:f.name,data:r.result,fecha:hoyStr()});logIt(e,'Evidencia: '+f.name);saveA();ficha(FILEIDX);};r.readAsDataURL(f);};
function delExp(i){if(!confirm('¿Eliminar '+A[i].folio+'?'))return;A.splice(i,1);saveA();closeDrw();compute();renderList();}
function exportCSV(){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const cab=['folio','clase','subtipo','titulo','pais','condicion','visa','cu','dependencia','programa','responsable','estado','vencimiento','nivel'];
 const rows=A.map(e=>[e.folio,e.clase,e.sub,e.titulo,e.pais,e.cond,e.visa,e.cu,e.dep,e.prog,e.resp,e.estado,e.venc,e.nivel].map(esc).join(','));
 const b=new Blob(['﻿'+cab.join(',')+'\n'+rows.join('\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='asuntos_internacionales.csv';a.click();}
function fichaWord(i){const e=A[i];
 const body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Unidad de Asuntos Internacionales</div>'+
  '<h2>EXPEDIENTE INTERNACIONAL — '+e.folio+'</h2>'+
  '<p style="font-size:11pt"><b>Asunto:</b> '+e.titulo+'<br><b>Clase / subtipo:</b> '+e.clase+' / '+(e.sub||'')+'<br><b>País/nacionalidad:</b> '+(e.pais||'—')+' · <b>Pasaporte:</b> '+(e.pasaporte||'—')+'<br><b>Condición migratoria:</b> '+(e.cond||'—')+(e.visa?' · <b>Visa:</b> '+e.visa:'')+'<br><b>CU/Dependencia:</b> '+(e.cu||'—')+' / '+(e.dep||'—')+(e.prog?' · <b>Programa:</b> '+e.prog:'')+(e.resp?'<br><b>Abogado(a) responsable:</b> '+e.resp:'')+'<br><b>Trámite:</b> '+e.tramite+' · <b>Estado:</b> '+e.estado+'<br><b>Vigencia:</b> '+(e.ini||'—')+' a '+(e.venc||'—')+'</p>'+
  '<p style="font-size:9pt;color:#666">Documento generado por el SIGEJ-UdeG (prototipo). Fundamento: Art. 221 RIAG-UdeG (texto a confirmar).</p>';
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Expediente_'+e.folio+'.doc';a.click();}
function cartaWord(i){const e=A[i];
 const body='<div style="text-align:right">Guadalajara, Jalisco, México.</div><br><div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>CARTA DE INVITACIÓN</div><br>'+
  '<p style="font-size:11pt">A quien corresponda (autoridad migratoria / consular):</p>'+
  '<p style="font-size:11pt">La Universidad de Guadalajara, por conducto de '+(e.cu||'la dependencia universitaria')+', extiende la presente <b>carta de invitación</b> a favor de <b>'+e.titulo+'</b>, de nacionalidad <b>'+(e.pais||'—')+'</b>, para participar en '+(e.prog||'actividades académicas')+' en calidad de '+(e.sub||'visitante')+'.'+'</p>'+
  '<p style="font-size:11pt">La estancia se prevé del '+(e.ini||'(fecha)')+' al '+(e.venc||'(fecha)')+'. La Universidad manifiesta su interés institucional y, en su caso, el respaldo de financiamiento ('+(e.fuente||'por definir')+').</p>'+
  '<p style="font-size:11pt">Se expide para los fines migratorios y/o consulares correspondientes.</p><br><br>'+
  '<div style="text-align:center">_______________________________<br>Oficina de la Abogacía General · Unidad de Asuntos Internacionales</div>'+
  '<p style="font-size:9pt;color:#666">Borrador generado por el SIGEJ-UdeG (prototipo). Revisar y validar antes de su emisión. Fundamento: Ley de Migración y su Reglamento.</p>';
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Carta_invitacion_'+e.folio+'.doc';a.click();}
/* t4 vigencias */
function renderVig(){const bdef=[[180,'≤180d','b3'],[90,'≤90d','b3'],[60,'≤60d','b2'],[30,'≤30d','b1'],[15,'≤15d','b1']];
 const venc=A.filter(e=>{const d=dr(e.venc);return d!==null&&d<0;}).length;
 el('vigBuckets').innerHTML='<div class="bk b1"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div>'+
  bdef.map(b=>{const n=A.filter(e=>{const d=dr(e.venc);return d!==null&&d>=0&&d<=b[0];}).length;return '<div class="bk '+b[2]+'"><div class="n">'+n+'</div><div class="l">'+b[1]+'</div></div>';}).join('');
 const fl=val('fVig');let arr=A.filter(e=>dr(e.venc)!==null);
 if(fl==='venc')arr=arr.filter(e=>dr(e.venc)<0);else if(fl)arr=arr.filter(e=>{const d=dr(e.venc);return d>=0&&d<=+fl;});
 arr.sort((a,b)=>dr(a.venc)-dr(b.venc));
 el('vigLista').innerHTML=arr.length?arr.map(e=>{const i=A.indexOf(e);const d=dr(e.venc);const c=d<0?'#ff9b8d':d<=30?'#ffce82':'#64748b';
  return '<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between"><span class="t">'+e.folio+' · '+e.titulo+'</span><span style="color:'+c+';font-weight:700">'+(d<0?'venció hace '+(-d)+'d':'en '+d+'d')+'</span></div><div class="m">'+(e.cond||e.clase)+(e.visa?' · '+e.visa:'')+' · '+(e.pais||'—')+' · '+rb(e.nivel)+'</div></div>';}).join(''):'<div class="empty">Sin vigencias en este rango.</div>';}
/* t5/t6/t7 por clase */
function listByClase(re){return A.map((e,i)=>({e:e,i:i})).filter(x=>re.test(x.e.clase));}
function renderMov(){const arr=listByClase(/Movilidad/);const K=[['',arr.length,'Movilidades',''],['',arr.filter(x=>dr(x.e.venc)!==null&&dr(x.e.venc)>=0&&dr(x.e.venc)<=30).length,'Próx. 30 días','y'],['',new Set(arr.map(x=>x.e.pais).filter(Boolean)).size,'Destinos',''],['',arr.filter(x=>!x.e.seguro).length,'Sin seguro reg.','r']];
 el('movKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('movLista').innerHTML=arr.length?arr.map(x=>'<div class="it" onclick="ficha('+x.i+')"><div class="t">'+x.e.folio+' · '+x.e.titulo+'</div><div class="m">'+(x.e.sub||'')+' · destino '+(x.e.pais||'—')+' · '+(x.e.cu||'—')+' · '+(x.e.ini||'—')+'→'+(x.e.venc||'—')+(x.e.seguro?' · seguro ✓':' · <span style="color:#ff9b8d">sin seguro</span>')+'</div></div>').join(''):'<div class="empty">Sin movilidades. Regístralas con clase «Movilidad de personal UdeG».</div>';}
function renderConv(){const arr=listByClase(/Convenio/);const K=[['',arr.length,'Convenios int.',''],['',arr.filter(x=>/Firma|Seguimiento/.test(x.e.estado)).length,'Vigentes/firma','g'],['',new Set(arr.map(x=>x.e.pais).filter(Boolean)).size,'Países',''],['',arr.filter(x=>dr(x.e.venc)!==null&&dr(x.e.venc)>=0&&dr(x.e.venc)<=180).length,'Por vencer ≤180d','y']];
 el('convKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('convLista').innerHTML=arr.length?arr.map(x=>'<div class="it" onclick="ficha('+x.i+')"><div class="t">'+x.e.folio+' · '+x.e.titulo+'</div><div class="m">'+(x.e.sub||'')+' · '+(x.e.pais||'—')+' · etapa '+x.e.estado+(x.e.venc?' · vence '+x.e.venc:'')+'</div></div>').join(''):'<div class="empty">Sin convenios internacionales. Regístralos con clase «Convenio internacional».</div>';}
function renderTrad(){const arr=listByClase(/Traducción/);let n=arr.length;A.forEach(e=>{n+=(e.traducciones||[]).length;});
 const K=[['',arr.length,'Expedientes de traducción',''],['',A.reduce((s,e)=>s+(e.traducciones||[]).length,0),'Traducciones en fichas',''],['',GL.length,'Términos en glosario','g'],['',new Set(arr.map(x=>x.e.idioma).filter(Boolean)).size,'Idiomas','']];
 el('tradKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('tradLista').innerHTML=arr.length?arr.map(x=>'<div class="it" onclick="ficha('+x.i+')"><div class="t">'+x.e.folio+' · '+x.e.titulo+'</div><div class="m">'+(x.e.sub||'')+' · idioma '+(x.e.idioma||'—')+' · etapa '+x.e.estado+'</div></div>').join(''):'<div class="empty">Sin expedientes de traducción. Regístralos con clase «Traducción jurídica».</div>';
 renderGlos();}
function saveTerm(){const s=val('g_src');if(!s){alert('Indica el término.');return;}GL.push({idioma:val('g_idioma'),src:s,dst:val('g_dst'),nota:val('g_nota')});saveGL();el('g_src').value='';el('g_dst').value='';el('g_nota').value='';renderGlos();renderTrad();}
function renderGlos(){el('glosList').innerHTML=GL.length?'<table><tr><th>Idioma</th><th>Término</th><th>Equivalente</th><th>Nota</th><th></th></tr>'+GL.map((g,i)=>'<tr><td>'+g.idioma+'</td><td>'+g.src+'</td><td>'+(g.dst||'—')+'</td><td>'+(g.nota||'')+'</td><td><span class="lk" onclick="delTerm('+i+')">✕</span></td></tr>').join('')+'</table>':'<div style="color:#64748b;font-size:12px">Banco terminológico vacío.</div>';}
function delTerm(i){GL.splice(i,1);saveGL();renderGlos();renderTrad();}
/* t8 riesgo */
function renderRiesgo(){const niv=['Crítico','Alto','Medio','Bajo'];const cats=D.riesgos_cat;
 const cell={};cats.forEach(c=>{cell[c]={};niv.forEach(n=>cell[c][n]=0);});let mx=1;
 A.forEach(e=>(e.riesgos||[]).forEach(r=>{if(cell[r.cat]&&cell[r.cat][r.nivel]!==undefined){cell[r.cat][r.nivel]++;mx=Math.max(mx,cell[r.cat][r.nivel]);}}));
 el('riskHeat').innerHTML='<tr><th class="lab">Categoría \\ Nivel</th>'+niv.map(n=>'<th>'+n+'</th>').join('')+'</tr>'+
  cats.map(c=>'<tr><td class="lab">'+c+'</td>'+niv.map(n=>{const v=cell[c][n];const al=v/mx;const col=n==='Crítico'?'192,57,43':n==='Alto'?'234,88,12':n==='Medio'?'224,142,11':'31,157,107';return '<td style="background:rgba('+col+','+(v?0.15+al*0.7:0.05)+');color:#fff">'+v+'</td>';}).join('')+'</tr>').join('');
 const box=el('riskList');const ord=A.map((e,i)=>[e,i]).sort((a,b)=>b[0].score-a[0].score);
 box.innerHTML=A.length?ord.map(([e,i])=>'<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between"><span class="t">'+e.folio+' · '+e.titulo+'</span><span>'+rb(e.nivel)+' '+e.score+'/100</span></div><div class="m">'+e.clase+' · '+(e.pais||'—')+' · '+((e.riesgos||[]).length)+' riesgo(s) registrados</div></div>').join(''):'<div class="empty">Sin expedientes.</div>';}
/* t9 conocimiento */
function saveKB(){const t=val('k_tit');if(!t){alert('Indica un título.');return;}KB.push({cat:val('k_cat'),tit:t,txt:val('k_txt'),fecha:hoyStr(),autor:localStorage.getItem('sigej_perfil')||'(perfil)'});saveKBs();el('k_tit').value='';el('k_txt').value='';renderKB();}
function renderKB(){el('marcoBox').innerHTML=D.marco.map(m=>'<div style="padding:5px 2px;border-bottom:1px solid var(--line);font-size:12px;color:#c7d6ea">📕 '+m+'</div>').join('');
 const q=(val('qkb')||'').toLowerCase();let arr=KB.filter(k=>!q||(k.tit+' '+(k.txt||'')+' '+k.cat).toLowerCase().indexOf(q)>=0);
 el('kbList').innerHTML=KB.length?(arr.map((k,i)=>'<div class="comp"><div style="display:flex;justify-content:space-between"><b>'+k.tit+'</b><span class="chip">'+k.cat+'</span></div><div style="font-size:12px;color:#c7d6ea;margin-top:5px">'+(k.txt||'—')+'</div><div style="font-size:11px;color:#64748b;margin-top:5px">'+k.fecha+' · '+k.autor+' <span class="lk" onclick="delKB('+KB.indexOf(k)+')">✕</span></div></div>').join('')||'<div class="empty" style="padding:14px">Sin coincidencias.</div>'):'<div class="empty" style="padding:14px">Repositorio vacío. Registra tratados, convenciones, criterios INM/USCIS, manuales consulares y derecho comparado.</div>';}
function delKB(i){if(!confirm('¿Eliminar?'))return;KB.splice(i,1);saveKBs();renderKB();}
/* t10 marco */
function renderMarco(){el('art221').textContent=D.art221;
 el('orgBox').innerHTML=D.organismos.map(o=>'<div style="padding:6px 2px;border-bottom:1px solid var(--line);font-size:12px"><b style="color:#0a4d8c">'+o[0]+'</b> <span style="color:#64748b">· '+o[1]+'</span></div>').join('');}
/* init */
window.addEventListener('storage',()=>{A=JSON.parse(localStorage.getItem('sigej_internacional')||'[]');compute();});
window.addEventListener('focus',compute);
compute();
</script>
__SNIP__
</body></html>"""
html=TPL.replace("__DATA__",DATAJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"internacional_SIGEJ.html","w",encoding="utf-8").write(html)
print("internacional_SIGEJ.html OK -",len(html),"bytes | clases",len(CLASES),"| flujos",len(FLUJOS),"| países",len(PAISES),"| idiomas",len(IDIOMAS))
