# -*- coding: utf-8 -*-
# Módulo de Instrumentos Jurídicos (CLM) — Legal ERP UdeG / Oficina de la Abogacía General
# Arranca vacío (solo catálogos). Acceso: equipo jurídico. Sin backend (prototipo cliente).
import json
B="/Users/edithroque/Documents/CLAUDE/"
# Padrón real de convenios firmados (Transparencia 2020-2026, corte junio 2026) — 1,122 registros.
CONVJ=open(B+"convenios_transparencia.json",encoding="utf-8").read()

AREAS={
 "OAG":{"nombre":"Oficina de la Abogacía General","fuente":"https://transparencia.udg.mx/contratos_oag","revisor":"Abogado adscrito · OAG","autoridad":"Abogado General"},
 "CGRH":{"nombre":"Coordinación General de Recursos Humanos","fuente":"https://transparencia.udg.mx/contratos_cgrh","revisor":"Jurídico · CGRH","autoridad":"Coordinador General de RH"},
 "CGSAIT":{"nombre":"Coordinación General de Servicios Administrativos e Infraestructura Tecnológica","fuente":"https://transparencia.udg.mx/contratos_administrativa","revisor":"Jurídico · CGSAIT","autoridad":"Coordinador General de SAIT"},
}
FAMILIAS=[
 {"fam":"Convenios","ic":"🤝","area":"OAG","tipos":["General","Específico","Modificatorio","Internacional","Servicio social","Prácticas profesionales","Confidencialidad","Propiedad intelectual","Terminación","Cooperación académica","Investigación","Transferencia tecnológica"]},
 {"fam":"Contratos administrativos","ic":"🏛️","area":"CGSAIT","tipos":["Obra pública","Servicios","Suministro","Concesiones","Arrendamientos","Adquisiciones"]},
 {"fam":"Contratos privados","ic":"📄","area":"OAG","tipos":["Compraventa","Donación","Permuta","Seguros","Bancarios","Licencias","Inversiones","Producción artística","Derechos de autor","Software"]},
 {"fam":"Instrumentos especiales","ic":"⭐","area":"OAG","tipos":["Fideicomiso","Asociación Público-Privada (APP)","Convenio con organismo internacional","Convenio con recursos federales","Convenio con recursos estatales","Convenio con recursos concurrentes","Anexo técnico"]},
 {"fam":"Personal","ic":"👔","area":"CGRH","tipos":["Contrato laboral","Honorarios","Prestación de servicios"]},
]
DEPENDENCIAS=["Rectoría General","Secretaría General","Oficina de la Abogacía General","Contraloría General","Coordinaciones Generales","CUAAD","CUCBA","CUCEA","CUCEI","CUCS","CUCSH","CUValles","CUNorte","CUSur","CUCiénega","CUCosta","CUCSur","CULagos","CUTonalá","SEMS","UDG Virtual","Hospital Civil de Guadalajara","FIL","FICG","Auditorio Telmex","Conjunto Santander","MUSA","Editorial Universitaria","Fundación UdeG","Entidades Productivas","Fideicomisos","Institutos y Centros de Investigación","Organismos vinculados"]
FUENTES=["Recursos propios","Recursos federales","Recursos estatales","Recursos concurrentes","Recursos internacionales","Mixto","No aplica"]
ESTADOS=["Solicitud","Elaboración","Revisión jurídica","Aprobación","Firma","Vigente","Por vencer","Vencido","Terminado","Cancelado"]
OBLIG=["Entregable","Pago","Garantía","Informe","Prórroga","Renovación"]
RIESGOS_CAT=["Jurídico","Financiero","Operativo","Reputacional","Auditoría","Transparencia","Datos personales","Corrupción"]
ROLES=[[90,"Abogado General"],[80,"Secretaría General"],[70,"Directores"],[60,"Coordinador General"],[50,"Coordinadores"],[40,"Jefes"],[30,"Abogados"],[20,"Analistas"],[10,"Asistentes"]]
RACI=[["R","Responsable — ejecuta / elabora"],["A","Aprueba — autoriza el instrumento"],["C","Consultado — opina antes de decidir"],["I","Informado — se le notifica el resultado"]]
CLAUSULAS=[
 {"clave":"CL-OBJ","titulo":"Objeto","fam":"General","riesgo":"Bajo","texto":"El presente instrumento tiene por objeto establecer las bases y mecanismos de colaboración entre LAS PARTES para [describir objeto], conforme a las disposiciones aplicables y al marco normativo de la Universidad de Guadalajara."},
 {"clave":"CL-VIG","titulo":"Vigencia","fam":"General","riesgo":"Medio","texto":"El presente instrumento entrará en vigor a partir de la fecha de su firma y tendrá una vigencia de [periodo], pudiendo prorrogarse por acuerdo escrito de LAS PARTES suscrito con al menos 30 días naturales de anticipación a su vencimiento."},
 {"clave":"CL-CONF","titulo":"Confidencialidad","fam":"Confidencialidad","riesgo":"Alto","texto":"LAS PARTES se obligan a mantener bajo estricta confidencialidad la información intercambiada con motivo del presente instrumento, y a no divulgarla a terceros sin consentimiento previo y por escrito, obligación que subsistirá por [periodo] posterior a su terminación."},
 {"clave":"CL-PI","titulo":"Propiedad intelectual","fam":"Propiedad intelectual","riesgo":"Alto","texto":"La titularidad de los derechos de propiedad intelectual que se generen se regirá por la Ley Federal del Derecho de Autor y la Ley Federal de Protección a la Propiedad Industrial; los derechos morales corresponderán a los autores y los patrimoniales se distribuirán conforme a la participación de LAS PARTES, reconociendo en todo caso la participación de la Universidad de Guadalajara."},
 {"clave":"CL-DP","titulo":"Protección de datos personales","fam":"Datos personales","riesgo":"Alto","texto":"El tratamiento de datos personales se sujetará a la Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados y a la normativa estatal y universitaria aplicable, limitándose a las finalidades del presente instrumento."},
 {"clave":"CL-NOLAB","titulo":"No relación laboral","fam":"General","riesgo":"Alto","texto":"LAS PARTES reconocen que el personal que cada una designe para el cumplimiento del presente instrumento mantendrá su relación laboral exclusivamente con quien lo contrató, sin que se genere relación laboral alguna respecto de la otra parte ni responsabilidad solidaria o sustituta."},
 {"clave":"CL-TERM","titulo":"Terminación anticipada","fam":"Terminación","riesgo":"Medio","texto":"Cualquiera de LAS PARTES podrá dar por terminado anticipadamente el presente instrumento mediante aviso por escrito con [días] de anticipación, sin perjuicio de concluir las actividades en curso y de cubrir las obligaciones devengadas."},
 {"clave":"CL-CASO","titulo":"Caso fortuito o fuerza mayor","fam":"General","riesgo":"Bajo","texto":"Ninguna de LAS PARTES será responsable por el incumplimiento de las obligaciones derivado de caso fortuito o fuerza mayor, debiendo notificarlo a la otra parte dentro de los [días] siguientes a que ocurra."},
 {"clave":"CL-GAR","titulo":"Garantías","fam":"Obra pública","riesgo":"Alto","texto":"EL CONTRATISTA otorgará garantía de cumplimiento por el [%] del monto total y, en su caso, garantía de vicios ocultos por el [%], mediante fianza expedida por institución autorizada a favor de la Universidad de Guadalajara."},
 {"clave":"CL-ANTI","titulo":"Anticorrupción y conflicto de interés","fam":"General","riesgo":"Alto","texto":"LAS PARTES manifiestan que se conducirán con integridad, absteniéndose de prácticas indebidas en términos de la Ley General de Responsabilidades Administrativas, y declaran no encontrarse en supuesto de conflicto de interés."},
 {"clave":"CL-JUR","titulo":"Jurisdicción y competencia","fam":"General","riesgo":"Medio","texto":"Para la interpretación y cumplimiento del presente instrumento, LAS PARTES se someten a la jurisdicción de los tribunales competentes en la Zona Metropolitana de Guadalajara, Jalisco, renunciando a cualquier otro fuero que pudiera corresponderles."},
 {"clave":"CL-TRANS","titulo":"Transparencia","fam":"Transparencia","riesgo":"Medio","texto":"LAS PARTES reconocen que el presente instrumento es información pública en términos de la legislación de transparencia, por lo que podrá publicarse en versión pública previo testado de datos personales y de información reservada o confidencial."},
]
# Plantillas de flujo BPMN por familia: [paso, R, A, C, I, SLA(días), fase->estado del ciclo]
FLUJOS={
 "Convenios":[
  ["Solicitud","Dependencia solicitante","Jefa de Unidad","—","OAG",3,"Solicitud"],
  ["Asignación y elaboración","Abogado","Jefa de Unidad","Dependencia solicitante","—",7,"Elaboración"],
  ["Revisión jurídica","Abogado","Coordinador Jurídico","—","Dependencia solicitante",5,"Revisión jurídica"],
  ["Visto bueno superior","Coordinador Jurídico","Abogado General","—","—",4,"Aprobación"],
  ["Firma","Abogado General","Abogado General","Contraparte","Dependencia solicitante",10,"Firma"],
  ["Resguardo y vigencia","Auxiliar jurídico","Jefa de Unidad","—","Dependencia solicitante",2,"Vigente"]],
 "Contratos administrativos":[
  ["Solicitud","Dependencia solicitante","Jefa de Unidad","—","CGSAIT",3,"Solicitud"],
  ["Validación técnica","Responsable técnico","Jefa de Unidad","—","—",5,"Elaboración"],
  ["Suficiencia presupuestal","Responsable financiero","Coordinador General de SAIT","—","Contraloría General",5,"Elaboración"],
  ["Elaboración del contrato","Abogado","Jefa de Unidad","—","—",7,"Elaboración"],
  ["Revisión jurídica","Abogado","Coordinador Jurídico","OAG","—",5,"Revisión jurídica"],
  ["Aprobación","Coordinador Jurídico","Coordinador General de SAIT","—","—",4,"Aprobación"],
  ["Firma","Coordinador General de SAIT","Coordinador General de SAIT","Contraparte","Dependencia solicitante",10,"Firma"],
  ["Resguardo y vigencia","Analista","Jefa de Unidad","—","—",2,"Vigente"]],
 "Contratos privados":[
  ["Solicitud","Dependencia solicitante","Jefa de Unidad","—","OAG",3,"Solicitud"],
  ["Elaboración","Abogado","Jefa de Unidad","Dependencia solicitante","—",6,"Elaboración"],
  ["Revisión jurídica","Abogado","Coordinador Jurídico","—","—",5,"Revisión jurídica"],
  ["Aprobación","Coordinador Jurídico","Abogado General","—","—",4,"Aprobación"],
  ["Firma","Abogado General","Abogado General","Contraparte","Dependencia solicitante",8,"Firma"],
  ["Resguardo y vigencia","Auxiliar jurídico","Jefa de Unidad","—","—",2,"Vigente"]],
 "Instrumentos especiales":[
  ["Solicitud","Dependencia solicitante","Jefa de Unidad","—","OAG",3,"Solicitud"],
  ["Dictamen jurídico","Abogado","Coordinador Jurídico","—","—",7,"Elaboración"],
  ["Análisis de riesgo y financiero","Responsable financiero","Coordinador General de SAIT","OAG","Contraloría General",7,"Elaboración"],
  ["Revisión jurídica integral","Coordinador Jurídico","Abogado General","—","—",6,"Revisión jurídica"],
  ["Autorización superior","Abogado General","Secretaría General","—","—",6,"Aprobación"],
  ["Firma","Abogado General","Secretaría General","Contraparte","—",12,"Firma"],
  ["Resguardo y vigencia","Auxiliar jurídico","Jefa de Unidad","—","Dependencia solicitante",3,"Vigente"]],
 "Personal":[
  ["Solicitud","Dependencia solicitante","Jefa de Unidad","—","CGRH",3,"Solicitud"],
  ["Validación de RH","Analista","Jefa de Unidad","—","—",4,"Elaboración"],
  ["Elaboración","Abogado","Jefa de Unidad","—","—",5,"Elaboración"],
  ["Revisión jurídica","Abogado","Coordinador Jurídico","—","—",4,"Revisión jurídica"],
  ["Aprobación","Coordinador Jurídico","Coordinador General de RH","—","—",3,"Aprobación"],
  ["Firma","Coordinador General de RH","Coordinador General de RH","Trabajador","—",5,"Firma"],
  ["Alta y vigencia","Analista","Jefa de Unidad","—","—",2,"Vigente"]],
}
DATA={"corte":"2026-06-18","areas":AREAS,"familias":FAMILIAS,"dependencias":DEPENDENCIAS,
 "fuentes":FUENTES,"estados":ESTADOS,"oblig":OBLIG,"riesgos_cat":RIESGOS_CAT,"roles":ROLES,"raci":RACI,"clausulas":CLAUSULAS,"flujos":FLUJOS}
