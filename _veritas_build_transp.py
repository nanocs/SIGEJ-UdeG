# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/transparencia_data.json",encoding="utf-8"))
DATA=json.dumps(d,ensure_ascii=False)
NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_SIGEJ.html" class="act">🔎 Transparencia</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>'''
TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Transparencia</title><style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#f4f6f9;--ok:#1f9d6b;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:14px 24px}
header h1{margin:0;font-size:18px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.tabs{display:flex;gap:4px;background:#0c2440;padding:0 20px}
.tabs button{background:none;border:none;color:#cbd5e1;padding:11px 16px;cursor:pointer;font-size:13px;border-bottom:3px solid transparent}
.tabs button.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:16px 22px;max-width:1320px;margin:auto}
.sec{display:none}.sec.act{display:block}
.cols{display:grid;grid-template-columns:310px 1fr;gap:16px}@media(max-width:900px){.cols{grid-template-columns:1fr}}
.card{background:#fff;border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.07);margin-bottom:14px}
.card h2{margin:0 0 12px;font-size:14px;color:var(--azul)}
.f{display:flex;flex-direction:column;gap:3px;margin-bottom:9px}
.f label{font-size:11.5px;color:var(--mut);font-weight:600}
.f input,.f select,.f textarea{padding:7px 8px;border:1px solid var(--line);border-radius:6px;font-size:12.5px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.chk{display:flex;gap:6px;align-items:center;font-size:12px;margin:4px 0}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(115px,1fr));gap:9px;margin-bottom:12px}
.kpi{background:#f4f6f9;border-radius:9px;padding:11px;border-left:4px solid var(--teal)}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul)}.kpi .l{font-size:10.5px;color:var(--mut)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:700px){.grid2{grid-template-columns:1fr}}
table{width:100%;border-collapse:collapse;font-size:12.5px}th,td{padding:6px 8px;text-align:left;border-bottom:1px solid var(--line)}th{color:var(--mut)}
.resp{background:#f8fafc;border:1px solid var(--line);border-radius:8px;padding:12px;font-size:13px;line-height:1.6;white-space:pre-wrap}
button{padding:8px 14px;border:none;border-radius:8px;cursor:pointer;font-size:12.5px;font-weight:600;color:#fff}
.b1{background:var(--azul2)}.b2{background:var(--teal)}.b3{background:var(--ok)}.bd{background:#eef2f7;color:var(--mut)}
.verif{background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:10px 12px;font-size:11.5px;color:#8a6d1a}
.verif b{color:#6d5410}.verif ul{margin:6px 0 0;padding-left:18px}
.warnbig{background:#fdecea;border:1px solid #f0b3ab;border-radius:8px;padding:9px 12px;font-size:12px;color:#a02c20;margin-bottom:12px;font-weight:600}
.lk{color:#0a4d8c;cursor:pointer;text-decoration:underline}.del{color:#c0392b;cursor:pointer}
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
<header><h1>🔎 SIGEJ-UdeG · Módulo de Transparencia</h1><div class="s">Buscador para solicitudes de información (UTI) con registro y verificación — Abogacía General · corte <b id="fc"></b></div></header>
__NAV__
<div class="tabs"><button id="tb_c" class="act" onclick="tab('c')">🔍 Consulta</button><button id="tb_r" onclick="tab('r')">📒 Registro de solicitudes (<span id="nreg">0</span>)</button></div>
<div class="wrap">

<section class="sec act" data-s="c"><div class="cols">
 <div><div class="card"><h2>Filtros de consulta</h2>
  <div class="f"><label>Búsqueda libre (nº, actor)</label><input id="q" oninput="run()" placeholder="texto…"></div>
  <div class="row2"><div class="f"><label>Año desde</label><input id="ad" type="number" min="1990" max="2026" oninput="run()"></div><div class="f"><label>Año hasta</label><input id="ah" type="number" min="1990" max="2026" oninput="run()"></div></div>
  <div class="f"><label>Vigencia</label><select id="vig" onchange="run()"><option value="act">Solo activas</option><option value="con">Solo concluidas</option><option value="all">Todas</option></select></div>
  <div class="f"><label>Materia</label><select id="materia" onchange="run()"></select></div>
  <div class="f"><label>Vía</label><select id="via" onchange="run()"></select></div>
  <div class="f"><label>Tipo de juicio</label><select id="tipo" onchange="run()"></select></div>
  <div class="f"><label>Estado procesal</label><select id="estado" onchange="run()"></select></div>
  <div class="f"><label>Responsable</label><select id="responsable" onchange="run()"></select></div>
  <div class="f"><label>Autoridad</label><input id="autoridad" list="l_aut" oninput="run()"><datalist id="l_aut"></datalist></div>
  <div class="f"><label>Dependencia</label><input id="dependencia" list="l_dep" oninput="run()"><datalist id="l_dep"></datalist></div>
  <div class="row2"><div class="f"><label>Cuantía desde ($)</label><input id="md" type="number" min="0" oninput="run()" placeholder="0"></div><div class="f"><label>Cuantía hasta ($)</label><input id="mh" type="number" min="0" oninput="run()" placeholder="∞"></div></div>
  <div class="chk"><input type="checkbox" id="x_monto" onchange="run()"><label>Solo con cuantía registrada</label></div>
  <div class="chk"><input type="checkbox" id="x_sent" onchange="run()"><label>Solo con sentencia/laudo</label></div>
  <div class="chk"><input type="checkbox" id="x_susp" onchange="run()"><label>Solo con suspensión provisional</label></div>
  <div class="chk"><input type="checkbox" id="x_conc" onchange="run()"><label>Solo resueltas en conciliación</label></div>
  <button class="bd" style="width:100%;margin-top:6px" onclick="limpiar()">Limpiar filtros</button>
 </div></div>
 <div>
  <div class="kpis" id="kpis"></div>
  <div class="grid2">
   <div class="card"><h2>Por materia</h2><table id="t_mat"></table></div>
   <div class="card"><h2>Por año</h2><table id="t_anio"></table></div>
   <div class="card"><h2>Por estado procesal</h2><table id="t_est"></table></div>
   <div class="card"><h2>Por vía</h2><table id="t_via"></table></div>
  </div>
  <div class="card"><h2>✔️ Verificación y congruencia</h2><div class="verif" id="verif"></div></div>
  <div class="card"><h2>Respuesta a la solicitud</h2>
   <div class="row2"><div class="f"><label>Folio UTI</label><input id="folio" placeholder="UTI/0628/2026"></div><div class="f"><label>Fecha de la solicitud</label><input id="fsol" type="date"></div></div>
   <div class="row2"><div class="f"><label>Fecha de respuesta</label><input id="fresp" type="date"></div><div class="f"><label>Responde (servidor público)</label><input id="quien" placeholder="nombre / cargo"></div></div>
   <div class="f"><label>Texto de la solicitud</label><textarea id="solicitud" rows="2" placeholder="Pega aquí la solicitud del peticionario…"></textarea></div>
   <div class="f"><label>Respuesta generada (editable)</label><textarea id="resp" rows="8" class="resp"></textarea></div>
   <button class="b2" onclick="genResp()">↻ Regenerar respuesta</button>
   <div class="chk" style="margin-top:8px"><input type="checkbox" id="verifico"><label><b>Verifiqué la congruencia de la respuesta con la solicitud y los criterios aplicados.</b></label></div>
   <div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap"><button class="b3" onclick="registrar()">💾 Registrar respuesta</button><button class="b1" onclick="copiar()">📋 Copiar</button><button class="bd" style="color:#fff;background:#5d6d7e" onclick="expCSV()">⬇ Expedientes (CSV)</button></div>
  </div>
 </div>
</div></section>

<section class="sec" data-s="r">
 <div class="warnbig">⚠️ La información de transparencia entregada genera responsabilidad. Verifica cada cifra y su criterio antes de oficializar. Este registro es de control interno.</div>
 <div class="card"><h2>Registro de solicitudes UTI atendidas <input id="rq" placeholder="buscar folio/texto" oninput="renderReg()" style="float:right;padding:6px 9px;border:1px solid var(--line);border-radius:6px;font-size:12px"></h2>
  <table id="t_reg"></table>
  <div style="margin-top:10px"><button class="b1" onclick="expReg()">⬇ Exportar registro (CSV)</button></div>
 </div>
</section>

</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;document.getElementById('fc').textContent=D.corte;
let REG=JSON.parse(localStorage.getItem('sigej_uti')||'[]');
function tab(t){document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('act'));document.getElementById('tb_'+t).classList.add('act');
 document.querySelectorAll('.sec').forEach(s=>s.classList.remove('act'));document.querySelector('[data-s="'+t+'"]').classList.add('act');if(t=='r')renderReg();}
function opt(id,arr,ph){document.getElementById(id).innerHTML=`<option value="">${ph}</option>`+arr.map(x=>`<option>${x}</option>`).join('');}
opt('materia',D.cats.materia,'Todas');opt('via',D.cats.via,'Todas');opt('tipo',D.cats.tipo,'Todos');opt('estado',D.cats.estado,'Todos');opt('responsable',D.cats.responsable,'Todos');
document.getElementById('l_aut').innerHTML=D.cats.autoridad.map(x=>`<option>${x}</option>`).join('');
document.getElementById('l_dep').innerHTML=D.cats.dependencia.map(x=>`<option>${x}</option>`).join('');
const V=id=>document.getElementById(id).value.trim();
let CUR=[];
function filtra(){const q=V('q').toLowerCase(),ad=+V('ad')||0,ah=+V('ah')||0,vig=V('vig'),
 mat=V('materia'),via=V('via'),tj=V('tipo'),est=V('estado'),resp=V('responsable'),aut=V('autoridad').toLowerCase(),dep=V('dependencia').toLowerCase(),
 xs=document.getElementById('x_sent').checked,xp=document.getElementById('x_susp').checked,xc=document.getElementById('x_conc').checked,
 md=+V('md')||0,mh=+V('mh')||0,xm=document.getElementById('x_monto').checked;
 return D.expedientes.filter(e=>{
  if(vig=='act'&&!e.activo)return false;if(vig=='con'&&e.activo)return false;
  if(xm&&!(e.monto>0))return false;if(md&&(!e.monto||e.monto<md))return false;if(mh&&(e.monto||0)>mh)return false;
  if(ad&&(!e.anio||e.anio<ad))return false;if(ah&&(!e.anio||e.anio>ah))return false;
  if(mat&&e.materia!==mat)return false;if(via&&e.via!==via)return false;if(tj&&e.tipo!==tj)return false;
  if(est&&e.estado!==est)return false;if(resp&&e.responsable!==resp)return false;
  if(aut&&!(e.autoridad||'').toLowerCase().includes(aut))return false;
  if(dep&&!(e.dependencia||'').toLowerCase().includes(dep))return false;
  if(xs&&!e.sentencia)return false;if(xp&&!e.susp)return false;if(xc&&!e.concil)return false;
  if(q&&!((e.num+' '+(e.actor||'')).toLowerCase().includes(q)))return false;return true;});}
function tbl(id,obj){const e=Object.entries(obj).sort((a,b)=>b[1]-a[1]);
 document.getElementById(id).innerHTML='<tr><th>Categoría</th><th>N</th></tr>'+e.map(x=>`<tr><td>${x[0]}</td><td><b>${x[1]}</b></td></tr>`).join('')+`<tr style="font-weight:700;background:#eef2f7"><td>Total</td><td>${e.reduce((s,x)=>s+x[1],0)}</td></tr>`;}
function group(L,k){const o={};L.forEach(e=>{const v=e[k]||'(s/d)';o[v]=(o[v]||0)+1;});return o;}
function run(){const L=filtra();CUR=L;
 const sent=L.filter(e=>e.sentencia).length,susp=L.filter(e=>e.susp).length,conc=L.filter(e=>e.concil).length,
 act=L.filter(e=>e.activo).length,cuantia=L.reduce((s,e)=>s+(e.monto||0),0),conm=L.filter(e=>e.monto>0).length;
 document.getElementById('kpis').innerHTML=[[L.length,'Total (filtro)'],[act,'Activas'],[L.length-act,'Concluidas'],[sent,'Con sentencia'],[susp,'Susp. provisional'],[conc,'Conciliación'],['$'+(cuantia/1e6).toFixed(2)+'M','Cuantía ('+conm+' exp.)']]
  .map(x=>`<div class="kpi"><div class="n">${x[0]}</div><div class="l">${x[1]}</div></div>`).join('');
 tbl('t_mat',group(L,'materia'));tbl('t_anio',group(L,'anio'));tbl('t_est',group(L,'estado'));tbl('t_via',group(L,'via'));
 verif(L);genResp();}
function criterios(){const c=[];const ad=V('ad'),ah=V('ah'),vig=V('vig');
 c.push(vig=='act'?'solo demandas activas':vig=='con'?'solo concluidas':'activas y concluidas');
 if(ad||ah)c.push('años '+(ad||'inicio')+'–'+(ah||'2026'));
 ['materia','via','tipo','estado','responsable'].forEach(k=>{if(V(k))c.push(k+': '+V(k));});
 if(V('autoridad'))c.push('autoridad ~ '+V('autoridad'));if(V('dependencia'))c.push('dependencia ~ '+V('dependencia'));
 if(V('md')||V('mh'))c.push('cuantía $'+(V('md')||'0')+'–$'+(V('mh')||'∞'));if(document.getElementById('x_monto').checked)c.push('con cuantía registrada');
 if(document.getElementById('x_sent').checked)c.push('con sentencia');if(document.getElementById('x_susp').checked)c.push('con suspensión provisional');if(document.getElementById('x_conc').checked)c.push('en conciliación');
 return c.join('; ');}
function verif(L){const susp=L.filter(e=>e.susp).length,conc=L.filter(e=>e.concil).length;
 document.getElementById('verif').innerHTML=`<b>Procedencia del dato:</b> ${D.fuente}, corte ${D.corte}.<br><b>Criterios aplicados:</b> ${criterios()||'(sin filtros — universo completo)'}.<br><b>Coincidencias:</b> ${L.length} expediente(s).`+
  `<ul><li><b>"Suspensión provisional"</b> (${susp}) = concedida, por análisis de texto del historial → confirmar caso por caso para efectos oficiales.</li>`+
  `<li><b>"Conciliación"</b> (${conc}) = convenio documentado; NO incluye desistimientos, caducidades ni sobreseimientos.</li>`+
  `<li><b>"Activa"</b> = expediente cuyo estado ≠ CONCLUIDO. <b>"Sentencia"</b> = etapa laudo/sentencia o con resolución registrada.</li>`+
  `<li><b>"Cuantía"</b> se extrae por NLP del texto del expediente (sanitizada ≤$100M); es un <b>piso parcial</b> de exposición, NO la cuantía oficial — verificar.</li>`+
  `<li>El "año" se deriva del número de expediente. Verifica la congruencia con lo solicitado antes de entregar.</li></ul>`;}
function genResp(){const L=CUR;const folio=V('folio')||'[folio]';
 const sent=L.filter(e=>e.sentencia).length,susp=L.filter(e=>e.susp).length,conc=L.filter(e=>e.concil).length,act=L.filter(e=>e.activo).length;
 const bm=group(L,'materia');const bml=Object.entries(bm).sort((a,b)=>b[1]-a[1]).map(x=>x[0]+': '+x[1]).join(', ');
 document.getElementById('resp').value=
`En atención a la solicitud ${folio}, con datos al corte ${D.corte}:

Bajo los criterios [${criterios()||'universo completo'}], la Universidad de Guadalajara registra ${L.length} expediente(s), de los cuales ${act} se encuentran activos y ${L.length-act} concluidos.

Desglose por materia: ${bml}.

De ese universo: ${sent} han llegado a etapa de sentencia/laudo; ${susp} cuentan con suspensión provisional concedida (dato documental, a confirmar); y ${conc} se han resuelto mediante conciliación/convenio documentado.

Nota metodológica: información obtenida de la base consolidada de expedientes (${D.fuente}). Las cifras de suspensión y conciliación derivan de análisis documental y deben verificarse caso por caso para efectos oficiales.`;}
function copiar(){navigator.clipboard&&navigator.clipboard.writeText(document.getElementById('resp').value);}
function limpiar(){['q','ad','ah','materia','via','tipo','estado','responsable','autoridad','dependencia','md','mh'].forEach(i=>document.getElementById(i).value='');
 document.getElementById('vig').value='act';['x_sent','x_susp','x_conc','x_monto'].forEach(i=>document.getElementById(i).checked=false);run();}
function registrar(){if(!V('folio')){alert('Indica el folio UTI.');return;}
 if(!document.getElementById('verifico').checked){alert('Debes marcar la casilla de verificación de congruencia antes de registrar.');return;}
 const r={folio:V('folio'),fecha_solicitud:V('fsol'),fecha_respuesta:V('fresp')||new Date().toISOString().slice(0,10),
  solicitud:V('solicitud'),responde:V('quien'),criterios:criterios(),total:CUR.length,
  activas:CUR.filter(e=>e.activo).length,sentencia:CUR.filter(e=>e.sentencia).length,susp:CUR.filter(e=>e.susp).length,concil:CUR.filter(e=>e.concil).length,
  respuesta:document.getElementById('resp').value,registrado:new Date().toISOString().slice(0,16).replace('T',' ')};
 const ix=REG.findIndex(x=>x.folio===r.folio);if(ix>=0){if(!confirm('El folio '+r.folio+' ya existe. ¿Actualizar?'))return;REG[ix]=r;}else REG.push(r);
 localStorage.setItem('sigej_uti',JSON.stringify(REG));document.getElementById('verifico').checked=false;document.getElementById('nreg').textContent=REG.length;
 alert('✓ Solicitud '+r.folio+' registrada.');}
function renderReg(){document.getElementById('nreg').textContent=REG.length;const q=(document.getElementById('rq').value||'').toLowerCase();
 const L=REG.filter(r=>(r.folio+' '+(r.solicitud||'')).toLowerCase().includes(q)).sort((a,b)=>(b.fecha_respuesta||'').localeCompare(a.fecha_respuesta||''));
 document.getElementById('t_reg').innerHTML=L.length?('<tr><th>Folio</th><th>F. solicitud</th><th>F. respuesta</th><th>Total</th><th>Responde</th><th>Criterios</th><th></th></tr>'+
  L.map(r=>`<tr><td><b>${r.folio}</b></td><td>${r.fecha_solicitud||'—'}</td><td>${r.fecha_respuesta||'—'}</td><td>${r.total}</td><td>${r.responde||'—'}</td><td style="font-size:11px;color:#64748b">${r.criterios||''}</td><td><span class="lk" onclick="verReg('${r.folio.replace(/'/g,"")}')">ver</span> · <span class="lk" onclick="oficio('${r.folio.replace(/'/g,"")}')">📄 oficio</span> · <span class="del" onclick="delReg('${r.folio.replace(/'/g,"")}')">✕</span></td></tr>`).join('')):'<tr><td colspan="7" style="color:#94a3b8;padding:12px">Sin solicitudes registradas.</td></tr>';}
function oficio(folio){const r=REG.find(x=>x.folio===folio);if(!r)return;
 const fr=r.fecha_respuesta||new Date().toISOString().slice(0,10);
 const body=`<div style="text-align:right;font-size:11pt">Guadalajara, Jalisco, a ${fr}.<br>Oficio de respuesta: ${r.folio}</div>`+
  `<p style="font-size:11pt"><b>UNIVERSIDAD DE GUADALAJARA</b><br>Oficina de la Abogacía General<br>Unidad de Transparencia</p>`+
  `<p style="font-size:11pt">En atención a la solicitud de información con folio <b>${r.folio}</b>${r.fecha_solicitud?', presentada el '+r.fecha_solicitud:''}, que a la letra refiere:</p>`+
  `<p style="font-size:10.5pt;font-style:italic;border-left:3px solid #888;padding-left:10px">${(r.solicitud||'(sin texto)').replace(/</g,'&lt;')}</p>`+
  `<p style="font-size:11pt">Se hace de su conocimiento lo siguiente:</p>`+
  `<p style="font-size:11pt;white-space:pre-wrap">${(r.respuesta||'').replace(/</g,'&lt;')}</p>`+
  `<p style="font-size:10pt;color:#555"><b>Criterios de búsqueda aplicados:</b> ${r.criterios||'universo completo'}. Cifras de control: total ${r.total}, activas ${r.activas}, con sentencia ${r.sentencia}, suspensión provisional ${r.susp}, conciliación ${r.concil}.</p>`+
  `<br><br><div style="text-align:center;font-size:11pt">_________________________________<br>${r.responde||'Servidor público habilitado'}<br>Oficina de la Abogacía General · UdeG</div>`;
 const html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"></head><body style="font-family:Calibri,Arial;margin:60px">'+body+'</body></html>';
 const b=new Blob(['﻿'+html],{type:'application/msword'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Oficio_'+folio.replace(/[\/]/g,'-')+'.doc';a.click();}
function verReg(folio){const r=REG.find(x=>x.folio===folio);if(!r)return;alert('Folio '+r.folio+'\n\nSolicitud: '+(r.solicitud||'—')+'\n\nCriterios: '+r.criterios+'\n\nRESPUESTA:\n'+r.respuesta);}
function delReg(folio){if(confirm('¿Eliminar el registro '+folio+'?')){REG=REG.filter(x=>x.folio!==folio);localStorage.setItem('sigej_uti',JSON.stringify(REG));renderReg();}}
function expReg(){if(!REG.length){alert('Sin registros.');return;}const cols=['folio','fecha_solicitud','fecha_respuesta','responde','criterios','total','activas','sentencia','susp','concil','solicitud','respuesta'];
 const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const csv=cols.join(',')+'\n'+REG.map(r=>cols.map(c=>esc(r[c])).join(',')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='registro_solicitudes_UTI.csv';a.click();}
function expCSV(){if(!CUR.length)return;const cols=['num','anio','materia','via','tipo','estado','responsable','monto','activo','sentencia','susp','concil'];
 const esc=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';
 const csv=cols.join(',')+'\n'+CUR.map(r=>cols.map(c=>esc(r[c])).join(',')).join('\n');
 const b=new Blob(['﻿'+csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='transparencia_'+(V('folio')||'consulta').replace(/[\/]/g,'-')+'.csv';a.click();}
document.getElementById('vig').value='act';document.getElementById('nreg').textContent=REG.length;run();
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
open("/Users/edithroque/Documents/CLAUDE/transparencia_SIGEJ.html","w",encoding="utf-8").write(TPL.replace("__DATA__",DATA).replace("__NAV__",NAV))
print("transparencia_SIGEJ.html OK")
