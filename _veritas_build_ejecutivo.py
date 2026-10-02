# -*- coding: utf-8 -*-
# Centro Ejecutivo — módulo unificado (Centro de Mando + CMI/BSC + Inteligencia + Sala de Mando)
# Restringido a Administrador, Abogado General, Coordinador Jurídico y Jefa de Unidad.
import json
B="/Users/edithroque/Documents/CLAUDE/"
comando=json.load(open(B+"comando_data.json",encoding="utf-8"))
lec=json.load(open(B+"lecciones_pro.json",encoding="utf-8"))
altad=json.load(open(B+"alta_direccion_data.json",encoding="utf-8"))
dd=json.load(open(B+"dashboard_data.json",encoding="utf-8"))
cu=json.load(open(B+"cuellos_data.json",encoding="utf-8"))
pv=json.load(open(B+"provision_base.json",encoding="utf-8"))
rm=json.load(open(B+"riesgo_materia.json",encoding="utf-8"))

# ---- Precálculo del Cuadro de Mando Integral (Kaplan & Norton, 4 perspectivas) ----
kpis=dd["kpis"]; lit=dd["litigios"]; dz=dd.get("desempeno",[])
ex=sum(d.get("exito",0) for d in dz); ad=sum(d.get("adv",0) for d in dz)
ampl=round(1000*ex/(ex+ad))/10 if (ex+ad) else None
pas=sum(x["pasivo_doc"] for x in pv["niveles"])
res=sum(x["pasivo_doc"]*x["pct_default"]/100 for x in pv["niveles"])
dur=round(cu["lifespan_med"]/365,1)
ator=cu["idle_counts"]["a24"]
tr=sorted(cu["transiciones"].items(), key=lambda a:-a[1]["mediana"])
cuello=tr[0] if tr else None
altoR=sum(x.get("altoR",0) for x in rm)
susp=(lit.get("susp") or {}).get("concedida",0)
M=lambda v:"$"+format(round(v/1e6,2),".2f")+"M"
bsc={
 "juridica":[["🟢 Tasa de éxito (estricta)",str(kpis["tasa_exito"])+"%"],
   ["🟢 Tasa de éxito (ampliada)",(str(ampl)+"%") if ampl is not None else "—"],
   ["🟢 Asuntos de alto riesgo",altoR],
   ["🟢 Suspensiones concedidas",susp]],
 "financiera":[["🟢 Pasivo contingente (piso)",M(pas)],
   ["🟢 Reserva sugerida",M(res)],
   ["🟢 Conciliaciones (MASC)",lit.get("conciliacion",0)],
   ["🟡 Costos / honorarios","a capturar"]],
 "procesos":[["🟢 Duración mediana del juicio",str(dur)+" años"],
   ["🟢 Cuello principal",(cuello[0]+" ("+str(cuello[1]["mediana"])+"d)") if cuello else "—"],
   ["🟢 Atorados > 24 meses",ator],
   ["🟢 % expedientes activos",str(kpis["pct_activos"])+"%"]],
 "aprendizaje":[["🟢 Abogados en plantilla",kpis["abogados"]],
   ["🟡 Capacitación / formación","a capturar"],
   ["🟡 Horas de formación","a capturar"],
   ["🟡 Evaluación de desempeño","a capturar"]],
 "corte":altad["meta"]["corte"]
}
D={"comando":comando,"bsc":bsc,"lec":lec,"altad":altad}
DATA=json.dumps(D,ensure_ascii=False)

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html" class="act">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''

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
<title>SIGEJ-UdeG · Centro Ejecutivo</title>
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
.rf{background:var(--azul2);color:#fff;border:none;border-radius:8px;padding:7px 13px;font-size:12.5px;font-weight:600;cursor:pointer}
.tabbar{display:flex;flex-wrap:wrap;gap:6px;padding:14px 24px 0;max-width:1400px;margin:auto}
.tb{background:var(--card);color:#475569;border:1px solid var(--line);border-bottom:none;border-radius:11px 11px 0 0;padding:11px 18px;font-size:13px;font-weight:600;cursor:pointer}
.tb:hover{color:#fff}.tb.on{background:var(--azul2);color:#fff;border-color:var(--azul2)}
.wrap{padding:14px 24px 34px;max-width:1400px;margin:auto}
.ce-tab{display:none}.ce-tab.on{display:block}
.note{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:10px;padding:9px 13px;font-size:12px;color:#e8cf95;margin:6px 0 14px}
/* === t1 Centro de Mando === */
#t1 .nov{background:rgba(212,163,44,.12);border:1px solid rgba(212,163,44,.4);border-radius:10px;padding:8px 12px;font-size:12px;color:#ffce82;margin-bottom:14px}
#t1 .kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:16px}
#t1 .kpi{background:linear-gradient(160deg,var(--card),var(--card2));border:1px solid var(--line);border-radius:13px;padding:14px}
#t1 .kpi .n{font-size:25px;font-weight:800}#t1 .kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
#t1 .kpi.g .n{color:#7ee0b4}#t1 .kpi.r .n{color:#ff9b8d}#t1 .kpi.y .n{color:#ffce82}
#t1 .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px}
#t1 .card{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:15px}
#t1 .card h3{margin:0 0 10px;font-size:13.5px;color:#0a4d8c}#t1 .card.s2{grid-column:span 2}
#t1 canvas{max-height:260px}
#t1 .heat{width:100%;border-collapse:collapse;font-size:12px}#t1 .heat td,#t1 .heat th{padding:5px 7px;text-align:center;border:2px solid var(--bg)}#t1 .heat th{color:var(--mut)}
/* === t2 CMI/BSC === */
#t2 .bscgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
#t2 .card{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:16px}
#t2 .card h3{margin:0 0 8px;font-size:14px}
#t2 .row{display:flex;justify-content:space-between;padding:8px 2px;border-bottom:1px solid var(--line);font-size:13px}
#t2 .row b{color:#0a1f3c}
/* === t3 Inteligencia (panel claro) === */
#t3{background:#f4f6f9;color:#0a1f3c;border-radius:14px;padding:14px}
#t3 .igrid{display:grid;grid-template-columns:280px 1fr;gap:16px}
@media(max-width:900px){#t3 .igrid{grid-template-columns:1fr}}
#t3 .list{background:#fff;border-radius:12px;padding:10px;box-shadow:0 1px 3px rgba(0,0,0,.07);max-height:78vh;overflow:auto}
#t3 .li{padding:10px 12px;border-radius:9px;cursor:pointer;margin-bottom:4px;border-left:4px solid #e2e8f0}
#t3 .li:hover{background:#f4f6f9}#t3 .li.sel{background:#f0f6ff;border-left-color:#0a4d8c}
#t3 .li .t{font-size:13px;font-weight:600;color:#00254a}#t3 .li .m{font-size:11px;color:#64748b}
#t3 .card{background:#fff;border-radius:12px;padding:18px;box-shadow:0 1px 3px rgba(0,0,0,.07);margin-bottom:14px}
#t3 .card h2{margin:0 0 4px;font-size:17px;color:#00254a}
#t3 .badges{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}
#t3 .bdg{font-size:11px;padding:3px 9px;border-radius:10px;font-weight:600}#t3 .b-r{background:#fdecea;color:#c0392b}#t3 .b-a{background:#fef3e0;color:#b9770e}#t3 .b-m{background:#fffbe9;color:#a07a10}#t3 .b-b{background:#e6f6ee;color:#1f7a4d}#t3 .b-c{background:#e6f0fb;color:#0a4d8c}
#t3 .ok{background:#e6f6ee;color:#1f7a4d;border:1px solid #9fd9b8;border-radius:8px;padding:1px 8px;font-size:11px}#t3 .warn{background:#fff8e6;color:#8a6d1a;border:1px solid #f0e0a8;border-radius:8px;padding:1px 8px;font-size:11px}
#t3 .grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:760px){#t3 .grid2{grid-template-columns:1fr}}
#t3 .box{background:#f8fafc;border-radius:9px;padding:11px;font-size:12.5px}#t3 .box b{color:#00254a}#t3 .box ul{margin:5px 0 0;padding-left:18px}
#t3 .chk{display:flex;align-items:center;gap:8px;padding:6px 0;font-size:12.5px;border-bottom:1px solid #e2e8f0}
#t3 .lec{background:#f0fbf6;border:1px solid #cdeede;border-radius:9px;padding:11px;font-size:12.5px;margin-top:8px}
#t3 .acc{background:#fff8e6;border:1px solid #f0e0a8;border-radius:9px;padding:11px;font-size:12.5px;margin-top:8px}
#t3 button{padding:8px 13px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
#t3 .b1{background:#0a4d8c}#t3 .bw{background:#2b579a}#t3 .b3{background:#1f9d6b}
#t3 .kv{font-size:12px;color:#64748b}#t3 .kv b{color:#0a1f3c}
/* === t4 Sala de Mando === */
#t4 .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
#t4 .tile{background:linear-gradient(160deg,var(--card),var(--card2));border:1px solid var(--line);border-radius:16px;padding:18px;cursor:pointer;transition:.15s;position:relative;overflow:hidden}
#t4 .tile:hover{transform:translateY(-3px);border-color:var(--teal)}
#t4 .tile .q{font-size:13px;color:var(--mut);min-height:34px}
#t4 .tile .big{font-size:32px;font-weight:800;margin:8px 0 2px}
#t4 .tile .sub{font-size:12px;color:var(--mut)}
#t4 .tile .ic{position:absolute;right:14px;top:14px;font-size:20px;opacity:.5}
#t4 .tile.r-red{border-left:4px solid var(--red)}#t4 .tile.r-amber{border-left:4px solid var(--amber)}#t4 .tile.r-teal{border-left:4px solid var(--teal)}#t4 .tile.r-gold{border-left:4px solid var(--gold)}
.bars{margin-top:10px}.bar{display:flex;align-items:center;gap:8px;margin:3px 0;font-size:11.5px}
.bar .t{width:42%;color:var(--mut);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar .track{flex:1;background:#0a1c34;border-radius:6px;height:9px;overflow:hidden}
.bar .fill{height:100%;background:linear-gradient(90deg,var(--teal),var(--azul2))}
.bar .v{width:38px;text-align:right;color:var(--ink)}
.drawer{position:fixed;inset:0;background:rgba(4,12,24,.7);display:none;align-items:center;justify-content:center;z-index:99990;padding:20px}
.drawer.on{display:flex}
.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;max-width:880px;width:100%;max-height:86vh;overflow:auto;padding:22px}
.panel h2{margin:0 0 4px;font-size:18px}.panel .pq{color:var(--mut);font-size:13px;margin-bottom:14px}
.panel .x{float:right;cursor:pointer;color:var(--mut);font-size:20px}
.panel table{width:100%;border-collapse:collapse;font-size:12.5px}
.panel th,.panel td{padding:7px 9px;text-align:left;border-bottom:1px solid var(--line)}.panel th{color:var(--mut)}
.pill{padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600}
.Crítico{background:rgba(192,57,43,.25);color:#ff9b8d}.Alto{background:rgba(224,142,11,.25);color:#ffce82}
.Medio{background:rgba(26,163,154,.2);color:#8fe0d8}.Bajo{background:rgba(143,166,196,.18);color:var(--mut)}
#t8 .kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:14px}
#t8 .kpi{background:linear-gradient(160deg,var(--card),var(--card2));border:1px solid var(--line);border-radius:13px;padding:14px}
#t8 .kpi .n{font-size:23px;font-weight:800}#t8 .kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
#t8 .kpi.g .n{color:#7ee0b4}#t8 .kpi.r .n{color:#ff9b8d}#t8 .kpi.y .n{color:#ffce82}
#t8 .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}
#t8 .card{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:15px}
#t8 .card h3{margin:0 0 10px;font-size:13px;color:#0a4d8c}#t8 .card.s2{grid-column:span 2}
#t8 canvas{max-height:240px}
#t8 .h{font-size:14px;color:#0a4d8c;font-weight:700;margin:16px 0 10px}
#t8 table{width:100%;border-collapse:collapse;font-size:12px}#t8 th,#t8 td{padding:7px 9px;text-align:left;border-bottom:1px solid var(--line)}#t8 th{color:var(--mut)}
#t8 .chip{display:inline-block;background:#f1f5fb;border:1px solid var(--line);border-radius:9px;padding:2px 8px;font-size:10.5px;color:#475569;margin:2px}
#t8 .modcard{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:12px;margin-bottom:9px}
#t8 .rb{font-size:10px;padding:2px 8px;border-radius:9px;font-weight:600}
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
<header><div><h1>🧭 SIGEJ-UdeG · Centro Ejecutivo — Oficina de la Abogacía General · UdeG</h1>
<div class="s">Mando integral para la dirección: Centro de Mando · Cuadro de Mando Integral · Inteligencia Jurídica · Sala de Mando · acceso directivo</div></div>
<div style="text-align:right"><span class="live"><span class="dot"></span>En vivo · <span id="upd"></span></span> <button class="rf" onclick="ceCompute()">↻ Actualizar</button></div></header>
__NAV__
<div class="tabbar">
 <button class="tb on" data-t="t1" onclick="tab('t1')">🛰️ Centro de Mando</button>
 <button class="tb" data-t="t2" onclick="tab('t2')">📐 Cuadro de Mando Integral</button>
 <button class="tb" data-t="t3" onclick="tab('t3')">🧠 Inteligencia Jurídica</button>
 <button class="tb" data-t="t4" onclick="tab('t4')">🎯 Sala de Mando</button>
 <button class="tb" data-t="t8" onclick="tab('t8')">🏛️ Integración por módulo</button>
 <button class="tb" data-t="t5" onclick="tab('t5')">📊 Dashboard</button>
 <button class="tb" data-t="t6" onclick="tab('t6')">⏱️ Horas y Gastos</button>
 <button class="tb" data-t="t9" onclick="tab('t9')">🏛️ Legal por CU</button>
 <button class="tb" data-t="t10" onclick="tab('t10')">🎯 BI Estratégico PDI</button>
 <button class="tb" data-t="t11" onclick="tab('t11')">🧭 Tablero de Seguimientos</button>
 <button class="tb" data-t="t12" onclick="tab('t12')">📅 Agenda del Titular</button>
 <button class="tb" data-t="t13" onclick="tab('t13')">🧑‍⚖️ Permisos y Licencias</button>
 <button class="tb" data-t="t7" onclick="tab('t7')">📑 Reportes</button>
</div>
<div class="wrap">
 <section id="t1" class="ce-tab on">
  <div class="nov" id="ceNov" style="display:none"></div>
  <div class="kpis" id="ceKpis"></div>
  <div class="grid">
   <div class="card"><h3>Expedientes por materia</h3><canvas id="cMat"></canvas></div>
   <div class="card"><h3>Nivel de riesgo</h3><canvas id="cRie"></canvas></div>
   <div class="card s2"><h3>Expedientes por año (radicación)</h3><canvas id="cAnio"></canvas></div>
   <div class="card s2"><h3>Productividad / carga por abogado (activos)</h3><canvas id="cAbo"></canvas></div>
   <div class="card"><h3>Vía</h3><canvas id="cVia"></canvas></div>
   <div class="card"><h3>Estado procesal</h3><canvas id="cEst"></canvas></div>
   <div class="card s2"><h3>Pareto — dependencias con mayor litigiosidad</h3><canvas id="cDep"></canvas></div>
   <div class="card s2"><h3>Mapa de calor — dependencia × materia (top)</h3><div id="ceHeat"></div></div>
  </div>
 </section>
 <section id="t2" class="ce-tab">
  <div class="note">📐 <b>Cuadro de Mando Integral</b> (Kaplan &amp; Norton) adaptado a la Abogacía General — 4 perspectivas. 🟢 dato real · 🟡 a capturar.</div>
  <div class="bscgrid" id="ceBsc"></div>
 </section>
 <section id="t3" class="ce-tab">
  <div class="igrid">
   <div class="list" id="ceList"></div>
   <div id="ceDetail"></div>
  </div>
 </section>
 <section id="t4" class="ce-tab">
  <div class="note">⚠️ <b>Riesgo jurídico</b>, <b>alto riesgo</b> y <b>atención inmediata</b> usan un <b>score proxy explicable</b> (monto, etapa, sentido, antigüedad, suspensión): la fuente no contiene un campo de riesgo capturado. El <b>pasivo contingente</b> es piso parcial (montos legibles). Cifras a validar por la Abogacía General.</div>
  <div class="grid" id="ceGrid"></div>
 </section>
 <section id="t8" class="ce-tab">
  <div class="note">🏛️ <b>Integración institucional</b> — el Centro Ejecutivo armoniza todos los módulos/áreas. Cada área tiene sus propios abogados; aquí se consolidan los asuntos, el riesgo y la carga <b>por módulo y por abogado</b>. Se recalcula en vivo con lo capturado en cada módulo.</div>
  <div class="kpis" id="intKpis"></div>
  <div class="grid">
   <div class="card s2"><h3>📊 Asuntos por módulo / área</h3><canvas id="cIntMod"></canvas></div>
   <div class="card s2"><h3>👤 Carga consolidada por responsable (todas las áreas)</h3><canvas id="cIntAbo"></canvas></div>
  </div>
  <div class="h">🗂️ Matriz por módulo / área</div><div class="card"><table id="intMatriz"></table></div>
  <div class="h">👥 Responsables por módulo (cada área con su equipo)</div><div id="intAbogados"></div>
 </section>
 <section id="t5" class="ce-tab">
  <div class="note">📊 <b>Dashboard / Cuadro de Mando Integral</b> completo — todas sus vistas (ejecutivo, litigios, productividad, desempeño, equidad, provisión, tiempos &amp; cuellos, agenda, alertas, lecciones, riesgos, gobierno de datos). Integrado aquí; acceso exclusivo de la dirección.</div>
  <iframe id="dashFrame" data-src="dashboard_SIGEJ.html?embed=1" title="Dashboard SIGEJ" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe>
 </section>
 <section id="t6" class="ce-tab">
  <div class="note">⏱️ <b>Horas y Gastos</b> (time &amp; expense) — armonizado en la vista ejecutiva: horas por expediente/abogado, gastos, productividad y costo por asunto.</div>
  <iframe id="horasFrame" data-src="horas_SIGEJ.html?embed=1" title="Horas y Gastos" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe>
 </section>
 <section id="t7" class="ce-tab">
  <div class="note">📑 <b>Reportes en 2 pasos</b> — generación de informes por materia, dependencia, abogado, riesgo, año y exportación (Excel/PDF/Word), integrado en la dirección.</div>
  <iframe id="repFrame" data-src="reportes_SIGEJ.html?embed=1" title="Reportes" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe>
 </section>
 <section id="t9" class="ce-tab"><div class="note">🏛️ <b>Legal por Centro Universitario</b> — cartera jurídica consolidada por CU (integrada en la dirección).</div><iframe id="lcuFrame" data-src="legalcu_SIGEJ.html?embed=1" title="Legal por CU" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe></section>
 <section id="t10" class="ce-tab"><div class="note">🎯 <b>BI Estratégico · Gobernanza (PDI 2025-2031)</b> — indicadores por eje del PDI (integrado en la dirección).</div><iframe id="biFrame" data-src="bipdi_SIGEJ.html?embed=1" title="BI PDI" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe></section>
 <section id="t11" class="ce-tab"><div class="note">🧭 <b>Tablero consolidado de Seguimientos</b> — todas las notas de seguimiento (de módulo y por expediente) del sistema, filtrables por módulo, abogado y fecha. Para revisión de pendientes por la dirección.</div><iframe id="seguFrame" data-src="seguimientos_SIGEJ.html?embed=1" title="Tablero de Seguimientos" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe></section>
 <section id="t13" class="ce-tab"><div class="note">🧑‍⚖️ <b>Permisos, Licencias, Incidencias y Descansos</b> — panel ejecutivo para conocimiento del Abogado General: solicitudes pendientes, incidencias por dependencia, incapacidades, permisos sindicales, estímulos por puntualidad y alertas de posible incumplimiento del CCT.</div><iframe id="labFrame" data-src="laboral_SIGEJ.html?embed=1&amp;vista=panel" title="Permisos y Licencias" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe></section>
 <section id="t12" class="ce-tab"><div class="note">📅 <b>Agenda de la Persona Titular de la Abogacía General</b> — registro y administración de las actividades del titular. Las marcadas como <b>públicas</b> se difunden automáticamente en Transparencia (misma fuente de datos).</div><iframe id="agFrame" data-src="agenda_titular_SIGEJ.html?embed=1" title="Agenda del Titular" style="width:100%;height:84vh;border:1px solid var(--line);border-radius:12px;background:#eef2f7"></iframe></section>
</div>
<div class="drawer" id="ceDrawer"><div class="panel"><span class="x" onclick="sClose()">✕</span>
<h2 id="ceDt"></h2><div class="pq" id="ceDq"></div><div id="ceDc"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;let CH={};
function tab(id){document.querySelectorAll('.ce-tab').forEach(s=>s.classList.toggle('on',s.id===id));
 document.querySelectorAll('.tb').forEach(b=>b.classList.toggle('on',b.getAttribute('data-t')===id));
 if(id==='t5'){var fr=document.getElementById('dashFrame');if(fr&&!fr.src)fr.src=fr.dataset.src;}
 if(id==='t6'){var fh=document.getElementById('horasFrame');if(fh&&!fh.src)fh.src=fh.dataset.src;}
 if(id==='t7'){var fp=document.getElementById('repFrame');if(fp&&!fp.src)fp.src=fp.dataset.src;}
 if(id==='t9'){var fl=document.getElementById('lcuFrame');if(fl&&!fl.src)fl.src=fl.dataset.src;}
 if(id==='t10'){var fb=document.getElementById('biFrame');if(fb&&!fb.src)fb.src=fb.dataset.src;}
 if(id==='t11'){var fs=document.getElementById('seguFrame');if(fs&&!fs.src)fs.src=fs.dataset.src;}
 if(id==='t12'){var fa=document.getElementById('agFrame');if(fa&&!fa.src)fa.src=fa.dataset.src;}
 if(id==='t13'){var flab=document.getElementById('labFrame');if(flab&&!flab.src)flab.src=flab.dataset.src;}
 if(id==='t8')setTimeout(renderIntegracion,20);
 if(id==='t1')setTimeout(ceCompute,30);}
function modAreas(){const out=[];
 try{out.push({mod:'Litigio / Contencioso',ic:'⚖️',rows:(D.comando.exp||[]).map(e=>({resp:e.resp||'',niv:e.niv||'',act:!!e.act}))});}catch(e){}
 const defs=[['Instrumentos (CLM)','📜','sigej_instrumentos','resp','nivel','estado'],['Patrimonio intangible','🧩','sigej_patrimonio','resp','nivel','estado'],['Asuntos internacionales','🌎','sigej_internacional','resp','nivel','estado'],['Normatividad','📖','sigej_normatividad','resp','nivel','estado'],['MASC','🤝','sigej_masc','responsable','','estado'],['Responsabilidades','⚖️','sigej_resp','responsable','','estado'],['Asesoría / consultas','💡','sigej_asesoria','responsable','','estado'],['Proyectos','📌','sigej_proyectos','resp','','estado'],['Oficialía de Partes','📨','sigej_oficialia','resp','nivel','estado'],['Control de Oficios','📋','sigej_oficios','resp','prio','estatus'],['Help Desk (ITSM)','🛠️','sigej_helpdesk','tec','prio','estado'],['Administración · Contable','💵','sigej_adm_contable','none','','estado'],['Administración · Bienes','🏷️','sigej_adm_bienes','resg','','estado'],['Administración · Personal','👥','sigej_adm_personal','none','','estado'],['Transparencia (UTI)','🔎','sigej_uti','responsable','','estado']];
 defs.forEach(d=>{try{const arr=JSON.parse(localStorage.getItem(d[2])||'[]');out.push({mod:d[0],ic:d[1],rows:arr.map(e=>({resp:(e[d[3]]||'').toString().trim(),niv:d[4]?(e[d[4]]||''):'',act:!/^(conclu|terminad|archiv|abrogad|derogad|cancelad|baja|rechazad|cerrad|pagad|comprobad|aplicad|entregad)/i.test(((d[5]?e[d[5]]:e.estado)||'vigente'))}))});}catch(e){}});
 return out;}
function renderIntegracion(){const MA=modAreas();let totA=0,totAct=0,totHi=0;const aboGlobal={};
 const perMod=MA.map(m=>{const rows=m.rows;const act=rows.filter(r=>r.act).length;const hi=rows.filter(r=>r.niv==='Alto'||r.niv==='Crítico').length;
  const abos={};rows.forEach(r=>{if(r.resp){abos[r.resp]=(abos[r.resp]||0)+1;aboGlobal[r.resp]=(aboGlobal[r.resp]||0)+1;}});
  totA+=rows.length;totAct+=act;totHi+=hi;return {mod:m.mod,ic:m.ic,total:rows.length,act:act,hi:hi,abos:abos,nAbo:Object.keys(abos).length};});
 const conDatos=perMod.filter(m=>m.total>0).length;
 const K=[['',totA,'Asuntos (todas las áreas)',''],['',totAct,'Activos','g'],['',totHi,'Riesgo alto','r'],['',Object.keys(aboGlobal).length,'Responsables (únicos)',''],['',conDatos+'/'+perMod.length,'Módulos con datos','y'],['',perMod.length,'Áreas integradas','']];
 document.getElementById('intKpis').innerHTML=K.map(k=>'<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>').join('');
 const wd=perMod.filter(m=>m.total>0);ceChart('cIntMod','bar',wd.map(m=>m.mod.split(' ')[0]),wd.map(m=>m.total),{color:'#0a4d8c'});
 const aboTop=Object.entries(aboGlobal).sort((a,b)=>b[1]-a[1]).slice(0,12);ceChart('cIntAbo','bar',aboTop.map(x=>x[0].split(' ').slice(0,2).join(' ')),aboTop.map(x=>x[1]),{horiz:true,color:'#1aa39a'});
 document.getElementById('intMatriz').innerHTML='<tr><th>Módulo / área</th><th>Asuntos</th><th>Activos</th><th>Riesgo alto</th><th>Responsables</th><th>Principal responsable</th></tr>'+
  perMod.map(m=>{const top=Object.entries(m.abos).sort((a,b)=>b[1]-a[1])[0];return '<tr><td>'+m.ic+' '+m.mod+'</td><td><b>'+m.total+'</b></td><td>'+m.act+'</td><td>'+(m.hi?'<span class="rb" style="background:rgba(192,57,43,.25);color:#ff9b8d">'+m.hi+'</span>':'0')+'</td><td>'+m.nAbo+'</td><td>'+(top?top[0]+' ('+top[1]+')':'—')+'</td></tr>';}).join('');
 document.getElementById('intAbogados').innerHTML=perMod.filter(m=>m.nAbo>0).map(m=>{const list=Object.entries(m.abos).sort((a,b)=>b[1]-a[1]);return '<div class="modcard"><b style="color:#0a4d8c">'+m.ic+' '+m.mod+'</b> <span style="color:#64748b;font-size:11px">· '+m.nAbo+' responsable(s)</span><div style="margin-top:6px">'+list.map(x=>'<span class="chip">'+x[0]+' · '+x[1]+'</span>').join('')+'</div></div>';}).join('')||'<div style="color:#64748b;font-size:12px;padding:10px">Captura asuntos con responsable en cada módulo para ver el equipo por área.</div>';}
function cePad(n){return (n<10?'0':'')+n;}
/* ---------- t1 Centro de Mando (autoactualizable) ---------- */
function ceUniverse(){
 let base=D.comando.exp.map(e=>Object.assign({},e));const byNum={};base.forEach(e=>byNum[e.num]=e);
 try{const ov=JSON.parse(localStorage.getItem('sigej_estado')||'{}');Object.keys(ov).forEach(n=>{if(byNum[n]){byNum[n].est=ov[n];byNum[n].act=ov[n].toUpperCase()!=='CONCLUIDO';byNum[n].stc=byNum[n].stc||ov[n]==='Laudo'||ov[n]==='Sentencia';byNum[n].mod=true;}});}catch(e){}
 try{const re=JSON.parse(localStorage.getItem('sigej_reasig')||'{}');Object.keys(re).forEach(n=>{if(byNum[n]){byNum[n].resp=re[n];byNum[n].mod=true;}});}catch(e){}
 let nuevos=0;
 try{const cap=JSON.parse(localStorage.getItem('sigej_capturas')||'[]');cap.forEach(r=>{base.push({num:r.num,mat:r.materia_fina||r.materia||'(s/d)',via:r.via||'Ordinaria',est:r.estado,resp:r.responsable||'(sin asignar)',niv:r.nivel_riesgo,sc:r.score||0,monto:+r.monto||0,an:r.anio,act:(r.estado||'').toUpperCase()!=='CONCLUIDO',sent:r.sentido,dep:r.dependencia,centro:r.centro,stc:(r.estado==='Laudo'||r.estado==='Sentencia')||!!r.sentido,nuevo:true});nuevos++;});}catch(e){}
 base._nuevos=nuevos;return base;
}
function ceCnt(arr,key){const o={};arr.forEach(e=>{const v=e[key]||'(s/d)';o[v]=(o[v]||0)+1;});return o;}
const PAL=['#1aa39a','#0a4d8c','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#16a085','#5d6d7e','#9d174d'];
function ceChart(id,type,labels,data,opts){if(CH[id])CH[id].destroy();const ctx=document.getElementById(id);if(!ctx)return;
 CH[id]=new Chart(ctx,{type:type,data:{labels:labels,datasets:[{data:data,backgroundColor:opts&&opts.multi?PAL:(opts&&opts.color||'#1aa39a'),borderColor:opts&&opts.line?'#1aa39a':undefined,fill:opts&&opts.line?true:undefined,tension:.3}]},
  options:{indexAxis:opts&&opts.horiz?'y':'x',plugins:{legend:{display:!!(opts&&opts.legend),position:'right',labels:{color:'#0a4d8c',font:{size:10}}}},
   scales:type==='doughnut'?{}:{x:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}},y:{ticks:{color:'#64748b',font:{size:9}},grid:{color:'#e2e8f0'}}}}});}
function ceCompute(){const U=ceUniverse();const act=U.filter(e=>e.act);
 const alto=U.filter(e=>e.niv==='Alto'||e.niv==='Crítico').length;
 const pasivo=act.reduce((s,e)=>s+(+e.monto||0),0);
 const stc=U.filter(e=>e.stc).length;
 let masc=0,resp=0,venc=0;
 try{const m=JSON.parse(localStorage.getItem('sigej_masc')||'[]');masc=m.length;}catch(e){}
 try{const r=JSON.parse(localStorage.getItem('sigej_resp')||'[]');resp=r.length;}catch(e){}
 try{const HOY=new Date(2026,5,18);const en=JSON.parse(localStorage.getItem('sigej_enr')||'{}');Object.keys(en).forEach(n=>(en[n].agenda||[]).forEach(a=>{const d=Math.round((new Date(a.fecha+'T00:00:00')-HOY)/864e5);if(d>=0&&d<=30)venc++;}));}catch(e){}
 const K=[['exp',U.length,'Expedientes',''],['act',act.length,'Activos','g'],['con',U.length-act.length,'Concluidos',''],['alt',alto,'Alto riesgo','r'],
  ['pas','$'+(pasivo/1e6).toFixed(2)+'M','Pasivo activo','y'],['stc',stc,'Con sentencia/laudo',''],['masc',masc,'Convenios MASC',''],['resp',resp,'Responsabilidades','y'],
  ['ven',venc,'Vencimientos ≤30d','r'],['nuv',U._nuevos,'Capturados localmente','g']];
 document.getElementById('ceKpis').innerHTML=K.map(k=>`<div class="kpi ${k[3]}"><div class="n">${k[1]}</div><div class="l">${k[2]}</div></div>`).join('');
 const mods=U.filter(e=>e.mod||e.nuevo).length;
 const nv=document.getElementById('ceNov');
 if(mods){nv.style.display='block';nv.innerHTML='✨ '+mods+' cambio(s) local(es) aplicado(s) en vivo ('+U._nuevos+' nuevos · '+(mods-U._nuevos)+' modificados). El cuadro de mando ya los refleja.';}else nv.style.display='none';
 const mat=ceCnt(U,'mat');ceChart('cMat','doughnut',Object.keys(mat),Object.values(mat),{multi:true,legend:true});
 const rie={};['Crítico','Alto','Medio','Bajo'].forEach(n=>rie[n]=U.filter(e=>e.niv===n).length);ceChart('cRie','bar',Object.keys(rie),Object.values(rie),{color:['#c0392b','#e08e0b','#1aa39a','#5d6d7e']});
 const an=ceCnt(U.filter(e=>e.an),'an');const ak=Object.keys(an).sort();ceChart('cAnio','line',ak,ak.map(k=>an[k]),{line:true});
 const abo=ceCnt(act,'resp');const ae=Object.entries(abo).sort((a,b)=>b[1]-a[1]).slice(0,12);ceChart('cAbo','bar',ae.map(x=>x[0].split(' ').slice(0,2).join(' ')),ae.map(x=>x[1]),{horiz:true,color:'#0a4d8c'});
 const via=ceCnt(U,'via');ceChart('cVia','doughnut',Object.keys(via),Object.values(via),{multi:true,legend:true});
 const est=ceCnt(U,'est');ceChart('cEst','bar',Object.keys(est),Object.values(est),{horiz:true,color:'#7e57c2'});
 const dep=ceCnt(U.filter(e=>e.dep),'dep');const de=Object.entries(dep).sort((a,b)=>b[1]-a[1]).slice(0,12);ceChart('cDep','bar',de.map(x=>x[0].slice(0,16)),de.map(x=>x[1]),{color:'#c0392b'});
 const topd=de.slice(0,8).map(x=>x[0]);const mats=['Laboral','Administrativa','Civil'];let mx=1;
 const H=topd.map(d=>{const row={d:d};mats.forEach(m=>{row[m]=U.filter(e=>e.dep===d&&e.mat===m).length;mx=Math.max(mx,row[m]);});return row;});
 document.getElementById('ceHeat').innerHTML='<table class="heat"><tr><th style="text-align:left">Dependencia</th>'+mats.map(m=>'<th>'+m+'</th>').join('')+'</tr>'+
  H.map(r=>'<tr><td style="text-align:left;color:#0a4d8c">'+r.d.slice(0,22)+'</td>'+mats.map(m=>{const a=r[m]/mx;return '<td style="background:rgba(192,57,43,'+(0.1+a*0.8)+');color:#fff">'+r[m]+'</td>';}).join('')+'</tr>').join('')+'</table>';
 const t=new Date();document.getElementById('upd').textContent='actualizado '+cePad(t.getHours())+':'+cePad(t.getMinutes())+':'+cePad(t.getSeconds());
}
window.addEventListener('storage',ceCompute);
window.addEventListener('focus',()=>{if(document.getElementById('t1').classList.contains('on'))ceCompute();});
/* ---------- t2 Cuadro de Mando Integral ---------- */
(function(){const B=D.bsc;
 function persp(t,c,rows){return '<div class="card"><h3 style="border-bottom:3px solid '+c+';padding-bottom:6px;color:'+c+'">'+t+'</h3>'+rows.map(r=>'<div class="row"><span>'+r[0]+'</span><b>'+r[1]+'</b></div>').join('')+'</div>';}
 document.getElementById('ceBsc').innerHTML=
  persp('⚖️ Jurídica','#5b9bd5',B.juridica)+
  persp('💰 Financiera','#ff9b8d',B.financiera)+
  persp('⚙️ Procesos','#8fe0d8',B.procesos)+
  persp('🎓 Aprendizaje','#ffce82',B.aprendizaje);
})();
/* ---------- t3 Inteligencia Jurídica ---------- */
const T=D.lec.tipos;let SEL=0;
let CK=JSON.parse(localStorage.getItem('sigej_checklist')||'{}');
function saveCK(){localStorage.setItem('sigej_checklist',JSON.stringify(CK));}
const RI={'Bajo':['🟢','b-b'],'Medio':['🟡','b-m'],'Alto':['🔴','b-r'],'Crítico':['⚫','b-r']};
document.getElementById('ceList').innerHTML=T.map((t,i)=>'<div class="li '+(i===0?'sel':'')+'" onclick="iSel('+i+')"><div class="t">'+(RI[t.riesgo]?RI[t.riesgo][0]:'')+' '+t.label+'</div><div class="m">'+t.n+' asuntos · '+t.clasif+'</div></div>').join('');
function iSel(i){SEL=i;document.querySelectorAll('#ceList .li').forEach((e,j)=>e.classList.toggle('sel',j===i));iDetail();}
function iVbadge(v){return v==='verificado'?'<span class="ok">✓ verificado en fuente oficial</span>':'<span class="warn">⚠ a confirmar en SJF</span>';}
function iDetail(){const t=T[SEL];const ri=RI[t.riesgo]||['🟡','b-m'];
 const ck=CK[t.sent]||{};
 const deps=t.deps.length?'<ul>'+t.deps.map(d=>'<li>'+d[0]+' <b>('+d[1]+')</b></li>').join('')+'</ul>':'—';
 const abos=t.abogados.length?'<ul>'+t.abogados.map(a=>'<li>'+(a[0]||'')+' <b>('+a[1]+')</b></li>').join('')+'</ul>':'—';
 const cau=t.causas_kb.length?'<ul>'+t.causas_kb.map(c=>'<li>'+c+'</li>').join('')+'</ul>':'—';
 const nlp=t.causas_nlp.length?t.causas_nlp.map(c=>c[0]+' ('+c[1]+')').join(' · '):'sin indicios';
 const chk=t.checklist.length?t.checklist.map((c,k)=>'<label class="chk"><input type="checkbox" '+(ck[k]?'checked':'')+' onchange="iTick(\''+t.sent+'\','+k+',this.checked)"> '+c+'</label>').join(''):'<div class="kv">Sin checklist para este tipo.</div>';
 document.getElementById('ceDetail').innerHTML=
  '<div class="card"><h2>'+t.label+'</h2><div class="badges"><span class="bdg '+ri[1]+'">'+ri[0]+' Riesgo '+t.riesgo+'</span><span class="bdg b-c">'+t.clasif+'</span><span class="bdg" style="background:#eef2f7;color:#475569">'+t.n+' asuntos</span>'+iVbadge(t.verif)+'</div>'+
  '<div class="kv"><b>¿Era previsible?</b> Evitabilidad: <b>'+t.evit+'</b> · Factor: <b>'+t.factor+'</b> · Prob. de repetición: <b>'+t.rep+'</b> · Impacto económico (piso): <b>$'+(t.impacto||0).toLocaleString('es-MX')+'</b></div></div>'+
  '<div class="grid2"><div class="card"><h2 style="font-size:14px">¿Por qué ocurrió? — Causa raíz (Ishikawa)</h2><div class="box">'+cau+'<div style="margin-top:8px;font-size:11.5px;color:#64748b"><b>Indicios NLP (a validar):</b> '+nlp+'</div></div></div>'+
  '<div class="card"><h2 style="font-size:14px">¿Quién y dónde?</h2><div class="box"><b>Dependencias con incidencia:</b> '+deps+'<div style="margin-top:6px"><b>Abogados que intervinieron:</b> '+abos+'</div></div></div></div>'+
  '<div class="card"><h2 style="font-size:14px">¿Qué hacer para que no se repita?</h2>'+
   '<div class="lec"><b>💡 Lección aprendida:</b> '+t.leccion+'</div><div class="acc"><b>🛡️ Acción preventiva:</b> '+t.accion+'</div>'+
   '<div style="margin-top:10px"><b style="font-size:13px;color:#00254a">✅ Checklist preventivo</b></div>'+chk+
   '<div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap"><button class="bw" onclick="iMemo()">📄 Memo de prevención (Word)</button><button class="b1" onclick="window.print()">🖨️ Ficha (PDF)</button><button class="b3" onclick="iExpChk()">⬇ Checklist (CSV)</button></div>'+
   '<div class="kv" style="margin-top:10px"><b>Fundamento:</b> '+t.fund+'</div></div>';}
function iTick(sent,k,v){if(!CK[sent])CK[sent]={};CK[sent][k]=v;saveCK();}
function iMemo(){const t=T[SEL];
 const body='<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Centro de Inteligencia Jurídica</div>'+
  '<h2>MEMORÁNDUM DE PREVENCIÓN — '+t.label.toUpperCase()+'</h2>'+
  '<p style="font-size:11pt"><b>Universo analizado:</b> '+t.n+' asuntos · <b>Clasificación:</b> '+t.clasif+' · <b>Nivel de riesgo:</b> '+t.riesgo+' · <b>Impacto económico (piso):</b> $'+(t.impacto||0).toLocaleString('es-MX')+'</p>'+
  '<h3>1. Diagnóstico (¿por qué ocurrió?)</h3><p style="font-size:11pt">Causa raíz (Ishikawa): '+(t.causas_kb.join('; ')||'—')+'.</p>'+
  '<h3>2. Dependencias y responsables</h3><p style="font-size:11pt">Mayor incidencia: '+(t.deps.map(d=>d[0]+' ('+d[1]+')').join(', ')||'—')+'. Abogados: '+(t.abogados.map(a=>a[0]+' ('+a[1]+')').join(', ')||'—')+'.</p>'+
  '<h3>3. Evitabilidad</h3><p style="font-size:11pt">'+t.evit+' · Factor '+t.factor+' · Probabilidad de repetición '+t.rep+'.</p>'+
  '<h3>4. Lección aprendida</h3><p style="font-size:11pt">'+t.leccion+'</p>'+
  '<h3>5. Acción preventiva</h3><p style="font-size:11pt">'+t.accion+'</p>'+
  '<h3>6. Checklist obligatorio</h3><ul>'+t.checklist.map(c=>'<li>'+c+'</li>').join('')+'</ul>'+
  '<h3>7. Fundamento jurídico</h3><p style="font-size:11pt">'+t.fund+' ('+(t.verif==='verificado'?'verificado en fuente oficial':'a confirmar')+').</p>'+
  '<br><br><div style="text-align:center">_______________________________<br>Oficina de la Abogacía General · UdeG</div>';
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Memo_prevencion_'+t.sent.replace(/[\/ ]/g,'-')+'.doc';a.click();}
function iExpChk(){const t=T[SEL];const ck=CK[t.sent]||{};const esc=v=>'"'+String(v).replace(/"/g,'""')+'"';
 const csv='item,cumplido\n'+t.checklist.map((c,k)=>esc(c)+','+(ck[k]?'sí':'no')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='checklist_'+t.sent.replace(/[\/ ]/g,'-')+'.csv';a.click();}
/* ---------- t4 Sala de Mando ---------- */
const AD=D.altad;
function sBars(o){const m=Math.max(...Object.values(o));return '<div class="bars">'+Object.entries(o).map(([k,v])=>
 '<div class="bar"><span class="t">'+k+'</span><span class="track"><span class="fill" style="width:'+Math.round(100*v/m)+'%"></span></span><span class="v">'+v+'</span></div>').join('')+'</div>';}
function sTbl(rows,cols){return '<table><tr>'+cols.map(c=>'<th>'+c[1]+'</th>').join('')+'</tr>'+
 rows.map(r=>'<tr>'+cols.map(c=>{let v=r[c[0]];if(c[0]=='nivel')v='<span class="pill '+v+'">'+v+'</span>';
 if(c[0]=='monto')v='$'+Number(v).toLocaleString('es-MX');return '<td>'+(v===undefined||v===''?'—':v)+'</td>';}).join('')+'</tr>').join('')+'</table>';}
const ST=[
 {ic:'📂',q:'¿Cuántos expedientes activos existen?',big:AD.q1_activos.valor,sub:AD.q1_activos.pct+'% del total ('+AD.q1_activos.total+')',cls:'r-teal',
  title:'Expedientes activos',det:()=>'<p style="color:#64748b">'+AD.q1_activos.valor+' activos de '+AD.q1_activos.total+' (criterio: estado ≠ CONCLUIDO).</p>'+sBars({'Activos':AD.q1_activos.valor,'Concluidos':AD.q1_activos.total-AD.q1_activos.valor})},
 {ic:'⚖️',q:'¿Materias con mayor litigiosidad?',big:Object.keys(AD.q2_materias)[0],sub:Object.values(AD.q2_materias)[0]+' expedientes',cls:'r-teal',
  title:'Litigiosidad por materia',det:()=>sBars(AD.q2_materias)},
 {ic:'🏛️',q:'¿Qué dependencias generan más conflictos?',big:Object.keys(AD.q3_dependencias)[0],sub:Object.values(AD.q3_dependencias)[0]+' expedientes',cls:'r-teal',
  title:'Dependencias con más conflictos',det:()=>sBars(AD.q3_dependencias)},
 {ic:'🔥',q:'¿Cuáles son los asuntos de alto riesgo?',big:AD.q4_alto_riesgo.conteo,sub:(AD.q4_alto_riesgo.niveles['Crítico']||0)+' críticos · '+(AD.q4_alto_riesgo.niveles['Alto']||0)+' altos',cls:'r-red',
  title:'Asuntos de alto riesgo (proxy)',det:()=>sTbl(AD.q4_alto_riesgo.top,[['exp','Expediente'],['materia','Materia'],['dependencia','Dependencia'],['nivel','Nivel'],['score','Score'],['drivers','Factores']])},
 {ic:'💰',q:'¿Cuál es el pasivo contingente institucional?',big:'$'+(AD.q5_pasivo.piso_parcial/1e6).toFixed(2)+'M',sub:'piso parcial · '+AD.q5_pasivo.exp_con_monto+' exp. con monto',cls:'r-gold',
  title:'Pasivo contingente (piso parcial)',det:()=>'<p style="color:#64748b">Suma de montos legibles: <b>$'+AD.q5_pasivo.piso_parcial.toLocaleString('es-MX')+'</b> en '+AD.q5_pasivo.exp_con_monto+' de '+AD.q5_pasivo.total+' expedientes. El resto tiene el monto en texto libre no estructurado → cifra real probablemente mayor.</p>'},
 {ic:'👤',q:'¿Qué abogados tienen mayor carga?',big:Object.keys(AD.q6_abogados)[0].split(' ')[0]+' '+(Object.keys(AD.q6_abogados)[0].split(' ')[1]||''),sub:Object.values(AD.q6_abogados)[0]+' expedientes',cls:'r-amber',
  title:'Carga de trabajo por abogado',det:()=>sBars(AD.q6_abogados)},
 {ic:'🎯',q:'¿Cuál es la tasa de éxito procesal?',big:AD.q7_tasa_exito.pct+'%',sub:AD.q7_tasa_exito.fav+' fav · '+AD.q7_tasa_exito.desf+' desf',cls:'r-gold',
  title:'Tasa de éxito procesal',det:()=>'<p style="color:#64748b">Favorables / (Favorables + Desfavorables) = '+AD.q7_tasa_exito.fav+'/('+AD.q7_tasa_exito.fav+'+'+AD.q7_tasa_exito.desf+') = <b>'+AD.q7_tasa_exito.pct+'%</b>.</p>'+sBars({'Favorables':AD.q7_tasa_exito.fav,'Desfavorables':AD.q7_tasa_exito.desf})},
 {ic:'🚨',q:'¿Qué asuntos requieren atención inmediata?',big:AD.q8_atencion.conteo,sub:'en laudo/sentencia, susp. concedida o críticos',cls:'r-red',
  title:'Atención inmediata',det:()=>sTbl(AD.q8_atencion.top,[['exp','Expediente'],['materia','Materia'],['dependencia','Dependencia'],['abogado','Abogado'],['estado','Etapa'],['nivel','Riesgo'],['score','Score']])},
];
(function(){const g=document.getElementById('ceGrid');
 ST.forEach((t,i)=>{const e=document.createElement('div');e.className='tile '+t.cls;
  e.innerHTML='<div class="ic">'+t.ic+'</div><div class="q">'+t.q+'</div><div class="big">'+t.big+'</div><div class="sub">'+t.sub+'</div>';
  e.onclick=()=>{document.getElementById('ceDt').textContent=t.title;document.getElementById('ceDq').textContent=t.q;
  document.getElementById('ceDc').innerHTML=t.det();document.getElementById('ceDrawer').classList.add('on');};g.appendChild(e);});})();
function sClose(){document.getElementById('ceDrawer').classList.remove('on');}
document.getElementById('ceDrawer').onclick=e=>{if(e.target.id=='ceDrawer')sClose();};
/* init */
iDetail();ceCompute();
</script>
__SNIP__
</body></html>"""
html=TPL.replace("__DATA__",DATA).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"centro_ejecutivo_SIGEJ.html","w",encoding="utf-8").write(html)
print("centro_ejecutivo_SIGEJ.html OK -",len(html),"bytes")
print("BSC pasivo",bsc["financiera"][0][1],"| reserva",bsc["financiera"][1][1],"| dur",bsc["procesos"][0][1],"| altoR",altoR,"| ampl",ampl)
