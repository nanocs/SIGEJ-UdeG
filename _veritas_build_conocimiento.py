# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/lecciones_pro.json",encoding="utf-8"))
DATA=json.dumps(d,ensure_ascii=False)
NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="comando_SIGEJ.html">🛰️ Centro de Mando</a><a href="dashboard_SIGEJ.html">📊 Dashboard</a><a href="conocimiento_SIGEJ.html" class="act">🧠 Inteligencia</a><a href="modulo_expedientes_SIGEJ.html">📁 Expedientes</a><a href="proyectos_SIGEJ.html">📌 Proyectos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="asesoria_SIGEJ.html">💡 Asesoría</a><a href="masc_SIGEJ.html">🤝 MASC</a><a href="resp_SIGEJ.html">⚖️ Responsabilidades</a><a href="alertas_centro_SIGEJ.html">🔔 Alertas</a></div>'''
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Inteligencia Jurídica</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--ok:#1f9d6b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#f4f6f9;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:14px 24px}
header h1{margin:0;font-size:18px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:16px 24px;max-width:1340px;margin:auto;display:grid;grid-template-columns:280px 1fr;gap:16px}
@media(max-width:900px){.wrap{grid-template-columns:1fr}}
.list{background:#fff;border-radius:12px;padding:10px;box-shadow:0 1px 3px rgba(0,0,0,.07);max-height:80vh;overflow:auto}
.li{padding:10px 12px;border-radius:9px;cursor:pointer;margin-bottom:4px;border-left:4px solid var(--line)}
.li:hover{background:#f4f6f9}.li.sel{background:#f0f6ff;border-left-color:var(--azul2)}
.li .t{font-size:13px;font-weight:600;color:var(--azul)}.li .m{font-size:11px;color:var(--mut)}
.card{background:#fff;border-radius:12px;padding:18px;box-shadow:0 1px 3px rgba(0,0,0,.07);margin-bottom:14px}
.card h2{margin:0 0 4px;font-size:17px;color:var(--azul)}
.badges{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}
.bdg{font-size:11px;padding:3px 9px;border-radius:10px;font-weight:600}.b-r{background:#fdecea;color:#c0392b}.b-a{background:#fef3e0;color:#b9770e}.b-m{background:#fffbe9;color:#a07a10}.b-b{background:#e6f6ee;color:#1f7a4d}.b-c{background:#e6f0fb;color:#0a4d8c}
.ok{background:#e6f6ee;color:#1f7a4d;border:1px solid #9fd9b8;border-radius:8px;padding:1px 8px;font-size:11px}.warn{background:#fff8e6;color:#8a6d1a;border:1px solid #f0e0a8;border-radius:8px;padding:1px 8px;font-size:11px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:760px){.grid2{grid-template-columns:1fr}}
.box{background:#f8fafc;border-radius:9px;padding:11px;font-size:12.5px}.box b{color:var(--azul)}.box ul{margin:5px 0 0;padding-left:18px}
.chk{display:flex;align-items:center;gap:8px;padding:6px 0;font-size:12.5px;border-bottom:1px solid var(--line)}
.lec{background:#f0fbf6;border:1px solid #cdeede;border-radius:9px;padding:11px;font-size:12.5px;margin-top:8px}
.acc{background:#fff8e6;border:1px solid #f0e0a8;border-radius:9px;padding:11px;font-size:12.5px;margin-top:8px}
button{padding:8px 13px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
.b1{background:var(--azul2)}.bw{background:#2b579a}.b3{background:var(--ok)}
.kv{font-size:12px;color:var(--mut)}.kv b{color:var(--ink)}
footer{padding:14px 24px;color:var(--mut);font-size:11px;text-align:center}
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
<header><h1>🧠 SIGEJ-UdeG · Centro de Inteligencia Jurídica</h1><div class="s">Legal Analytics + Gestión del Conocimiento + Lecciones Aprendidas + Prevención de Riesgos</div></header>
__NAV__
<div class="wrap">
 <div class="list" id="list"></div>
 <div id="detail"></div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const T=D.tipos;let SEL=0;
let CK=JSON.parse(localStorage.getItem('sigej_checklist')||'{}');
function saveCK(){localStorage.setItem('sigej_checklist',JSON.stringify(CK));}
const RI={'Bajo':['🟢','b-b'],'Medio':['🟡','b-m'],'Alto':['🔴','b-r'],'Crítico':['⚫','b-r']};
document.getElementById('list').innerHTML=T.map((t,i)=>`<div class="li ${i===0?'sel':''}" onclick="sel(${i})"><div class="t">${RI[t.riesgo]?RI[t.riesgo][0]:''} ${t.label}</div><div class="m">${t.n} asuntos · ${t.clasif}</div></div>`).join('');
function sel(i){SEL=i;document.querySelectorAll('.li').forEach((e,j)=>e.classList.toggle('sel',j===i));detail();}
function vbadge(v){return v==='verificado'?'<span class="ok">✓ verificado en fuente oficial</span>':'<span class="warn">⚠ a confirmar en SJF</span>';}
function detail(){const t=T[SEL];const ri=RI[t.riesgo]||['🟡','b-m'];
 const ck=CK[t.sent]||{};
 const deps=t.deps.length?'<ul>'+t.deps.map(d=>'<li>'+d[0]+' <b>('+d[1]+')</b></li>').join('')+'</ul>':'—';
 const abos=t.abogados.length?'<ul>'+t.abogados.map(a=>'<li>'+(a[0]||'')+' <b>('+a[1]+')</b></li>').join('')+'</ul>':'—';
 const cau=t.causas_kb.length?'<ul>'+t.causas_kb.map(c=>'<li>'+c+'</li>').join('')+'</ul>':'—';
 const nlp=t.causas_nlp.length?t.causas_nlp.map(c=>c[0]+' ('+c[1]+')').join(' · '):'sin indicios';
 const chk=t.checklist.length?t.checklist.map((c,k)=>`<label class="chk"><input type="checkbox" ${ck[k]?'checked':''} onchange="tick('${t.sent}',${k},this.checked)"> ${c}</label>`).join(''):'<div class="kv">Sin checklist para este tipo.</div>';
 document.getElementById('detail').innerHTML=
  `<div class="card"><h2>${t.label}</h2><div class="badges"><span class="bdg ${ri[1]}">${ri[0]} Riesgo ${t.riesgo}</span><span class="bdg b-c">${t.clasif}</span><span class="bdg" style="background:#eef2f7;color:#475569">${t.n} asuntos</span>${vbadge(t.verif)}</div>`+
  `<div class="kv"><b>¿Era previsible?</b> Evitabilidad: <b>${t.evit}</b> · Factor: <b>${t.factor}</b> · Prob. de repetición: <b>${t.rep}</b> · Impacto económico (piso): <b>$${(t.impacto||0).toLocaleString('es-MX')}</b></div></div>`+
  `<div class="grid2"><div class="card"><h2 style="font-size:14px">¿Por qué ocurrió? — Causa raíz (Ishikawa)</h2><div class="box">${cau}<div style="margin-top:8px;font-size:11.5px;color:#64748b"><b>Indicios NLP (a validar):</b> ${nlp}</div></div></div>`+
  `<div class="card"><h2 style="font-size:14px">¿Quién y dónde?</h2><div class="box"><b>Dependencias con incidencia:</b> ${deps}<div style="margin-top:6px"><b>Abogados que intervinieron:</b> ${abos}</div></div></div></div>`+
  `<div class="card"><h2 style="font-size:14px">¿Qué hacer para que no se repita?</h2>`+
   `<div class="lec"><b>💡 Lección aprendida:</b> ${t.leccion}</div><div class="acc"><b>🛡️ Acción preventiva:</b> ${t.accion}</div>`+
   `<div style="margin-top:10px"><b style="font-size:13px;color:#00254a">✅ Checklist preventivo</b></div>${chk}`+
   `<div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap"><button class="bw" onclick="memo()">📄 Memo de prevención (Word)</button><button class="b1" onclick="window.print()">🖨️ Ficha (PDF)</button><button class="b3" onclick="expChk()">⬇ Checklist (CSV)</button></div>`+
   `<div class="kv" style="margin-top:10px"><b>Fundamento:</b> ${t.fund}</div></div>`;}
function tick(sent,k,v){if(!CK[sent])CK[sent]={};CK[sent][k]=v;saveCK();}
function memo(){const t=T[SEL];
 const body=`<div style="text-align:center"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General · Centro de Inteligencia Jurídica</div>`+
  `<h2>MEMORÁNDUM DE PREVENCIÓN — ${t.label.toUpperCase()}</h2>`+
  `<p style="font-size:11pt"><b>Universo analizado:</b> ${t.n} asuntos · <b>Clasificación:</b> ${t.clasif} · <b>Nivel de riesgo:</b> ${t.riesgo} · <b>Impacto económico (piso):</b> $${(t.impacto||0).toLocaleString('es-MX')}</p>`+
  `<h3>1. Diagnóstico (¿por qué ocurrió?)</h3><p style="font-size:11pt">Causa raíz (Ishikawa): ${t.causas_kb.join('; ')||'—'}.</p>`+
  `<h3>2. Dependencias y responsables</h3><p style="font-size:11pt">Mayor incidencia: ${t.deps.map(d=>d[0]+' ('+d[1]+')').join(', ')||'—'}. Abogados: ${t.abogados.map(a=>a[0]+' ('+a[1]+')').join(', ')||'—'}.</p>`+
  `<h3>3. Evitabilidad</h3><p style="font-size:11pt">${t.evit} · Factor ${t.factor} · Probabilidad de repetición ${t.rep}.</p>`+
  `<h3>4. Lección aprendida</h3><p style="font-size:11pt">${t.leccion}</p>`+
  `<h3>5. Acción preventiva</h3><p style="font-size:11pt">${t.accion}</p>`+
  `<h3>6. Checklist obligatorio</h3><ul>`+t.checklist.map(c=>'<li>'+c+'</li>').join('')+'</ul>'+
  `<h3>7. Fundamento jurídico</h3><p style="font-size:11pt">${t.fund} (${t.verif==='verificado'?'verificado en fuente oficial':'a confirmar'}).</p>`+
  `<br><br><div style="text-align:center">_______________________________<br>Oficina de la Abogacía General · UdeG</div>`;
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri;margin:55px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Memo_prevencion_'+t.sent.replace(/[\/ ]/g,'-')+'.doc';a.click();}
function expChk(){const t=T[SEL];const ck=CK[t.sent]||{};const esc=v=>'"'+String(v).replace(/"/g,'""')+'"';
 const csv='item,cumplido\n'+t.checklist.map((c,k)=>esc(c)+','+(ck[k]?'sí':'no')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='checklist_'+t.sent.replace(/[\/ ]/g,'-')+'.csv';a.click();}
detail();
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
open("/Users/edithroque/Documents/CLAUDE/conocimiento_SIGEJ.html","w",encoding="utf-8").write(TPL.replace("__DATA__",DATA).replace("__NAV__",NAV))
print("conocimiento_SIGEJ.html OK")
