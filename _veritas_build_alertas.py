# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/alertas_centro_data.json",encoding="utf-8"))
DATA=json.dumps(d,ensure_ascii=False)
NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="modulo_expedientes_SIGEJ.html">📁 Expedientes</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="proyectos_SIGEJ.html">📌 Proyectos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="asesoria_SIGEJ.html">💡 Asesoría</a><a href="captura_expediente_SIGEJ.html">➕ Captura</a><a href="abogados_SIGEJ.html">👤 Abogados</a><a href="documental_SIGEJ.html">🗂️ Documental</a><a href="transparencia_SIGEJ.html">🔎 Transparencia</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="masc_SIGEJ.html">🤝 MASC</a><a href="resp_SIGEJ.html">⚖️ Responsabilidades</a><a href="alertas_centro_SIGEJ.html" class="act">🔔 Alertas</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Centro de Alertas y Riesgo</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--amber:#e08e0b;--orange:#ea580c;--ok:#1f9d6b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#f4f6f9;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
.hero{background:linear-gradient(120deg,#06182c,#0a3a6b);color:#fff;padding:16px 24px}
.hero h1{margin:0;font-size:18px}.hero .s{opacity:.8;font-size:12px;margin-top:2px}
.strat{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin-top:12px}
.sc{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.15);border-radius:12px;padding:12px}
.sc .n{font-size:23px;font-weight:800}.sc .l{font-size:11px;color:#aebfd6;margin-top:2px}
.sc.r .n{color:#ff9b8d}.sc.y .n{color:#ffce82}
.navbar{background:#06182c;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:16px 24px;max-width:1340px;margin:auto}
.h{font-size:14px;color:var(--azul);font-weight:700;margin:18px 0 10px}
.cats{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.cat{background:#fff;border-radius:11px;padding:13px;box-shadow:0 1px 3px rgba(0,0,0,.07);border-left:5px solid var(--red);display:flex;justify-content:space-between;align-items:center}
.cat.cap{border-left-color:#9fb3c8}
.cat .t{font-size:12.5px;font-weight:600}.cat .n{font-size:24px;font-weight:800;color:var(--azul)}
.buckets{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:9px}
.bk{background:#fff;border-radius:10px;padding:12px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.bk .n{font-size:22px;font-weight:800}.bk .l{font-size:11px;color:var(--mut)}
.bk.b7 .n{color:#c0392b}.bk.b15 .n{color:#ea580c}.bk.b30 .n{color:#e08e0b}
.card{background:#fff;border-radius:12px;padding:14px;box-shadow:0 1px 3px rgba(0,0,0,.07)}
table{width:100%;border-collapse:collapse;font-size:12.5px}th,td{padding:7px 9px;text-align:left;border-bottom:1px solid var(--line)}th{background:#eef2f7;color:var(--mut)}
.rb{font-size:10px;padding:2px 8px;border-radius:9px;font-weight:600}.rb-Crítico{background:#fdecea;color:#c0392b}.rb-Alto{background:#fff0e6;color:#ea580c}.rb-Medio{background:#fffbe9;color:#a07a10}.rb-Bajo{background:#e6f6ee;color:#1f7a4d}.rb-Indeterminado{background:#eef2f7;color:#64748b}
.al{background:#fff;border-radius:11px;padding:13px;margin-bottom:9px;box-shadow:0 1px 3px rgba(0,0,0,.06);border-left:5px solid #9fb3c8}
.al.s-rojo{border-left-color:#c0392b}.al.s-naranja{border-left-color:#ea580c}.al.s-amar{border-left-color:#e08e0b}.al.s-verde{border-left-color:#1f9d6b}
.al .top{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:center}
.al .exp{font-size:14px;font-weight:700;color:var(--azul)}
.gauge{width:46px;height:46px;border-radius:50%;text-align:center;line-height:46px;font-weight:800;color:#fff;font-size:14px}
.g-rojo{background:#c0392b}.g-naranja{background:#ea580c}.g-amar{background:#e08e0b}.g-verde{background:#1f9d6b}
.al .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:6px;margin-top:8px;font-size:11.5px}
.al .kv b{color:var(--ink)}.al .kv{color:var(--mut)}
.al .intel{background:#f8fafc;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:11.5px}
.warn{background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:9px 11px;font-size:11.5px;color:#8a6d1a;margin:12px 0}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px}.bar select{padding:6px 8px;border:1px solid var(--line);border-radius:6px;font-size:12px}
footer{padding:14px 24px;color:var(--mut);font-size:11px;text-align:center}
/* LIGHT-UNIF · tema claro institucional — Manual VI (fondo blanco, tarjetas con sombra, pie naranja) */
body{background:#eef2f7!important;color:#0a1f3c!important}
.card,.kpi,.it,.panel{box-shadow:0 1px 3px rgba(2,40,90,.07)!important}
.navbar a{color:#c2d2e8!important}.navbar a:hover,.navbar a.act{color:#fff!important}
.warn{background:#fff8e6!important;border:1px solid #e7c66b!important;color:#8a6d1a!important}
.kpi.g .n{color:#15803d!important}.kpi.r .n{color:#c0392b!important}.kpi.y .n{color:#b45309!important}
.bd{background:#64748b!important;color:#fff!important}
footer{background:#e8731c!important;color:#fff!important;border-top:3px solid #c75e10!important;margin-top:20px}
</style></head><body>
<div class="hero"><h1>🔔 SIGEJ-UdeG · Centro de Alertas y Riesgo</h1><div class="s">Tablero predictivo para el Abogado General — administra el riesgo, no solo lo registra · corte <b id="fc"></b></div>
 <div class="strat" id="strat"></div></div>
__NAV__
<div class="wrap">
 <div class="h">🚨 Categorías de riesgo crítico</div><div class="cats" id="cats"></div>
 <div class="h">⏳ Alertas preventivas por plazo</div><div class="buckets" id="buckets"></div>
 <div class="h">🏛️ Matriz de riesgo institucional (por dependencia)</div><div class="card"><table id="matriz"></table></div>
 <div class="h">🔴 Expedientes en riesgo de caducidad — priorizados por riesgo financiero</div>
 <div class="bar"><select id="fb" onchange="render()"><option value="">Todo semáforo</option><option value="rojo">🔴 Rojo (81-100)</option><option value="naranja">🟠 Naranja (51-80)</option><option value="amar">🟡 Amarillo (21-50)</option></select><span style="font-size:12px;color:#64748b" id="cnt"></span></div>
 <div id="lista"></div>
 <div class="warn">⚠️ <b>Notificaciones automáticas</b> (correo/Teams/Outlook/WhatsApp a 30/15/7/3 días/24h) y la <b>probabilidad de pérdida con IA</b> son fase de implementación con backend. El riesgo es proxy explicable; el pasivo es piso parcial (montos NLP, a validar). Fundamento de caducidad verificado.</div>
 <div class="h">📅 Plazos y términos de las altas protegidas (marco normativo)</div>
 <div class="card"><div id="slaKpis" class="buckets"></div><div id="slaAltas"></div>
  <div class="intel" style="margin-top:8px">Los <b>plazos</b> se calculan con el <b>catálogo SLA</b> (abajo) que administra Help Desk. Ámbito <b>Federal / Estatal / Interno</b>; el <b>fundamento normativo</b> lo captura Help Desk conforme a la ley aplicable (no se presume articulado).</div></div>
 <div class="h">⚖️ Hallazgos de cumplimiento normativo (abiertos)</div>
 <div class="card"><div id="cumplHall"></div></div>
 <div class="h">📮 Pendientes de dependencias externas (pruebas / documentos) — recordatorios</div>
 <div class="card"><div id="extForm"></div><div id="extList" style="margin-top:8px"></div></div>
 <div class="h">⚙️ Catálogo de plazos (SLA) · control de Help Desk</div>
 <div class="card"><div id="slaCat"></div></div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;document.getElementById('fc').textContent=D.corte;
const HOY=new Date(2026,5,18);
function dr(f){return Math.round((new Date(f+'T00:00:00')-HOY)/864e5);}
function band(s){return s>=81?'rojo':s>=51?'naranja':s>=21?'amar':'verde';}
function bandLabel(s){return s>=81?'Intervención inmediata':s>=51?'Atención prioritaria':s>=21?'Revisión semanal':'Seguimiento ordinario';}
function M(v){return '$'+Number(v).toLocaleString('es-MX');}
function localAg(){let a=[];try{const e=JSON.parse(localStorage.getItem('sigej_enr')||'{}');Object.keys(e).forEach(n=>(e[n].agenda||[]).forEach(x=>a.push(Object.assign({exp:n},x))));}catch(e){}
 try{const c=JSON.parse(localStorage.getItem('sigej_capturas')||'[]');c.forEach(r=>(r.agenda||[]).forEach(x=>a.push(Object.assign({exp:r.num},x))));}catch(e){}return a;}
function localResp(){try{const r=JSON.parse(localStorage.getItem('sigej_resp')||'[]');const y={'Falta no grave':3,'Falta grave':7};return r.filter(x=>['En investigación','En substanciación'].includes(x.estado)&&x.finicio&&x.clasif).map(x=>{const f=new Date(x.finicio+'T00:00:00');f.setFullYear(f.getFullYear()+(y[x.clasif]||3));return {exp:x.folio||x.id,fecha:f.toISOString().slice(0,10)};});}catch(e){return [];}}
function localMasc(){let a=[];try{const m=JSON.parse(localStorage.getItem('sigej_masc')||'[]');m.forEach(r=>(r.parcialidades||[]).forEach(p=>{if(!p.pagada)a.push({exp:r.exp||r.id,fecha:p.fecha});}));}catch(e){}return a;}
function conveniosPend(){try{const m=JSON.parse(localStorage.getItem('sigej_masc')||'[]');return m.filter(x=>x.cumplimiento&&x.cumplimiento!=='Cumplido').length;}catch(e){return 0;}}
function strat(){const ag=localAg(),rp=localResp(),S=D.estrategico;
 const prox30=ag.filter(a=>{const d=dr(a.fecha);return d>=0&&d<=30;}).length+rp.filter(a=>{const d=dr(a.fecha);return d>=0&&d<=30;}).length+D.caducidad.filter(c=>c.score>=80).length;
 document.getElementById('strat').innerHTML=[['$'+(S.riesgo_total/1e6).toFixed(1)+'M','Riesgo total estimado','r'],['$'+(S.pasivo_contingente/1e6).toFixed(1)+'M','Pasivo contingente (piso)','y'],[S.criticos,'Expedientes críticos','r'],[prox30,'Plazos próximos 30 días','y'],[S.prob_global+'%','Probabilidad global de contingencia','']]
  .map(x=>'<div class="sc '+x[2]+'"><div class="n">'+x[0]+'</div><div class="l">'+x[1]+'</div></div>').join('');}
function cats(){const ag=localAg(),rp=localResp();
 const cad=D.caducidad.filter(c=>c.score>=80).length;
 const presc=rp.filter(a=>dr(a.fecha)<=180).length;
 const aud=ag.filter(a=>a.tipo==='Audiencia'&&dr(a.fecha)>=0&&dr(a.fecha)<=7).length;
 const cont=ag.filter(a=>a.tipo==='Contestación'&&dr(a.fecha)>=0).length;
 const term=ag.filter(a=>a.tipo==='Término'&&dr(a.fecha)>=0&&dr(a.fecha)<=15).length;
 const seg=ag.filter(a=>a.tipo==='Seguimiento'&&dr(a.fecha)>=0).length;
 const conv=conveniosPend();
 const C=[['🔴 Caducidad inminente',cad,''],['🔴 Prescripción próxima',presc,''],['🔴 Audiencias en 7 días',aud,''],['🔴 Contestaciones pendientes',cont,''],['🔴 Términos por vencer (15d)',term,''],['🔴 Seguimientos pendientes',seg,''],['🔴 Convenios sin ejecutar',conv,''],['🟡 Contratos por vencer','—','cap']];
 document.getElementById('cats').innerHTML=C.map(x=>'<div class="cat '+(x[2]||'')+'"><div class="t">'+x[0]+'</div><div class="n">'+x[1]+'</div></div>').join('');}
function buckets(){const all=localAg().concat(localResp()).concat(localMasc()).map(a=>dr(a.fecha)).filter(d=>d>=0);
 const b=[['≤ 7 días',all.filter(d=>d<=7).length,'b7'],['≤ 15 días',all.filter(d=>d>7&&d<=15).length,'b15'],['≤ 30 días',all.filter(d=>d>15&&d<=30).length,'b30'],['≤ 60 días',all.filter(d=>d>30&&d<=60).length,''],['≤ 90 días',all.filter(d=>d>60&&d<=90).length,''],['> 90 días',all.filter(d=>d>90).length,'']];
 document.getElementById('buckets').innerHTML=b.map(x=>'<div class="bk '+x[2]+'"><div class="n">'+x[1]+'</div><div class="l">'+x[0]+'</div></div>').join('');}
function matriz(){document.getElementById('matriz').innerHTML='<tr><th>Dependencia</th><th>Expedientes</th><th>Alto riesgo</th><th>Pasivo (piso)</th><th>Riesgo</th></tr>'+
 D.matriz.map(m=>'<tr><td><b>'+m.dep.slice(0,32)+'</b></td><td>'+m.n+'</td><td>'+m.alto+'</td><td>'+M(m.pasivo)+'</td><td><span class="rb rb-'+m.riesgo+'">'+m.riesgo+'</span></td></tr>').join('');}
function render(){const fb=document.getElementById('fb').value;
 let L=D.caducidad.slice();if(fb)L=L.filter(c=>band(c.score)===fb);
 document.getElementById('cnt').textContent=L.length+' expedientes';
 document.getElementById('lista').innerHTML=L.slice(0,60).map(function(c){var b=band(c.score);
  return '<div class="al s-'+b+'"><div class="top"><div><span class="exp">'+c.num+'</span> <span class="rb rb-'+c.riesgo_fin+'">'+c.materia+'</span></div><div class="gauge g-'+b+'">'+c.score+'</div></div>'+
   '<div class="grid"><div class="kv">Pasivo contingente<br><b>'+M(c.pasivo)+'</b></div><div class="kv">Riesgo financiero<br><b>'+c.riesgo_fin+'</b></div><div class="kv">Prob. de pérdida<br><b>'+c.prob_perdida+'%</b></div><div class="kv">Sin movimiento<br><b>'+c.meses+' meses</b></div><div class="kv">Última actuación<br><b>'+(c.ultimo||'—')+'</b></div><div class="kv">Responsable<br><b>'+(c.resp||'—').split(' ').slice(0,2).join(' ')+'</b></div></div>'+
   '<div class="intel"><b>¿Por qué está en alerta?</b> Sin promoción registrada desde hace '+c.meses+' meses · <b>Prob. de consumación:</b> '+c.prob_caducidad+'% · <b>Acción ('+bandLabel(c.score)+'):</b> revisar si existe archivo definitivo o resolución firme no capturada; de lo contrario, impulsar o provisionar. <b>Fundamento:</b> '+D.fund_caducidad+' <span style="background:#e6f6ee;color:#1f7a4d;border:1px solid #9fd9b8;border-radius:8px;padding:1px 7px">✓ verificado</span></div></div>';
 }).join('')+(L.length>60?'<div style="text-align:center;color:#94a3b8;font-size:12px">… 60 de '+L.length+'</div>':'');}
strat();cats();buckets();matriz();render();
/* ===== Refuerzo: catálogo SLA (Help Desk), plazos de altas protegidas y pendientes externos ===== */
var HDROLES=['Administrador','Sistemas','Jefe del Área de Sistemas'];
function opPerfil(){return localStorage.getItem('sigej_perfil')||'(perfil)';}
function isHD(){return HDROLES.indexOf(opPerfil())>=0;}
function jl(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function svl(k,v){localStorage.setItem(k,JSON.stringify(v));}
function ecx(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function todayISO(){return new Date().toISOString().slice(0,10);}
function daysTo(iso){return Math.round((new Date(iso+'T00:00:00')-new Date(todayISO()+'T00:00:00'))/864e5);}
function blogA(t,a){try{var L=jl('sigej_bitacora');L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:opPerfil(),modulo:'alertas_centro_SIGEJ',tipo:t,accion:String(a||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);svl('sigej_bitacora',L);}catch(e){}}
var SLA_OPER=[
 {id:'sla1',tipo:'Respuesta a oficio urgente',dias:1,base:'habiles',ambito:'Interno',fundamento:'Plazo interno de la Oficina (configurable por Help Desk)',rec:[0],activo:true},
 {id:'sla2',tipo:'Respuesta a oficio ordinario',dias:5,base:'habiles',ambito:'Interno',fundamento:'Plazo interno de la Oficina (configurable por Help Desk)',rec:[2,0],activo:true},
 {id:'sla3',tipo:'Requerimiento de autoridad',dias:3,base:'habiles',ambito:'Federal',fundamento:'Conforme al término señalado en el requerimiento y la ley aplicable (capturar fundamento)',rec:[1,0],activo:true},
 {id:'sla4',tipo:'Contestacion / tramite administrativo',dias:10,base:'habiles',ambito:'Estatal',fundamento:'Ley del Procedimiento Administrativo del Estado de Jalisco y sus Municipios (capturar artículo aplicable)',rec:[3,1,0],activo:true},
 {id:'sla5',tipo:'Solicitud de informacion / transparencia',dias:8,base:'habiles',ambito:'Estatal',fundamento:'Ley de Transparencia y Acceso a la Información Pública del Estado de Jalisco (capturar artículo)',rec:[3,1],activo:true},
 {id:'sla6',tipo:'Requisicion de papeleria',dias:5,base:'naturales',ambito:'Interno',fundamento:'Plazo interno (configurable)',rec:[1],activo:true},
 {id:'sla7',tipo:'Viaticos / comprobacion',dias:10,base:'naturales',ambito:'Interno',fundamento:'Normatividad de la UdeG en materia de viáticos (capturar fundamento)',rec:[3,1],activo:true}
];
/* Plazos NORMATIVOS verificados (citan artículo y fuente oficial; alimentan los recordatorios y el widget de Alta protegida) */
var SLA_VER=[
 {id:'slaN1',tipo:'Presentación de demanda de nulidad (cont. adm. federal)',dias:30,base:'habiles',ambito:'Federal',fundamento:'LFPCA Art. 13, frac. I: la demanda se presenta dentro de los 30 días siguientes a que surta efectos la notificación de la resolución impugnada.',rec:[15,10,5,3,1,0],activo:true,verif:{ok:true,fuente:'https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPCA.pdf',fecha:'DOF 09-06-2026'}},
 {id:'slaN2',tipo:'Contestación de demanda (cont. adm. federal)',dias:30,base:'habiles',ambito:'Federal',fundamento:'LFPCA Art. 19: contestación dentro de 30 días desde el emplazamiento (ampliación 10 días).',rec:[15,10,5,3,1,0],activo:true,verif:{ok:true,fuente:'https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPCA.pdf',fecha:'DOF 09-06-2026'}},
 {id:'slaN3',tipo:'Interposición de amparo indirecto',dias:15,base:'habiles',ambito:'Federal',fundamento:'Ley de Amparo Art. 17: 15 días (30 días en norma autoaplicativa o extradición).',rec:[10,5,3,1,0],activo:true,verif:{ok:true,fuente:'https://www.diputados.gob.mx/LeyesBiblio/pdf/LAmp.pdf',fecha:'DOF 16-10-2025'}},
 {id:'slaN4',tipo:'Caducidad de la primera instancia (alerta de inactividad)',dias:40,base:'habiles',ambito:'Federal',fundamento:'CNPCyF Art. 234: caducidad de pleno derecho a los 40 días hábiles sin promoción (vigencia por declaratoria estatal).',rec:[30,15,10,5,3,1,0],activo:true,verif:{ok:true,fuente:'https://www.diputados.gob.mx/LeyesBiblio/pdf/CNPCF.pdf',fecha:'DOF 15-01-2026'}},
 {id:'slaN5',tipo:'Condición de estancia · visitante (migratorio)',dias:180,base:'naturales',ambito:'Federal',fundamento:'Ley de Migración Art. 52: visitante hasta 180 días ininterrumpidos.',rec:[30,15,10,5,3,1,0],activo:true,verif:{ok:true,fuente:'https://www.diputados.gob.mx/LeyesBiblio/pdf/LMigra.pdf',fecha:'DOF 15-01-2026'}}
];
function seedSLA(){var c=jl('sigej_sla_catalogo');if(!c.length){svl('sigej_sla_catalogo',SLA_OPER.concat(SLA_VER));return;}var ids={};c.forEach(function(x){ids[x.id]=1;});var ch=false;SLA_VER.forEach(function(v){if(!ids[v.id]){c.push(v);ch=true;}});if(ch)svl('sigej_sla_catalogo',c);}
seedSLA();
function amColor(a){return a==='Federal'?'#0a4d8c':a==='Estatal'?'#1a6d64':'#64748b';}
function renderSLACat(){var c=jl('sigej_sla_catalogo');var hd=isHD();
 var h='<div style="font-size:11.5px;color:#64748b;margin-bottom:8px">'+(hd?'✏️ Como <b>Help Desk / Administrador</b> puedes ajustar los plazos (p. ej. <b>1, 5 o 10 días</b>), su base (hábiles/naturales), ámbito y fundamento normativo.':'Catálogo vigente. Solo <b>Help Desk / Administrador</b> puede modificarlo.')+'</div>';
 h+='<table style="width:100%;border-collapse:collapse;font-size:12px"><tr style="text-align:left;color:#64748b"><th style="padding:4px">Tipo de trámite</th><th>Plazo</th><th>Ámbito</th><th>Fundamento (capturado por HD)</th><th>Recordatorios</th><th>Estado</th>'+(hd?'<th></th>':'')+'</tr>';
 h+=c.map(function(x,i){return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px"><b>'+ecx(x.tipo)+'</b></td><td><b>'+x.dias+'</b> d '+ecx(x.base)+'</td><td><span style="background:'+amColor(x.ambito)+';color:#fff;border-radius:9px;padding:1px 7px;font-size:10px">'+ecx(x.ambito)+'</span></td><td style="font-size:11px;color:#475569">'+ecx(x.fundamento)+(x.verif&&x.verif.ok?' <span style="background:#e6f6ee;color:#1f7a4d;border:1px solid #9fd9b8;border-radius:8px;padding:0 6px;font-size:9.5px;white-space:nowrap">✓ verificado</span>'+(x.verif.fuente?' <a href="'+ecx(x.verif.fuente)+'" target="_blank" rel="noopener" style="font-size:9.5px;color:#0a4d8c">fuente ↗</a>':'')+(x.verif.fecha?' <span style="font-size:9.5px;color:#94a3b8">'+ecx(x.verif.fecha)+'</span>':''):'')+'</td><td style="font-size:11px">'+((x.rec||[]).length?('recordar a '+x.rec.join(', ')+' d antes'):'—')+'</td><td>'+(x.activo!==false?'🟢 activo':'⚪ inactivo')+'</td>'+(hd?'<td style="white-space:nowrap"><button class="bd" style="font-size:10.5px;padding:3px 7px" onclick="editSLA('+i+')">✏️</button> <button class="bd" style="font-size:10.5px;padding:3px 7px" onclick="toggleSLA('+i+')">⏯️</button></td>':'')+'</tr>';}).join('');
 h+='</table>';
 if(hd)h+='<div style="margin-top:8px"><button class="bd" onclick="addSLA()" style="font-size:12px">＋ Nuevo tipo de plazo</button></div>';
 h+='<div class="warn" style="margin-top:8px">⚖️ Los <b>días</b> son parámetros operativos que fija la Oficina/Help Desk. El <b>fundamento normativo</b> (federal/estatal) debe capturarse conforme a la ley aplicable a cada trámite; el sistema <b>no presume el articulado</b>. La verificación jurídica del término corresponde al área.</div>';
 document.getElementById('slaCat').innerHTML=h;}
function editSLA(i){if(!isHD())return;var c=jl('sigej_sla_catalogo');var x=c[i];if(!x)return;
 var d=prompt('Plazo en días (ej. 1, 5, 10):',x.dias);if(d===null)return;var nd=parseInt(d,10);if(isNaN(nd)||nd<0){alert('Días no válidos.');return;}
 var bs=prompt('Base — escribe: habiles  o  naturales',x.base);if(bs===null)return;bs=/natural/i.test(bs)?'naturales':'habiles';
 var am=prompt('Ámbito — Federal / Estatal / Interno',x.ambito);if(am===null)return;am=/federal/i.test(am)?'Federal':(/estatal/i.test(am)?'Estatal':'Interno');
 var fu=prompt('Fundamento normativo (capturar la ley/artículo aplicable):',x.fundamento);if(fu===null)return;
 x.dias=nd;x.base=bs;x.ambito=am;x.fundamento=fu.trim();svl('sigej_sla_catalogo',c);blogA('Acción','HD edita SLA '+x.tipo+' → '+nd+' d');renderSLACat();renderAltasPlazos();}
function toggleSLA(i){if(!isHD())return;var c=jl('sigej_sla_catalogo');c[i].activo=!(c[i].activo!==false);svl('sigej_sla_catalogo',c);blogA('Acción','HD '+(c[i].activo?'activa':'desactiva')+' SLA '+c[i].tipo);renderSLACat();}
function addSLA(){if(!isHD())return;var t=prompt('Nombre del tipo de trámite:','');if(t===null||!t.trim())return;var d=prompt('Plazo en días:','5');var nd=parseInt(d,10);if(isNaN(nd))nd=5;var am=prompt('Ámbito (Federal/Estatal/Interno):','Interno');am=/federal/i.test(am||'')?'Federal':(/estatal/i.test(am||'')?'Estatal':'Interno');var fu=prompt('Fundamento (ley/artículo aplicable):','(capturar fundamento)');
 var c=jl('sigej_sla_catalogo');c.push({id:'sla'+Date.now().toString(36),tipo:t.trim(),dias:nd,base:'habiles',ambito:am,fundamento:(fu||'').trim(),rec:[1,0],activo:true});svl('sigej_sla_catalogo',c);blogA('Acción','HD agrega SLA '+t.trim());renderSLACat();}
function renderAltasPlazos(){var A=jl('sigej_altas').filter(function(a){return a.fechaLimite&&!a.anulado;});
 A.sort(function(a,b){return (a.fechaLimite||'').localeCompare(b.fechaLimite||'');});
 var venc=A.filter(function(a){return daysTo(a.fechaLimite)<0;}).length,hoy=A.filter(function(a){return daysTo(a.fechaLimite)===0;}).length,prox=A.filter(function(a){var d=daysTo(a.fechaLimite);return d>0&&d<=2;}).length,sem=A.filter(function(a){var d=daysTo(a.fechaLimite);return d>2&&d<=7;}).length;
 document.getElementById('slaKpis').innerHTML=[['🔴 Vencidos',venc,'b7'],['🟠 Vencen hoy',hoy,'b7'],['🟡 ≤ 2 días',prox,'b15'],['🟢 ≤ 7 días',sem,'b30'],['Σ con plazo',A.length,'']].map(function(x){return '<div class="bk '+x[2]+'"><div class="n">'+x[1]+'</div><div class="l">'+x[0]+'</div></div>';}).join('');
 var TH=[30,15,10,5,3,1,0];
 var hoyRec=A.filter(function(a){return TH.indexOf(daysTo(a.fechaLimite))>=0;});
 var ladderHtml='<div class="card" style="box-shadow:none;border:1px solid #e2e8f0;margin-top:10px;padding:10px"><b style="font-size:12.5px;color:#0a4d8c">🔔 Escalera de recordatorios (30 / 15 / 10 / 5 / 3 / 1 días · vencimiento)</b><div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:6px">'+TH.map(function(th){var n=A.filter(function(a){return daysTo(a.fechaLimite)===th;}).length;var venc=th===0;return '<div style="background:'+(n?(venc?'#fdeaea':'#fff8e6'):'#f1f5f9')+';color:'+(n?(venc?'#c0392b':'#8a6d1a'):'#64748b')+';border-radius:8px;padding:4px 9px;font-size:11px;font-weight:700">'+(venc?'Vence hoy':th+' d antes')+': '+n+'</div>';}).join('')+'</div>'+(hoyRec.length?'<div style="font-size:11px;color:#8a6d1a;margin-top:6px">⏰ Hoy se disparan <b>'+hoyRec.length+'</b> recordatorio(s) en los umbrales. El envío automático (correo/Teams a cada umbral 30/15/10/5/3/1/24h) es fase backend; aquí se listan y se difunden por el <a href="notificaciones_SIGEJ.html" style="color:#0a4d8c">Centro de Notificaciones</a>.</div>':'<div style="font-size:11px;color:#128c4a;margin-top:6px">Sin recordatorios en los umbrales el día de hoy.</div>')+'</div>';
 document.getElementById('slaAltas').innerHTML=ladderHtml+(A.length?('<table style="width:100%;border-collapse:collapse;font-size:12px;margin-top:8px"><tr style="text-align:left;color:#64748b"><th style="padding:4px">Folio</th><th>Módulo</th><th>Tipo / título</th><th>Plazo</th><th>Límite</th><th>Estado</th><th>Captura</th></tr>'+A.slice(0,80).map(function(a){var d=daysTo(a.fechaLimite);var col=d<0?'#c0392b':(d<=2?'#e08e0b':'#128c4a');var txt=d<0?('vencido '+(-d)+'d'):(d===0?'hoy':'en '+d+'d');return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px"><b>'+ecx(a.folio)+'</b></td><td style="font-size:11px">'+ecx(a.modulo)+'</td><td>'+ecx(a.tipo)+' · '+ecx(a.titulo)+'</td><td style="font-size:11px">'+ecx(a.plazoTipo||'—')+'</td><td>'+ecx(a.fechaLimite)+'</td><td><span style="color:'+col+';font-weight:700">'+txt+'</span></td><td style="font-size:10.5px;color:#94a3b8">'+ecx(a.capturadoPor)+'<br>'+ecx(a.fechaCaptura)+'</td></tr>';}).join('')+'</table>'):'<div style="color:#94a3b8;font-size:12px;padding:6px">Sin altas con plazo asignado. Asígnalos con el widget “➕ Alta protegida” de cada módulo.</div>');}
function renderExternos(){var canW=['Secretaría General','Director','Coordinador General','Consulta'].indexOf(opPerfil())<0;
 document.getElementById('extForm').innerHTML=canW?('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:6px">'+
  '<input id="ex_dep" placeholder="Dependencia externa *" style="padding:7px;border:1px solid #cbd5e1;border-radius:8px">'+
  '<input id="ex_tram" placeholder="Trámite / folio relacionado" style="padding:7px;border:1px solid #cbd5e1;border-radius:8px">'+
  '<input id="ex_doc" placeholder="Documento/prueba esperada *" style="padding:7px;border:1px solid #cbd5e1;border-radius:8px">'+
  '<input id="ex_fc" type="date" title="Fecha compromiso" style="padding:7px;border:1px solid #cbd5e1;border-radius:8px">'+
  '<button class="bd" style="background:#1f9d6b;color:#fff;font-weight:700" onclick="addExterno()">＋ Registrar pendiente</button></div><span id="ex_msg" style="font-size:11px"></span>'):'<div style="font-size:11.5px;color:#8a6d1a">Perfil de solo lectura: consulta de pendientes.</div>';
 var E=jl('sigej_pendientes_externos');
 document.getElementById('extList').innerHTML=E.length?('<table style="width:100%;border-collapse:collapse;font-size:12px"><tr style="text-align:left;color:#64748b"><th style="padding:4px">Dependencia</th><th>Documento esperado</th><th>Trámite</th><th>Compromiso</th><th>Estado</th><th>Recordatorios</th><th></th></tr>'+E.map(function(x,i){var rec=x.recibido;var d=x.fcompromiso?daysTo(x.fcompromiso):null;var est=rec?'✅ Recibido':(d!=null&&d<0?'🔴 Vencido '+(-d)+'d':(d!=null?'🟡 en '+d+'d':'⏳ Pendiente'));return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px"><b>'+ecx(x.dependencia)+'</b></td><td>'+ecx(x.documento)+'</td><td style="font-size:11px">'+ecx(x.tramite||'—')+'</td><td>'+ecx(x.fcompromiso||'—')+'</td><td style="font-size:11px">'+est+'</td><td style="font-size:11px">'+((x.recordatorios||[]).length)+'</td><td style="white-space:nowrap">'+(rec?'':'<button class="bd" style="font-size:10.5px;padding:3px 7px" onclick="recordarExt('+i+')">📧 Recordar</button> <button class="bd" style="font-size:10.5px;padding:3px 7px" onclick="recibirExt('+i+')">✅ Recibido</button>')+'</td></tr>';}).join('')+'</table>'):'<div style="color:#94a3b8;font-size:12px;padding:6px">Sin pendientes externos registrados.</div>';}
function addExterno(){var dep=(document.getElementById('ex_dep').value||'').trim(),doc=(document.getElementById('ex_doc').value||'').trim();if(!dep||!doc){document.getElementById('ex_msg').style.color='#c0392b';document.getElementById('ex_msg').textContent='Dependencia y documento son obligatorios.';return;}
 var E=jl('sigej_pendientes_externos');E.push({id:'PEX-'+Date.now().toString(36),dependencia:dep,tramite:(document.getElementById('ex_tram').value||'').trim(),documento:doc,fcompromiso:document.getElementById('ex_fc').value||'',fsol:todayISO(),estado:'Pendiente',recordatorios:[],recibido:null,capturadoPor:opPerfil(),ts:new Date().toISOString().slice(0,16).replace('T',' ')});svl('sigej_pendientes_externos',E);blogA('Acción','Registra pendiente externo · '+dep+' · '+doc);document.getElementById('ex_dep').value='';document.getElementById('ex_doc').value='';document.getElementById('ex_tram').value='';renderExternos();}
function recordarExt(i){var E=jl('sigej_pendientes_externos');var x=E[i];if(!x)return;(x.recordatorios=x.recordatorios||[]).push({ts:new Date().toISOString().slice(0,16).replace('T',' '),por:opPerfil()});svl('sigej_pendientes_externos',E);blogA('Acción','Recordatorio a '+x.dependencia+' por '+x.documento);
 var asunto=encodeURIComponent('Recordatorio: '+x.documento+(x.tramite?' ('+x.tramite+')':''));var cuerpo=encodeURIComponent('Estimada dependencia '+x.dependencia+':\n\nLe recordamos atentamente el envío de: '+x.documento+'.\nTrámite relacionado: '+(x.tramite||'—')+'\nFecha compromiso: '+(x.fcompromiso||'—')+'\n\nOficina de la Abogacía General · UdeG');window.location.href='mailto:?subject='+asunto+'&body='+cuerpo;renderExternos();}
function recibirExt(i){var E=jl('sigej_pendientes_externos');var x=E[i];if(!x)return;if(!confirm('¿Marcar como recibido? (el registro no se borra, queda con acuse)'))return;x.recibido={ts:new Date().toISOString().slice(0,16).replace('T',' '),por:opPerfil()};x.estado='Recibido';svl('sigej_pendientes_externos',E);blogA('Acción','Documento recibido de '+x.dependencia);renderExternos();}
function renderHall(){var H=(jl('sigej_cumplimiento_hallazgos')||[]).filter(function(h){return h.estado!=='Cerrado';});
 var MN={instrumentos_SIGEJ:'Instrumentos',contencioso_SIGEJ:'Contencioso',patrimonio_SIGEJ:'Patrimonio Intangible',internacional_SIGEJ:'Asuntos Internacionales',normatividad_SIGEJ:'Normatividad',oficialia_SIGEJ:'Oficialía'};
 document.getElementById('cumplHall').innerHTML=H.length?('<div style="font-size:11.5px;color:#64748b;margin-bottom:6px">'+H.length+' hallazgo(s) abiertos detectados en la <a href="cumplimiento_SIGEJ.html" style="color:#0a4d8c">Validación de cumplimiento</a>. Gestiónalos (atender/cerrar) en el Motor de Cumplimiento.</div><table style="width:100%;border-collapse:collapse;font-size:12px"><tr style="text-align:left;color:#64748b"><th style="padding:4px">Módulo</th><th>Procedimiento</th><th>Riesgo</th><th>Criticidad</th><th>Estado</th></tr>'+H.slice(-30).reverse().map(function(h){var c=h.crit==='Crítica'?'#c0392b':h.crit==='Alta'?'#ea580c':'#b45309';return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px;font-size:11px">'+ecx(MN[h.modulo]||h.modulo)+'</td><td style="font-size:11.5px">'+ecx(h.proc)+(h.ref?' · '+ecx(h.ref):'')+'</td><td style="font-size:11px">'+ecx(h.riesgo||'')+'</td><td><span style="color:'+c+';font-weight:700;font-size:11px">'+ecx(h.crit||'—')+'</span></td><td style="font-size:11px">'+ecx(h.estado)+'</td></tr>';}).join('')+'</table>'):'<div style="color:#128c4a;font-size:12px;padding:6px">Sin hallazgos de cumplimiento abiertos ✓</div>';}
renderSLACat();renderAltasPlazos();renderExternos();renderHall();
window.addEventListener('focus',function(){strat();cats();buckets();renderAltasPlazos();renderExternos();renderHall();});
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
})();</script><script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;margin-top:0!important}";document.head.appendChild(st);function clean(){try{var c=document.getElementById("__chg");if(c&&c.parentNode)c.parentNode.style.display="none";document.querySelectorAll("div[style*=\"99999\"]").forEach(function(o){o.remove();});}catch(e){}}clean();setTimeout(clean,150);setTimeout(clean,500);setTimeout(clean,1200);})();</script>
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
open("/Users/edithroque/Documents/CLAUDE/alertas_centro_SIGEJ.html","w",encoding="utf-8").write(TPL.replace("__DATA__",DATA).replace("__NAV__",NAV))
print("alertas_centro_SIGEJ.html OK")