DATAJ=json.dumps(DATA,ensure_ascii=False)
json.dump(DATA,open(B+"instrumentos_catalogos.json","w",encoding="utf-8"),ensure_ascii=False)

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html" class="act">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''

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
<title>SIGEJ-UdeG · Instrumentos Jurídicos (CLM)</title>
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
.tb{background:var(--card);color:#475569;border:1px solid var(--line);border-bottom:none;border-radius:11px 11px 0 0;padding:10px 15px;font-size:12.5px;font-weight:600;cursor:pointer}
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
.pipe{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px}
.pstep{flex:0 0 auto;min-width:120px;background:var(--card2);border:1px solid var(--line);border-radius:10px;padding:10px 12px;text-align:center}
.pstep .pn{font-size:20px;font-weight:800}.pstep .pl{font-size:10.5px;color:var(--mut)}
.buckets{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:9px}
.bk{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px;text-align:center}
.bk .n{font-size:21px;font-weight:800}.bk .l{font-size:10.5px;color:var(--mut)}
.bk.b1 .n{color:#c0392b}.bk.b2 .n{color:#ea580c}.bk.b3 .n{color:#e08e0b}
table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:7px 8px;text-align:left;border-bottom:1px solid var(--line)}th{color:var(--mut)}
.rb{font-size:10px;padding:2px 8px;border-radius:9px;font-weight:600}
.rb-Crítico{background:rgba(192,57,43,.25);color:#ff9b8d}.rb-Alto{background:rgba(234,88,12,.22);color:#ffb38f}.rb-Medio{background:rgba(224,142,11,.2);color:#ffce82}.rb-Bajo{background:rgba(31,157,107,.2);color:#8fe0d8}.rb-Indeterminado{background:rgba(143,166,196,.18);color:var(--mut)}
.f{display:inline-flex;flex-direction:column;gap:3px;margin:0 8px 9px 0}.f label{font-size:11px;color:var(--mut);font-weight:600}
.f input,.f select,.f textarea{padding:7px 8px;border:1px solid var(--line);border-radius:6px;font-size:12.5px;background:#f1f5fb;color:var(--ink);min-width:150px}
.f textarea{min-width:320px;min-height:48px}
button{padding:8px 13px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
.b1{background:var(--azul2)}.b3{background:var(--ok)}.bw{background:#2b579a}.bd{background:#33507a}.mini{padding:4px 9px;font-size:11px}
.comp{background:#f1f5fb;border:1px solid var(--line);border-radius:10px;padding:12px;margin:6px 0;font-size:12px}
.comp b{color:#0a4d8c}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px}.bar input,.bar select{padding:6px 8px;border:1px solid var(--line);border-radius:6px;font-size:12px;background:#f1f5fb;color:var(--ink)}
.it{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:12px;margin-bottom:9px;cursor:pointer}
.it:hover{border-color:var(--teal)}.it .t{font-weight:700;color:#0a4d8c;font-size:13px}.it .m{font-size:11px;color:var(--mut);margin-top:3px}
.heat{width:100%;border-collapse:collapse;font-size:11.5px}.heat td,.heat th{padding:6px;text-align:center;border:2px solid var(--bg)}.heat th{color:var(--mut)}.heat td.lab{text-align:left;color:#0a4d8c}
.cl{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:13px;margin-bottom:10px}
.cl .clt{font-weight:700;color:#0a4d8c;font-size:13px}.cl .clx{font-size:12px;color:#c7d6ea;margin-top:6px;line-height:1.5}
.drawer{position:fixed;inset:0;background:rgba(4,12,24,.72);display:none;align-items:center;justify-content:center;z-index:9000;padding:18px}
.drawer.on{display:flex}.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;max-width:900px;width:100%;max-height:88vh;overflow:auto;padding:20px}
.panel .x{float:right;cursor:pointer;color:var(--mut);font-size:20px}
.warn{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:9px;padding:9px 12px;font-size:11.5px;color:#e8cf95;margin:8px 0}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:26px;text-align:center;color:var(--mut);font-size:13px}
.chip{display:inline-block;background:#f1f5fb;border:1px solid var(--line);border-radius:9px;padding:2px 8px;font-size:10.5px;color:#475569;margin:2px}
.bpmn{display:flex;align-items:stretch;gap:4px;overflow-x:auto;padding:8px 0}
.bpmn-arr{align-self:center;color:#5d6d7e;font-size:18px}
.bpmn-node{flex:0 0 auto;min-width:132px;max-width:152px;background:var(--card2);border:2px solid #33507a;border-radius:10px;padding:8px;font-size:11px}
.bn-st{display:inline-block;color:#fff;border-radius:8px;padding:1px 7px;font-size:9.5px;font-weight:700;margin-bottom:4px}
.bn-p{font-weight:700;color:#0a4d8c;font-size:11.5px;line-height:1.2}
.bn-r{color:#64748b;margin-top:3px}.bn-sla{color:#64748b;margin-top:2px;font-size:10px}
.gantt{position:relative;margin-top:8px}
.grow{display:flex;align-items:center;min-height:24px}
.glab{width:160px;flex:0 0 160px;font-size:11px;color:#0a4d8c;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding-right:8px}
.gtrack{position:relative;flex:1;height:14px;background:#f1f5fb;border-radius:5px}
.g-plan{position:absolute;top:2px;height:10px;background:#33507a;border-radius:4px;opacity:.85}
.g-real{position:absolute;top:2px;height:10px;border-radius:4px}
.gaxis{display:flex;justify-content:space-between;margin-left:160px;border-top:1px solid var(--line);font-size:9.5px;color:#64748b;padding-top:3px}
.gtoday{position:absolute;top:0;bottom:16px;border-left:2px dashed #d4a32c;z-index:2}
.gleg{display:inline-block;width:10px;height:10px;border-radius:2px;vertical-align:middle;margin-right:3px}
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
<header><div><h1>📜 SIGEJ-UdeG · Instrumentos Jurídicos — Legal ERP / Contract Lifecycle Management</h1>
<div class="s">Oficina de la Abogacía General · UdeG — convenios, contratos e instrumentos especiales · ciclo de vida, riesgos, obligaciones y alertas</div></div>
<div style="text-align:right"><span class="live"><span class="dot"></span>En vivo · <span id="upd"></span></span> <button class="b1 mini" onclick="compute()">↻ Actualizar</button></div></header>
__NAV__
<div class="tabbar">
 <button class="tb on" data-t="t1" onclick="tab('t1')">🛰️ Centro de Mando</button>
 <button class="tb" data-t="t2" onclick="tab('t2')">➕ Alta / Captura</button>
 <button class="tb" data-t="t3" onclick="tab('t3')">📁 Instrumentos</button>
 <button class="tb" data-t="t10" onclick="tab('t10')">🔀 Flujos y aprobaciones</button>
 <button class="tb" data-t="t4" onclick="tab('t4')">⚠️ Riesgos</button>
 <button class="tb" data-t="t5" onclick="tab('t5')">📋 Obligaciones</button>
 <button class="tb" data-t="t6" onclick="tab('t6')">🔔 Alertas</button>
 <button class="tb" data-t="t7" onclick="tab('t7')">📚 Cláusuloteca</button>
 <button class="tb" data-t="t8" onclick="tab('t8')">🧠 Conocimiento</button>
 <button class="tb" data-t="t11" onclick="tab('t11')">🌐 Portal dependencias/contrapartes</button>
</div>
<div class="wrap">
 <section id="t1" class="tab on">
  <div class="kpis" id="ceKpis"></div>
  <div class="h">🔄 Ciclo de vida (pipeline CLM)</div><div class="pipe" id="cePipe"></div>
  <div class="h">⏳ Instrumentos por vencer</div><div class="buckets" id="ceBuckets"></div>
  <div class="grid" style="margin-top:14px">
   <div class="card"><h3>Por familia</h3><canvas id="cFam"></canvas></div>
   <div class="card"><h3>Por área responsable</h3><canvas id="cArea"></canvas></div>
   <div class="card"><h3>Por estado del ciclo</h3><canvas id="cEst"></canvas></div>
   <div class="card"><h3>Monto administrado por área (MXN)</h3><canvas id="cMonto"></canvas></div>
   <div class="card s2"><h3>Top dependencias solicitantes</h3><canvas id="cDep"></canvas></div>
   <div class="card s2"><h3>Contrapartes recurrentes</h3><div id="ceContra"></div></div>
  </div>
 </section>

 <section id="t2" class="tab">
  <div class="card" style="border-left:4px solid #7a5a1f">
   <h3>🗄️ Conclusión masiva por año (para archivo)</h3>
   <div style="font-size:12px;color:#64748b;margin:2px 0 8px">Marca como <b>terminados</b> los instrumentos <b>activos</b> de un año (conclusión interna al 31-dic), para que entren al ciclo de archivo (concentración → baja). Útil para el padrón de convenios de Transparencia. La conclusión queda en la bitácora.</div>
   <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:end">
    <div class="f" style="max-width:150px"><label>Año</label><select id="bc_year"><option value="">— elige —</option><option>2020</option><option>2021</option><option>2022</option><option>2023</option><option>2024</option><option>2025</option><option>2026</option></select></div>
    <div class="f" style="max-width:220px"><label><input type="checkbox" id="bc_conv" checked style="width:auto;vertical-align:middle"> Solo familia «Convenios»</label></div>
    <button class="b3" style="background:#7a5a1f" onclick="bulkConcluir()">Marcar como terminados</button> <span id="bc_msg" style="font-size:12px;color:#7a5a1f"></span>
   </div>
  </div>
  <div class="card">
   <h3>Alta de instrumento jurídico · área responsable automática</h3>
   <div class="f"><label>Familia</label><select id="i_fam" onchange="famChange()"></select></div>
   <div class="f"><label>Tipo</label><select id="i_tipo" onchange="liveRisk()"></select></div>
   <div class="f"><label>Dependencia solicitante</label><input id="i_dep" list="l_dep"><datalist id="l_dep"></datalist></div>
   <div class="f"><label>Contraparte</label><input id="i_contra"></div>
   <div class="f" style="display:flex"><label>Objeto</label><textarea id="i_obj"></textarea></div>
   <div class="f"><label>Monto (MXN)</label><input id="i_monto" type="number" min="0" oninput="liveRisk()"></div>
   <div class="f"><label>Fuente de financiamiento</label><select id="i_fuente" onchange="liveRisk()"></select></div>
   <div class="f"><label>Fecha de firma</label><input id="i_firma" type="date"></div>
   <div class="f"><label>Inicio de vigencia</label><input id="i_ini" type="date"></div>
   <div class="f"><label>Fin de vigencia</label><input id="i_fin" type="date" oninput="liveRisk()"></div>
   <div class="f"><label>Estado del ciclo</label><select id="i_estado"></select></div>
   <div class="f"><label>Abogado responsable</label><input id="i_resp"></div>
   <div class="f" style="grid-column:1/-1"><div style="font-size:11px;font-weight:700;color:#0a4d8c;border-top:1px solid var(--line);padding-top:6px">🗄️ Expediente y archivo (Ley General de Archivos)</div></div>
   <div class="f"><label>Fecha de apertura del expediente</label><input id="i_fap" type="date"></div>
   <div class="f"><label>Oficio de apertura del expediente</label><input id="i_oficio"></div>
   <div class="f"><label>Oficio del área que envía</label><input id="i_ofarea"></div>
   <div class="f"><label>No. de expediente interno</label><input id="i_exp"></div>
   <div class="f"><label>No. de expediente de Rectoría</label><input id="i_rect"></div>
   <div class="f"><label>No. de conclusión interna</label><input id="i_ncon"></div>
   <div class="f"><label>Fecha de conclusión interna</label><input id="i_fcon" type="date"></div>
   <div class="f"><label>Etiqueta archivo muerto</label><input id="i_etiq"></div>
   <div class="comp" id="compBox"></div>
   <div style="margin-top:6px"><button class="b3" onclick="saveInstr()">＋ Registrar instrumento</button>
   <span id="i_msg" style="font-size:12px;color:#7ee0b4;margin-left:10px"></span></div>
  </div>
  <div class="warn">⚠️ Captura local del navegador (prototipo). <b>Firma electrónica</b> (e.firma SAT / Firma UDG / DocuSign / Adobe Sign), <b>IA jurídica</b> (borradores, detección de cláusulas faltantes), <b>OCR</b>, <b>portales de dependencias/contrapartes</b> y <b>publicación en la PNT</b> son fase de implementación con backend.</div>
 </section>

 <section id="t3" class="tab">
  <div class="bar">
   <input id="q" placeholder="Buscar (folio, objeto, contraparte, dependencia)…" oninput="renderList()" style="min-width:240px">
   <select id="fEstado" onchange="renderList()"><option value="">Todo estado</option></select>
   <select id="fArea" onchange="renderList()"><option value="">Toda área</option></select>
   <select id="fRiesgo" onchange="renderList()"><option value="">Todo riesgo</option><option>Crítico</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
   <button class="bd mini" onclick="exportCSV()">⬇ CSV</button>
   <span id="listCnt" style="font-size:12px;color:#64748b"></span>
  </div>
  <div id="lista"></div>
 </section>

 <section id="t10" class="tab">
  <div class="kpis" id="flKpis"></div>
  <div class="h">✅ Mis aprobaciones pendientes</div><div id="flApr"></div>
  <div class="h">📨 Mis solicitudes</div><div id="flSol"></div>
  <div class="h">⏱️ SLA vencidos / escalamientos</div><div id="flSla"></div>
  <div class="warn">Las etapas, la matriz <b>RACI</b> y los <b>SLA</b> provienen de plantillas BPMN por familia de instrumento. La aprobación cambia el estado del ciclo y queda en la bitácora y el control de versiones. Las <b>notificaciones automáticas</b> a los aprobadores (correo/app/push) son fase backend.</div>
 </section>

 <section id="t4" class="tab">
  <div class="h">🗺️ Matriz de riesgos institucional — instrumentos por categoría × nivel</div>
  <div class="card"><table class="heat" id="riskHeat"></table>
   <div style="font-size:11px;color:#64748b;margin-top:8px">El nivel se deriva de un <b>score proxy explicable</b> (monto, tipo de instrumento, fuente de financiamiento y vigencia). La categoría aplica a todo el instrumento.</div></div>
  <div class="h">Instrumentos por nivel de riesgo</div><div id="riskList"></div>
 </section>

 <section id="t5" class="tab">
  <div class="kpis" id="obKpis"></div>
  <div class="bar"><select id="fOb" onchange="renderOblig()"><option value="">Toda obligación</option></select>
   <select id="fObEst" onchange="renderOblig()"><option value="">Todo estatus</option><option>Pendiente</option><option>Cumplida</option><option>Vencida</option></select></div>
  <div class="card"><table id="obTable"></table></div>
 </section>

 <section id="t6" class="tab">
  <div class="h">⏰ Motor de alertas — vencimientos de instrumentos y obligaciones</div>
  <div class="buckets" id="alBuckets"></div>
  <div class="h">Detalle priorizado</div>
  <div class="bar"><select id="fAl" onchange="renderAlertas()"><option value="">Todo</option><option value="90">≤ 90 días</option><option value="60">≤ 60 días</option><option value="30">≤ 30 días</option><option value="15">≤ 15 días</option><option value="7">≤ 7 días</option><option value="1">≤ 24 h</option><option value="venc">Vencidos</option></select></div>
  <div id="alLista"></div>
  <div class="warn">⚠️ Notificaciones automáticas (correo/app/push a 90/60/30/15/7 días/24 h) = fase backend. Aquí se calculan y priorizan en pantalla.</div>
 </section>

 <section id="t7" class="tab">
  <div class="bar"><input id="qcl" placeholder="Buscar cláusula…" oninput="renderClaus()" style="min-width:240px">
   <select id="fclr" onchange="renderClaus()"><option value="">Todo riesgo</option><option>Alto</option><option>Medio</option><option>Bajo</option></select>
   <span style="font-size:11.5px;color:#64748b">Biblioteca de cláusulas modelo aprobadas — base institucional curada (a validar por la OAG).</span></div>
  <div id="clausList"></div>
 </section>

 <section id="t8" class="tab">
  <div class="card"><h3>Centro de Conocimiento — memoria jurídica institucional</h3>
   <div class="f"><label>Categoría</label><select id="k_cat"><option>Dictamen</option><option>Opinión jurídica</option><option>Plantilla</option><option>Convenio modelo</option><option>Criterio institucional</option><option>Precedente</option><option>Manual</option><option>Jurisprudencia</option></select></div>
   <div class="f"><label>Título</label><input id="k_tit" style="min-width:260px"></div>
   <div class="f" style="display:flex"><label>Contenido / referencia</label><textarea id="k_txt"></textarea></div>
   <div><button class="b3" onclick="saveKB()">＋ Registrar en el repositorio</button></div>
  </div>
  <div class="bar" style="margin-top:12px"><input id="qkb" placeholder="Buscar conocimiento…" oninput="renderKB()" style="min-width:240px">
   <select id="fkb" onchange="renderKB()"><option value="">Toda categoría</option></select></div>
  <div id="kbList"></div>
 </section>

 <section id="t11" class="tab">
  <div class="warn">🌐 <b>Portal de Dependencias y Contrapartes</b> integrado: las dependencias solicitan instrumentos y dan seguimiento; las contrapartes consultan estado, suben documentos y firman electrónicamente. Comparte el mismo expediente (sigej_instrumentos) que este módulo.</div>
  <iframe id="portalFrame" data-src="portal_SIGEJ.html?embed=1" title="Portal de Dependencias y Contrapartes" style="width:100%;height:82vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe>
 </section>
</div>

<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const HOY=new Date(2026,5,18);let CH={};
let INSTR=JSON.parse(localStorage.getItem('sigej_instrumentos')||'[]');
/* Siembra ÚNICA del padrón de convenios firmados (Transparencia 2020-2026). No borra capturas: solo agrega folios ausentes. */
const CONV_SEED=__CONVSEED__;
(function(){try{if(localStorage.getItem('sigej_instr_convseed2'))return;var byF={};INSTR.forEach(function(e){byF[e.folio]=e;});var ch=0;CONV_SEED.forEach(function(e){var ex=byF[e.folio];if(!ex){INSTR.push(e);ch++;}else if(!ex.fApertura&&e.fApertura){ex.fApertura=e.fApertura;if(!ex.expInterno&&e.expInterno)ex.expInterno=e.expInterno;ch++;}});if(ch)localStorage.setItem('sigej_instrumentos',JSON.stringify(INSTR));localStorage.setItem('sigej_instr_convseed2','1');}catch(e){}})();
let KB=JSON.parse(localStorage.getItem('sigej_instr_kb')||'[]');
function saveAll(){localStorage.setItem('sigej_instrumentos',JSON.stringify(INSTR));}
function saveKBs(){localStorage.setItem('sigej_instr_kb',JSON.stringify(KB));}
function pad(n){return (n<10?'0':'')+n;}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-HOY)/864e5);}
function areaOf(fam){const f=D.familias.find(x=>x.fam===fam);return f?f.area:'OAG';}
function nivel(s){return s>70?'Crítico':s>=50?'Alto':s>=28?'Medio':s>0?'Bajo':'Indeterminado';}
function scoreOf(o){let s=0;const m=+o.monto||0;
 s+= m>50e6?40:m>10e6?34:m>1e6?26:m>1e5?16:m>0?8:0;
 const hi=['Obra pública','Asociación Público-Privada (APP)','Fideicomiso','Concesiones','Bancarios','Inversiones','Transferencia tecnológica','Convenio con recursos federales','Convenio con recursos concurrentes','Convenio con organismo internacional'];
 const md=['Servicios','Suministro','Adquisiciones','Arrendamientos','Compraventa','Licencias','Software','Propiedad intelectual','Investigación','Seguros','Derechos de autor','Convenio con recursos estatales'];
 s+= hi.indexOf(o.tipo)>=0?20:md.indexOf(o.tipo)>=0?10:4;
 const fu={'Recursos federales':12,'Recursos concurrentes':12,'Recursos internacionales':10,'Recursos estatales':8,'Mixto':8,'Recursos propios':2,'No aplica':0};
 s+= fu[o.fuente]||0;
 const d=dr(o.fin); if(d!==null){ if(d<0)s+=18; else if(d<=30)s+=12; else if(d<=90)s+=6; }
 return Math.min(100,Math.round(s));
}
function tab(id){document.querySelectorAll('.tab').forEach(s=>s.classList.toggle('on',s.id===id));
 document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 if(id==='t1')setTimeout(compute,20);if(id==='t3')renderList();if(id==='t4')renderRisk();if(id==='t5')renderOblig();if(id==='t6')renderAlertas();if(id==='t7')renderClaus();if(id==='t8')renderKB();if(id==='t10')renderFlujos();if(id==='t11'){var pf=document.getElementById('portalFrame');if(pf&&!pf.src)pf.src=pf.dataset.src;}}
function activo(e){return ['Solicitud','Elaboración','Revisión jurídica','Aprobación','Firma','Vigente','Por vencer'].indexOf(e.estado)>=0;}
/* --- Archivística · Ley General de Archivos (DOF 15/06/2018): trámite → concentración → histórico/baja. Plazos SUGERIDOS; los oficiales los fija el CADIDO de la UdeG. --- */
var ARCH={tramite:2,concentracion:5};
function iAddYears(f,n){if(!f)return '';var d=new Date(f+'T00:00:00');if(isNaN(d))return '';d.setFullYear(d.getFullYear()+n);return d.toISOString().slice(0,10);}
function iConcluido(e){return /Terminado|Cancelado/.test(e.estado||'')||(!!e.fin&&new Date(e.fin+'T00:00:00')<HOY&&['Vigente','Por vencer'].indexOf(e.estado)<0);}
function iArchivo(e){var vivo=!iConcluido(e);var base=e.fConclusion||e.fin||'';var fT=vivo?'':iAddYears(base,ARCH.tramite);var fB=fT?iAddYears(fT,ARCH.concentracion):'';var h=hoyStr();var fase;
 if(vivo)fase='Archivo de trámite';else if(fT&&h>=fB)fase='Baja documental / histórico';else if(fT&&h>=fT)fase='Archivo de concentración';else fase='Trámite (por transferir)';return {fase:fase,fT:fT,fB:fB,base:base};}
function iArchColor(f){return /Baja/.test(f)?'#c0392b':/concentración/i.test(f)?'#b45309':/por transferir/i.test(f)?'#0a4d8c':'#15803d';}
function iMovs(e){var m=(e.movimientos||[]).slice();if(!m.length&&(e.oficioAp||e.fApertura))m.push({fecha:e.fApertura||'',oficio:e.oficioAp||'',area:e.oficioArea||'OAG',desc:'Apertura de expediente'});return m;}
function addMovI(i){var e=INSTR[i];var g=function(id){var el=document.getElementById(id);return el?el.value.trim():'';};var f=g('imv_f_'+i),o=g('imv_o_'+i),a=g('imv_a_'+i),ds=g('imv_d_'+i);
 if(!o&&!ds){alert('Indica al menos el número de oficio o la descripción.');return;}e.movimientos=e.movimientos||[];e.movimientos.push({fecha:f||hoyStr(),oficio:o,area:a,desc:ds});logIt(e,'Movimiento de oficio: '+(o||'s/n')+' '+(ds||''));saveAll();ficha(i);}
function setConclI(i){var e=INSTR[i];var el=document.getElementById('ifcon_'+i);var f=el?el.value:'';if(!f){alert('Indica la fecha de conclusión interna.');return;}e.fConclusion=f;if(!/Cancelado/.test(e.estado))e.estado='Terminado';logIt(e,'Conclusión interna registrada ('+f+')');e.score=scoreOf(e);e.nivel=nivel(e.score);saveAll();ficha(i);}
/* ---------- catálogos en selects ---------- */
function fill(id,arr,ph){const el=document.getElementById(id);if(!el)return;el.innerHTML=(ph?'<option value="">'+ph+'</option>':'')+arr.map(x=>'<option>'+x+'</option>').join('');}
fill('i_fam',D.familias.map(f=>f.fam));fill('i_fuente',D.fuentes);fill('i_estado',D.estados);
fill('fEstado',D.estados,'Todo estado');fill('fArea',Object.keys(D.areas),'Toda área');fill('fOb',D.oblig,'Toda obligación');fill('fkb',['Dictamen','Opinión jurídica','Plantilla','Convenio modelo','Criterio institucional','Precedente','Manual','Jurisprudencia'],'Toda categoría');
document.getElementById('l_dep').innerHTML=D.dependencias.map(x=>'<option>'+x+'</option>').join('');
function famChange(){const fam=document.getElementById('i_fam').value;const f=D.familias.find(x=>x.fam===fam);fill('i_tipo',f?f.tipos:[]);liveRisk();}
famChange();
/* ---------- captura: matriz de competencias + riesgo en vivo ---------- */
let OBL=[];
function liveRisk(){const fam=document.getElementById('i_fam').value;const ac=areaOf(fam);const a=D.areas[ac];
 const o={tipo:document.getElementById('i_tipo').value,monto:document.getElementById('i_monto').value,fuente:document.getElementById('i_fuente').value,fin:document.getElementById('i_fin').value};
 const sc=scoreOf(o);const nv=nivel(sc);
 document.getElementById('compBox').innerHTML='<b>⚖️ Área responsable (automática)</b><br>Área responsable: <b>'+a.nombre+'</b> ('+ac+')<br>Revisor jurídico: <b>'+a.revisor+'</b> · Autoridad autorizadora: <b>'+a.autoridad+'</b><br>Fuente de transparencia: <a href="'+a.fuente+'" target="_blank" style="color:#7ee0b4">'+a.fuente+'</a><br><span style="margin-top:6px;display:inline-block">Riesgo estimado: <span class="rb rb-'+nv+'">'+nv+' · '+sc+'/100</span> <span style="color:#64748b;font-size:11px">(proxy explicable)</span></span>';
}
function obRow(){return '<div class="f"><label>Tipo</label><select class="ob_t">'+D.oblig.map(x=>'<option>'+x+'</option>').join('')+'</select></div>';}
function saveInstr(){const fam=document.getElementById('i_fam').value;const tipo=document.getElementById('i_tipo').value;
 const dep=document.getElementById('i_dep').value.trim();
 if(!tipo||!dep){document.getElementById('i_msg').textContent='Indica al menos tipo y dependencia.';document.getElementById('i_msg').style.color='#ff9b8d';return;}
 const ac=areaOf(fam);const yr=(document.getElementById('i_firma').value||'2026').slice(0,4);
 const folio='INSTR-'+yr+'-'+String(INSTR.length+1).padStart(3,'0');
 const o={folio:folio,fam:fam,tipo:tipo,area:ac,dep:dep,contra:document.getElementById('i_contra').value.trim(),
  obj:document.getElementById('i_obj').value.trim(),monto:+document.getElementById('i_monto').value||0,
  fuente:document.getElementById('i_fuente').value,firma:document.getElementById('i_firma').value,ini:document.getElementById('i_ini').value,
  fin:document.getElementById('i_fin').value,estado:document.getElementById('i_estado').value||'Solicitud',
  resp:document.getElementById('i_resp').value.trim(),oblig:[],
  fApertura:document.getElementById('i_fap').value,oficioAp:document.getElementById('i_oficio').value.trim(),oficioArea:document.getElementById('i_ofarea').value.trim(),
  expInterno:document.getElementById('i_exp').value.trim(),expRectoria:document.getElementById('i_rect').value.trim(),
  numConclusion:document.getElementById('i_ncon').value.trim(),fConclusion:document.getElementById('i_fcon').value,etiqueta:document.getElementById('i_etiq').value.trim(),
  movimientos:(document.getElementById('i_oficio').value.trim()||document.getElementById('i_fap').value)?[{fecha:document.getElementById('i_fap').value||new Date().toISOString().slice(0,10),oficio:document.getElementById('i_oficio').value.trim(),area:document.getElementById('i_ofarea').value.trim()||'OAG',desc:'Apertura de expediente'}]:[],
  versiones:[{v:1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:new Date().toISOString().slice(0,10),nota:'Alta del instrumento'}],
  bitacora:[{ts:new Date().toISOString().slice(0,19).replace('T',' '),accion:'Alta',usuario:localStorage.getItem('sigej_perfil')||'(perfil)'}]};
 o.score=scoreOf(o);o.nivel=nivel(o.score);
 seedFlujo(o,document.getElementById('i_estado').value);
 INSTR.push(o);saveAll();
 if(window.__bitlog)__bitlog('Acción','Registrar instrumento '+folio);
 ['i_contra','i_obj','i_monto','i_resp','i_firma','i_ini','i_fin'].forEach(id=>document.getElementById(id).value='');
 const m=document.getElementById('i_msg');m.style.color='#7ee0b4';m.textContent='✓ '+folio+' registrado.';compute();
}
/* ---------- t1 Centro de Mando ---------- */
function cnt(arr,key){const o={};arr.forEach(e=>{const v=(typeof key==='function'?key(e):e[key])||'(s/d)';o[v]=(o[v]||0)+1;});return o;}
function chart(id,type,labels,data,opts){if(!window.Chart)return;if(CH[id])CH[id].destroy();const ctx=document.getElementById(id);if(!ctx)return;
 CH[id]=new Chart(ctx,{type:type,data:{labels:labels,datasets:[{data:data,backgroundColor:opts&&opts.multi?PAL:(opts&&opts.color||'#1aa39a')}]},
  options:{indexAxis:opts&&opts.horiz?'y':'x',plugins:{legend:{display:!!(opts&&opts.legend),position:'right',labels:{color:'#0a4d8c',font:{size:9}}}},
   scales:type==='doughnut'?{}:{x:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}},y:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}}}}});}
const PAL=['#1aa39a','#0a4d8c','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#16a085','#5d6d7e','#9d174d'];
function compute(){INSTR.forEach(e=>{e.score=scoreOf(e);e.nivel=nivel(e.score);});saveAll();
 const act=INSTR.filter(activo);const crit=INSTR.filter(e=>e.nivel==='Crítico'||e.nivel==='Alto').length;
 const monto=INSTR.reduce((s,e)=>s+(+e.monto||0),0);
 const porVen=INSTR.filter(e=>{const d=dr(e.fin);return activo(e)&&d!==null&&d>=0&&d<=90;}).length;
 const obTot=INSTR.reduce((s,e)=>s+(e.oblig?e.oblig.length:0),0);
 const K=[['',INSTR.length,'Instrumentos',''],['',act.length,'Activos','g'],['',crit,'Críticos/Alto','r'],['',porVen,'Por vencer ≤90d','y'],
  ['',M(monto),'Monto administrado','y'],['',obTot,'Obligaciones',''],['',new Set(INSTR.map(e=>e.contra).filter(Boolean)).size,'Contrapartes',''],['',new Set(INSTR.map(e=>e.dep).filter(Boolean)).size,'Dependencias','']];
 document.getElementById('ceKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 // pipeline
 document.getElementById('cePipe').innerHTML=D.estados.map(s=>{const n=INSTR.filter(e=>e.estado===s).length;return '<div class="pstep"><div class="pn">'+n+'</div><div class="pl">'+s+'</div></div>';}).join('');
 // buckets
 const bdef=[[7,'≤ 7 días','b1'],[15,'≤ 15 días','b1'],[30,'≤ 30 días','b2'],[60,'≤ 60 días','b3'],[90,'≤ 90 días','b3']];
 const venc=INSTR.filter(e=>activo(e)&&dr(e.fin)!==null&&dr(e.fin)<0).length;
 document.getElementById('ceBuckets').innerHTML='<div class="bk b1"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div>'+
  bdef.map(b=>{const n=INSTR.filter(e=>{const d=dr(e.fin);return activo(e)&&d!==null&&d>=0&&d<=b[0];}).length;return '<div class="bk '+b[2]+'"><div class="n">'+n+'</div><div class="l">'+b[1]+'</div></div>';}).join('');
 // charts
 if(INSTR.length){const fam=cnt(INSTR,'fam');chart('cFam','doughnut',Object.keys(fam),Object.values(fam),{multi:true,legend:true});
  const ar=cnt(INSTR,'area');chart('cArea','bar',Object.keys(ar),Object.values(ar),{color:'#0a4d8c'});
  const es=cnt(INSTR,'estado');chart('cEst','bar',Object.keys(es),Object.values(es),{horiz:true,color:'#7e57c2'});
  const mo={};INSTR.forEach(e=>mo[e.area]=(mo[e.area]||0)+(+e.monto||0));chart('cMonto','bar',Object.keys(mo),Object.values(mo),{color:'#d4a32c'});
  const dep=cnt(INSTR.filter(e=>e.dep),'dep');const de=Object.entries(dep).sort((a,b)=>b[1]-a[1]).slice(0,10);chart('cDep','bar',de.map(x=>x[0]),de.map(x=>x[1]),{horiz:true,color:'#c0392b'});
  const co=cnt(INSTR.filter(e=>e.contra),'contra');const ce=Object.entries(co).sort((a,b)=>b[1]-a[1]).slice(0,8);
  document.getElementById('ceContra').innerHTML=ce.length?ce.map(x=>'<div style="display:flex;justify-content:space-between;padding:6px 2px;border-bottom:1px solid var(--line);font-size:12px"><span>'+x[0]+'</span><b>'+x[1]+'</b></div>').join(''):'<div style="color:#64748b;font-size:12px">Sin contrapartes capturadas.</div>';
 } else {['cFam','cArea','cEst','cMonto','cDep'].forEach(id=>{if(CH[id])CH[id].destroy();});document.getElementById('ceContra').innerHTML='<div class="empty" style="padding:14px">Aún no hay instrumentos. Captura el primero en <b>➕ Alta / Captura</b>.</div>';}
 const t=new Date();document.getElementById('upd').textContent='actualizado '+pad(t.getHours())+':'+pad(t.getMinutes())+':'+pad(t.getSeconds());
}
/* ---------- t3 lista + ficha ---------- */
function rb(n){return '<span class="rb rb-'+n+'">'+n+'</span>';}
function renderList(){const q=(document.getElementById('q').value||'').toLowerCase();const fe=document.getElementById('fEstado').value,fa=document.getElementById('fArea').value,fr=document.getElementById('fRiesgo').value;
 let arr=INSTR.filter(e=>(!fe||e.estado===fe)&&(!fa||e.area===fa)&&(!fr||e.nivel===fr));
 if(q)arr=arr.filter(e=>(e.folio+' '+e.tipo+' '+(e.obj||'')+' '+(e.contra||'')+' '+(e.dep||'')).toLowerCase().indexOf(q)>=0);
 document.getElementById('listCnt').textContent=arr.length+' de '+INSTR.length;
 const box=document.getElementById('lista');
 if(!INSTR.length){box.innerHTML='<div class="empty">📭 Sin instrumentos registrados.<br>Captura el primero en la pestaña <b>➕ Alta / Captura</b>. El módulo arranca vacío para no contener datos no verificados.</div>';return;}
 box.innerHTML=arr.map((e,i)=>{const d=dr(e.fin);const dl=d===null?'':(d<0?'venció hace '+(-d)+'d':'en '+d+'d');const idx=INSTR.indexOf(e);
  return '<div class="it" onclick="ficha('+idx+')"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><span class="t">'+e.folio+' · '+e.tipo+'</span><span>'+rb(e.nivel)+' <span class="chip">'+e.estado+'</span></span></div><div class="m">'+e.fam+' · '+e.area+' · '+(e.dep||'—')+(e.contra?' · '+e.contra:'')+' · '+M(e.monto)+(dl?' · ⏳ '+dl:'')+'</div></div>';}).join('')||'<div class="empty" style="padding:14px">Sin coincidencias.</div>';
}
function ficha(i){const e=INSTR[i];ensureFlujo(e);if(curStep(e)&&curStep(e).fase==='Firma'){ensureFirma(e);if(e.firmaCfg&&e.firmaCfg.firmantes.every(x=>x.estado==='Firmado'))checkFirmaComplete(e);}const a=D.areas[e.area];const d=dr(e.fin);
 const obl=(e.oblig&&e.oblig.length)?'<table><tr><th>Tipo</th><th>Descripción</th><th>Fecha</th><th>Monto</th><th>Estatus</th></tr>'+e.oblig.map((o,k)=>'<tr><td>'+o.tipo+'</td><td>'+(o.desc||'—')+'</td><td>'+(o.fecha||'—')+'</td><td>'+(o.monto?M(o.monto):'—')+'</td><td>'+(o.estado||'Pendiente')+'</td></tr>').join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin obligaciones registradas.</div>';
 const ver=e.versiones.map(v=>'<div style="font-size:11.5px;color:#475569">v'+v.v+' · '+v.fecha+' · '+v.autor+' — '+v.nota+'</div>').join('');
 const bit=e.bitacora.slice(-8).map(b=>'<div style="font-size:11.5px;color:#475569">'+b.ts+' · '+b.usuario+' — '+b.accion+'</div>').join('');
 document.getElementById('drwBody').innerHTML='<h2 style="margin:0 0 4px;color:#0a4d8c">'+e.folio+' · '+e.tipo+'</h2>'+
  '<div style="margin:4px 0 10px">'+rb(e.nivel)+' <span class="chip">'+e.estado+'</span> <span class="chip">'+e.fam+'</span> <span class="chip">'+e.area+'</span></div>'+
  '<div class="comp"><b>Datos generales</b><br>Objeto: '+(e.obj||'—')+'<br>Dependencia solicitante: <b>'+(e.dep||'—')+'</b> · Contraparte: <b>'+(e.contra||'—')+'</b><br>Monto: <b>'+M(e.monto)+'</b> · Fuente: '+(e.fuente||'—')+'<br>Firma: '+(e.firma||'—')+' · Vigencia: '+(e.ini||'—')+' → '+(e.fin||'—')+(d!==null?' ('+(d<0?'vencido hace '+(-d)+'d':'vence en '+d+'d')+')':'')+'<br>Responsable: '+(e.resp||'—')+'</div>'+
  '<div class="comp"><b>⚖️ Área responsable</b><br>Área: <b>'+a.nombre+'</b> · Revisor: '+a.revisor+' · Autoridad: '+a.autoridad+'</div>'+
  (function(){var ar=iArchivo(e);return '<div class="comp" style="border-left:4px solid '+iArchColor(ar.fase)+'"><b>🗄️ Expediente y archivo</b> <span class="chip" style="background:'+iArchColor(ar.fase)+'22;color:'+iArchColor(ar.fase)+'">'+ar.fase+'</span>'+
   '<br>Fecha de apertura del expediente: <b>'+(e.fApertura||'—')+'</b> · Oficio de apertura: <b>'+(e.oficioAp||'—')+'</b>'+
   '<br>Oficio del área que envía: <b>'+(e.oficioArea||'—')+'</b>'+
   '<br>No. de expediente interno: <b>'+(e.expInterno||'—')+'</b> · No. de expediente de Rectoría: <b>'+(e.expRectoria||'—')+'</b>'+
   '<br>Conclusión interna: No. <b>'+(e.numConclusion||'—')+'</b> · '+(e.fConclusion||'—')+
   '<br>Transferencia a concentración: <b>'+(ar.fT||'—')+'</b> · Fecha de baja: <b>'+(ar.fB||'—')+'</b> · Etiqueta archivo muerto: <b>'+(e.etiqueta||'—')+'</b>'+
   '<div style="margin-top:6px;display:flex;gap:6px;flex-wrap:wrap;align-items:center"><input id="ifcon_'+i+'" type="date" value="'+(e.fConclusion||'')+'" style="width:auto;padding:5px;border:1px solid var(--line);border-radius:6px"><button class="b3 mini" onclick="setConclI('+i+')">Registrar conclusión interna</button></div>'+
   '<div style="font-size:10.5px;color:#94a3b8;margin-top:5px">Plazos sugeridos (Ley General de Archivos): '+ARCH.tramite+' años en trámite tras la conclusión → concentración; '+ARCH.concentracion+' años en concentración → baja. Los oficiales los fija el CADIDO de la UdeG.</div></div>'+
   '<div class="comp"><b>📨 Historial de oficios (movimientos)</b><div style="margin-top:4px">'+(iMovs(e).length?iMovs(e).map(function(m){return '<div style="font-size:11.5px;color:#475569;border-bottom:1px solid #eef2f7;padding:3px 0">'+(m.fecha||'—')+' · <b>'+(m.oficio||'s/n')+'</b> · '+(m.area||'')+' — '+(m.desc||'')+'</div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin movimientos.</span>')+
   '<div style="margin-top:6px;display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:4px"><input id="imv_f_'+i+'" type="date" style="padding:5px;border:1px solid var(--line);border-radius:6px"><input id="imv_o_'+i+'" placeholder="No. de oficio" style="padding:5px;border:1px solid var(--line);border-radius:6px"><input id="imv_a_'+i+'" placeholder="Área que envía" style="padding:5px;border:1px solid var(--line);border-radius:6px"><input id="imv_d_'+i+'" placeholder="Descripción" style="padding:5px;border:1px solid var(--line);border-radius:6px"></div><div style="margin-top:5px"><button class="b3 mini" onclick="addMovI('+i+')">＋ Agregar movimiento</button></div></div>';})()+
  '<div class="comp"><b>📋 Obligaciones</b> <button class="b3 mini" onclick="addOblig('+i+')">＋ Agregar</button><div style="margin-top:8px">'+obl+'</div></div>'+
  bpmnPanel(i)+ganttFlujo(i)+
  '<div class="comp"><b>🗂️ Versiones</b><div style="margin-top:6px">'+ver+'</div></div>'+
  '<div class="comp" style="border-left:4px solid #0a4d8c"><b>📝 Seguimiento (notas del equipo)</b><div style="margin-top:4px">'+((e.seguimiento||[]).length?(e.seguimiento||[]).slice().reverse().map(function(s){return '<div style="font-size:11.5px;color:#334155;border-bottom:1px solid #eef2f7;padding:4px 0"><b style="color:#0a4d8c">'+(s.usuario||'')+'</b> <span style="color:#94a3b8;font-size:10px">'+(s.ts||'')+'</span><br>'+String(s.texto||'').replace(/</g,"&lt;")+'</div>';}).join(''):'<span style="color:#94a3b8;font-size:12px">Sin notas.</span>')+'</div><div style="margin-top:6px"><textarea id="iseg_'+i+'" rows="2" placeholder="Escribe una nota de seguimiento del instrumento…" style="width:100%;padding:7px;border:1px solid var(--line);border-radius:8px"></textarea><button class="b3 mini" style="margin-top:5px" onclick="addSegI('+i+')">＋ Agregar nota</button></div></div>'+
  '<div class="comp"><b>🧾 Bitácora / trazabilidad</b><div style="margin-top:6px">'+bit+'</div></div>'+
  '<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="bw" onclick="fichaWord('+i+')">📄 Ficha (Word)</button><button class="bw mini" onclick="docExp('+i+')">📎 Expediente electrónico</button> <button class="bd" onclick="closeDrw()">Cerrar</button> <button class="bd" style="background:#5a2330" onclick="delInstr('+i+')">🚫 Anular</button></div>'+(INSTR[i].anulado?'<div style="margin-top:8px;background:#fdeaea;border:1px solid #e7a0a0;color:#c0392b;border-radius:8px;padding:7px 10px;font-size:11.5px">⛔ <b>Instrumento anulado</b> — '+ec(INSTR[i].anulado.por||'')+' · '+ec(INSTR[i].anulado.ts||'')+' — '+ec(INSTR[i].anulado.motivo||'')+'</div>':'');
 document.getElementById('drw').classList.add('on');
}
function closeDrw(){document.getElementById('drw').classList.remove('on');}
document.getElementById('drw').onclick=e=>{if(e.target.id==='drw')closeDrw();};
function logIt(e,accion){e.bitacora.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),accion:accion,usuario:localStorage.getItem('sigej_perfil')||'(perfil)'});}
function bulkConcluir(){var y=document.getElementById('bc_year').value;var soloConv=document.getElementById('bc_conv').checked;var m=document.getElementById('bc_msg');
 if(!y){if(m){m.style.color='#c0392b';m.textContent='Elige un año.';}return;}
 var activos=['Solicitud','Elaboración','Revisión jurídica','Aprobación','Firma','Vigente','Por vencer'];
 function yrOf(e){var s=(e.fApertura||e.firma||e.ini||'').slice(0,4);if(/^\d{4}$/.test(s))return s;var mm=(e.folio||'').match(/-(20\d\d)-/);return mm?mm[1]:'';}
 var cand=INSTR.filter(function(e){return yrOf(e)===y&&activos.indexOf(e.estado)>=0&&(!soloConv||e.fam==='Convenios');});
 if(!cand.length){if(m){m.style.color='#b45309';m.textContent='No hay instrumentos activos del '+y+(soloConv?' (Convenios).':'.');}return;}
 if(!confirm('Se marcarán '+cand.length+' instrumento(s) del año '+y+' como TERMINADOS (conclusión interna '+y+'-12-31), para que entren al ciclo de archivo (concentración/baja). Esta acción asume que ya concluyeron. ¿Continuar?'))return;
 var f=y+'-12-31';cand.forEach(function(e){e.estado='Terminado';e.fConclusion=f;e.score=scoreOf(e);e.nivel=nivel(e.score);logIt(e,'Conclusión masiva por año ('+y+') → Terminado');});
 saveAll();compute();try{renderList();}catch(e){}
 if(m){m.style.color='#1f9d6b';m.textContent='✓ '+cand.length+' del '+y+' marcados como terminados.';}}
function setEstado(i,s){const e=INSTR[i];e.estado=s;logIt(e,'Cambio de estado → '+s);e.versiones.push({v:e.versiones.length+1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:new Date().toISOString().slice(0,10),nota:'Estado: '+s});e.score=scoreOf(e);e.nivel=nivel(e.score);saveAll();ficha(i);compute();renderList();}
function addOblig(i){const e=INSTR[i];const tipo=prompt('Tipo de obligación ('+D.oblig.join(' / ')+'):','Entregable');if(!tipo)return;const desc=prompt('Descripción:','')||'';const fecha=prompt('Fecha de vencimiento (AAAA-MM-DD):','')||'';const monto=+(prompt('Monto (opcional):','0')||0);
 e.oblig.push({tipo:tipo,desc:desc,fecha:fecha,monto:monto,estado:'Pendiente'});logIt(e,'Alta de obligación: '+tipo);saveAll();ficha(i);compute();}
function delInstr(i){var r=INSTR[i];if(!r)return;if(r.anulado){alert('Este instrumento ya está anulado. La información no se elimina.');return;}
 var m=prompt('Motivo de ANULACIÓN de '+r.folio+'.\nLa información NO se elimina: el instrumento queda anulado, con sello y en la bitácora de auditoría.','');if(m===null||!m.trim())return;
 var pf=localStorage.getItem('sigej_perfil')||'(perfil)';var ts=new Date().toISOString().slice(0,16).replace('T',' ');
 r.anulado={motivo:m.trim(),por:pf,ts:ts};
 if(Array.isArray(r.traza))r.traza.push({ts:ts,usuario:pf,accion:'Anulación: '+m.trim()});
 if(Array.isArray(r.estHist))r.estHist.push({est:'Anulado',ts:ts,usuario:pf});
 saveAll();if(window.__bitlog)__bitlog('Acción','Anula instrumento '+r.folio+' — '+m.trim());closeDrw();compute();renderList();
 alert('🚫 Instrumento '+r.folio+' anulado. El registro se conserva (no se elimina).');}
function addSegI(i){var e=INSTR[i];var el=document.getElementById('iseg_'+i);var t=el?el.value.trim():'';if(!t){alert('Escribe la nota.');return;}e.seguimiento=e.seguimiento||[];e.seguimiento.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),usuario:localStorage.getItem('sigej_perfil')||'(perfil)',texto:t});saveAll();ficha(i);}
function exportCSV(){const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const cab=['folio','familia','tipo','area','dependencia','contraparte','monto','fuente','firma','inicio','fin','estado','nivel','score','responsable'];
 const rows=INSTR.map(e=>[e.folio,e.fam,e.tipo,e.area,e.dep,e.contra,e.monto,e.fuente,e.firma,e.ini,e.fin,e.estado,e.nivel,e.score,e.resp].map(esc).join(','));
 const csv=cab.join(',')+'\n'+rows.join('\n');const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='instrumentos_SIGEJ.csv';a.click();}
function fichaWord(i){const e=INSTR[i];const a=D.areas[e.area];
 const body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Sistema de Instrumentos Jurídicos</div>'+
  '<h2>FICHA DE INSTRUMENTO — '+e.folio+'</h2>'+
  '<p style="font-size:11pt"><b>Familia / tipo:</b> '+e.fam+' / '+e.tipo+'<br><b>Área responsable:</b> '+a.nombre+'<br><b>Revisor:</b> '+a.revisor+' · <b>Autoridad:</b> '+a.autoridad+'<br><b>Dependencia solicitante:</b> '+(e.dep||'—')+'<br><b>Contraparte:</b> '+(e.contra||'—')+'<br><b>Objeto:</b> '+(e.obj||'—')+'<br><b>Monto:</b> '+M(e.monto)+' · <b>Fuente:</b> '+(e.fuente||'—')+'<br><b>Firma:</b> '+(e.firma||'—')+' · <b>Vigencia:</b> '+(e.ini||'—')+' a '+(e.fin||'—')+'<br><b>Estado:</b> '+e.estado+' · <b>Riesgo (proxy):</b> '+e.nivel+' ('+e.score+'/100)<br><b>Responsable:</b> '+(e.resp||'—')+'</p>'+
  '<p style="font-size:9pt;color:#666">Documento generado por el SIGEJ-UdeG (prototipo). El score de riesgo es un proxy explicable, no una valoración jurídica definitiva.</p>';
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a2=document.createElement('a');a2.href=URL.createObjectURL(b);a2.download='Ficha_'+e.folio+'.doc';a2.click();}
/* ---------- t4 riesgos ---------- */
function renderRisk(){const niv=['Crítico','Alto','Medio','Bajo'];const cats=D.riesgos_cat;
 let mx=1;const cell={};cats.forEach(c=>{cell[c]={};niv.forEach(n=>{const v=INSTR.filter(e=>e.nivel===n).length;cell[c][n]=v;});});
 // matriz: filas categorías de riesgo (todas aplican), columnas nivel agregado del instrumento
 const tot={};niv.forEach(n=>{tot[n]=INSTR.filter(e=>e.nivel===n).length;mx=Math.max(mx,tot[n]);});
 document.getElementById('riskHeat').innerHTML='<tr><th class="lab">Categoría de riesgo \\ Nivel</th>'+niv.map(n=>'<th>'+n+'</th>').join('')+'</tr>'+
  cats.map(c=>'<tr><td class="lab">'+c+'</td>'+niv.map(n=>{const v=tot[n];const al=v/mx;const col=n==='Crítico'?'192,57,43':n==='Alto'?'234,88,12':n==='Medio'?'224,142,11':'31,157,107';return '<td style="background:rgba('+col+','+(0.12+al*0.7)+');color:#fff">'+v+'</td>';}).join('')+'</tr>').join('');
 const box=document.getElementById('riskList');
 if(!INSTR.length){box.innerHTML='<div class="empty">Sin instrumentos para evaluar riesgo.</div>';return;}
 const ord=INSTR.map((e,i)=>[e,i]).sort((a,b)=>b[0].score-a[0].score);
 box.innerHTML=ord.map(([e,i])=>'<div class="it" onclick="ficha('+i+')"><div style="display:flex;justify-content:space-between"><span class="t">'+e.folio+' · '+e.tipo+'</span><span>'+rb(e.nivel)+' '+e.score+'/100</span></div><div class="m">'+e.area+' · '+(e.dep||'—')+' · '+M(e.monto)+' · '+(e.fuente||'—')+'</div></div>').join('');
}
/* ---------- t5 obligaciones ---------- */
function allOblig(){const r=[];INSTR.forEach((e,i)=>(e.oblig||[]).forEach(o=>r.push(Object.assign({folio:e.folio,idx:i},o))));return r;}
function renderOblig(){const arr=allOblig();const ft=document.getElementById('fOb').value,fe=document.getElementById('fObEst').value;
 const pend=arr.filter(o=>o.estado!=='Cumplida').length;const venc=arr.filter(o=>{const d=dr(o.fecha);return o.estado!=='Cumplida'&&d!==null&&d<0;}).length;
 const K=[['',arr.length,'Obligaciones',''],['',pend,'Pendientes','y'],['',venc,'Vencidas','r'],['',M(arr.reduce((s,o)=>s+(+o.monto||0),0)),'Monto en obligaciones','']];
 document.getElementById('obKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 let f=arr.filter(o=>(!ft||o.tipo===ft)&&(!fe||(o.estado||'Pendiente')===fe));
 document.getElementById('obTable').innerHTML=f.length?'<tr><th>Instrumento</th><th>Tipo</th><th>Descripción</th><th>Vence</th><th>Monto</th><th>Estatus</th></tr>'+f.sort((a,b)=>(a.fecha||'9').localeCompare(b.fecha||'9')).map(o=>{const d=dr(o.fecha);const c=d===null?'':d<0?'#ff9b8d':d<=15?'#ffce82':'#64748b';return '<tr><td><span class="lk" style="color:#7ee0b4;cursor:pointer" onclick="ficha('+o.idx+')">'+o.folio+'</span></td><td>'+o.tipo+'</td><td>'+(o.desc||'—')+'</td><td style="color:'+c+'">'+(o.fecha||'—')+(d!==null?' ('+(d<0?'-'+(-d):d)+'d)':'')+'</td><td>'+(o.monto?M(o.monto):'—')+'</td><td>'+(o.estado||'Pendiente')+'</td></tr>';}).join(''):'<tr><td style="color:#64748b;padding:14px">Sin obligaciones registradas. Agrégalas desde la ficha de cada instrumento.</td></tr>';
}
/* ---------- t6 alertas ---------- */
function alItems(){const r=[];INSTR.forEach((e,i)=>{const d=dr(e.fin);if(activo(e)&&d!==null)r.push({folio:e.folio,idx:i,tipo:'Vigencia',ref:e.tipo,d:d,nivel:e.nivel});});
 allOblig().forEach(o=>{const d=dr(o.fecha);if((o.estado!=='Cumplida')&&d!==null)r.push({folio:o.folio,idx:o.idx,tipo:o.tipo,ref:o.desc||'',d:d,nivel:'—'});});
 return r.sort((a,b)=>a.d-b.d);}
function renderAlertas(){const it=alItems();const buc=[[1,'≤ 24 h','b1'],[7,'≤ 7 días','b1'],[15,'≤ 15 días','b2'],[30,'≤ 30 días','b2'],[60,'≤ 60 días','b3'],[90,'≤ 90 días','b3']];
 const venc=it.filter(x=>x.d<0).length;
 document.getElementById('alBuckets').innerHTML='<div class="bk b1"><div class="n">'+venc+'</div><div class="l">Vencidos</div></div>'+
  buc.map(b=>{const n=it.filter(x=>x.d>=0&&x.d<=b[0]).length;return '<div class="bk '+b[2]+'"><div class="n">'+n+'</div><div class="l">'+b[1]+'</div></div>';}).join('');
 const fl=document.getElementById('fAl').value;let arr=it;
 if(fl==='venc')arr=it.filter(x=>x.d<0);else if(fl)arr=it.filter(x=>x.d>=0&&x.d<=+fl);
 const box=document.getElementById('alLista');
 box.innerHTML=arr.length?arr.map(x=>{const c=x.d<0?'#ff9b8d':x.d<=7?'#ffce82':'#64748b';return '<div class="it" onclick="ficha('+x.idx+')"><div style="display:flex;justify-content:space-between"><span class="t">'+x.folio+' · '+x.tipo+'</span><span style="color:'+c+';font-weight:700">'+(x.d<0?'venció hace '+(-x.d)+'d':'en '+x.d+'d')+'</span></div><div class="m">'+(x.ref||'')+(x.nivel!=='—'?' · '+x.nivel:'')+'</div></div>';}).join(''):'<div class="empty">Sin alertas en este rango.</div>';
}
/* ---------- t7 cláusuloteca ---------- */
function renderClaus(){const q=(document.getElementById('qcl').value||'').toLowerCase();const fr=document.getElementById('fclr').value;
 let arr=D.clausulas.filter(c=>(!fr||c.riesgo===fr)&&(!q||(c.titulo+' '+c.texto+' '+c.fam).toLowerCase().indexOf(q)>=0));
 document.getElementById('clausList').innerHTML=arr.map(c=>'<div class="cl"><div style="display:flex;justify-content:space-between"><span class="clt">'+c.clave+' · '+c.titulo+'</span><span>'+rb(c.riesgo)+' <span class="chip">'+c.fam+'</span></span></div><div class="clx">'+c.texto+'</div><div style="margin-top:8px"><button class="bd mini" onclick="copyCl(\''+c.clave+'\')">📋 Copiar</button></div></div>').join('');
}
function copyCl(clave){const c=D.clausulas.find(x=>x.clave===clave);if(c&&navigator.clipboard)navigator.clipboard.writeText(c.texto);}
/* ---------- t8 conocimiento ---------- */
function saveKB(){const tit=document.getElementById('k_tit').value.trim();if(!tit){alert('Indica un título.');return;}
 KB.push({cat:document.getElementById('k_cat').value,tit:tit,txt:document.getElementById('k_txt').value.trim(),fecha:new Date().toISOString().slice(0,10),autor:localStorage.getItem('sigej_perfil')||'(perfil)'});saveKBs();
 document.getElementById('k_tit').value='';document.getElementById('k_txt').value='';renderKB();if(window.__bitlog)__bitlog('Acción','Registrar conocimiento: '+tit);}
function renderKB(){const q=(document.getElementById('qkb').value||'').toLowerCase();const fc=document.getElementById('fkb').value;
 let arr=KB.filter(k=>(!fc||k.cat===fc)&&(!q||(k.tit+' '+(k.txt||'')+' '+k.cat).toLowerCase().indexOf(q)>=0));
 const box=document.getElementById('kbList');
 box.innerHTML=KB.length?(arr.map((k,i)=>'<div class="cl"><div style="display:flex;justify-content:space-between"><span class="clt">'+k.tit+'</span><span class="chip">'+k.cat+'</span></div><div class="clx">'+(k.txt||'—')+'</div><div style="font-size:11px;color:#64748b;margin-top:6px">'+k.fecha+' · '+k.autor+' <span class="del" style="color:#ff9b8d;cursor:pointer;margin-left:8px" onclick="delKB('+KB.indexOf(k)+')">✕</span></div></div>').join('')||'<div class="empty" style="padding:14px">Sin coincidencias.</div>'):'<div class="empty">📭 Repositorio vacío. Registra dictámenes, opiniones, plantillas, criterios y precedentes para construir la memoria institucional.</div>';
}
function delKB(i){var k=KB[i];if(!k)return;if(k.anulado){alert('Ya anulado. No se elimina.');return;}var m=prompt('Motivo de anulación (no se elimina, queda anulado):','');if(m===null||!m.trim())return;k.anulado={motivo:m.trim(),por:(localStorage.getItem('sigej_perfil')||'(perfil)'),ts:new Date().toISOString().slice(0,16).replace('T',' ')};saveKBs();if(window.__bitlog)__bitlog('Acción','Anula registro de conocimiento');renderKB();}
/* ---------- flujo BPMN / RACI / SLA / aprobaciones ---------- */
function hoyStr(){return HOY.toISOString().slice(0,10);}
function seedFlujo(o,estadoSel){const tpl=D.flujos[o.fam]||D.flujos['Convenios'];
 o.flujo=tpl.map(s=>({paso:s[0],R:s[1],A:s[2],C:s[3],I:s[4],sla:s[5],fase:s[6],estado:'Pendiente',inicio:null,fin:null,obs:'',escalado:false}));
 let target=0;const fin=['Vigente','Por vencer','Terminado','Cancelado'];
 if(estadoSel&&estadoSel!=='Solicitud'){const idx=o.flujo.map(s=>s.fase).lastIndexOf(estadoSel);if(idx>=0)target=idx;if(fin.indexOf(estadoSel)>=0)target=o.flujo.length-1;}
 for(let k=0;k<target;k++){o.flujo[k].estado='Aprobado';o.flujo[k].inicio=hoyStr();o.flujo[k].fin=hoyStr();}
 o.flujo[target].estado='En curso';o.flujo[target].inicio=hoyStr();o.pasoActual=target;
 if(fin.indexOf(estadoSel)>=0){o.flujo[target].estado='Aprobado';o.flujo[target].fin=hoyStr();o.estado=estadoSel;}
 else o.estado=o.flujo[target].fase;
}
function ensureFlujo(e){if(!e.flujo||!e.flujo.length){seedFlujo(e,e.estado);saveAll();}return e.flujo;}
function diasEn(s){if(!s.inicio)return null;return Math.round((HOY-new Date(s.inicio+'T00:00:00'))/864e5);}
function curStep(e){return (e.flujo||[]).find(s=>s.estado==='En curso');}
function puedeAprobar(s){const p=localStorage.getItem('sigej_perfil')||'';if(p==='Administrador'||p==='Abogado General')return true;if(!s||!p)return false;
 if(s.A&&s.A.indexOf(p)>=0)return true;
 if(p==='Coordinador Jurídico'&&/Coordinador/.test(s.A))return true;
 if(p==='Jefa de Unidad'&&/Jefa/.test(s.A))return true;
 return false;}
function stCol(st){return st==='Aprobado'?'#1f9d6b':st==='En curso'?'#0a4d8c':st==='Rechazado'?'#c0392b':st==='Observado'?'#e08e0b':'#33507a';}
function bpmnDiagram(e){return '<div class="bpmn">'+e.flujo.map((s,k)=>{const cur=s.estado==='En curso';const d=diasEn(s);const over=cur&&d!==null&&d>s.sla;
 return (k?'<div class="bpmn-arr">▸</div>':'')+'<div class="bpmn-node" style="border-color:'+stCol(s.estado)+(cur?';box-shadow:0 0 0 2px '+stCol(s.estado):'')+'"><div class="bn-st" style="background:'+stCol(s.estado)+'">'+s.estado+(s.escalado?' ⏫':'')+'</div><div class="bn-p">'+s.paso+'</div><div class="bn-r">A: '+s.A+'</div><div class="bn-sla">SLA '+s.sla+'d'+(cur?' · '+(d||0)+'d'+(over?' ⚠️':''):'')+'</div></div>';}).join('')+'</div>';}
function raciTable(s){const rows=[['R','Responsable',s.R],['A','Aprueba',s.A],['C','Consultado',s.C],['I','Informado',s.I]];
 return '<table style="margin-top:6px"><tr><th>RACI</th><th>Rol</th><th>Actor</th></tr>'+rows.map(r=>'<tr><td><b style="color:#0a4d8c">'+r[0]+'</b></td><td>'+r[1]+'</td><td>'+(r[2]||'—')+'</td></tr>').join('')+'</table>';}
function bpmnPanel(i){const e=INSTR[i];ensureFlujo(e);const s=curStep(e);
 let p='<div class="comp"><b>🔀 Flujo de aprobación (BPMN) · RACI · SLA</b>'+bpmnDiagram(e);
 if(s){const d=diasEn(s);const over=d!==null&&d>s.sla;const can=puedeAprobar(s);
  p+='<div style="margin-top:10px;background:#f1f5fb;border:1px solid var(--line);border-radius:8px;padding:10px">'+
   '<b style="color:#0a4d8c">Etapa actual: '+s.paso+'</b> '+(over?'<span class="rb rb-Alto">SLA vencido ('+d+'/'+s.sla+'d)</span>':'<span class="chip">'+(d||0)+'/'+s.sla+' días</span>')+
   raciTable(s)+
   (s.fase==='Firma'?firmaInner(i,can):(can?'<div style="margin-top:8px;display:flex;gap:6px;flex-wrap:wrap"><button class="b3 mini" onclick="aprobarPaso('+i+')">✅ Aprobar</button><button class="mini" style="background:#e08e0b" onclick="observarPaso('+i+')">✏️ Observar / devolver</button><button class="mini" style="background:#c0392b" onclick="rechazarPaso('+i+')">⛔ Rechazar</button><button class="bd mini" onclick="escalarPaso('+i+')">⏫ Escalar</button><button class="bd mini" onclick="reasignarPaso('+i+')">🔁 Reasignar</button></div>':'<div class="warn" style="margin-top:8px">Pendiente de aprobación por <b>'+s.A+'</b>. Tu perfil no es el aprobador de esta etapa.</div>'))+
   (s.obs?'<div style="margin-top:6px;font-size:11.5px;color:#ffce82">Última observación: '+s.obs+'</div>':'')+'</div>';
 } else {p+='<div class="warn" style="margin-top:8px">Flujo concluido — instrumento <b>'+e.estado+'</b>.</div>';}
 return p+'</div>';}
/* ---------- firma electrónica interna: flujo de firmantes secuencial/paralelo ---------- */
function advanceStep(e){const s=curStep(e);if(!s)return;s.estado='Aprobado';s.fin=hoyStr();const idx=e.flujo.indexOf(s);
 if(idx+1<e.flujo.length){const nx=e.flujo[idx+1];nx.estado='En curso';nx.inicio=hoyStr();e.pasoActual=idx+1;e.estado=nx.fase;}else{e.estado='Vigente';}}
function ensureFirma(e){const s=curStep(e);if(!s||s.fase!=='Firma')return;
 if(!e.firmaCfg){const a=D.areas[e.area]||{};const r=[{nombre:'',cargo:a.autoridad||'Autoridad UdeG',parte:'UdeG',orden:1,estado:'Pendiente',fecha:'',sello:''}];
  if(e.contra)r.push({nombre:e.contra,cargo:'Representante legal',parte:'Contraparte',orden:2,estado:'Pendiente',fecha:'',sello:''});
  e.firmaCfg={modo:'Secuencial',firmantes:r};saveAll();}
 reconcileFirmas(e);}
function reconcileFirmas(e){if(!e.firmaCfg)return;(e.firmas||[]).forEach(fm=>{const c=e.firmaCfg.firmantes.find(x=>x.parte===fm.parte&&x.estado!=='Firmado');if(c){c.estado='Firmado';c.fecha=fm.fecha;c.sello=fm.sello;if(!c.nombre)c.nombre=fm.nombre;}});saveAll();}
function canSignRow(e,k){const f=e.firmaCfg;const x=f.firmantes[k];if(x.estado==='Firmado'||x.parte==='Contraparte')return false;
 if(f.modo==='Paralelo')return true;for(let j=0;j<k;j++){if(f.firmantes[j].estado!=='Firmado')return false;}return true;}
function firmarComo(i,k){const e=INSTR[i];ensureFirma(e);const x=e.firmaCfg.firmantes[k];
 if(x.parte==='Contraparte'){alert('La contraparte firma desde el Portal de Contrapartes.');return;}
 if(!canSignRow(e,k)){alert('Aún no es el turno de este firmante (modo secuencial).');return;}
 const nombre=x.nombre||prompt('Nombre del firmante ('+x.cargo+'):','');if(!nombre)return;x.nombre=nombre;
 const sello='UDG-'+Date.now().toString(36).toUpperCase();x.estado='Firmado';x.fecha=hoyStr();x.sello=sello;
 e.firmas=e.firmas||[];e.firmas.push({parte:x.parte,nombre:nombre,fecha:hoyStr(),sello:sello});
 logIt(e,'Firma '+x.parte+': '+nombre+' (sello '+sello+')');logV(e,'Firma de '+x.cargo+' ('+x.parte+')');saveAll();
 if(window.__bitlog)__bitlog('Acción','Firma '+x.parte+' · '+e.folio);
 checkFirmaComplete(e);ficha(i);compute();renderList();}
function checkFirmaComplete(e){if(!e.firmaCfg)return false;const all=e.firmaCfg.firmantes.every(x=>x.estado==='Firmado');
 if(all){const s=curStep(e);if(s&&s.fase==='Firma'){advanceStep(e);logIt(e,'Firma completada — instrumento vigente');logV(e,'Firma electrónica completada (todos los firmantes)');saveAll();return true;}}return false;}
function setModoFirma(i,m){const e=INSTR[i];ensureFirma(e);e.firmaCfg.modo=m;saveAll();ficha(i);}
function addFirmante(i){const e=INSTR[i];ensureFirma(e);const nombre=prompt('Nombre del firmante adicional (testigo de honor / representante):','');if(!nombre)return;
 const cargo=prompt('Cargo:','Testigo de honor')||'Testigo';
 e.firmaCfg.firmantes.push({nombre:nombre,cargo:cargo,parte:'Testigo',orden:e.firmaCfg.firmantes.length+1,estado:'Pendiente',fecha:'',sello:''});saveAll();ficha(i);}
function rechazarFirma(i,k){const e=INSTR[i];const x=e.firmaCfg.firmantes[k];const m=prompt('Motivo de no firmar / rechazo:','');if(m===null)return;
 x.estado='Rechazado';x.obs=m;e.estado='Cancelado';logIt(e,'Firma rechazada por '+x.cargo+': '+m);logV(e,'Rechazo de firma');saveAll();compute();renderList();ficha(i);}
function firmaInner(i,can){const e=INSTR[i];ensureFirma(e);const f=e.firmaCfg;const firmadas=f.firmantes.filter(x=>x.estado==='Firmado').length;
 let h='<div style="margin-top:8px"><b style="color:#0a4d8c">✒️ Firma electrónica</b> <span class="chip">'+firmadas+'/'+f.firmantes.length+' firmas</span> '+
  'Modo: <button class="'+(f.modo==='Secuencial'?'b1':'bd')+' mini" onclick="setModoFirma('+i+',\'Secuencial\')">Secuencial</button> <button class="'+(f.modo==='Paralelo'?'b1':'bd')+' mini" onclick="setModoFirma('+i+',\'Paralelo\')">Paralelo</button>'+
  '<table style="margin-top:6px"><tr><th>#</th><th>Firmante</th><th>Parte</th><th>Estado</th><th></th></tr>'+
  f.firmantes.map((x,k)=>{const cs=canSignRow(e,k)&&can;const stc=x.estado==='Firmado'?'#7ee0b4':x.estado==='Rechazado'?'#ff9b8d':'#ffce82';
   const acc=x.estado==='Firmado'?'✓':(x.parte==='Contraparte'?'<span style="font-size:10px;color:#64748b">firma en portal</span>':(cs?'<button class="b3 mini" onclick="firmarComo('+i+','+k+')">✒️ Firmar</button> <button class="mini" style="background:#c0392b" onclick="rechazarFirma('+i+','+k+')">⛔</button>':'<span style="font-size:10px;color:#64748b">en espera</span>'));
   return '<tr><td>'+(k+1)+'</td><td>'+(x.nombre||'<i style="color:#64748b">por designar</i>')+'<div style="font-size:10px;color:#64748b">'+x.cargo+'</div></td><td><span class="chip">'+x.parte+'</span></td><td style="color:'+stc+'">'+x.estado+(x.sello?'<div style="font-size:10px;color:#64748b">'+x.sello+' · '+x.fecha+'</div>':'')+'</td><td>'+acc+'</td></tr>';}).join('')+'</table>'+
  '<div style="margin-top:6px"><button class="bd mini" onclick="addFirmante('+i+')">＋ Agregar firmante</button>'+(can?' <button class="mini" style="background:#e08e0b" onclick="observarPaso('+i+')">✏️ Observar</button>':'')+'</div>'+
  '<div style="font-size:10.5px;color:#64748b;margin-top:5px">Modo <b>secuencial</b>: cada firmante habilita al siguiente. <b>Paralelo</b>: todos pueden firmar a la vez. Al completar todas las firmas el instrumento pasa a <b>Vigente</b>. Firma con validez legal (e.firma SAT / Firma UDG / DocuSign) = fase backend.</div></div>';
 return h;}
function addDays(d,n){return new Date(d.getTime()+n*864e5);}
function dstr(d){return d.toISOString().slice(0,10);}
function parseD(s){return s?new Date(s+'T00:00:00'):null;}
function ganttFlujo(i){const e=INSTR[i];ensureFlujo(e);const f=e.flujo;
 let base=parseD(e.firma)||parseD(f[0].inicio)||HOY;
 let acc=0;const plan=f.map(s=>{const ps=addDays(base,acc);acc+=s.sla;const pe=addDays(base,acc);return {ps:ps,pe:pe};});
 const planEnd=addDays(base,acc);
 let realEnd=base;f.forEach(s=>{const rf=parseD(s.fin)||(s.estado==='En curso'?HOY:null);if(rf&&rf>realEnd)realEnd=rf;});
 const end=new Date(Math.max(planEnd.getTime(),realEnd.getTime(),HOY.getTime()));
 const span=Math.max(1,(end-base)/864e5);
 const pct=d=>Math.max(0,Math.min(100,100*((d-base)/864e5)/span));
 const rows=f.map((s,k)=>{const p=plan[k];const pl=pct(p.ps),pr=pct(p.pe);
   const ri=parseD(s.inicio);const rf=parseD(s.fin)||(s.estado==='En curso'?HOY:null);let realBar='';
   if(ri&&rf){const a=pct(ri),b=pct(rf);const over=s.estado==='En curso'&&diasEn(s)>s.sla;
     realBar='<div class="g-real" title="real" style="left:'+a+'%;width:'+Math.max(1.5,b-a)+'%;background:'+stCol(s.estado)+(over?';outline:2px solid #c0392b':'')+'"></div>';}
   return '<div class="grow"><div class="glab" title="'+s.paso+'">'+s.paso+'</div><div class="gtrack"><div class="g-plan" title="planeado '+s.sla+'d" style="left:'+pl+'%;width:'+Math.max(1.5,pr-pl)+'%"></div>'+realBar+'</div></div>';}).join('');
 const todayPct=pct(HOY)/100;
 const avance=Math.round(100*f.filter(s=>s.estado==='Aprobado').length/f.length);
 const ticks=[0,.25,.5,.75,1].map(t=>dstr(addDays(base,Math.round(span*t))).slice(5)).map(d=>'<span>'+d+'</span>').join('');
 return '<div class="comp"><b>📊 Gantt del flujo (planeado vs real)</b>'+
  '<div style="font-size:11.5px;color:#64748b;margin:4px 0">Avance <b style="color:#7ee0b4">'+avance+'%</b> · días plan total <b>'+acc+'</b> · conclusión estimada <b>'+dstr(planEnd)+'</b> · base '+dstr(base)+'</div>'+
  '<div class="gantt"><div class="gtoday" style="left:calc(160px + (100% - 160px) * '+todayPct+')"></div>'+rows+'<div class="gaxis">'+ticks+'</div></div>'+
  '<div style="font-size:11px;color:#64748b;margin-top:6px"><span class="gleg" style="background:#33507a"></span>planeado (SLA) &nbsp;<span class="gleg" style="background:#1f9d6b"></span>real &nbsp;<span style="border-left:2px dashed #d4a32c;padding-left:4px">hoy</span></div></div>';}
function logV(e,nota){e.versiones.push({v:e.versiones.length+1,autor:localStorage.getItem('sigej_perfil')||'(perfil)',fecha:hoyStr(),nota:nota});}
function aprobarPaso(i){const e=INSTR[i];const s=curStep(e);if(!s)return;if(!puedeAprobar(s)){alert('Tu perfil no aprueba esta etapa.');return;}
 s.estado='Aprobado';s.fin=hoyStr();const idx=e.flujo.indexOf(s);
 if(idx+1<e.flujo.length){const nx=e.flujo[idx+1];nx.estado='En curso';nx.inicio=hoyStr();e.pasoActual=idx+1;e.estado=nx.fase;}else{e.estado='Vigente';}
 logIt(e,'Aprobada etapa: '+s.paso);logV(e,'Aprobación de "'+s.paso+'"');e.score=scoreOf(e);e.nivel=nivel(e.score);saveAll();
 if(window.__bitlog)__bitlog('Acción','Aprobar etapa '+s.paso+' · '+e.folio);ficha(i);compute();renderList();}
function observarPaso(i){const e=INSTR[i];const s=curStep(e);if(!s||!puedeAprobar(s)){alert('Tu perfil no aprueba esta etapa.');return;}
 const obs=prompt('Observación / motivo de devolución:','');if(obs===null)return;const idx=e.flujo.indexOf(s);
 s.estado='Pendiente';s.inicio=null;s.obs=obs;
 if(idx>0){const pv=e.flujo[idx-1];pv.estado='En curso';pv.fin=null;pv.inicio=hoyStr();pv.obs=obs;e.pasoActual=idx-1;e.estado=pv.fase;}else{s.estado='En curso';s.inicio=hoyStr();}
 logIt(e,'Observada/devuelta etapa: '+s.paso+' — '+obs);logV(e,'Observación en "'+s.paso+'"');saveAll();ficha(i);compute();renderList();}
function rechazarPaso(i){const e=INSTR[i];const s=curStep(e);if(!s||!puedeAprobar(s)){alert('Tu perfil no aprueba esta etapa.');return;}
 const m=prompt('Motivo de rechazo:','');if(m===null)return;s.estado='Rechazado';s.obs=m;e.estado='Cancelado';
 logIt(e,'Rechazada etapa: '+s.paso+' — '+m);logV(e,'Rechazo en "'+s.paso+'"');saveAll();ficha(i);compute();renderList();}
function escalarPaso(i){const e=INSTR[i];const s=curStep(e);if(!s)return;s.escalado=true;logIt(e,'Escalada etapa: '+s.paso+' (SLA)');saveAll();ficha(i);}
function reasignarPaso(i){const e=INSTR[i];const s=curStep(e);if(!s)return;const r=prompt('Reasignar responsable (R) de la etapa a:',s.R);if(!r)return;s.R=r;logIt(e,'Reasignación R='+r+' en '+s.paso);saveAll();ficha(i);}
function renderFlujos(){const p=localStorage.getItem('sigej_perfil')||'(perfil)';INSTR.forEach(ensureFlujo);
 const apr=[];INSTR.forEach((e,i)=>{const s=curStep(e);if(s&&puedeAprobar(s))apr.push({e:e,i:i,s:s});});
 const sol=INSTR.map((e,i)=>({e:e,i:i})).filter(x=>x.e.versiones&&x.e.versiones[0]&&x.e.versiones[0].autor===p);
 const sla=[];INSTR.forEach((e,i)=>{const s=curStep(e);if(s){const d=diasEn(s);if(d!==null&&d>s.sla)sla.push({e:e,i:i,s:s,d:d});}});
 const K=[['',apr.length,'Mis aprobaciones pendientes','y'],['',sol.length,'Mis solicitudes',''],['',sla.length,'SLA vencidos','r'],['',INSTR.filter(activo).length,'En flujo activo','g']];
 document.getElementById('flKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 function row(x,extra){const s=x.s||curStep(x.e);return '<div class="it" onclick="ficha('+x.i+')"><div style="display:flex;justify-content:space-between"><span class="t">'+x.e.folio+' · '+x.e.tipo+'</span>'+(s?'<span class="chip">'+s.paso+'</span>':'')+'</div><div class="m">'+x.e.area+' · '+(x.e.dep||'—')+(s?' · A: '+s.A:'')+(extra||'')+'</div></div>';}
 document.getElementById('flApr').innerHTML=apr.length?apr.map(x=>{const d=diasEn(x.s);return row(x,' · '+(d||0)+'/'+x.s.sla+'d');}).join(''):'<div class="empty" style="padding:14px">No hay aprobaciones pendientes para el perfil <b>'+p+'</b>.</div>';
 document.getElementById('flSol').innerHTML=sol.length?sol.map(x=>row(x)).join(''):'<div class="empty" style="padding:14px">No has registrado instrumentos con este perfil.</div>';
 document.getElementById('flSla').innerHTML=sla.length?sla.map(x=>row(x,' · <span style="color:#ff9b8d">vencido +'+(x.d-x.s.sla)+'d</span>')).join(''):'<div class="empty" style="padding:14px">Sin SLA vencidos. 👌</div>';
}
/* init */
window.addEventListener('storage',()=>{INSTR=JSON.parse(localStorage.getItem('sigej_instrumentos')||'[]');compute();});
liveRisk();compute();
</script>
<script>
/* Expediente electrónico — adjuntar archivos por categoría documental */
const DCATS=['Convenio / contrato firmado','Anexo técnico','Anexo financiero','Identificación / poderes','Acta','Adenda / modificatorio','Comprobante','Evidencia','Otro'];let __DOCREF=null;
function __rec(ref){return (typeof ref==='number')?INSTR[ref]:INSTR.find(function(x){return x.id===ref;});}
function docExp(ref){var rec=__rec(ref);if(!rec)return;if(!rec.docs)rec.docs=[];
 var ov=document.getElementById('__docov')||document.createElement('div');ov.id='__docov';ov.style.cssText='position:fixed;inset:0;background:rgba(10,31,60,.5);display:flex;align-items:center;justify-content:center;z-index:99998;padding:18px';
 var co=DCATS.map(function(c){return '<option>'+c+'</option>';}).join('');
 var ls=rec.docs.length?rec.docs.map(function(x,k){return '<div style="font-size:12px;color:#334155;padding:4px 0;border-bottom:1px solid #eef2f7">\ud83d\udcce <b>'+(x.cat||'')+'</b> \u00b7 '+x.nombre+' \u00b7 '+(x.fecha||'')+' <a href="'+x.data+'" download="'+x.nombre+'">descargar</a> \u00b7 <span style="color:#0a4d8c;cursor:pointer;text-decoration:underline" onclick="docVerR(\''+(rec.id!=null?rec.id:ref)+'\','+k+')">\ud83d\udc41 ver</span></div>';}).join(''):'<div style="color:#64748b;font-size:12px">Sin documentos en el expediente.</div>';
 ov.innerHTML='<div style="background:#fff;border-radius:14px;max-width:640px;width:100%;max-height:85vh;overflow:auto;padding:20px"><span style="float:right;cursor:pointer;color:#64748b;font-size:20px" onclick="document.getElementById(\'__docov\').remove()">\u2715</span><h3 style="margin:0 0 4px;color:#0a4d8c">\ud83d\udcce Expediente electr\u00f3nico</h3><div style="font-size:12px;color:#64748b;margin-bottom:10px">'+((rec.folio||rec.exp||rec.id||rec.nombre||'')+' \u00b7 '+(rec.tipo||rec.asunto||rec.clasif||''))+'</div><div style="display:flex;gap:6px;align-items:center;margin-bottom:10px;flex-wrap:wrap"><select id="__doccat" style="padding:6px 8px;border:1px solid #cbd5e1;border-radius:6px;font-size:12px">'+co+'</select><button onclick="docPick(\''+(rec.id!=null?rec.id:ref)+'\')" style="padding:6px 11px;border:none;border-radius:7px;background:#0a4d8c;color:#fff;font-size:12px;font-weight:600;cursor:pointer">\ud83d\udcce Adjuntar archivo</button> <button onclick="docOCR(\''+(rec.id!=null?rec.id:ref)+'\')" style="padding:6px 11px;border:none;border-radius:7px;background:#d4a32c;color:#3a2c05;font-size:12px;font-weight:600;cursor:pointer">🔎 OCR / extraer datos</button></div>'+ls+'<div style="font-size:10.5px;color:#94a3b8;margin-top:10px">Conforma el expediente electr\u00f3nico del registro \u00b7 PDF/imagen/Word \u22641.8 MB (prototipo en este equipo).</div></div>';
 if(!ov.parentNode)document.body.appendChild(ov);}
function docPick(ref){__DOCREF=ref;var c=document.getElementById('__doccat');window.__dcat=c?c.value:(DCATS[0]||'Documento');var inp=document.getElementById('__docfile');if(!inp){inp=document.createElement('input');inp.type='file';inp.id='__docfile';inp.style.display='none';inp.onchange=docOn;document.body.appendChild(inp);}inp.value='';inp.click();}
function docOn(){var f=this.files[0];if(!f||__DOCREF==null)return;if(f.size>1.8e6){alert('M\u00e1ximo 1.8 MB por archivo.');return;}var rec=__rec(__DOCREF);if(!rec)return;if(!rec.docs)rec.docs=[];var r=new FileReader();r.onload=function(){rec.docs.push({nombre:f.name,tipo:f.type,cat:window.__dcat||'Documento',data:r.result,fecha:new Date().toISOString().slice(0,10)});try{saveAll();}catch(e){}if(window.__bitlog)__bitlog('Acci\u00f3n','Adjuntar documento al expediente ('+(window.__dcat||'')+')');docExp(__DOCREF);try{renderList();}catch(e){}};r.readAsDataURL(f);}
function docVerR(ref,k){var rec=__rec(ref);var x=rec.docs[k];var w=window.open('','_blank');if(!w)return;if(/image/.test(x.tipo))w.document.write('<img src="'+x.data+'" style="max-width:100%">');else if(/pdf/.test(x.tipo))w.document.write('<iframe src="'+x.data+'" style="border:0;width:100%;height:100vh"></iframe>');else w.document.write('<a href="'+x.data+'" download="'+x.nombre+'">Descargar '+x.nombre+'</a>');}
function docOCR(ref){var rec=__rec(ref);if(!rec)return;var t=prompt('Pega el texto del documento (escaneo/PDF). El OCR de imagen es fase backend; aquí se extraen datos por reglas y se llenan campos:','');if(t===null||!t.trim())return;var folio=(t.match(/\b\d{1,5}\s*\/\s*\d{2,4}(?:-[A-Za-z]+)?\b/)||[''])[0].replace(/\s/g,'');var fecha=(t.match(/\b\d{4}-\d{2}-\d{2}\b/)||t.match(/\b\d{1,2}\/\d{1,2}\/\d{4}\b/)||[''])[0];var monto=(t.match(/\$\s?[\d,]+(?:\.\d{2})?/)||[''])[0];var am=t.match(/asunto\s*:?\s*([^\n\r]+)/i);var asunto=am?am[1].trim():t.replace(/\s+/g,' ').trim().slice(0,120);rec.ocr={folio:folio,fecha:fecha,monto:monto};var cs=['asunto','obj','objeto','descripcion','desc','nota','observaciones','titulo','tit'];for(var ci=0;ci<cs.length;ci++){if(cs[ci] in rec){if(!rec[cs[ci]])rec[cs[ci]]=asunto;break;}}if(!rec.docs)rec.docs=[];rec.docs.push({nombre:'Texto OCR (reglas).txt',tipo:'text/plain',cat:'OCR / extracción',data:'data:text/plain;base64,'+btoa(unescape(encodeURIComponent(t.slice(0,5000)))),fecha:new Date().toISOString().slice(0,10)});try{saveAll();}catch(e){}if(window.__bitlog)__bitlog('Acción','OCR/extracción al expediente');alert('Extraído por reglas — Folio: '+(folio||'—')+' · Fecha: '+(fecha||'—')+(monto?' · Monto: '+monto:'')+'. Texto guardado en el expediente; se llenó el asunto si estaba vacío. (OCR de imagen real = fase backend.)');docExp(ref);try{renderList();}catch(e){}}

</script>
__SNIP__
</body></html>"""
html=TPL.replace("__DATA__",DATAJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP).replace("__CONVSEED__",CONVJ)
open(B+"instrumentos_SIGEJ.html","w",encoding="utf-8").write(html)
print("instrumentos_SIGEJ.html OK -",len(html),"bytes | familias",len(FAMILIAS),"| cláusulas",len(CLAUSULAS),"| dependencias",len(DEPENDENCIAS))
