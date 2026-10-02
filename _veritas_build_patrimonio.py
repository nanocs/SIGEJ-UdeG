# -*- coding: utf-8 -*-
# Módulo de Gestión del Patrimonio Intangible (IPMS/TTO) — Unidad de Protección del Patrimonio Intangible · OAG UdeG
# Base: Art. 220 del Reglamento Interior de la Administración General de la UdeG (atribuciones citadas por la usuaria).
# Arranca vacío (catálogos). Acceso: equipo jurídico. Sin backend (prototipo cliente).
import json
B="/Users/edithroque/Documents/CLAUDE/"

CATS=[
 {"cat":"Propiedad Industrial","ic":"🏭","tipos":["Patente","Modelo de utilidad","Diseño industrial","Esquema de trazado de circuitos integrados","Marca","Marca colectiva","Aviso comercial","Nombre comercial","Secreto industrial","Indicación geográfica","Denominación de origen"]},
 {"cat":"Derecho de Autor","ic":"✍️","tipos":["Obra literaria","Obra científica","Obra artística","Obra audiovisual","Obra musical","Fotografía","Software","Base de datos","Material didáctico","Curso","Manual","Tesis","Artículo científico","Revista","Contenido multimedia","Diseño gráfico","Obra arquitectónica"]},
 {"cat":"Reservas y seriales","ic":"🔢","tipos":["Reserva de derechos","ISBN","ISSN","Derecho conexo"]},
 {"cat":"Variedades Vegetales","ic":"🌱","tipos":["Título de obtentor","Material vegetal","Banco de germoplasma"]},
 {"cat":"Activos Digitales","ic":"💻","tipos":["Software institucional","App","Plataforma","Algoritmo","Modelo de IA","Dataset","Gemelo digital"]},
 {"cat":"Transferencia / Know-how","ic":"🔁","tipos":["Know-how","Tecnología protegida","Tecnología no protegida","Prototipo","Spin-off","Startup","Conocimiento tradicional"]},
]
# Flujos (BPMN simplificado) por trámite — secuencias de la guía institucional / autoridades
FLUJOS={
 "Registro de obra (INDAUTOR)":["Solicitud","Revisión documental","Validación jurídica","Integración del expediente","Envío a INDAUTOR","Seguimiento","Obtención del certificado","Digitalización","Archivo","Alertas de conservación"],
 "Registro de marca (IMPI)":["Solicitud","Búsqueda fonética","Análisis de viabilidad","Clasificación de Niza","Revisión jurídica","Presentación ante IMPI","Contestación de requerimientos","Concesión","Renovación"],
 "Patente":["Divulgación de invención","Evaluación de patentabilidad","Estado de la técnica","Dictamen técnico","Presentación ante IMPI","Seguimiento","Concesión","Mantenimiento","Transferencia tecnológica"],
 "Modelo de utilidad":["Divulgación","Evaluación","Estado de la técnica","Presentación ante IMPI","Seguimiento","Concesión","Mantenimiento"],
 "Diseño industrial":["Solicitud","Examen de forma","Clasificación de Locarno","Presentación ante IMPI","Seguimiento","Concesión","Mantenimiento"],
 "ISSN (INDAUTOR)":["Solicitud","Validación","Revisión de reserva de derechos","Integración documental","Trámite ante INDAUTOR","Asignación","Archivo","Control de vigencia"],
 "ISBN":["Solicitud","Integración documental","Revisión","Asignación","Digitalización","Repositorio"],
 "Reserva de derechos":["Solicitud","Búsqueda de antecedentes","Integración documental","Trámite ante INDAUTOR","Concesión","Control de vigencia"],
 "Variedad vegetal (SNICS/UPOV)":["Solicitud","Examen de novedad","Examen técnico (DHE)","Dictamen","Título de obtentor","Vigilancia","Renovación"],
 "Software (Derecho de Autor)":["Solicitud","Depósito de código","Validación jurídica","Envío a INDAUTOR","Certificado","Repositorio","Control de versiones"],
 "Secreto industrial / Know-how":["Identificación","Clasificación de confidencialidad","Medidas de protección (NDA)","Control de accesos","Vigilancia de divulgación"],
 "Transferencia tecnológica":["Divulgación","Valorización (TRL)","Estrategia de protección","Negociación de licencia","Contrato","Regalías","Seguimiento"],
 "Genérico":["Solicitud","Revisión","Integración","Trámite","Concesión","Archivo"],
}
# tipo -> trámite por defecto
TIPO_TRAMITE={
 "Patente":"Patente","Modelo de utilidad":"Modelo de utilidad","Diseño industrial":"Diseño industrial",
 "Marca":"Registro de marca (IMPI)","Marca colectiva":"Registro de marca (IMPI)","Aviso comercial":"Registro de marca (IMPI)","Nombre comercial":"Registro de marca (IMPI)",
 "Secreto industrial":"Secreto industrial / Know-how","Know-how":"Secreto industrial / Know-how",
 "Indicación geográfica":"Genérico","Denominación de origen":"Genérico","Esquema de trazado de circuitos integrados":"Genérico",
 "Software":"Software (Derecho de Autor)","Software institucional":"Software (Derecho de Autor)","App":"Software (Derecho de Autor)","Plataforma":"Software (Derecho de Autor)","Algoritmo":"Software (Derecho de Autor)","Modelo de IA":"Software (Derecho de Autor)","Gemelo digital":"Software (Derecho de Autor)",
 "ISBN":"ISBN","ISSN":"ISSN (INDAUTOR)","Reserva de derechos":"Reserva de derechos","Derecho conexo":"Registro de obra (INDAUTOR)",
 "Título de obtentor":"Variedad vegetal (SNICS/UPOV)","Material vegetal":"Variedad vegetal (SNICS/UPOV)","Banco de germoplasma":"Variedad vegetal (SNICS/UPOV)",
 "Spin-off":"Transferencia tecnológica","Startup":"Transferencia tecnológica","Conocimiento tradicional":"Transferencia tecnológica","Tecnología protegida":"Transferencia tecnológica","Tecnología no protegida":"Transferencia tecnológica","Prototipo":"Transferencia tecnológica",
}
CU=["CUAAD","CUCBA","CUCEA","CUCEI","CUCS","CUCSH","CUValles","CUNorte","CUSur","CUCiénega","CUCosta","CUCSur","CULagos","CUTonalá","SEMS","UDG Virtual","Rectoría General","Coordinación de Investigación","Editorial Universitaria","Institutos y Centros de Investigación"]
TIT_ROLES=["Autor","Coautor","Inventor","Titular moral","Titular patrimonial","Cotitular","Dependencia universitaria"]
CONTRATOS=["Cesión de derechos","Licencia exclusiva","Licencia no exclusiva","Convenio de confidencialidad (NDA)","MTA (Material Transfer Agreement)","CDA","Technology License Agreement","Sponsored Research Agreement","Joint Development Agreement","Research Collaboration Agreement","Acuerdo de cotitularidad","Convenio de explotación","Creative Commons"]
OBSERV=["Oposición","Nulidad","Caducidad","Cancelación","Infracción","Juicio de nulidad","Amparo","Arbitraje","Mediación"]
OBS_AUT=["IMPI","INDAUTOR","SNICS","TFJA","Tribunal Colegiado","SCJN","OMPI"]
FUENTES=["Recursos propios UdeG","SECIHTI","CONAHCYT","SEP","NIH","NSF","Unión Europea","Banco Mundial","Mixto","No aplica"]
TRL=[["TRL 1","Principios básicos observados"],["TRL 2","Concepto tecnológico formulado"],["TRL 3","Prueba de concepto"],["TRL 4","Validación en laboratorio"],["TRL 5","Validación en entorno relevante"],["TRL 6","Demostración en entorno relevante"],["TRL 7","Prototipo en entorno real"],["TRL 8","Sistema completo y calificado"],["TRL 9","Sistema probado en entorno real"]]
NIZA=["1 Productos químicos","2 Pinturas","3 Cosméticos y limpieza","4 Aceites y combustibles","5 Productos farmacéuticos","6 Metales comunes","7 Máquinas","8 Herramientas manuales","9 Aparatos científicos y software","10 Aparatos médicos","11 Aparatos de alumbrado","12 Vehículos","13 Armas de fuego","14 Joyería","15 Instrumentos musicales","16 Papel e imprenta","17 Caucho y plásticos","18 Cuero","19 Materiales de construcción","20 Muebles","21 Utensilios domésticos","22 Cuerdas y textiles","23 Hilos","24 Tejidos","25 Prendas de vestir","26 Encajes y bordados","27 Alfombras","28 Juegos y juguetes","29 Carne y alimentos","30 Café, té y pastelería","31 Productos agrícolas","32 Cervezas y refrescos","33 Bebidas alcohólicas","34 Tabaco","35 Publicidad y negocios","36 Seguros y finanzas","37 Construcción y reparación","38 Telecomunicaciones","39 Transporte","40 Tratamiento de materiales","41 Educación y formación","42 Servicios científicos y tecnológicos","43 Restauración y hospedaje","44 Servicios médicos y agrícolas","45 Servicios jurídicos y de seguridad"]
ART220=("Artículo 220 (Reglamento Interior de la Administración General de la UdeG) — Atribuciones de la Unidad de Protección del Patrimonio Intangible: "
 "I. Brindar asesoría legal en materia de propiedad intelectual para el registro y protección jurídica del patrimonio intangible de la Universidad; "
 "II. Realizar los trámites de propiedad industrial (patentes, modelos de utilidad, diseños industriales, esquemas de trazado de circuitos integrados, marcas, avisos comerciales, nombres comerciales, denominaciones de origen/indicaciones geográficas y variedades vegetales); "
 "III. Inscribir obras en materia de derecho de autor y derechos conexos, reservas de derechos, y registrar convenios y contratos que confieran, modifiquen, transmitan, graven o extingan derechos patrimoniales ante el Registro Público del Derecho de Autor; "
 "IV. Tramitar solicitudes de declaración administrativa de nulidad, caducidad, cancelación e infracción; "
 "V. Tramitar solicitudes de ISBN e ISSN de las publicaciones de la Universidad; "
 "VI. Coadyuvar con la Red Universitaria en difusión, promoción y vinculación del patrimonio intangible; "
 "VII. Las demás que establezca la normatividad vigente.")
CLASIF=[["Clasificación de Niza","Marcas (productos y servicios) — 45 clases"],["Clasificación de Viena","Elementos figurativos de marcas"],["Clasificación de Locarno","Diseños industriales"],["Clasificación Internacional de Patentes (IPC)","Patentes"],["Clasificación Cooperativa de Patentes (CPC)","Patentes (EPO/USPTO)"]]
VIGILANCIA=[["IMPI · MARCANET","Marcas y patentes nacionales","https://acervomarcas.impi.gob.mx"],["Espacenet (EPO)","Patentes mundiales","https://worldwide.espacenet.com"],["WIPO PATENTSCOPE","Solicitudes PCT","https://patentscope.wipo.int"],["WIPO Global Brand Database","Marcas internacionales","https://branddb.wipo.int"],["Google Patents","Patentes","https://patents.google.com"],["USPTO","EE. UU.","https://www.uspto.gov"]]

DATA={"corte":"2026-06-18","cats":CATS,"flujos":FLUJOS,"tipo_tramite":TIPO_TRAMITE,"cu":CU,"tit_roles":TIT_ROLES,
 "contratos":CONTRATOS,"observ":OBSERV,"obs_aut":OBS_AUT,"fuentes":FUENTES,"trl":TRL,"niza":NIZA,"art220":ART220,"clasif":CLASIF,"vigilancia":VIGILANCIA}
DATAJ=json.dumps(DATA,ensure_ascii=False)

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html" class="act">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''

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
<title>SIGEJ-UdeG · Patrimonio Intangible (IPMS/TTO)</title>
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
.drawer{position:fixed;inset:0;background:rgba(4,12,24,.72);display:none;align-items:center;justify-content:center;z-index:9000;padding:18px}
.drawer.on{display:flex}.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;max-width:920px;width:100%;max-height:88vh;overflow:auto;padding:20px}
.panel .x{float:right;cursor:pointer;color:var(--mut);font-size:20px}
.warn{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:9px;padding:9px 12px;font-size:11.5px;color:#e8cf95;margin:8px 0}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:26px;text-align:center;color:var(--mut);font-size:13px}
.trl{display:flex;gap:3px}.trlb{flex:1;height:22px;border-radius:4px;background:#f1f5fb;border:1px solid var(--line);font-size:9px;display:flex;align-items:center;justify-content:center;color:#64748b}
.trlb.on{background:linear-gradient(90deg,var(--teal),var(--azul2));color:#fff;font-weight:700}
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
<header><div><h1>🧩 SIGEJ-UdeG · Gestión del Patrimonio Intangible — Unidad de Protección del Patrimonio Intangible · OAG</h1>
<div class="s">IPMS / TTO: propiedad industrial, derecho de autor, variedades vegetales, activos digitales, transferencia tecnológica · Art. 220 RIAG-UdeG</div></div>
<div style="text-align:right"><span class="live"><span class="dot"></span>En vivo · <span id="upd"></span></span> <button class="b1 mini" onclick="compute()">↻ Actualizar</button></div></header>
__NAV__
<div class="tabbar">
 <button class="tb on" data-t="t1" onclick="tab('t1')">🛰️ Tablero (BI)</button>
 <button class="tb" data-t="t2" onclick="tab('t2')">➕ Alta de activo</button>
 <button class="tb" data-t="t3" onclick="tab('t3')">📁 Activos / Expedientes</button>
 <button class="tb" data-t="t4" onclick="tab('t4')">⏳ Vigencias</button>
 <button class="tb" data-t="t5" onclick="tab('t5')">👥 Titularidad</button>
 <button class="tb" data-t="t6" onclick="tab('t6')">🔁 Transferencia (TRL)</button>
 <button class="tb" data-t="t7" onclick="tab('t7')">🛡️ Observancia y defensa</button>
 <button class="tb" data-t="t8" onclick="tab('t8')">🧠 Conocimiento</button>
 <button class="tb" data-t="t9" onclick="tab('t9')">🔍 Repositorio / búsqueda</button>
 <button class="tb" data-t="t10" onclick="tab('t10')">🏛️ Marco y vigilancia</button>
 <button class="tb" data-t="t11" onclick="tab('t11')">📚 Publicaciones y editorial (IP)</button>
 <button class="tb" data-t="t12" onclick="tab('t12')">🚀 Transferencia tecnológica (OTT)</button>
</div>
<div class="wrap">
 <section id="t1" class="tab on">
  <div class="kpis" id="ceKpis"></div>
  <div class="h">⏳ Vigencias próximas (alertas 180/90/60/30/15 días)</div><div class="buckets" id="ceBuckets"></div>
  <div class="grid" style="margin-top:14px">
   <div class="card"><h3>Por categoría</h3><canvas id="cCat"></canvas></div>
   <div class="card"><h3>Por estado del trámite</h3><canvas id="cEst"></canvas></div>
   <div class="card s2"><h3>Activos por Centro Universitario</h3><canvas id="cCU"></canvas></div>
   <div class="card"><h3>Por tipo (top)</h3><canvas id="cTipo"></canvas></div>
   <div class="card"><h3>Regalías por CU (MXN)</h3><canvas id="cReg"></canvas></div>
   <div class="card s2"><h3>🗺️ Mapa de innovación — por Centro Universitario</h3><div id="ceMapa"></div></div>
  </div>
 </section>

 <section id="t2" class="tab">
  <div class="card"><h3>Alta de activo intangible · expediente electrónico de PI</h3>
   <div class="f"><label>Categoría</label><select id="i_cat" onchange="catChange()"></select></div>
   <div class="f"><label>Tipo</label><select id="i_tipo" onchange="tipoChange()"></select></div>
   <div class="f"><label>Trámite (flujo)</label><select id="i_tramite"></select></div>
   <div class="f" style="display:flex"><label>Título / denominación del activo</label><textarea id="i_titulo" style="min-height:38px"></textarea></div>
   <div class="f"><label>Centro Universitario</label><select id="i_cu"></select></div>
   <div class="f"><label>Dependencia</label><input id="i_dep"></div>
   <div class="f"><label>Autor / Inventor principal</label><input id="i_autor"></div>
   <div class="f"><label>Responsable del trámite</label><input id="i_resp"></div>
   <div class="f"><label>Fuente de financiamiento</label><select id="i_fuente"></select></div>
   <div class="f"><label>Clase de Niza (marcas)</label><select id="i_niza"></select></div>
   <div class="f"><label>TRL (tecnología)</label><select id="i_trl"></select></div>
   <div class="f"><label>Fecha de solicitud</label><input id="i_sol" type="date"></div>
   <div class="f"><label>Fecha de concesión</label><input id="i_conc" type="date"></div>
   <div class="f"><label>Fecha de vencimiento</label><input id="i_venc" type="date"></div>
   <div style="margin-top:6px"><button class="b3" onclick="saveAsset()">＋ Registrar activo</button> <span id="i_msg" style="font-size:12px;color:#7ee0b4;margin-left:8px"></span></div>
  </div>
  <div class="warn">⚠️ Captura local (prototipo). <b>IA jurídica</b> (búsqueda de anterioridades, colisión marcaria, resúmenes), <b>blockchain / sellos de tiempo</b>, <b>OCR</b>, <b>vigilancia externa</b> (Espacenet/IMPI/WIPO/USPTO), <b>plagio</b> (Turnitin/iThenticate), <b>valorización automática</b> e integración con INDAUTOR/IMPI/SNICS = fase de implementación con backend.</div>
 </section>

 <section id="t3" class="tab">
  <div class="bar">
   <input id="q" placeholder="Buscar (folio, título, autor, dependencia, tipo)…" oninput="renderList()" style="min-width:240px">
   <select id="fCat" onchange="renderList()"><option value="">Toda categoría</option></select>
   <select id="fCU" onchange="renderList()"><option value="">Todo CU</option></select>
   <select id="fRiesgo" onchange="renderList()"><option value="">Todo riesgo</option><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
   <button class="bd mini" onclick="exportCSV()">⬇ CSV</button><span id="listCnt" style="font-size:12px;color:#64748b"></span>
  </div>
  <div id="lista"></div>
 </section>

 <section id="t4" class="tab">
  <div class="h">⏳ Matriz de vigencias — renovaciones y caducidades</div>
  <div class="buckets" id="vigBuckets"></div>
  <div class="bar" style="margin-top:12px"><select id="fVig" onchange="renderVig()"><option value="">Todo</option><option value="venc">Vencidos</option><option value="15">≤ 15 días</option><option value="30">≤ 30 días</option><option value="60">≤ 60 días</option><option value="90">≤ 90 días</option><option value="180">≤ 180 días</option></select></div>
  <div id="vigLista"></div>
  <div class="warn">Notificaciones automáticas (correo/app/push) a 180/90/60/30/15 días = fase backend. La <b>analítica predictiva</b> de caducidad/abandono usa un score proxy explicable (días a vencimiento + estado + renovaciones).</div>
 </section>

 <section id="t5" class="tab">
  <div class="h">👥 Matriz de titularidad institucional</div>
  <div class="card"><table id="titTable"></table>
   <div style="font-size:11px;color:#64748b;margin-top:8px">Agrega titulares (autor/coautor/inventor/titular moral/patrimonial/cotitular) con su % de participación desde la ficha de cada activo. La titularidad patrimonial por defecto corresponde a la Universidad de Guadalajara.</div></div>
 </section>

 <section id="t6" class="tab">
  <div class="kpis" id="ttKpis"></div>
  <div class="h">📈 Madurez tecnológica (TRL) — distribución del portafolio</div><div class="card"><div id="trlDist"></div></div>
  <div class="h">💱 Licencias y regalías</div><div class="card"><table id="licTable"></table></div>
 </section>

 <section id="t7" class="tab">
  <div class="kpis" id="obKpis"></div>
  <div class="h">🛡️ Procedimientos de observancia y defensa</div>
  <div class="card"><table id="obTable"></table>
   <div style="font-size:11px;color:#64748b;margin-top:8px">Registra oposiciones, nulidades, caducidades, cancelaciones, infracciones y litigios desde la ficha del activo (Art. 220 fr. IV).</div></div>
 </section>

 <section id="t8" class="tab">
  <div class="card"><h3>🧠 Centro de Conocimiento — criterios, dictámenes y clasificaciones</h3>
   <div class="f"><label>Categoría</label><select id="k_cat"><option>Criterio institucional</option><option>Dictamen</option><option>Manual / Guía</option><option>Tratado internacional</option><option>Jurisprudencia</option><option>Clasificación</option></select></div>
   <div class="f"><label>Título</label><input id="k_tit" style="min-width:260px"></div>
   <div class="f" style="display:flex"><label>Contenido / referencia</label><textarea id="k_txt"></textarea></div>
   <div><button class="b3" onclick="saveKB()">＋ Registrar</button></div>
  </div>
  <div class="grid" style="margin-top:12px">
   <div class="card"><h3>📚 Clasificaciones internacionales</h3><div id="clasifBox"></div></div>
   <div class="card s2"><h3>🗂️ Repositorio institucional</h3><div id="kbList"></div></div>
  </div>
 </section>

 <section id="t9" class="tab">
  <div class="bar"><input id="q9" placeholder="Búsqueda en el repositorio histórico (folio, título, autor, registro, clase, palabra clave)…" oninput="renderRepo()" style="min-width:340px">
   <select id="f9cat" onchange="renderRepo()"><option value="">Toda categoría</option></select></div>
  <div id="repoList"></div>
  <div class="warn">La <b>búsqueda semántica</b> y el <b>OCR</b> de documentos soporte son fase backend; aquí la búsqueda es por palabras clave sobre los campos capturados.</div>
 </section>

 <section id="t10" class="tab">
  <div class="card"><h3>🏛️ Fundamento — Art. 220 RIAG-UdeG</h3><div id="art220" style="font-size:12.5px;color:#c7d6ea;line-height:1.6"></div></div>
  <div class="grid" style="margin-top:12px">
   <div class="card"><h3>🔭 Vigilancia tecnológica y marcaria</h3><div id="vigil"></div><div class="warn" style="margin-top:8px">Integración en vivo con estas bases (detección de anterioridades, colisiones y oposiciones) = fase backend. Aquí se enlazan las fuentes oficiales para consulta manual.</div></div>
   <div class="card"><h3>🤖 IA y blockchain (hoja de ruta)</h3><div style="font-size:12px;color:#c7d6ea;line-height:1.7">🔹 <b>IA jurídica</b>: búsqueda de anterioridades, análisis de colisión marcaria, resúmenes de patentes, matrices comparativas, reportes ejecutivos.<br>🔹 <b>Blockchain</b>: sellos de tiempo, certificados de existencia, registro de prioridad, cadena de custodia.<br>🔹 <b>Sistema experto</b>: ¿es patentable? ¿derecho de autor? ¿marca? ¿secreto industrial? ¿hay colisión? estrategia de protección.<br>🔹 <b>Plagio</b>: Turnitin / iThenticate.<br><span style="color:#e8cf95">Todo lo anterior es fase de implementación con backend e integraciones.</span></div></div>
  </div>
 </section>
 <section id="t11" class="tab">
  <div id="pubNav" style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px">
   <button onclick="pubGo('panel')" style="border:none;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer;background:#0a4d8c;color:#fff;font-weight:700">📊 Panel</button>
   <button onclick="pubGo('lista')" style="border:none;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer;background:#e2e8f0;color:#0a1f3c">📚 Publicaciones</button>
   <button onclick="pubGo('venc')" style="border:none;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer;background:#e2e8f0;color:#0a1f3c">⏳ Vencimientos</button>
  </div>
  <div id="pubBody"></div>
 </section>
 <section id="t12" class="tab">
  <div id="ottNav" style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px">
   <button onclick="ottGo('panel')" style="border:none;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer;background:#0a4d8c;color:#fff;font-weight:700">📊 Panel / embudo</button>
   <button onclick="ottGo('cartera')" style="border:none;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer;background:#e2e8f0;color:#0a1f3c">🧪 Cartera OTT (5 etapas)</button>
   <button onclick="ottGo('reg')" style="border:none;border-radius:8px;padding:8px 13px;font-size:12.5px;cursor:pointer;background:#e2e8f0;color:#0a1f3c">💱 Licenciamiento y regalías</button>
  </div>
  <div id="ottBody"></div>
 </section>
</div>
<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div></div>
<input type="file" id="fileIn" style="display:none">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const HOY=new Date(2026,5,18);let CH={};let FILEIDX=null;
let A=JSON.parse(localStorage.getItem('sigej_patrimonio')||'[]');
let KB=JSON.parse(localStorage.getItem('sigej_pi_kb')||'[]');
function saveA(){localStorage.setItem('sigej_patrimonio',JSON.stringify(A));}
function saveKBs(){localStorage.setItem('sigej_pi_kb',JSON.stringify(KB));}
function el(id){return document.getElementById(id);}
function val(id){return (el(id).value||'').trim();}
function pad(n){return (n<10?'0':'')+n;}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function nowStr(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function hoyStr(){return HOY.toISOString().slice(0,10);}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-HOY)/864e5);}
function catOf(tipo){const c=D.cats.find(x=>x.tipos.indexOf(tipo)>=0);return c?c.cat:'Otros';}
function nivel(s){return s>70?'Crítico':s>=50?'Alto':s>=28?'Medio':s>0?'Bajo':'Indeterminado';}
function scoreOf(e){let s=0;const d=dr(e.venc);
 if(d!==null){s+= d<0?60:d<=15?50:d<=30?40:d<=60?28:d<=90?18:d<=180?10:2;}
 if((e.estado||'').match(/Renovaci|Mantenimiento|Vigilancia|Control de vigencia/))s+=10;
 if(!e.renov||e.renov<1)s+=8;
 if((e.cat||'')==='Propiedad Industrial')s+=6;
 return Math.min(100,Math.round(s));}
function tab(id){document.querySelectorAll('.tab').forEach(s=>s.classList.toggle('on',s.id===id));
 document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 if(id==='t1')setTimeout(compute,20);if(id==='t3')renderList();if(id==='t4')renderVig();if(id==='t5')renderTit();if(id==='t6')renderTT();if(id==='t7')renderObs();if(id==='t8')renderKB();if(id==='t9')renderRepo();if(id==='t10')renderMarco();if(id==='t11')renderPub();if(id==='t12')renderOTT();}
/* ===== Submódulo: Transferencia Tecnológica (OTT) — proceso de 5 etapas + licenciamiento/cesión/regalías ===== */
function OTT(){try{return JSON.parse(localStorage.getItem('sigej_ott')||'[]');}catch(e){return [];}}
function ottS(x){localStorage.setItem('sigej_ott',JSON.stringify(x));}
function ov(id){var e=el(id);return e?(e.value||'').trim():'';}
function oesc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function ouid(){return 'ott'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function onow(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function ohoy(){return new Date().toISOString().slice(0,10);}
function oopt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
function oM(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function onotif(t,f){try{var N=JSON.parse(localStorage.getItem('sigej_notificaciones')||'[]');N.push({ts:onow(),area:'Transferencia tecnológica (OTT)',texto:t,folio:f||'',modulo:'Patrimonio Intangible',leida:false});localStorage.setItem('sigej_notificaciones',JSON.stringify(N));}catch(e){}}
var OTTETAPA=['1. Identificación','2. Protección','3. Valorización','4. Promoción','5. Negociación'];
var OTTMEC=['Por definir','Licenciamiento (regalías)','Cesión / venta de derechos','Spin-off / startup'];
var OTTEST=['Activa','Licenciada','Cedida','Spin-off creada','Descartada'];
var OTTCU=['CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUTonalá','CUCiénega','Coord. Gral. de Investigación'];
var OTTV='panel';
function ottSeed(){if(localStorage.getItem('sigej_ott'))return;ottS([
 {id:ouid(),folio:'OTT-2026-001',titulo:'Biosensor de glucosa no invasivo',inventor:'Dr. Luis Márquez',cu:'CUCEI',trl:5,etapa:'3. Valorización',potencial:'Alto — dispositivos médicos',piVinc:'P-XXXX (patente en trámite)',valoracion:'Modelo de licencia a fabricante de dispositivos',actores:'Industria de dispositivos médicos',mecanismo:'Licenciamiento (regalías)',contraparte:'',regTipo:'% sobre ventas',regValor:'5%',ingresos:[],estado:'Activa',docs:[],traza:[{ts:onow(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:ouid(),folio:'OTT-2026-002',titulo:'Software de análisis jurídico (algoritmo)',inventor:'Equipo CUCEA',cu:'CUCEA',trl:7,etapa:'5. Negociación',potencial:'Medio — legaltech',piVinc:'Derecho de autor (software)',valoracion:'Licencia SaaS',actores:'Despachos y legaltech',mecanismo:'Licenciamiento (regalías)',contraparte:'LegalTech S.A.',regTipo:'Monto fijo anual',regValor:'120000',ingresos:[{fecha:'2026-06-01',monto:120000}],estado:'Licenciada',docs:[],traza:[{ts:onow(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:ouid(),folio:'OTT-2026-003',titulo:'Variedad vegetal resistente a sequía',inventor:'CUCBA',cu:'CUCBA',trl:4,etapa:'2. Protección',potencial:'Alto — agro',piVinc:'Título de obtentor (en trámite)',valoracion:'',actores:'',mecanismo:'Por definir',contraparte:'',regTipo:'',regValor:'',ingresos:[],estado:'Activa',docs:[],traza:[{ts:onow(),usuario:'Sistema',accion:'Alta (demo)'}]}
]);}
function ottGo(v){OTTV=v;var m={panel:0,cartera:1,reg:2};[].forEach.call(document.querySelectorAll('#ottNav button'),function(b,k){b.style.background=(k===m[v])?'#0a4d8c':'#e2e8f0';b.style.color=(k===m[v])?'#fff':'#0a1f3c';b.style.fontWeight=(k===m[v])?'700':'400';});renderOTT();}
function renderOTT(){ottSeed();if(OTTV==='panel')ottPanel();else if(OTTV==='cartera')ottCartera();else ottReg();}
function ottIngresos(x){return (x.ingresos||[]).reduce(function(a,r){return a+(+r.monto||0);},0);}
function ottPanel(){var A=OTT();
 var lic=A.filter(function(x){return x.estado==='Licenciada';}).length,ced=A.filter(function(x){return x.estado==='Cedida';}).length,spin=A.filter(function(x){return x.estado==='Spin-off creada';}).length;
 var reg=A.reduce(function(a,x){return a+ottIngresos(x);},0);
 var trlProm=A.length?Math.round(A.reduce(function(a,x){return a+(+x.trl||0);},0)/A.length):0;
 function k(n,l,c){return '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:11px;padding:13px"><div style="font-size:22px;font-weight:800;color:'+(c||'#00254a')+'">'+n+'</div><div style="font-size:11px;color:#64748b;margin-top:2px">'+l+'</div></div>';}
 var kp='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px">'+k(A.length,'Tecnologías')+k(lic,'Licenciadas','#1f9d6b')+k(ced,'Cedidas / vendidas')+k(spin,'Spin-offs','#d4a32c')+k(oM(reg),'Regalías/ingresos','#1f9d6b')+k('TRL '+trlProm,'TRL promedio')+'</div>';
 var funnel=OTTETAPA.map(function(e){var n=A.filter(function(x){return x.etapa===e;}).length;var w=A.length?Math.max(6,Math.round(100*n/A.length)):6;return '<div style="margin:5px 0"><div style="display:flex;justify-content:space-between;font-size:12px"><span>'+e+'</span><b>'+n+'</b></div><div style="height:14px;background:#eef2f7;border-radius:7px;overflow:hidden"><div style="height:100%;width:'+w+'%;background:linear-gradient(90deg,#1aa39a,#0a4d8c)"></div></div></div>';}).join('');
 el('ottBody').innerHTML='<h3 style="margin:0 0 4px;color:#00254a">📊 Panel del pipeline OTT</h3><p style="color:#64748b;font-size:12.5px;margin:0 0 12px">Proceso de transferencia en 5 etapas: Identificación → Protección → Valorización → Promoción → Negociación.</p>'+kp+
  '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:14px;margin-bottom:12px"><b style="color:#0a4d8c">Embudo por etapa</b>'+funnel+'</div>'+
  '<div style="background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px">ℹ️ <b>Mecanismos:</b> Licenciamiento (uso bajo condiciones + regalías) · Cesión/venta (transfiere totalmente los derechos) · Spin-off (empresa emergente). La búsqueda de socios industriales, la valuación financiera y la gestión de contratos con firma electrónica son fase backend. Este submódulo complementa la vista de TRL/regalías (pestaña «Transferencia (TRL)»).</div>';
}
function ottForm(){function f(id,l,ty){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+l+'</label><input id="'+id+'"'+(ty?' type="'+ty+'"':'')+' style="width:100%;padding:7px 9px;border:1px solid #e2e8f0;border-radius:7px;font-size:13px"></div>';}
 function s(id,l,a){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+l+'</label><select id="'+id+'" style="width:100%;padding:7px 9px;border:1px solid #e2e8f0;border-radius:7px;font-size:13px">'+oopt(a,'')+'</select></div>';}
 var g='display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px';
 return '<div style="'+g+'">'+f('ot_tit','Tecnología / innovación *')+f('ot_inv','Inventor(es)')+s('ot_cu','CU',OTTCU)+f('ot_trl','TRL (1-9)','number')+s('ot_et','Etapa',OTTETAPA)+f('ot_pot','Potencial de mercado')+f('ot_pi','PI vinculada (patente/marca/software)')+s('ot_mec','Mecanismo',OTTMEC)+f('ot_val','Valorización / modelo de negocio')+f('ot_act','Actores de industria interesados')+'</div><div style="margin-top:8px"><button onclick="ottAdd()" style="border:none;border-radius:8px;padding:9px 14px;background:#1f9d6b;color:#fff;font-weight:700;cursor:pointer">＋ Registrar tecnología</button> <span id="ot_msg" style="font-size:12px;color:#1f9d6b"></span></div>';}
function ottCartera(){var A=OTT();var q=(ov('ottq')||'').toLowerCase(),fe=ov('ottfe');
 var form='<div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:10px;overflow:hidden;background:#fff"><div onclick="var d=el(\'ottForm\');d.style.display=d.style.display===\'none\'?\'block\':\'none\'" style="background:#f8fafc;padding:10px 13px;font-weight:700;color:#0a4d8c;cursor:pointer;font-size:13px">➕ Registrar tecnología — clic para abrir/cerrar</div><div id="ottForm" style="display:none;padding:12px">'+ottForm()+'</div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="ottq" value="'+oesc(ov('ottq'))+'" placeholder="🔎 Buscar tecnología…" oninput="renderOTT()" style="flex:1;min-width:160px;padding:8px;border:1px solid #e2e8f0;border-radius:8px"><select id="ottfe" onchange="renderOTT()" style="max-width:180px;padding:8px;border:1px solid #e2e8f0;border-radius:8px"><option value="">Toda etapa</option>'+oopt(OTTETAPA,fe)+'</select></div>';
 var rows=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){return (!q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0)&&(!fe||o.x.etapa===fe);});
 var tbl='<table style="width:100%;border-collapse:collapse;font-size:12.5px"><tr style="text-align:left;color:#64748b"><th style="padding:6px;border-bottom:2px solid #e2e8f0">Folio</th><th style="border-bottom:2px solid #e2e8f0">Tecnología</th><th style="border-bottom:2px solid #e2e8f0">TRL</th><th style="border-bottom:2px solid #e2e8f0">Etapa</th><th style="border-bottom:2px solid #e2e8f0">Mecanismo</th><th style="border-bottom:2px solid #e2e8f0">Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var c=x.estado==='Licenciada'||x.estado==='Cedida'?'#15803d':x.estado==='Descartada'?'#c0392b':'#b45309';return '<tr onclick="ottFicha('+o.i+')" style="cursor:pointer;border-bottom:1px solid #f1f5f9"><td style="padding:6px">'+oesc(x.folio)+'</td><td><b>'+oesc(x.titulo)+'</b><br><span style="font-size:10px;color:#64748b">'+oesc(x.cu||'')+'</span></td><td>TRL '+(x.trl||'—')+'</td><td style="font-size:11px">'+oesc(x.etapa)+'</td><td style="font-size:11px">'+oesc(x.mecanismo)+'</td><td style="color:'+c+';font-weight:700">'+oesc(x.estado)+'</td></tr>';}).join(''):'<tr><td colspan="6" style="padding:16px;text-align:center;color:#64748b">Sin tecnologías.</td></tr>')+'</table>';
 el('ottBody').innerHTML='<h3 style="margin:0 0 4px;color:#00254a">🧪 Cartera de tecnologías (5 etapas)</h3><p style="color:#64748b;font-size:12.5px;margin:0 0 10px">Registra y haz avanzar cada tecnología por el proceso de transferencia.</p>'+form+ctrl+tbl;
}
function ottAdd(){if(!ov('ot_tit')){el('ot_msg').style.color='#c0392b';el('ot_msg').textContent='Indica la tecnología.';return;}
 var A=OTT();var folio='OTT-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 A.push({id:ouid(),folio:folio,titulo:ov('ot_tit'),inventor:ov('ot_inv'),cu:ov('ot_cu'),trl:+ov('ot_trl')||0,etapa:ov('ot_et'),potencial:ov('ot_pot'),piVinc:ov('ot_pi'),valoracion:ov('ot_val'),actores:ov('ot_act'),mecanismo:ov('ot_mec'),contraparte:'',regTipo:'',regValor:'',ingresos:[],estado:'Activa',docs:[],traza:[{ts:onow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Alta en etapa '+ov('ot_et')}]});
 ottS(A);if(window.__bitlog)__bitlog('Transferencia tecnológica (OTT)','Alta '+folio+' · '+ov('ot_tit'));el('ot_msg').style.color='#1f9d6b';el('ot_msg').textContent='✓ '+folio+' registrada.';renderOTT();}
function ottFicha(i){var A=OTT();var x=A[i];if(!x)return;var ci=OTTETAPA.indexOf(x.etapa);
 var steps=OTTETAPA.map(function(e,k){return '<span style="display:inline-block;font-size:10.5px;padding:2px 8px;border-radius:10px;margin:1px;background:'+(k<ci?'#1f9d6b;color:#fff':k===ci?'#0a4d8c;color:#fff':'#eef2f7;color:#64748b')+'">'+e+'</span>';}).join(' ');
 var ing=(x.ingresos||[]).length?(x.ingresos||[]).map(function(r){return '<div style="font-size:11.5px">💰 '+r.fecha+' · '+oM(r.monto)+'</div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin ingresos registrados.</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+oesc(t.usuario)+' — '+oesc(t.accion)+'</div>';}).join('');
 function box(t,b,bd){return '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6'+(bd?';border-left:4px solid '+bd:'')+'"><b>'+t+'</b><br>'+b+'</div>';}
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+oesc(x.titulo)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+oesc(x.folio)+' · '+oesc(x.cu||'')+' · TRL '+(x.trl||'—')+' · '+oesc(x.estado)+'</div>'+
  box('🔄 Etapa del proceso','<div style="margin-top:4px;line-height:2">'+steps+'</div><div style="margin-top:6px"><button onclick="ottAvanzar('+i+')" style="border:none;border-radius:7px;padding:5px 10px;background:#0a4d8c;color:#fff;font-size:11px;cursor:pointer">▶ Avanzar etapa</button></div>')+
  box('💡 Tecnología','Inventor: '+oesc(x.inventor||'—')+'<br>Potencial: '+oesc(x.potencial||'—')+'<br>PI vinculada: '+oesc(x.piVinc||'—')+'<br>Valorización: '+oesc(x.valoracion||'—')+'<br>Actores: '+oesc(x.actores||'—'))+
  box('🤝 Mecanismo y regalías','Mecanismo: <b>'+oesc(x.mecanismo)+'</b><br>Contraparte: '+oesc(x.contraparte||'—')+'<br>Regalía: '+oesc(x.regTipo||'—')+' '+oesc(x.regValor||'')+'<br>Ingresos acumulados: <b>'+oM(ottIngresos(x))+'</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap"><button onclick="ottMec('+i+')" style="border:none;border-radius:7px;padding:5px 9px;background:#e2e8f0;font-size:11px;cursor:pointer">Definir mecanismo/regalía</button><button onclick="ottIngreso('+i+')" style="border:none;border-radius:7px;padding:5px 9px;background:#e6f6ee;color:#15803d;font-size:11px;cursor:pointer">＋ Registrar ingreso</button></div><div style="margin-top:5px">'+ing+'</div>',(x.mecanismo&&x.mecanismo!=='Por definir'?'#1f9d6b':''))+
  '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button onclick="closeDrw()" style="border:none;border-radius:7px;padding:7px 12px;background:#e2e8f0;cursor:pointer">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function ottAvanzar(i){var A=OTT();var x=A[i];var ci=OTTETAPA.indexOf(x.etapa);if(ci<OTTETAPA.length-1){x.etapa=OTTETAPA[ci+1];x.traza.push({ts:onow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Avanza a '+x.etapa});if(/Negociación/.test(x.etapa))onotif('Tecnología "'+x.titulo+'" llegó a Negociación (contrato/licencia/spin-off)',x.folio);ottS(A);if(window.__bitlog)__bitlog('Transferencia tecnológica (OTT)',x.folio+' → '+x.etapa);ottFicha(i);}else{alert('Ya está en la última etapa. Define el mecanismo y el estado (licenciada/cedida/spin-off).');}}
function ottMec(i){var A=OTT();var x=A[i];var m=prompt('Mecanismo (Licenciamiento (regalías) / Cesión / venta de derechos / Spin-off / startup):',x.mecanismo||'');if(m===null)return;x.mecanismo=m.trim()||x.mecanismo;x.contraparte=prompt('Contraparte (licenciatario/adquirente):',x.contraparte||'')||x.contraparte;x.regTipo=prompt('Tipo de regalía (% sobre ventas / monto fijo…):',x.regTipo||'')||x.regTipo;x.regValor=prompt('Valor de la regalía:',x.regValor||'')||x.regValor;
 if(/Licenciamiento/i.test(x.mecanismo))x.estado='Licenciada';else if(/Cesión|venta/i.test(x.mecanismo))x.estado='Cedida';else if(/Spin/i.test(x.mecanismo))x.estado='Spin-off creada';
 x.traza.push({ts:onow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Mecanismo: '+x.mecanismo+' · '+x.estado});ottS(A);if(window.__bitlog)__bitlog('Transferencia tecnológica (OTT)',x.folio+' · '+x.mecanismo);onotif('Tecnología "'+x.titulo+'" → '+x.estado,x.folio);ottFicha(i);}
function ottIngreso(i){var A=OTT();var x=A[i];var m=prompt('Monto del ingreso/regalía (MXN):','');if(m===null||!(+m))return;x.ingresos=x.ingresos||[];x.ingresos.push({fecha:ohoy(),monto:+m});x.traza.push({ts:onow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Ingreso de regalía '+oM(+m)});ottS(A);if(window.__bitlog)__bitlog('Transferencia tecnológica (OTT)','Ingreso '+x.folio+' '+oM(+m));ottFicha(i);}
function ottReg(){var A=OTT().filter(function(x){return x.mecanismo&&x.mecanismo!=='Por definir';});
 var total=A.reduce(function(a,x){return a+ottIngresos(x);},0);
 var tbl='<table style="width:100%;border-collapse:collapse;font-size:12.5px"><tr style="text-align:left;color:#64748b"><th style="padding:6px;border-bottom:2px solid #e2e8f0">Tecnología</th><th style="border-bottom:2px solid #e2e8f0">Mecanismo</th><th style="border-bottom:2px solid #e2e8f0">Contraparte</th><th style="border-bottom:2px solid #e2e8f0">Regalía</th><th style="border-bottom:2px solid #e2e8f0">Ingresos acum.</th></tr>'+
  (A.length?A.map(function(x){return '<tr style="border-bottom:1px solid #f1f5f9"><td style="padding:6px"><b>'+oesc(x.titulo)+'</b></td><td style="font-size:11px">'+oesc(x.mecanismo)+'</td><td style="font-size:11px">'+oesc(x.contraparte||'—')+'</td><td style="font-size:11px">'+oesc(x.regTipo||'—')+' '+oesc(x.regValor||'')+'</td><td><b>'+oM(ottIngresos(x))+'</b></td></tr>';}).join(''):'<tr><td colspan="5" style="padding:16px;text-align:center;color:#64748b">Sin licenciamientos/cesiones.</td></tr>')+'</table>';
 el('ottBody').innerHTML='<h3 style="margin:0 0 4px;color:#00254a">💱 Licenciamiento, cesiones y regalías</h3><p style="color:#64748b;font-size:12.5px;margin:0 0 10px">Ingresos totales por transferencia: <b>'+oM(total)+'</b>.</p>'+tbl+
  '<div style="background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin-top:10px">La gestión de contratos de licencia/cesión con firma electrónica y el cálculo automático de regalías por ventas reportadas son fase backend.</div>';
}
/* ===== Submódulo: Publicaciones y Editorial (registro IP: ISBN/ISSN · Reserva INDAUTOR · licitud SEGOB · cesiones/licencias · radio/TV) ===== */
function PUB(){try{return JSON.parse(localStorage.getItem('sigej_patrimonio_pub')||'[]');}catch(e){return [];}}
function pubSave(x){localStorage.setItem('sigej_patrimonio_pub',JSON.stringify(x));}
function pv(id){var e=el(id);return e?(e.value||'').trim():'';}
function pesc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function puid(){return 'pub'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function pnow(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function phoy(){return new Date().toISOString().slice(0,10);}
function pdr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(phoy()+'T00:00:00'))/864e5);}
function popt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
function pnotif(t,f){try{var N=JSON.parse(localStorage.getItem('sigej_notificaciones')||'[]');N.push({ts:pnow(),area:'Publicaciones y editorial',texto:t,folio:f||'',modulo:'Patrimonio Intangible',leida:false});localStorage.setItem('sigej_notificaciones',JSON.stringify(N));}catch(e){}}
var PUBTIPO=['Libro','Revista / publicación periódica','Capítulo de libro','Manual','Boletín','Programa de radio','Programa de televisión','Difusión periódica (radio/TV)','Fonograma','Publicación electrónica','Otro'];
var PUBGEN=['Publicaciones periódicas','Difusiones periódicas (radio/TV)','Personajes','Nombres / títulos','Promociones publicitarias','Obra artística','No aplica'];
var PUBCES=['Sin cesión','Cesión de derechos patrimoniales','Licencia de uso','Coedición','Contrato editorial'];
var PUBEST=['En trámite','Registrado','Vigente','Vencido','Cancelado'];
var PUBV='panel';
function pubSeed(){if(localStorage.getItem('sigej_patrimonio_pub'))return;pubSave([
 {id:puid(),folio:'PUB-2026-001',titulo:'Revista Jurídica UdeG',tipo:'Revista / publicación periódica',autores:'OAG / CUCSH',cu:'CUCSH',isbn:'',issn:'2007-XXXX',reservaNum:'04-2026-XXXXXX',reservaGen:'Publicaciones periódicas',reservaFecha:'2026-01-20',reservaVig:'2027-01-20',ltNum:'CCPRI-XXXX',ltFecha:'2026-01-25',lcNum:'CCPRI-XXXX',lcFecha:'2026-01-25',cesion:'Contrato editorial',cesionContra:'Editorial Universitaria',cesionVig:'2028-12-31',estado:'Vigente',obs:'',docs:[],traza:[{ts:pnow(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:puid(),folio:'PUB-2026-002',titulo:'Programa "Derecho al Día" (Radio UdeG)',tipo:'Difusión periódica (radio/TV)',autores:'Coordinación de Comunicación',cu:'Toda la Red',isbn:'',issn:'',reservaNum:'04-2025-XXXXXX',reservaGen:'Difusiones periódicas (radio/TV)',reservaFecha:'2025-09-01',reservaVig:'2026-09-01',ltNum:'',ltFecha:'',lcNum:'',lcFecha:'',cesion:'Sin cesión',cesionContra:'',cesionVig:'',estado:'Vigente',obs:'Reserva de difusión periódica ante INDAUTOR',docs:[],traza:[{ts:pnow(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:puid(),folio:'PUB-2026-003',titulo:'Manual de Amparo (libro institucional)',tipo:'Libro',autores:'Autor institucional',cu:'CUCSH',isbn:'978-607-XXXX-XX-X',issn:'',reservaNum:'',reservaGen:'No aplica',reservaFecha:'',reservaVig:'',ltNum:'',ltFecha:'',lcNum:'',lcFecha:'',cesion:'Cesión de derechos patrimoniales',cesionContra:'Autor → UdeG',cesionVig:'',estado:'Registrado',obs:'',docs:[],traza:[{ts:pnow(),usuario:'Sistema',accion:'Alta (demo)'}]}
]);}
function pubGo(v){PUBV=v;var m={panel:0,lista:1,venc:2};[].forEach.call(document.querySelectorAll('#pubNav button'),function(b,k){b.style.background=(k===m[v])?'#0a4d8c':'#e2e8f0';b.style.color=(k===m[v])?'#fff':'#0a1f3c';b.style.fontWeight=(k===m[v])?'700':'400';});renderPub();}
function renderPub(){pubSeed();if(PUBV==='panel')pubPanel();else if(PUBV==='lista')pubLista();else pubVenc();}
function pubEstReal(x){if(x.estado==='Cancelado')return 'Cancelado';var vigs=[x.reservaVig,x.cesionVig].filter(Boolean);var d=vigs.map(pdr).filter(function(z){return z!==null;});if(d.some(function(z){return z<0;}))return 'Vencido (renovar)';return x.estado;}
function pubPanel(){var A=PUB();
 var isbn=A.filter(function(x){return x.isbn;}).length,issn=A.filter(function(x){return x.issn;}).length;
 var res=A.filter(function(x){return x.reservaNum;}).length,seg=A.filter(function(x){return x.ltNum||x.lcNum;}).length;
 var rtv=A.filter(function(x){return /radio|televis|Difusión/i.test(x.tipo);}).length;
 var ces=A.filter(function(x){return x.cesion&&x.cesion!=='Sin cesión';}).length;
 var venc=A.filter(function(x){return [x.reservaVig,x.cesionVig].filter(Boolean).map(pdr).some(function(d){return d!==null&&d<=90;});}).length;
 function k(n,l,c){return '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:11px;padding:13px"><div style="font-size:22px;font-weight:800;color:'+(c||'#00254a')+'">'+n+'</div><div style="font-size:11px;color:#64748b;margin-top:2px">'+l+'</div></div>';}
 var kp='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px">'+k(A.length,'Publicaciones')+k(isbn,'Con ISBN')+k(issn,'Con ISSN')+k(res,'Con Reserva INDAUTOR','#1f9d6b')+k(seg,'Con licitud (SEGOB)')+k(rtv,'Radio / TV')+k(ces,'Cesiones / licencias')+k(venc,'Por vencer (≤90d)','#c0392b')+'</div>';
 var falta=A.filter(function(x){return /Revista|periódica|Difusión|radio|televis/i.test(x.tipo)&&!x.reservaNum;});
 var al=falta.length?'<div style="background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px">🚨 <b>'+falta.length+' publicación(es) periódica(s)/de radio-TV SIN Reserva de Derechos INDAUTOR.</b></div>':'';
 el('pubBody').innerHTML='<h3 style="margin:0 0 4px;color:#00254a">📊 Panel de publicaciones y editorial</h3><p style="color:#64748b;font-size:12.5px;margin:0 0 12px">Registro de propiedad intelectual editorial: ISBN/ISSN, Reserva de Derechos al Uso Exclusivo (INDAUTOR), certificados de licitud de título y contenido (Comisión Calificadora · SEGOB), cesiones y licencias.</p>'+al+kp+
  '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:14px"><b style="color:#0a4d8c">Publicaciones por tipo</b><canvas id="pubch" height="130"></canvas></div>'+
  '<div style="background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin-top:10px">ℹ️ ISBN = libros · ISSN = publicaciones seriadas · <b>Reserva de Derechos</b> = INDAUTOR (títulos de publicaciones periódicas y difusiones periódicas de radio/TV) · <b>certificados de licitud de título y de contenido</b> = Comisión Calificadora de Publicaciones y Revistas Ilustradas (SEGOB). El trámite en línea ante INDAUTOR/SEGOB es fase backend.</div>';
 try{var t={};A.forEach(function(x){var kk=x.tipo.replace(/ \(.*/,'').replace(/ \/.*/,'');t[kk]=(t[kk]||0)+1;});if(window.__pubch)window.__pubch.destroy();window.__pubch=new Chart(el('pubch'),{type:'bar',data:{labels:Object.keys(t),datasets:[{data:Object.values(t),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
function pubFormHTML(){function f(id,l,ty){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+l+'</label><input id="'+id+'"'+(ty?' type="'+ty+'"':'')+' style="width:100%;padding:7px 9px;border:1px solid #e2e8f0;border-radius:7px;font-size:13px"></div>';}
 function s(id,l,a){return '<div style="margin:0 0 6px"><label style="font-size:11px;color:#64748b;display:block;margin-bottom:2px">'+l+'</label><select id="'+id+'" style="width:100%;padding:7px 9px;border:1px solid #e2e8f0;border-radius:7px;font-size:13px">'+popt(a,'')+'</select></div>';}
 var g='display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px';var h='<div style="font-weight:700;color:#0a4d8c;margin:10px 0 4px;font-size:13px">';
 return h+'📖 Datos de la obra</div><div style="'+g+'">'+f('pf_tit','Título *')+s('pf_tipo','Tipo',PUBTIPO)+f('pf_aut','Autor(es)')+f('pf_cu','CU / dependencia')+'</div>'+
  h+'🔢 ISBN / ISSN</div><div style="'+g+'">'+f('pf_isbn','ISBN (libros)')+f('pf_issn','ISSN (seriadas)')+'</div>'+
  h+'©️ Reserva de Derechos al Uso Exclusivo (INDAUTOR)</div><div style="'+g+'">'+f('pf_rnum','Número de reserva')+s('pf_rgen','Género',PUBGEN)+f('pf_rfec','Fecha','date')+f('pf_rvig','Vigencia','date')+'</div>'+
  h+'🏛️ Certificados de licitud (Comisión Calificadora · SEGOB)</div><div style="'+g+'">'+f('pf_ltn','Licitud de TÍTULO (núm.)')+f('pf_ltf','Fecha título','date')+f('pf_lcn','Licitud de CONTENIDO (núm.)')+f('pf_lcf','Fecha contenido','date')+'</div>'+
  h+'🔁 Cesión / licencia</div><div style="'+g+'">'+s('pf_ces','Tipo',PUBCES)+f('pf_cescontra','Contraparte / editorial')+f('pf_cesvig','Vigencia cesión','date')+s('pf_est','Estado',PUBEST)+'</div>'+
  '<div style="margin-top:8px"><button onclick="pubAdd()" style="border:none;border-radius:8px;padding:9px 14px;background:#1f9d6b;color:#fff;font-weight:700;cursor:pointer">＋ Registrar publicación</button> <span id="pf_msg" style="font-size:12px;color:#1f9d6b"></span></div>';}
function pubLista(){var A=PUB();var q=(pv('pubq')||'').toLowerCase();
 var form='<div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:10px;overflow:hidden"><div onclick="var f=el(\'pubForm\');f.style.display=f.style.display===\'none\'?\'block\':\'none\'" style="background:#f8fafc;padding:10px 13px;font-weight:700;color:#00254a;cursor:pointer;font-size:13px">➕ Registrar publicación — clic para abrir/cerrar</div><div id="pubForm" style="display:none;padding:12px">'+pubFormHTML()+'</div></div>';
 var rows=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:6px 0"><input id="pubq" value="'+pesc(pv('pubq'))+'" placeholder="🔎 Buscar (título, ISBN, ISSN, reserva, autor)…" oninput="renderPub()" style="width:100%;padding:8px;border:1px solid #e2e8f0;border-radius:8px"></div>'+
  '<table style="width:100%;border-collapse:collapse;font-size:12.5px"><tr style="text-align:left;color:#64748b"><th style="padding:6px;border-bottom:2px solid #e2e8f0">Folio</th><th style="border-bottom:2px solid #e2e8f0">Título</th><th style="border-bottom:2px solid #e2e8f0">Tipo</th><th style="border-bottom:2px solid #e2e8f0">ISBN/ISSN</th><th style="border-bottom:2px solid #e2e8f0">Reserva</th><th style="border-bottom:2px solid #e2e8f0">Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var er=pubEstReal(x);var c=/Vigente|Registrado/.test(er)?'#15803d':/Vencido|Cancelado/.test(er)?'#c0392b':'#b45309';return '<tr onclick="pubFicha('+o.i+')" style="cursor:pointer;border-bottom:1px solid #f1f5f9"><td style="padding:6px">'+pesc(x.folio)+'</td><td><b>'+pesc(x.titulo)+'</b></td><td style="font-size:11px">'+pesc(x.tipo)+'</td><td style="font-size:11px">'+pesc(x.isbn||x.issn||'—')+'</td><td style="font-size:11px">'+(x.reservaNum?'<span style="color:#15803d">✓</span> '+pesc(x.reservaNum):'—')+'</td><td style="color:'+c+';font-weight:700">'+pesc(er)+'</td></tr>';}).join(''):'<tr><td colspan="6" style="padding:16px;text-align:center;color:#64748b">Sin publicaciones.</td></tr>')+'</table>';
 el('pubBody').innerHTML='<h3 style="margin:0 0 4px;color:#00254a">📚 Publicaciones</h3><p style="color:#64748b;font-size:12.5px;margin:0 0 10px">Padrón de obras con su registro de propiedad intelectual.</p>'+form+tbl;
}
function pubAdd(){if(!pv('pf_tit')){el('pf_msg').style.color='#c0392b';el('pf_msg').textContent='Indica el título.';return;}
 var A=PUB();var folio='PUB-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 var x={id:puid(),folio:folio,titulo:pv('pf_tit'),tipo:pv('pf_tipo'),autores:pv('pf_aut'),cu:pv('pf_cu'),isbn:pv('pf_isbn'),issn:pv('pf_issn'),reservaNum:pv('pf_rnum'),reservaGen:pv('pf_rgen'),reservaFecha:pv('pf_rfec'),reservaVig:pv('pf_rvig'),ltNum:pv('pf_ltn'),ltFecha:pv('pf_ltf'),lcNum:pv('pf_lcn'),lcFecha:pv('pf_lcf'),cesion:pv('pf_ces'),cesionContra:pv('pf_cescontra'),cesionVig:pv('pf_cesvig'),estado:pv('pf_est'),obs:'',docs:[],traza:[{ts:pnow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Alta de publicación'}]};
 A.push(x);pubSave(A);if(window.__bitlog)__bitlog('Publicaciones y editorial','Alta '+folio+' · '+pv('pf_tit'));
 if(/Revista|periódica|Difusión|radio|televis/i.test(pv('pf_tipo'))&&!pv('pf_rnum'))pnotif('Publicación "'+pv('pf_tit')+'" requiere Reserva de Derechos INDAUTOR',folio);
 el('pf_msg').style.color='#1f9d6b';el('pf_msg').textContent='✓ '+folio+' registrada.';renderPub();}
function pubFicha(i){var A=PUB();var x=A[i];if(!x)return;
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+pesc(d.cat||'Doc')+' · '+pesc(d.nombre)+' <a href="'+d.data+'" download="'+pesc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos (título de reserva, certificados, contrato de cesión).</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+pesc(t.usuario)+' — '+pesc(t.accion)+'</div>';}).join('');
 function box(t,b){return '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6"><b>'+t+'</b><br>'+b+'</div>';}
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+pesc(x.titulo)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+pesc(x.folio)+' · '+pesc(x.tipo)+' · '+pesc(x.cu||'')+' · '+pesc(pubEstReal(x))+'</div>'+
  box('📖 Obra','Autor(es): '+pesc(x.autores||'—'))+
  box('🔢 ISBN / ISSN','ISBN: '+pesc(x.isbn||'—')+' · ISSN: '+pesc(x.issn||'—'))+
  box('©️ Reserva de Derechos (INDAUTOR)','Número: '+pesc(x.reservaNum||'—')+'<br>Género: '+pesc(x.reservaGen||'—')+' · Fecha: '+pesc(x.reservaFecha||'—')+' · Vigencia: '+pesc(x.reservaVig||'—'))+
  box('🏛️ Certificados de licitud (SEGOB · Comisión Calificadora)','Licitud de título: '+pesc(x.ltNum||'—')+(x.ltFecha?' ('+pesc(x.ltFecha)+')':'')+'<br>Licitud de contenido: '+pesc(x.lcNum||'—')+(x.lcFecha?' ('+pesc(x.lcFecha)+')':''))+
  box('🔁 Cesión / licencia','Tipo: '+pesc(x.cesion||'—')+' · Contraparte: '+pesc(x.cesionContra||'—')+' · Vigencia: '+pesc(x.cesionVig||'—'))+
  '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0"><b>🗂️ Expediente</b> <button onclick="pubAdj('+i+')" style="border:none;border-radius:7px;padding:5px 9px;background:#e2e8f0;font-size:11px;cursor:pointer">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:11px;margin:8px 0"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button onclick="pubWord('+i+')" style="border:none;border-radius:7px;padding:7px 12px;background:#d4a32c;color:#3a2c05;font-weight:700;cursor:pointer">📄 Ficha registral (Word)</button> <button onclick="closeDrw()" style="border:none;border-radius:7px;padding:7px 12px;background:#e2e8f0;cursor:pointer">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function pubAdj(i){el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Título de reserva / Certificado de licitud / Contrato de cesión / ISBN-ISSN / Otro):','Título de reserva')||'Documento';var r=new FileReader();r.onload=function(){var A=PUB();A[i].docs=A[i].docs||[];A[i].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:phoy()});A[i].traza.push({ts:pnow(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',accion:'Adjuntó '+cat+': '+f.name});pubSave(A);pubFicha(i);};r.readAsDataURL(f);};el('fileIn').click();}
function pubWord(i){var x=PUB()[i];var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Ficha registral de publicación — '+pesc(x.folio)+'</h3><p><b>Título:</b> '+pesc(x.titulo)+'<br><b>Tipo:</b> '+pesc(x.tipo)+' · <b>Autor(es):</b> '+pesc(x.autores)+' · <b>CU:</b> '+pesc(x.cu)+'</p><p><b>ISBN:</b> '+pesc(x.isbn)+' · <b>ISSN:</b> '+pesc(x.issn)+'</p><p><b>Reserva de Derechos (INDAUTOR):</b> '+pesc(x.reservaNum)+' — género '+pesc(x.reservaGen)+' — vigencia '+pesc(x.reservaVig)+'</p><p><b>Certificado de licitud de título (SEGOB):</b> '+pesc(x.ltNum)+' '+pesc(x.ltFecha)+'<br><b>Certificado de licitud de contenido (SEGOB):</b> '+pesc(x.lcNum)+' '+pesc(x.lcFecha)+'</p><p><b>Cesión/licencia:</b> '+pesc(x.cesion)+' — '+pesc(x.cesionContra)+' — vigencia '+pesc(x.cesionVig)+'</p></body></html>';var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Publicacion_'+x.folio+'.doc';a.click();}
function pubVenc(){var A=PUB();var items=[];
 A.forEach(function(x){if(x.reservaVig){items.push({t:'Reserva INDAUTOR',pub:x.titulo,num:x.reservaNum,vig:x.reservaVig,d:pdr(x.reservaVig)});}if(x.cesionVig){items.push({t:'Cesión/licencia',pub:x.titulo,num:x.cesionContra,vig:x.cesionVig,d:pdr(x.cesionVig)});}});
 items=items.filter(function(z){return z.d!==null&&z.d<=180;}).sort(function(a,b){return a.d-b.d;});
 var tbl='<table style="width:100%;border-collapse:collapse;font-size:12.5px"><tr style="text-align:left;color:#64748b"><th style="padding:6px;border-bottom:2px solid #e2e8f0">Concepto</th><th style="border-bottom:2px solid #e2e8f0">Publicación</th><th style="border-bottom:2px solid #e2e8f0">Referencia</th><th style="border-bottom:2px solid #e2e8f0">Vigencia</th><th style="border-bottom:2px solid #e2e8f0">Días</th></tr>'+
  (items.length?items.map(function(z){var c=z.d<0?'#c0392b':z.d<=90?'#b45309':'#15803d';return '<tr style="border-bottom:1px solid #f1f5f9"><td style="padding:6px">'+pesc(z.t)+'</td><td><b>'+pesc(z.pub)+'</b></td><td style="font-size:11px">'+pesc(z.num||'—')+'</td><td>'+pesc(z.vig)+'</td><td style="color:'+c+';font-weight:700">'+(z.d<0?'vencido '+(-z.d)+'d':z.d+'d')+'</td></tr>';}).join(''):'<tr><td colspan="5" style="padding:16px;text-align:center;color:#64748b">Sin vencimientos próximos (≤180d).</td></tr>')+'</table>';
 el('pubBody').innerHTML='<h3 style="margin:0 0 4px;color:#00254a">⏳ Vencimientos de reservas, licencias y cesiones</h3><p style="color:#64748b;font-size:12.5px;margin:0 0 10px">Las <b>reservas de derechos periódicas (INDAUTOR)</b> y las difusiones de radio/TV se <b>renuevan anualmente</b>. Vigila también las cesiones/licencias.</p>'+tbl;
}
function rb(n){return '<span class="rb rb-'+n+'">'+n+'</span>';}
/* catálogos */
function fill(id,arr,ph){const e=el(id);if(!e)return;e.innerHTML=(ph?'<option value="">'+ph+'</option>':'')+arr.map(x=>'<option>'+x+'</option>').join('');}
fill('i_cat',D.cats.map(c=>c.cat));fill('i_cu',D.cu);fill('i_fuente',D.fuentes);
fill('i_niza',['(no aplica)'].concat(D.niza));fill('i_trl',['(no aplica)'].concat(D.trl.map(t=>t[0]+' — '+t[1])));
fill('fCat',D.cats.map(c=>c.cat),'Toda categoría');fill('fCU',D.cu,'Todo CU');fill('f9cat',D.cats.map(c=>c.cat),'Toda categoría');
function catChange(){const c=D.cats.find(x=>x.cat===val('i_cat'));fill('i_tipo',c?c.tipos:[]);tipoChange();}
function tipoChange(){const t=val('i_tipo');const tr=D.tipo_tramite[t]||'Genérico';fill('i_tramite',Object.keys(D.flujos));el('i_tramite').value=tr;}
catChange();
/* alta */
function saveAsset(){const tipo=val('i_tipo');if(!tipo||!val('i_titulo')){el('i_msg').style.color='#ff9b8d';el('i_msg').textContent='Indica tipo y título.';return;}
 const tram=val('i_tramite');const flujo=(D.flujos[tram]||D.flujos['Genérico']).slice();
 const yr=(val('i_sol')||'2026').slice(0,4);const folio='PI-'+yr+'-'+String(A.length+1).padStart(3,'0');
 const o={folio:folio,cat:val('i_cat'),tipo:tipo,tramite:tram,flujo:flujo,etapaIdx:0,estado:flujo[0],
  titulo:val('i_titulo'),cu:val('i_cu'),dep:val('i_dep'),autor:val('i_autor'),resp:val('i_resp'),fuente:val('i_fuente'),
  niza:(val('i_niza')&&val('i_niza')!=='(no aplica)')?val('i_niza'):'',trl:(val('i_trl')&&val('i_trl')!=='(no aplica)')?val('i_trl'):'',
  sol:val('i_sol'),conc:val('i_conc'),venc:val('i_venc'),renov:0,
  titulares:[{rol:'Titular patrimonial',nombre:'Universidad de Guadalajara',pct:100}],
  contratos:[],licencias:[],regalias:[],observancia:[],evidencias:[],
  versiones:[{v:1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:hoyStr(),nota:'Alta del activo'}],
  bitacora:[{ts:nowStr(),accion:'Alta',usuario:localStorage.getItem('sigej_perfil')||'(perfil)'}]};
 if(val('i_autor'))o.titulares.unshift({rol:'Autor / Inventor',nombre:val('i_autor'),pct:0});
 o.score=scoreOf(o);o.nivel=nivel(o.score);A.push(o);saveA();
 if(window.__bitlog)__bitlog('Acción','Registrar activo '+folio);
 ['i_titulo','i_dep','i_autor','i_resp','i_sol','i_conc','i_venc'].forEach(id=>el(id).value='');
 el('i_msg').style.color='#7ee0b4';el('i_msg').textContent='✓ '+folio+' registrado.';compute();}
/* t1 BI */
function cnt(arr,key){const o={};arr.forEach(e=>{const v=(typeof key==='function'?key(e):e[key])||'(s/d)';o[v]=(o[v]||0)+1;});return o;}
const PAL=['#1aa39a','#0a4d8c','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#16a085','#5d6d7e','#9d174d'];
function chart(id,type,labels,data,opts){if(!window.Chart)return;if(CH[id])CH[id].destroy();const ctx=el(id);if(!ctx)return;
 CH[id]=new Chart(ctx,{type:type,data:{labels:labels,datasets:[{data:data,backgroundColor:opts&&opts.multi?PAL:(opts&&opts.color||'#1aa39a')}]},
  options:{indexAxis:opts&&opts.horiz?'y':'x',plugins:{legend:{display:!!(opts&&opts.legend),position:'right',labels:{color:'#0a4d8c',font:{size:9}}}},
   scales:type==='doughnut'?{}:{x:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}},y:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}}}}});}
function compute(){A.forEach(e=>{e.score=scoreOf(e);e.nivel=nivel(e.score);});saveA();
 const reg=A.reduce((s,e)=>s+(e.regalias||[]).reduce((a,r)=>a+(+r.monto||0),0),0);
 const lic=A.reduce((s,e)=>s+(e.licencias||[]).length,0);
 const vig=A.filter(e=>{const d=dr(e.venc);return d!==null&&d>=0&&d<=180;}).length;
 const K=[['',A.length,'Activos intangibles',''],['',cnt(A,'cat')['Propiedad Industrial']||0,'Propiedad industrial',''],['',(cnt(A,'cat')['Derecho de Autor']||0),'Derecho de autor',''],
  ['',vig,'Vigencias ≤180d','y'],['',lic,'Licencias',''],['',M(reg),'Regalías','g'],['',A.filter(e=>e.nivel==='Crítico'||e.nivel==='Alto').length,'Riesgo alto','r'],['',A.reduce((s,e)=>s+(e.observancia||[]).length,0),'Observancia','y']];
 el('ceKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 const bdef=[[15,'≤ 15 días','b1'],[30,'≤ 30 días','b1'],[60,'≤ 60 días','b2'],[90,'≤ 90 días','b3'],[180,'≤ 180 días','b3']];
 const venc=A.filter(e=>{const d=dr(e.venc);return d!==null&&d<0;}).length;
 el('ceBuckets').innerHTML='<div class="bk b1"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div>'+
  bdef.map(b=>{const n=A.filter(e=>{const d=dr(e.venc);return d!==null&&d>=0&&d<=b[0];}).length;return '<div class="bk '+b[2]+'"><div class="n">'+n+'</div><div class="l">'+b[1]+'</div></div>';}).join('');
 if(A.length){const ca=cnt(A,'cat');chart('cCat','doughnut',Object.keys(ca),Object.values(ca),{multi:true,legend:true});
  const es=cnt(A,'estado');chart('cEst','bar',Object.keys(es),Object.values(es),{horiz:true,color:'#7e57c2'});
  const cu=cnt(A.filter(e=>e.cu),'cu');const ce=Object.entries(cu).sort((a,b)=>b[1]-a[1]);chart('cCU','bar',ce.map(x=>x[0]),ce.map(x=>x[1]),{color:'#0a4d8c'});
  const tp=cnt(A,'tipo');const te=Object.entries(tp).sort((a,b)=>b[1]-a[1]).slice(0,8);chart('cTipo','bar',te.map(x=>x[0].slice(0,14)),te.map(x=>x[1]),{horiz:true,color:'#1aa39a'});
  const rg={};A.forEach(e=>{const t=(e.regalias||[]).reduce((a,r)=>a+(+r.monto||0),0);if(t)rg[e.cu||'(s/d)']=(rg[e.cu||'(s/d)']||0)+t;});chart('cReg','bar',Object.keys(rg),Object.values(rg),{color:'#d4a32c'});
  // mapa innovación
  const cus=Array.from(new Set(A.map(e=>e.cu).filter(Boolean)));
  el('ceMapa').innerHTML='<table><tr><th>Centro Universitario</th><th>Activos</th><th>P. Industrial</th><th>D. Autor</th><th>Software</th><th>Riesgo alto</th></tr>'+
   cus.map(c=>{const m=A.filter(e=>e.cu===c);return '<tr><td>'+c+'</td><td><b>'+m.length+'</b></td><td>'+m.filter(e=>e.cat==='Propiedad Industrial').length+'</td><td>'+m.filter(e=>e.cat==='Derecho de Autor').length+'</td><td>'+m.filter(e=>/Software|App|Algoritmo|Modelo de IA|Plataforma/.test(e.tipo)).length+'</td><td>'+m.filter(e=>e.nivel==='Crítico'||e.nivel==='Alto').length+'</td></tr>';}).join('')+'</table>';
 } else {['cCat','cEst','cCU','cTipo','cReg'].forEach(id=>{if(CH[id])CH[id].destroy();});el('ceMapa').innerHTML='<div class="empty" style="padding:14px">Aún no hay activos. Registra el primero en <b>➕ Alta de activo</b>.</div>';}
 const t=new Date();el('upd').textContent='actualizado '+pad(t.getHours())+':'+pad(t.getMinutes())+':'+pad(t.getSeconds());}
/* t3 lista + ficha */
function renderList(){const q=(val('q')||'').toLowerCase();const fc=val('fCat'),fcu=val('fCU'),fr=val('fRiesgo');
 let arr=A.filter(e=>(!fc||e.cat===fc)&&(!fcu||e.cu===fcu)&&(!fr||e.nivel===fr));
 if(q)arr=arr.filter(e=>(e.folio+' '+e.titulo+' '+e.tipo+' '+(e.autor||'')+' '+(e.dep||'')).toLowerCase().indexOf(q)>=0);
 el('listCnt').textContent=arr.length+' de '+A.length;
 const box=el('lista');
 if(!A.length){box.innerHTML='<div class="empty">📭 Sin activos registrados.<br>Registra el primero en <b>➕ Alta de activo</b>. El módulo arranca vacío para no contener datos no verificados.</div>';return;}
 box.innerHTML=arr.map(e=>{const i=A.indexOf(e);const d=dr(e.venc);
  return '<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><span class="t">'+e.folio+' · '+(e.titulo||e.tipo)+'</span><span>'+rb(e.nivel)+' <span class="chip">'+e.estado+'</span></span></div><div class="m">'+e.cat+' · '+e.tipo+' · '+(e.cu||'—')+(e.autor?' · '+e.autor:'')+(d!==null?' · vence '+(d<0?'hace '+(-d)+'d':'en '+d+'d'):'')+'</div></div>';}).join('')||'<div class="empty" style="padding:14px">Sin coincidencias.</div>';}
function pipe(e){return '<div class="pipe">'+e.flujo.map((s,k)=>'<div class="st '+(k<e.etapaIdx?'done':k===e.etapaIdx?'cur':'')+'">'+s+'</div>').join('')+'</div>';}
function ficha(i){const e=A[i];const d=dr(e.venc);
 const tit=(e.titulares||[]).map((t,k)=>'<tr><td>'+t.rol+'</td><td>'+t.nombre+'</td><td>'+(t.pct||0)+'%</td><td><span class="lk" onclick="delTit('+i+','+k+')">✕</span></td></tr>').join('');
 const lic=(e.licencias||[]).length?'<table><tr><th>Tipo</th><th>Licenciatario</th><th>Territorio</th><th>Regalía</th></tr>'+(e.licencias||[]).map(l=>'<tr><td>'+l.tipo+'</td><td>'+(l.licenciatario||'—')+'</td><td>'+(l.territorio||'—')+'</td><td>'+(l.regalia||'—')+'</td></tr>').join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin licencias.</div>';
 const con=(e.contratos||[]).length?(e.contratos||[]).map(c=>'<div style="font-size:11.5px;color:#475569">📄 '+c.tipo+' · '+(c.contraparte||'')+' · '+(c.fecha||'')+'</div>').join(''):'<div style="color:#64748b;font-size:12px">Sin contratos.</div>';
 const reg=(e.regalias||[]).length?(e.regalias||[]).map(r=>'<div style="font-size:11.5px;color:#475569">💰 '+M(r.monto)+' · '+(r.fecha||'')+(r.inventor?' · '+r.inventor:'')+'</div>').join(''):'<div style="color:#64748b;font-size:12px">Sin regalías.</div>';
 const obs=(e.observancia||[]).length?'<table><tr><th>Tipo</th><th>Autoridad</th><th>Estado</th><th>Fecha</th></tr>'+(e.observancia||[]).map(o=>'<tr><td>'+o.tipo+'</td><td>'+(o.autoridad||'—')+'</td><td>'+(o.estado||'—')+'</td><td>'+(o.fecha||'—')+'</td></tr>').join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin procedimientos.</div>';
 const ev=(e.evidencias||[]).length?(e.evidencias||[]).map(x=>'<div style="font-size:11.5px;color:#475569">📎 '+x.nombre+' · '+x.fecha+' <a class="dl" href="'+x.data+'" download="'+x.nombre+'">descargar</a></div>').join(''):'<div style="color:#64748b;font-size:12px">Sin evidencias.</div>';
 const ver=e.versiones.map(v=>'<div style="font-size:11.5px;color:#475569">v'+v.v+' · '+v.fecha+' · '+v.autor+' — '+v.nota+'</div>').join('');
 const bit=e.bitacora.slice(-6).map(b=>'<div style="font-size:11.5px;color:#475569">'+b.ts+' · '+b.usuario+' — '+b.accion+'</div>').join('');
 const trlIdx=e.trl?(parseInt(e.trl.replace(/[^0-9]/g,''))||0):0;
 const trlBar=e.trl?'<div class="trl" style="margin-top:6px">'+D.trl.map((t,k)=>'<div class="trlb '+(k+1<=trlIdx?'on':'')+'" title="'+t[1]+'">'+(k+1)+'</div>').join('')+'</div>':'';
 el('drwBody').innerHTML='<h2 style="margin:0 0 4px;color:#0a4d8c">'+e.folio+' · '+(e.titulo||e.tipo)+'</h2>'+
  '<div style="margin:4px 0 10px">'+rb(e.nivel)+' <span class="chip">'+e.cat+'</span> <span class="chip">'+e.tipo+'</span> <span class="chip">'+e.estado+'</span>'+(e.niza?' <span class="chip">Niza '+e.niza.split(' ')[0]+'</span>':'')+'</div>'+
  '<div class="comp"><b>Expediente electrónico</b><br>CU: <b>'+(e.cu||'—')+'</b> · Dependencia: '+(e.dep||'—')+'<br>Autor/Inventor: <b>'+(e.autor||'—')+'</b> · Responsable: '+(e.resp||'—')+'<br>Trámite: '+e.tramite+' · Fuente: '+(e.fuente||'—')+'<br>Solicitud: '+(e.sol||'—')+' · Concesión: '+(e.conc||'—')+' · Vencimiento: '+(e.venc||'—')+(d!==null?' ('+(d<0?'vencido hace '+(-d)+'d':'vence en '+d+'d')+')':'')+' · Renovaciones: '+(e.renov||0)+trlBar+'</div>'+
  '<div class="comp"><b>🔄 Flujo del trámite (BPMN)</b>'+pipe(e)+'<div style="margin-top:6px"><button class="bd mini" onclick="retroEtapa('+i+')">← Etapa anterior</button> <button class="b3 mini" onclick="avanzaEtapa('+i+')">Avanzar etapa →</button> '+((e.estado||'').match(/Concesi|Renovaci|Asignaci|Título/)?'<button class="b1 mini" onclick="renovar('+i+')">🔁 Registrar renovación</button>':'')+'</div></div>'+
  '<div class="comp"><b>👥 Titularidad</b> <button class="b3 mini" onclick="addTit('+i+')">＋ Agregar</button><table style="margin-top:6px"><tr><th>Rol</th><th>Nombre</th><th>%</th><th></th></tr>'+(tit||'<tr><td colspan=4 style="color:#64748b">Sin titulares.</td></tr>')+'</table></div>'+
  '<div class="comp"><b>📑 Contratos y licencias</b> <button class="bd mini" onclick="addContrato('+i+')">＋ Contrato</button> <button class="bd mini" onclick="addLicencia('+i+')">＋ Licencia</button><div style="margin-top:6px">'+con+'</div><div style="margin-top:6px">'+lic+'</div></div>'+
  '<div class="comp"><b>💰 Regalías</b> <button class="bd mini" onclick="addRegalia('+i+')">＋ Registrar</button><div style="margin-top:6px">'+reg+'</div></div>'+
  '<div class="comp"><b>🛡️ Observancia y defensa</b> <button class="bd mini" onclick="addObs('+i+')">＋ Procedimiento</button><div style="margin-top:6px">'+obs+'</div></div>'+
  '<div class="comp"><b>📎 Evidencias / soporte</b> <button class="bd mini" onclick="pickFile('+i+')">Subir</button><div style="margin-top:6px">'+ev+'</div></div>'+
  '<div class="comp"><b>🗂️ Versiones</b><div style="margin-top:6px">'+ver+'</div></div>'+
  '<div class="comp"><b>🧾 Bitácora</b><div style="margin-top:6px">'+bit+'</div></div>'+
  '<div class="comp" style="border-left:4px solid #0a4d8c"><b>📝 Seguimiento (notas del equipo)</b><div style="margin-top:4px">'+((e.seguimiento||[]).length?(e.seguimiento||[]).slice().reverse().map(function(s){return '<div style="font-size:11.5px;color:#334155;border-bottom:1px solid #eef2f7;padding:4px 0"><b style="color:#0a4d8c">'+(s.usuario||'')+'</b> <span style="color:#94a3b8;font-size:10px">'+(s.ts||'')+'</span><br>'+String(s.texto||'').replace(/</g,"&lt;")+'</div>';}).join(''):'<span style="color:#94a3b8;font-size:12px">Sin notas.</span>')+'</div><div style="margin-top:6px"><textarea id="pseg_'+i+'" rows="2" placeholder="Nota de seguimiento del activo…" style="width:100%;padding:7px;border:1px solid var(--line);border-radius:8px"></textarea><button class="b3 mini" style="margin-top:5px" onclick="addSegP('+i+')">＋ Agregar nota</button></div></div>'+
  '<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="bw" onclick="fichaWord('+i+')">📄 Ficha (Word)</button><button class="bd" onclick="closeDrw()">Cerrar</button> <button class="bd" style="background:#5a2330" onclick="delAsset('+i+')">🗑 Eliminar</button></div>';
 el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
function addSegP(i){var e=A[i];var el2=document.getElementById('pseg_'+i);var t=el2?el2.value.trim():'';if(!t){alert('Escribe la nota.');return;}e.seguimiento=e.seguimiento||[];e.seguimiento.push({ts:nowStr(),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',texto:t});saveA();ficha(i);}
el('drw').onclick=ev=>{if(ev.target.id==='drw')closeDrw();};
function logIt(e,a){e.bitacora.push({ts:nowStr(),accion:a,usuario:localStorage.getItem('sigej_perfil')||'(perfil)'});}
function logV(e,n){e.versiones.push({v:e.versiones.length+1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:hoyStr(),nota:n});}
function avanzaEtapa(i){const e=A[i];if(e.etapaIdx<e.flujo.length-1){e.etapaIdx++;e.estado=e.flujo[e.etapaIdx];logIt(e,'Avance de trámite → '+e.estado);logV(e,'Etapa: '+e.estado);e.score=scoreOf(e);e.nivel=nivel(e.score);saveA();ficha(i);compute();renderList();}}
function retroEtapa(i){const e=A[i];if(e.etapaIdx>0){e.etapaIdx--;e.estado=e.flujo[e.etapaIdx];logIt(e,'Retroceso de trámite → '+e.estado);saveA();ficha(i);compute();}}
function renovar(i){const e=A[i];const f=prompt('Nueva fecha de vencimiento (AAAA-MM-DD):',e.venc||'');if(!f)return;e.renov=(e.renov||0)+1;e.venc=f;logIt(e,'Renovación #'+e.renov+' · nueva vigencia '+f);logV(e,'Renovación #'+e.renov);e.score=scoreOf(e);e.nivel=nivel(e.score);saveA();ficha(i);compute();}
function addTit(i){const e=A[i];const rol=prompt('Rol ('+D.tit_roles.join(' / ')+'):','Coautor');if(!rol)return;const nombre=prompt('Nombre:','')||'';const pct=+(prompt('% de participación:','0')||0);
 e.titulares.push({rol:rol,nombre:nombre,pct:pct});logIt(e,'Titular: '+rol+' '+nombre);saveA();ficha(i);}
function delTit(i,k){A[i].titulares.splice(k,1);saveA();ficha(i);}
function addContrato(i){const e=A[i];const tipo=prompt('Tipo ('+D.contratos.slice(0,6).join(' / ')+'…):','Licencia no exclusiva');if(!tipo)return;const cp=prompt('Contraparte:','')||'';const fch=prompt('Fecha (AAAA-MM-DD):','')||'';
 e.contratos.push({tipo:tipo,contraparte:cp,fecha:fch});logIt(e,'Contrato: '+tipo);saveA();ficha(i);}
function addLicencia(i){const e=A[i];const tipo=prompt('Licencia (exclusiva/no exclusiva/territorial/Creative Commons…):','Licencia no exclusiva');if(!tipo)return;const lt=prompt('Licenciatario:','')||'';const terr=prompt('Territorio:','Nacional')||'';const reg=prompt('Regalía (% o texto):','')||'';
 e.licencias.push({tipo:tipo,licenciatario:lt,territorio:terr,regalia:reg});logIt(e,'Licencia: '+tipo);saveA();ficha(i);compute();}
function addRegalia(i){const e=A[i];const monto=+(prompt('Monto de regalía (MXN):','0')||0);if(!monto)return;const fch=prompt('Fecha (AAAA-MM-DD):',hoyStr())||hoyStr();const inv=prompt('Inventor/autor beneficiario:','')||'';
 e.regalias.push({monto:monto,fecha:fch,inventor:inv});logIt(e,'Regalía: '+M(monto));saveA();ficha(i);compute();}
function addObs(i){const e=A[i];const tipo=prompt('Procedimiento ('+D.observ.join(' / ')+'):','Oposición');if(!tipo)return;const aut=prompt('Autoridad ('+D.obs_aut.join('/')+'):','IMPI')||'';const est=prompt('Estado:','En trámite')||'';const fch=prompt('Fecha:',hoyStr())||hoyStr();
 e.observancia.push({tipo:tipo,autoridad:aut,estado:est,fecha:fch});logIt(e,'Observancia: '+tipo+' ('+aut+')');saveA();ficha(i);compute();}
function pickFile(i){FILEIDX=i;el('fileIn').value='';el('fileIn').click();}
el('fileIn').onchange=function(){const f=this.files[0];if(!f||FILEIDX===null)return;if(f.size>1.5e6){alert('Máx 1.5 MB.');return;}
 const r=new FileReader();r.onload=()=>{const e=A[FILEIDX];e.evidencias=e.evidencias||[];e.evidencias.push({nombre:f.name,data:r.result,fecha:hoyStr()});logIt(e,'Evidencia: '+f.name);saveA();ficha(FILEIDX);};r.readAsDataURL(f);};
function delAsset(i){if(!confirm('¿Eliminar '+A[i].folio+'?'))return;A.splice(i,1);saveA();closeDrw();compute();renderList();}
function exportCSV(){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const cab=['folio','categoria','tipo','titulo','cu','dependencia','autor','estado','solicitud','vencimiento','renovaciones','nivel','niza','trl'];
 const rows=A.map(e=>[e.folio,e.cat,e.tipo,e.titulo,e.cu,e.dep,e.autor,e.estado,e.sol,e.venc,e.renov,e.nivel,e.niza,e.trl].map(esc).join(','));
 const b=new Blob(['﻿'+cab.join(',')+'\n'+rows.join('\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='patrimonio_intangible.csv';a.click();}
function fichaWord(i){const e=A[i];const tit=(e.titulares||[]).map(t=>t.rol+': '+t.nombre+' ('+(t.pct||0)+'%)').join('; ');
 const body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Unidad de Protección del Patrimonio Intangible</div>'+
  '<h2>FICHA DE ACTIVO INTANGIBLE — '+e.folio+'</h2>'+
  '<p style="font-size:11pt"><b>Título:</b> '+(e.titulo||'')+'<br><b>Categoría / tipo:</b> '+e.cat+' / '+e.tipo+'<br><b>Trámite:</b> '+e.tramite+' · <b>Estado:</b> '+e.estado+'<br><b>Centro Universitario:</b> '+(e.cu||'—')+' · <b>Dependencia:</b> '+(e.dep||'—')+'<br><b>Autor/Inventor:</b> '+(e.autor||'—')+'<br><b>Titularidad:</b> '+tit+'<br><b>Vigencia:</b> solicitud '+(e.sol||'—')+' · concesión '+(e.conc||'—')+' · vencimiento '+(e.venc||'—')+' · renovaciones '+(e.renov||0)+(e.niza?'<br><b>Clase de Niza:</b> '+e.niza:'')+(e.trl?'<br><b>TRL:</b> '+e.trl:'')+'</p>'+
  '<p style="font-size:9pt;color:#666">Documento generado por el SIGEJ-UdeG (prototipo). Fundamento: Art. 220 RIAG-UdeG.</p>';
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Ficha_'+e.folio+'.doc';a.click();}
/* t4 vigencias */
function renderVig(){const bdef=[[180,'≤180d','b3'],[90,'≤90d','b3'],[60,'≤60d','b2'],[30,'≤30d','b1'],[15,'≤15d','b1']];
 const venc=A.filter(e=>{const d=dr(e.venc);return d!==null&&d<0;}).length;
 el('vigBuckets').innerHTML='<div class="bk b1"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div>'+
  bdef.map(b=>{const n=A.filter(e=>{const d=dr(e.venc);return d!==null&&d>=0&&d<=b[0];}).length;return '<div class="bk '+b[2]+'"><div class="n">'+n+'</div><div class="l">'+b[1]+'</div></div>';}).join('');
 const fl=val('fVig');let arr=A.filter(e=>dr(e.venc)!==null);
 if(fl==='venc')arr=arr.filter(e=>dr(e.venc)<0);else if(fl)arr=arr.filter(e=>{const d=dr(e.venc);return d>=0&&d<=+fl;});
 arr.sort((a,b)=>(dr(a.venc))-(dr(b.venc)));
 el('vigLista').innerHTML=arr.length?arr.map(e=>{const i=A.indexOf(e);const d=dr(e.venc);const c=d<0?'#ff9b8d':d<=30?'#ffce82':'#64748b';
  return '<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between"><span class="t">'+e.folio+' · '+(e.titulo||e.tipo)+'</span><span style="color:'+c+';font-weight:700">'+(d<0?'venció hace '+(-d)+'d':'en '+d+'d')+'</span></div><div class="m">'+e.tipo+' · '+(e.cu||'—')+' · renov '+(e.renov||0)+' · '+rb(e.nivel)+'</div></div>';}).join(''):'<div class="empty">Sin vigencias en este rango. Registra fechas de vencimiento en los activos.</div>';}
/* t5 titularidad */
function renderTit(){const rows=[];A.forEach(e=>(e.titulares||[]).forEach(t=>rows.push({folio:e.folio,titulo:e.titulo,i:A.indexOf(e),rol:t.rol,nombre:t.nombre,pct:t.pct})));
 el('titTable').innerHTML=rows.length?'<tr><th>Activo</th><th>Rol</th><th>Titular</th><th>%</th></tr>'+rows.map(r=>'<tr><td><span class="lk" onclick="ficha('+r.i+')">'+r.folio+'</span> · '+(r.titulo||'').slice(0,28)+'</td><td>'+r.rol+'</td><td>'+r.nombre+'</td><td>'+(r.pct||0)+'%</td></tr>').join(''):'<tr><td style="color:#64748b;padding:14px">Sin titulares. La titularidad patrimonial por defecto es la Universidad de Guadalajara.</td></tr>';}
/* t6 transferencia */
function renderTT(){const lic=A.reduce((s,e)=>s+(e.licencias||[]).length,0);const reg=A.reduce((s,e)=>s+(e.regalias||[]).reduce((a,r)=>a+(+r.monto||0),0),0);
 const tech=A.filter(e=>e.trl);const spin=A.filter(e=>e.tipo==='Spin-off').length;
 const K=[['',tech.length,'Con TRL asignado',''],['',lic,'Licencias','g'],['',M(reg),'Regalías acumuladas','g'],['',spin,'Spin-offs','y']];
 el('ttKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 const dist={};D.trl.forEach(t=>dist[t[0]]=0);A.forEach(e=>{if(e.trl){const k='TRL '+(parseInt(e.trl.replace(/[^0-9]/g,''))||0);if(dist[k]!==undefined)dist[k]++;}});
 const mx=Math.max(1,...Object.values(dist));
 el('trlDist').innerHTML=D.trl.map(t=>{const v=dist[t[0]]||0;return '<div style="display:flex;align-items:center;gap:8px;margin:3px 0;font-size:11.5px"><span style="width:46px;color:#0a4d8c">'+t[0]+'</span><span style="flex:1;background:#f1f5fb;border-radius:5px;height:14px;overflow:hidden"><span style="display:block;height:100%;width:'+Math.round(100*v/mx)+'%;background:linear-gradient(90deg,var(--teal),var(--azul2))"></span></span><span style="width:24px;text-align:right">'+v+'</span><span style="color:#64748b;font-size:10px">'+t[1]+'</span></div>';}).join('');
 const rows=[];A.forEach(e=>(e.licencias||[]).forEach(l=>rows.push({folio:e.folio,i:A.indexOf(e),l:l})));
 el('licTable').innerHTML=rows.length?'<tr><th>Activo</th><th>Licencia</th><th>Licenciatario</th><th>Territorio</th><th>Regalía</th></tr>'+rows.map(r=>'<tr><td><span class="lk" onclick="ficha('+r.i+')">'+r.folio+'</span></td><td>'+r.l.tipo+'</td><td>'+(r.l.licenciatario||'—')+'</td><td>'+(r.l.territorio||'—')+'</td><td>'+(r.l.regalia||'—')+'</td></tr>').join(''):'<tr><td style="color:#64748b;padding:14px">Sin licencias registradas. Agrégalas desde la ficha del activo.</td></tr>';}
/* t7 observancia */
function renderObs(){const rows=[];A.forEach(e=>(e.observancia||[]).forEach(o=>rows.push({folio:e.folio,i:A.indexOf(e),o:o})));
 const K=[['',rows.length,'Procedimientos',''],['',rows.filter(r=>/Infracci|Nulidad|Cancelaci/.test(r.o.tipo)).length,'Infracción/nulidad','r'],['',rows.filter(r=>/Oposici/.test(r.o.tipo)).length,'Oposiciones','y'],['',rows.filter(r=>/Litigio|Amparo|Juicio/.test(r.o.tipo)).length,'Litigios','r']];
 el('obKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 el('obTable').innerHTML=rows.length?'<tr><th>Activo</th><th>Procedimiento</th><th>Autoridad</th><th>Estado</th><th>Fecha</th></tr>'+rows.map(r=>'<tr><td><span class="lk" onclick="ficha('+r.i+')">'+r.folio+'</span></td><td>'+r.o.tipo+'</td><td>'+(r.o.autoridad||'—')+'</td><td>'+(r.o.estado||'—')+'</td><td>'+(r.o.fecha||'—')+'</td></tr>').join(''):'<tr><td style="color:#64748b;padding:14px">Sin procedimientos. Registra oposiciones/nulidades/infracciones desde la ficha del activo (Art. 220 fr. IV).</td></tr>';}
/* t8 conocimiento */
function saveKB(){const t=val('k_tit');if(!t){alert('Indica un título.');return;}KB.push({cat:val('k_cat'),tit:t,txt:val('k_txt'),fecha:hoyStr(),autor:localStorage.getItem('sigej_perfil')||'(perfil)'});saveKBs();el('k_tit').value='';el('k_txt').value='';renderKB();}
function renderKB(){el('clasifBox').innerHTML=D.clasif.map(c=>'<div style="padding:6px 2px;border-bottom:1px solid var(--line);font-size:12px"><b style="color:#0a4d8c">'+c[0]+'</b><div style="color:#64748b;font-size:11px">'+c[1]+'</div></div>').join('');
 el('kbList').innerHTML=KB.length?KB.map((k,i)=>'<div class="comp"><div style="display:flex;justify-content:space-between"><b>'+k.tit+'</b><span class="chip">'+k.cat+'</span></div><div style="font-size:12px;color:#c7d6ea;margin-top:5px">'+(k.txt||'—')+'</div><div style="font-size:11px;color:#64748b;margin-top:5px">'+k.fecha+' · '+k.autor+' <span class="lk" onclick="delKB('+i+')">✕</span></div></div>').join(''):'<div class="empty" style="padding:14px">Repositorio vacío. Registra criterios, dictámenes, manuales y tratados.</div>';}
function delKB(i){if(!confirm('¿Eliminar?'))return;KB.splice(i,1);saveKBs();renderKB();}
/* t9 repositorio */
function renderRepo(){const q=(val('q9')||'').toLowerCase();const fc=val('f9cat');
 let arr=A.filter(e=>(!fc||e.cat===fc)&&(!q||(e.folio+' '+e.titulo+' '+e.tipo+' '+(e.autor||'')+' '+(e.dep||'')+' '+(e.cu||'')+' '+(e.niza||'')).toLowerCase().indexOf(q)>=0));
 el('repoList').innerHTML=A.length?(arr.length?arr.map(e=>{const i=A.indexOf(e);return '<div class="it" onclick="ficha('+i+')"><div class="t">'+e.folio+' · '+(e.titulo||e.tipo)+'</div><div class="m">'+e.cat+' · '+e.tipo+' · '+(e.cu||'—')+(e.autor?' · '+e.autor:'')+' · '+e.estado+'</div></div>';}).join(''):'<div class="empty">Sin coincidencias.</div>'):'<div class="empty">Repositorio vacío. Los activos registrados aparecerán aquí para búsqueda histórica.</div>';}
/* t10 marco */
function renderMarco(){el('art220').textContent=D.art220;
 el('vigil').innerHTML=D.vigilancia.map(v=>'<div style="padding:6px 2px;border-bottom:1px solid var(--line);font-size:12px"><a class="dl" href="'+v[2]+'" target="_blank">'+v[0]+'</a> <span style="color:#64748b">· '+v[1]+'</span></div>').join('');}
/* init */
window.addEventListener('storage',()=>{A=JSON.parse(localStorage.getItem('sigej_patrimonio')||'[]');compute();});
window.addEventListener('focus',compute);
compute();
</script>
__SNIP__
</body></html>"""
html=TPL.replace("__DATA__",DATAJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"patrimonio_SIGEJ.html","w",encoding="utf-8").write(html)
print("patrimonio_SIGEJ.html OK -",len(html),"bytes | categorías",len(CATS),"| flujos",len(FLUJOS),"| Niza",len(NIZA),"| CU",len(CU))
