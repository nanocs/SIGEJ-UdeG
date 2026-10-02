# -*- coding: utf-8 -*-
import json
d=json.load(open("/Users/edithroque/Documents/CLAUDE/dashboard_data.json",encoding="utf-8"))
try: d["equidad"]=json.load(open("/Users/edithroque/Documents/CLAUDE/equidad_data.json",encoding="utf-8"))
except Exception: d["equidad"]=None
try: d["mod"]=json.load(open("/Users/edithroque/Documents/CLAUDE/alertas_data.json",encoding="utf-8"))
except Exception: d["mod"]=None
try: d["lecpro"]=json.load(open("/Users/edithroque/Documents/CLAUDE/lecciones_pro.json",encoding="utf-8"))
except Exception: d["lecpro"]=None
try: d["riesgo_materia"]=json.load(open("/Users/edithroque/Documents/CLAUDE/riesgo_materia.json",encoding="utf-8"))
except Exception: d["riesgo_materia"]=None
try: d["provision"]=json.load(open("/Users/edithroque/Documents/CLAUDE/provision_base.json",encoding="utf-8"))
except Exception: d["provision"]=None
try:
    d["cuellos"]=json.load(open("/Users/edithroque/Documents/CLAUDE/cuellos_data.json",encoding="utf-8"))
    d["cuellos"].pop("data",None)  # aligerar: la vista usa agregados, no los 748 registros
except Exception: d["cuellos"]=None
DATA=json.dumps(d,ensure_ascii=False)

TPL=r"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Cuadro de Mando Integral · Abogacía General</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--ink:#0a1f3c;--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--red:#c0392b;
--bg:#f4f6f9;--card:#fff;--mut:#64748b;--line:#e2e8f0;--ok:#1f9d6b;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,var(--azul),var(--azul2));color:#fff;padding:18px 28px}
header h1{margin:0;font-size:20px;letter-spacing:.3px}
header .sub{opacity:.85;font-size:12.5px;margin-top:4px}
.badge{display:inline-block;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);
border-radius:20px;padding:2px 10px;font-size:11px;margin-right:6px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:0 16px;border-bottom:1px solid #14304f}
.navbar a{color:#aebfd6;text-decoration:none;padding:9px 12px;font-size:12.5px;border-bottom:3px solid transparent}
.navbar a:hover{color:#fff}.navbar a.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
nav{display:flex;gap:4px;background:var(--ink);padding:0 20px;flex-wrap:wrap}
nav button{background:none;border:none;color:#cbd5e1;padding:12px 16px;cursor:pointer;font-size:13px;border-bottom:3px solid transparent}
nav button.act{color:#fff;border-bottom-color:var(--gold);font-weight:600}
.wrap{padding:20px 28px;max-width:1400px;margin:auto}
.sec{display:none}.sec.act{display:block}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-bottom:18px}
.kpi{background:var(--card);border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.07);border-left:4px solid var(--teal)}
.kpi .n{font-size:28px;font-weight:700;color:var(--azul)}
.kpi .l{font-size:12px;color:var(--mut);margin-top:2px}
.kpi.warn{border-left-color:var(--gold)}.kpi.bad{border-left-color:var(--red)}.kpi.good{border-left-color:var(--ok)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px}
.card{background:var(--card);border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.07)}
.card h3{margin:0 0 12px;font-size:14px;color:var(--azul)}
.card.span2{grid-column:span 2}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th,td{padding:6px 8px;text-align:left;border-bottom:1px solid var(--line)}
th{color:var(--mut);font-weight:600}
.heat td{text-align:center;font-weight:600;color:#fff;border:2px solid #fff;border-radius:4px}
.note{background:#fff8e6;border:1px solid var(--gold);border-radius:10px;padding:14px;font-size:12.5px;margin-top:18px}
.note b{color:#8a6d1a}
.pill{font-size:11px;padding:2px 8px;border-radius:10px;background:#eef2f7;color:var(--mut)}
footer{padding:16px 28px;color:var(--mut);font-size:11.5px;text-align:center}
canvas{max-height:300px}
.alist{max-height:340px;overflow:auto}.alist .it{padding:8px 6px;border-bottom:1px solid var(--line);font-size:12.5px;display:flex;justify-content:space-between;gap:8px}
.exp{color:var(--azul2);font-weight:600;cursor:pointer;text-decoration:underline dotted}
.tag{font-size:10.5px;padding:1px 7px;border-radius:9px;font-weight:600}
.t-Crítico{background:#fdecea;color:#c0392b}.t-Alto{background:#fef3e0;color:#b9770e}.t-Medio{background:#e6f6f4;color:#138a7f}.t-Bajo{background:#eef2f7;color:#64748b}
.modal{position:fixed;inset:0;background:rgba(8,20,38,.55);display:none;align-items:center;justify-content:center;z-index:50;padding:18px}
.modal.on{display:flex}.mbox{background:#fff;border-radius:14px;max-width:760px;width:100%;max-height:88vh;overflow:auto;padding:22px;box-shadow:0 10px 40px rgba(0,0,0,.3)}
.mx{float:right;cursor:pointer;color:var(--mut);font-size:22px}
.mtx{font-size:12px;color:var(--mut);background:#f4f6f9;border-radius:8px;padding:8px 10px;margin:3px 0}
.estr{border-left:3px solid var(--teal);background:#f6fbfb;padding:10px 12px;margin:8px 0;border-radius:0 8px 8px 0}
.estr b{color:var(--azul)}.mtag{display:inline-block;padding:1px 8px;border-radius:9px;font-size:10.5px;background:#eef2f7;color:#475569;margin-left:6px}
.lcard{background:var(--card);border-radius:12px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.07);margin-bottom:14px}
.lcard h4{margin:0 0 6px;color:var(--azul);font-size:15px}
.lrow{font-size:12.8px;margin:5px 0}.lrow b{color:#0a2a4a}
.warnbox{background:#fff8e6;border:1px solid var(--gold);border-radius:8px;padding:4px 9px;font-size:11px;color:#8a6d1a;display:inline-block}
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
<header>
<h1>⚖️ SIGEJ-UdeG · Sistema Integral de Gestión Jurídica</h1>
<div class="sub">Cuadro de Mando Integral — Oficina de la Abogacía General · Universidad de Guadalajara</div>
<div style="margin-top:8px">
<span class="badge">Universo: <b id="bu"></b> expedientes</span>
<span class="badge">Corte: <b id="bf"></b></span>
<span class="badge">Fuente: juicios.tab</span>
<span class="badge">Motor analítico: 🔍 Veritas / LEXCLAW</span>
<a href="SIGEJ_inicio.html" class="badge" style="text-decoration:none;color:#fff;background:rgba(255,255,255,.18)">🏠 Inicio</a>
<a href="modulo_expedientes_SIGEJ.html" class="badge" style="text-decoration:none;color:#fff;background:rgba(212,163,44,.35);border-color:#d4a32c">📁 Módulo de Expedientes →</a>
<a href="captura_expediente_SIGEJ.html" class="badge" style="text-decoration:none;color:#fff;background:rgba(31,157,107,.35);border-color:#1f9d6b">➕ Capturar nuevo →</a>
</div></header>
<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="dashboard_SIGEJ.html" class="act">📊 Dashboard</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Asuntos Internacionales</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="chat_SIGEJ.html">💬 Chat</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a></div>
<nav id="nav"></nav>
<div class="wrap">

<section class="sec act" data-s="exec"><div class="kpis" id="kexec"></div>
 <div class="grid">
  <div class="card"><h3>Expedientes por materia (rama sustantiva)</h3><canvas id="cMat"></canvas></div>
  <div class="card"><h3>Estado / etapa procesal</h3><canvas id="cEst"></canvas></div>
  <div class="card span2"><h3>Demandas por año (radicación según expediente)</h3><canvas id="cAnio"></canvas></div>
  <div class="card"><h3>Tipo de juicio</h3><canvas id="cTJ"></canvas></div>
  <div class="card"><h3>Órgano jurisdiccional</h3><canvas id="cOrg"></canvas></div>
 </div></section>

<section class="sec" data-s="bsc">
 <div style="font-size:12.5px;color:#64748b;margin-bottom:12px">Cuadro de Mando Integral (Kaplan & Norton) adaptado a la Abogacía General — 4 perspectivas. 🟢 dato real · 🟡 a capturar.</div>
 <div class="grid" id="bscGrid"></div>
</section>

<section class="sec" data-s="lit"><div class="kpis" id="klit"></div>
 <div class="grid">
  <div class="card"><h3>Sentido de la resolución</h3><canvas id="cSent"></canvas></div>
  <div class="card"><h3>Suspensión provisional (de 48 que la mencionan)</h3><canvas id="cSusp"></canvas></div>
  <div class="card span2"><h3>Embudo de conclusión procesal</h3><canvas id="cFun"></canvas></div>
 </div></section>

<section class="sec" data-s="prod"><div class="kpis" id="kprod"></div>
 <div class="grid"><div class="card span2"><h3>Carga de trabajo por abogado (nº de expedientes)</h3><canvas id="cAbo"></canvas></div></div></section>

<section class="sec" data-s="desemp">
 <div class="grid">
  <div class="card span2"><h3>Tasa de éxito por abogado — estricta vs ampliada (base ≥10)</h3><canvas id="cDesemp"></canvas></div>
  <div class="card span2"><h3>Tabla de desempeño (carga + tasas)</h3>
   <div style="font-size:11.5px;color:#64748b;margin-bottom:8px">Estricta = Fav/(Fav+Desf) · Ampliada = Éxito/(Éxito+Adverso, incluye sobreseimientos y amparos negados a la contraparte). 🟢 base≥15 · 🟡 base 7-14 · 🔴 base&lt;7.</div>
   <table id="tDesemp"></table></div>
 </div></section>

<section class="sec" data-s="equidad"><div class="kpis" id="kequi"></div>
 <div class="grid">
  <div class="card span2"><h3>Carga vigente vs. asuntos de alto riesgo (burbuja = pasivo $)</h3><canvas id="cEqui"></canvas></div>
  <div class="card span2"><h3>Tablero de equidad de cargas</h3>
   <div style="font-size:11.5px;color:#64748b;margin-bottom:8px">Dens.% = alto riesgo / carga vigente · Score prom = riesgo medio de la cartera · 🔴 marca al abogado con carga alta + riesgo alto + tasa baja.</div>
   <table id="tEqui"></table></div>
 </div></section>

<section class="sec" data-s="provision">
 <div class="card" style="margin-bottom:14px"><h3>Política de provisión — ajusta los % (recalcula en vivo)</h3>
  <div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center;font-size:13px">
   <label>🔴 Crítico % <input id="pc_Crítico" type="number" min="0" max="100" style="width:60px;padding:5px;border:1px solid #e2e8f0;border-radius:6px" oninput="prov()"></label>
   <label>🟠 Alto % <input id="pc_Alto" type="number" min="0" max="100" style="width:60px;padding:5px;border:1px solid #e2e8f0;border-radius:6px" oninput="prov()"></label>
   <label>🟡 Medio % <input id="pc_Medio" type="number" min="0" max="100" style="width:60px;padding:5px;border:1px solid #e2e8f0;border-radius:6px" oninput="prov()"></label>
   <label>⚪ Bajo % <input id="pc_Bajo" type="number" min="0" max="100" style="width:60px;padding:5px;border:1px solid #e2e8f0;border-radius:6px" oninput="prov()"></label>
   <label style="margin-left:10px"><input type="checkbox" id="pc_imp" checked onchange="prov()"> Imputar montos faltantes (mediana)</label>
   <label><input type="checkbox" id="pc_bajo" onchange="prov()"> Incluir "Bajo" en la imputación</label>
   <button onclick="provReset()" style="padding:6px 12px;border:none;border-radius:7px;background:#0a4d8c;color:#fff;cursor:pointer">Restablecer</button>
  </div>
 </div>
 <div class="kpis" id="kprov"></div>
 <div class="grid">
  <div class="card span2"><h3>Reserva por nivel (documentada vs. estimada)</h3><canvas id="cProv"></canvas></div>
  <div class="card span2"><h3>Detalle de provisión</h3><table id="tProv"></table>
   <div class="warnbox" style="margin-top:10px">Reserva documentada = solo montos capturados (38 de 659 activos). Estimada = imputa la mediana ($<span id="pc_med"></span>) a los expedientes sin monto. Los % son política contable — decisión de la Abogacía General. NIF C-9 / IAS 37.</div>
  </div>
 </div>
</section>

<section class="sec" data-s="tiempos"><div class="kpis" id="ktiempos"></div>
 <div class="grid">
  <div class="card span2"><h3>Cuellos de botella — días entre etapas procesales (mediana)</h3><canvas id="cTrans"></canvas></div>
  <div class="card"><h3>Duración del juicio por materia (días)</h3><canvas id="cDurMat"></canvas></div>
  <div class="card"><h3>Expedientes activos más atorados</h3><table id="tAtor"></table></div>
 </div>
 <div class="warnbox" style="margin-top:12px">"Sin movimiento" = sin actuación <b>registrada en el texto</b> desde la última fecha; puede indicar estancamiento real o falta de captura. Duraciones medidas entre primer y último evento fechado del historial.</div>
</section>

<section class="sec" data-s="agenda"><div class="kpis" id="kagenda"></div>
 <div class="card"><h3>Agenda consolidada — audiencias, términos, plazos, contestaciones, seguimientos</h3><div id="agBody"></div></div>
</section>

<section class="sec" data-s="alertas"><div class="kpis" id="kalert"></div>
 <div class="grid">
  <div class="card"><h3>⏰ Vencimientos / próximos términos</h3><div class="alist" id="aVenc"></div></div>
  <div class="card"><h3>⚠️ Inactividad — riesgo de caducidad (≥18 meses sin movimiento)</h3><div class="alist" id="aInact"></div></div>
  <div class="card"><h3>💰 Contingente en riesgo (alto riesgo + monto)</h3><div class="alist" id="aCont"></div></div>
  <div class="card"><h3>🎯 Fichas de estrategia por riesgo — clic en el expediente</h3><div class="alist" id="aFichas"></div></div>
 </div>
 <div class="warnbox" style="margin-top:12px">⚠️ "Fecha de término" es un campo a capturar: las alertas de vencimiento se poblarán por completo al migrar. Estrategias = plantillas orientativas trazables; artículos marcados "verificar". Validación profesional: Edith.</div>
</section>

<section class="sec" data-s="lecciones">
 <div style="font-size:13px;color:#475569;margin-bottom:8px"><b>🧠 Centro de Inteligencia Jurídica</b> — Legal Analytics + Gestión del Conocimiento. No solo "¿qué pasó?", también <b>por qué, si era previsible, cómo evitarlo, quién intervino, qué cuesta y qué hacer para que no se repita</b>.</div>
 <div class="warnbox" style="margin-bottom:12px">🟢 dato real (conteos, dependencias, abogados, montos). La <b>causa raíz (Ishikawa)</b>, lección y acción son <b>base de conocimiento curada</b>; los "indicios NLP" son menciones detectadas en el texto (a validar); impacto = piso parcial. Fundamento con sello de verificación.</div>
 <div id="lecCards"></div>
</section>

<section class="sec" data-s="risk">
 <div class="grid">
  <div class="card span2"><h3>Mapa de calor — Litigiosidad por dependencia × materia</h3><div id="heat"></div></div>
  <div class="card span2"><h3>Pareto — Dependencias con mayor litigiosidad</h3><canvas id="cPareto"></canvas></div>
  <div class="card span2"><h3>Pasivo contingente (activo) por materia</h3><canvas id="cPasMat"></canvas></div>
  <div class="card span2"><h3>Riesgo por materia (rama sustantiva)</h3><table id="tRieMat"></table></div>
 </div></section>

<section class="sec" data-s="gov">
 <div class="card"><h3>Gobierno y calidad de datos (estado de la fuente)</h3>
 <table id="govt"></table></div>
 <div class="note"><b>⚠️ Campos a capturar en el sistema (NO existen en el archivo actual):</b>
 Riesgo jurídico, Probabilidad de éxito, Monto contingente estructurado, Fecha de cierre, Responsable por rol,
 Documentos/correos vinculados. El dashboard muestra <b>solo dato documentado</b>; estos campos se habilitan al migrar a SIGEJ.
 El "Pasivo contingente" mostrado es un <b>piso parcial</b> (montos extraídos por texto de 42 expedientes).</div>
</section>

</div>
<div class="modal" id="modal"><div class="mbox"><span class="mx" onclick="cf()">✕</span><div id="mbody"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;
document.getElementById('bu').textContent=D.meta.universo;
document.getElementById('bf').textContent=D.meta.fecha_corte;
const PAL=['#00254a','#0a4d8c','#1aa39a','#d4a32c','#c0392b','#7e57c2','#2e7d32','#e07b39','#5d6d7e','#16a085'];
const peso=(o,n)=>Object.entries(o).slice(0,n||99);
function nav(){const s=[['exec','Ejecutivo'],['bsc','CMI · Balanced Scorecard'],['lit','Litigios'],['prod','Productividad'],['desemp','Desempeño'],['equidad','Equidad de cargas'],['provision','Provisión'],['tiempos','Tiempos & Cuellos'],['agenda','Agenda'],['alertas','Alertas & Estrategia'],['lecciones','Lecciones aprendidas'],['risk','Riesgos'],['gov','Gobierno de datos']];
 const n=document.getElementById('nav');s.forEach((x,i)=>{const b=document.createElement('button');b.textContent=x[1];if(i==0)b.className='act';
 b.onclick=()=>{document.querySelectorAll('nav button').forEach(z=>z.classList.remove('act'));b.classList.add('act');
 document.querySelectorAll('.sec').forEach(z=>z.classList.remove('act'));document.querySelector('[data-s="'+x[0]+'"]').classList.add('act');};n.appendChild(b);});}
function kpi(el,arr){document.getElementById(el).innerHTML=arr.map(k=>`<div class="kpi ${k[2]||''}"><div class="n">${k[0]}</div><div class="l">${k[1]}</div></div>`).join('');}
function bar(id,o,horiz,clr){new Chart(document.getElementById(id),{type:'bar',data:{labels:Object.keys(o),
 datasets:[{data:Object.values(o),backgroundColor:clr||'#0a4d8c'}]},options:{indexAxis:horiz?'y':'x',
 plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:10}}},y:{ticks:{font:{size:10}}}}}});}
function do()=>0;
// KPIs
const k=D.kpis;
kpi('kexec',[[k.total,'Expedientes (base estructurada)'],[k.activos,'Activos','good'],[k.concluidos,'Concluidos'],
 [k.pct_activos+'%','% activos','warn'],[D.meta.universo,'Universo real (+recuperados)'],[k.abogados,'Abogados']]);
kpi('klit',[[k.tasa_exito+'%','Tasa de éxito (Fav/Fav+Desf)','warn'],[D.litigios.con_resolucion,'Con resolución de fondo'],
 [D.litigios.laudo+D.litigios.sentencia_etapa,'En etapa laudo/sentencia'],[k.susp_concedidas,'Susp. prov. concedidas*','bad'],
 [k.conciliaciones,'Conciliaciones'],[D.litigios.favorable,'Favorables','good']]);
kpi('kprod',[[k.abogados,'Abogados activos'],[Math.round(k.total/k.abogados),'Carga promedio / abogado'],
 [Object.values(D.abogado)[0],'Carga máxima','bad'],[k.total,'Expedientes asignados']]);
// charts
new Chart(cMat,{type:'doughnut',data:{labels:Object.keys(D.materia_fina||D.materia),datasets:[{data:Object.values(D.materia_fina||D.materia),backgroundColor:PAL}]},options:{plugins:{legend:{position:'right',labels:{font:{size:11}}}}}});
bar('cEst',D.estado,true,'#1aa39a');
new Chart(cAnio,{type:'line',data:{labels:Object.keys(D.anio),datasets:[{data:Object.values(D.anio),borderColor:'#00254a',backgroundColor:'rgba(10,77,140,.15)',fill:true,tension:.3}]},options:{plugins:{legend:{display:false}}}});
bar('cTJ',D.tipo_juicio,true,'#0a4d8c');
bar('cOrg',D.organo,true,'#5d6d7e');
bar('cSent',D.sentido,true,'#7e57c2');
new Chart(cSusp,{type:'doughnut',data:{labels:Object.keys(D.litigios.susp),datasets:[{data:Object.values(D.litigios.susp),backgroundColor:['#1f9d6b','#c0392b','#d4a32c']}]}});
const fun={'Total':D.kpis.total,'Activos':D.kpis.activos,'Con resolución':D.litigios.con_resolucion,'Laudo/Sentencia':D.litigios.laudo+D.litigios.sentencia_etapa,'Conciliados':D.litigios.conciliacion,'Concluidos':D.kpis.concluidos};
bar('cFun',fun,false,'#00254a');
bar('cAbo',D.abogado,true,'#0a4d8c');
// heatmap
const mats=['Laboral','Civil','Penal'];let mx=0;D.heatmap.forEach(r=>mats.forEach(m=>mx=Math.max(mx,r[m])));
let h='<table class="heat"><tr><th style="color:#64748b">Dependencia</th>'+mats.map(m=>'<th style="color:#64748b;text-align:center">'+m+'</th>').join('')+'</tr>';
D.heatmap.forEach(r=>{h+='<tr><td style="color:#0a1f3c;text-align:left">'+r.dependencia+'</td>'+mats.map(m=>{const v=r[m];const a=v/mx;return '<td style="background:rgba(192,57,43,'+(0.12+a*0.85)+')">'+v+'</td>';}).join('')+'</tr>';});
h+='</table>';document.getElementById('heat').innerHTML=h;
bar('cPareto',D.dependencia,false,'#c0392b');
// desempeño por abogado
const dz=D.desempeno.slice().sort((a,b)=>(b.tasa_ampliada||0)-(a.tasa_ampliada||0));
const dzc=dz.filter(x=>x.base_ampliada>=10);
new Chart(cDesemp,{type:'bar',data:{labels:dzc.map(x=>x.abogado.split(' ').slice(0,2).join(' ')),
 datasets:[{label:'Estricta %',data:dzc.map(x=>x.tasa_estricta),backgroundColor:'#5d6d7e'},
           {label:'Ampliada %',data:dzc.map(x=>x.tasa_ampliada),backgroundColor:'#1aa39a'}]},
 options:{plugins:{legend:{position:'top'}},scales:{y:{max:100,ticks:{callback:v=>v+'%'}},x:{ticks:{font:{size:9}}}}}});
// equidad de cargas
if(D.equidad){const E=D.equidad;
 kpi('kequi',[[E.corr_carga_riesgo,'Correlación carga↔riesgo','bad'],[E.gini_carga,'Gini de carga','warn'],
  [E.gini_riesgo,'Gini de riesgo','warn'],[E.total_alto,'Asuntos alto riesgo']]);
 const col=a=>a.tasa_ampliada===null?'#94a3b8':a.tasa_ampliada<50?'#c0392b':a.tasa_ampliada<58?'#e08e0b':'#1f9d6b';
 new Chart(cEqui,{type:'bubble',data:{datasets:E.abogados.filter(a=>a.vigentes>0).map(a=>({label:a.abogado.split(' ').slice(0,2).join(' '),
   data:[{x:a.vigentes,y:a.alto_riesgo,r:Math.max(4,Math.sqrt(a.pasivo)/120)}],backgroundColor:col(a)+'cc',borderColor:col(a)}))},
  options:{plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>c.dataset.label+': carga '+c.raw.x+', alto riesgo '+c.raw.y}}},
   scales:{x:{title:{display:true,text:'Carga vigente'}},y:{title:{display:true,text:'Asuntos de alto riesgo'},beginAtZero:true}}}});
 const flag=a=>(a.vigentes>=60&&a.alto_riesgo>=5&&(a.tasa_ampliada||100)<50)?'🔴':'';
 document.getElementById('tEqui').innerHTML='<tr><th>Abogado</th><th>Carga vig.</th><th>Alto riesgo</th><th>Crít.</th><th>Dens.%</th><th>Score prom</th><th>Tasa ampl.</th><th>Pasivo</th><th></th></tr>'+
  E.abogados.map(a=>`<tr><td>${a.abogado}</td><td><b>${a.vigentes}</b></td><td>${a.alto_riesgo}</td><td>${a.critico||''}</td><td>${a.dens_riesgo}%</td><td>${a.score_prom}</td><td>${a.tasa_ampliada===null?'s/d':a.tasa_ampliada+'%'}</td><td>$${Number(a.pasivo).toLocaleString('es-MX')}</td><td>${flag(a)}</td></tr>`).join('');
}
// riesgo y pasivo por materia
if(D.riesgo_materia){const RM=D.riesgo_materia.filter(x=>x.n>=2);
 new Chart(cPasMat,{type:'bar',data:{labels:RM.map(x=>x.materia),datasets:[{data:RM.map(x=>x.pasivo),backgroundColor:'#c0392b'}]},
  options:{plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>'$'+c.raw.toLocaleString('es-MX')}}},scales:{y:{ticks:{callback:v=>'$'+(v/1e6).toFixed(1)+'M'}}}}});
 document.getElementById('tRieMat').innerHTML='<tr><th>Materia</th><th>Expedientes</th><th>Activos</th><th>Alto riesgo</th><th>Críticos</th><th>Densidad %</th><th>Score prom</th><th>Pasivo activo</th></tr>'+
  D.riesgo_materia.map(x=>`<tr><td><b>${x.materia}</b></td><td>${x.n}</td><td>${x.activos}</td><td>${x.altoR}</td><td>${x.critico||''}</td><td>${x.dens}%</td><td>${x.score_prom}</td><td>$${x.pasivo.toLocaleString('es-MX')}</td></tr>`).join('');
}
// provisión contable (interactiva)
let provChart=null;const PV=D.provision;
function prov(){if(!PV)return;const imp=document.getElementById('pc_imp').checked,incBajo=document.getElementById('pc_bajo').checked,med=PV.mediana;
 let rows=[],totD=0,totE=0;
 PV.niveles.forEach(x=>{const pct=(+document.getElementById('pc_'+x.nivel).value||0)/100;
  const impMonto=(imp&&(incBajo||x.nivel!=='Bajo'))?x.sin_monto*med:0;
  const rdoc=x.pasivo_doc*pct,rest=(x.pasivo_doc+impMonto)*pct;
  rows.push(Object.assign({},x,{pct:pct,rdoc:rdoc,rest:rest}));totD+=rdoc;totE+=rest;});
 kpi('kprov',[['$'+(totD/1e6).toFixed(2)+'M','Reserva documentada','good'],['$'+(totE/1e6).toFixed(2)+'M','Reserva estimada','warn'],
   [PV.activos,'Expedientes activos'],[PV.con_monto+'/'+PV.activos,'Con monto capturado','bad']]);
 document.getElementById('tProv').innerHTML='<tr><th>Nivel</th><th>Exp.</th><th>% Prov</th><th>Pasivo doc.</th><th>Sin monto</th><th>Reserva doc.</th><th>Reserva estim.</th></tr>'+
  rows.map(r=>`<tr><td><b>${r.nivel}</b></td><td>${r.n}</td><td>${Math.round(r.pct*100)}%</td><td>$${r.pasivo_doc.toLocaleString('es-MX')}</td><td>${r.sin_monto}</td><td>$${Math.round(r.rdoc).toLocaleString('es-MX')}</td><td>$${Math.round(r.rest).toLocaleString('es-MX')}</td></tr>`).join('')+
  `<tr style="font-weight:700;background:#eef2f7"><td>TOTAL</td><td>${PV.activos}</td><td>—</td><td>—</td><td>—</td><td>$${Math.round(totD).toLocaleString('es-MX')}</td><td>$${Math.round(totE).toLocaleString('es-MX')}</td></tr>`;
 if(provChart)provChart.destroy();
 provChart=new Chart(cProv,{type:'bar',data:{labels:rows.map(r=>r.nivel),datasets:[
   {label:'Reserva documentada',data:rows.map(r=>Math.round(r.rdoc)),backgroundColor:'#1f9d6b'},
   {label:'Reserva estimada',data:rows.map(r=>Math.round(r.rest)),backgroundColor:'#e08e0b'}]},
   options:{plugins:{legend:{position:'top'}},scales:{y:{ticks:{callback:v=>'$'+(v/1e6).toFixed(1)+'M'}}}}});}
function provReset(){PV.niveles.forEach(x=>document.getElementById('pc_'+x.nivel).value=x.pct_default);
 document.getElementById('pc_imp').checked=true;document.getElementById('pc_bajo').checked=false;prov();}
if(PV){document.getElementById('pc_med').textContent=PV.mediana.toLocaleString('es-MX');provReset();}
// CMI · Balanced Scorecard (4 perspectivas)
(function(){const cu=D.cuellos,pv=D.provision,dz=D.desempeno||[],rm=D.riesgo_materia||[];
 let ex=0,ad=0;dz.forEach(d=>{ex+=d.exito||0;ad+=d.adv||0;});
 const ampl=(ex+ad)?Math.round(1000*ex/(ex+ad))/10:null;
 const pas=pv?pv.niveles.reduce((s,x)=>s+x.pasivo_doc,0):0,res=pv?pv.niveles.reduce((s,x)=>s+x.pasivo_doc*x.pct_default/100,0):0;
 const dur=cu?(cu.lifespan_med/365).toFixed(1)+' años':'—',ator=cu?cu.idle_counts.a24:0;
 const cuello=cu?Object.entries(cu.transiciones).sort((a,b)=>b[1].mediana-a[1].mediana)[0]:null;
 const altoR=rm.reduce((s,x)=>s+x.altoR,0);
 const M=v=>'$'+(v/1e6).toFixed(2)+'M';
 function persp(t,c,rows){return `<div class="card"><h3 style="border-bottom:3px solid ${c};padding-bottom:6px;color:${c}">${t}</h3>`+rows.map(r=>`<div style="display:flex;justify-content:space-between;padding:7px 2px;border-bottom:1px solid var(--line);font-size:13px"><span>${r[0]}</span><b style="color:${r[2]||'#00254a'}">${r[1]}</b></div>`).join('')+'</div>';}
 document.getElementById('bscGrid').innerHTML=
  persp('⚖️ Jurídica','#0a4d8c',[['🟢 Tasa de éxito (estricta)',D.kpis.tasa_exito+'%'],['🟢 Tasa de éxito (ampliada)',ampl!=null?ampl+'%':'—'],['🟢 Asuntos de alto riesgo',altoR],['🟢 Suspensiones concedidas',(D.litigios.susp&&D.litigios.susp.concedida)||0]])+
  persp('💰 Financiera','#c0392b',[['🟢 Pasivo contingente (piso)',M(pas)],['🟢 Reserva sugerida',M(res)],['🟢 Conciliaciones (ahorro)',D.litigios.conciliacion],['🟡 Costos / honorarios','a capturar']])+
  persp('⚙️ Procesos','#1aa39a',[['🟢 Duración mediana del juicio',dur],['🟢 Cuello principal',cuello?cuello[0]+' ('+cuello[1].mediana+'d)':'—'],['🟢 Atorados > 24 meses',ator],['🟢 % expedientes activos',D.kpis.pct_activos+'%']])+
  persp('🎓 Aprendizaje','#d4a32c',[['🟢 Abogados en plantilla',D.kpis.abogados],['🟡 Capacitación / formación','a capturar'],['🟡 Horas de formación','a capturar'],['🟡 Evaluación de desempeño','a capturar']]);
})();
// tiempos y cuellos de botella
if(D.cuellos){const CU=D.cuellos;const a12=CU.idle_counts.a12,a24=CU.idle_counts.a24;
 const tr=Object.entries(CU.transiciones).sort((a,b)=>b[1].mediana-a[1].mediana);
 const peor=tr[0];
 kpi('ktiempos',[[Math.round(CU.lifespan_med/365*10)/10+' a','Duración mediana del juicio'],
  [peor?peor[1].mediana+' d':'—','Cuello principal: '+(peor?peor[0]:''),'bad'],
  [a12,'Activos atorados >12 meses','bad'],[a24,'Atorados >24 meses','warn']]);
 bar('cTrans',Object.fromEntries(tr.map(t=>[t[0],t[1].mediana])),true,'#c0392b');
 bar('cDurMat',CU.dur_materia,false,'#0a4d8c');
 const top=CU.atorados.slice(0,12);
 document.getElementById('tAtor').innerHTML='<tr><th>Expediente</th><th>Materia</th><th>Sin movimiento</th><th>Último</th></tr>'+
  top.map(x=>`<tr><td><b>${x.num}</b></td><td>${x.materia}</td><td style="color:#c0392b;font-weight:700">${Math.round(x.idle_dias/30)} meses</td><td>${x.ultimo}</td></tr>`).join('');
}
// agenda consolidada (lee localStorage del módulo/captura)
(function(){const HOY2=new Date(2026,5,18);let it=[];
 try{const ENR=JSON.parse(localStorage.getItem('sigej_enr')||'{}');Object.keys(ENR).forEach(num=>(ENR[num].agenda||[]).forEach(a=>it.push({num:num,tipo:a.tipo,fecha:a.fecha,nota:a.nota})));}catch(e){}
 try{const SES=JSON.parse(localStorage.getItem('sigej_capturas')||'[]');SES.forEach(r=>(r.agenda||[]).forEach(a=>it.push({num:r.num,tipo:a.tipo,fecha:a.fecha,nota:a.nota})));}catch(e){}
 it.sort((x,y)=>x.fecha.localeCompare(y.fecha));
 const dr=f=>Math.round((new Date(f+'T00:00:00')-HOY2)/86400000);
 const venc=it.filter(a=>dr(a.fecha)<0).length,urg=it.filter(a=>{const d=dr(a.fecha);return d>=0&&d<=7;}).length,prox=it.filter(a=>{const d=dr(a.fecha);return d>7&&d<=30;}).length;
 kpi('kagenda',[[it.length,'Eventos en agenda'],[venc,'Vencidos','bad'],[urg,'≤ 7 días','bad'],[prox,'8–30 días','warn']]);
 const cl=d=>d<0?'#c0392b':d<=7?'#e08e0b':d<=30?'#d4a32c':'#64748b';
 document.getElementById('agBody').innerHTML=it.length?('<table><tr><th>Tipo</th><th>Expediente</th><th>Fecha</th><th>Días restantes</th><th>Nota</th></tr>'+it.map(a=>{const d=dr(a.fecha);return `<tr><td><b>${a.tipo}</b></td><td>${a.num}</td><td>${a.fecha}</td><td style="color:${cl(d)};font-weight:700">${d<0?'venció hace '+(-d):'en '+d} d</td><td>${a.nota||''}</td></tr>`;}).join('')+'</table>'):'<div class="note">Aún no hay agenda capturada. Regístrala en el <b>Módulo de Expedientes</b> (📅 Agenda en cada ficha) o en <b>Captura</b>. Se lee del almacenamiento local del mismo navegador.</div>';
})();
// alertas, fichas y lecciones
if(D.mod){const M=D.mod;const A=M.alertas;
 kpi('kalert',[[A.kpi.venc,'Vencimientos próximos','warn'],[A.kpi.inact,'Riesgo de caducidad','bad'],
  [A.kpi.conting,'Contingente en riesgo','bad'],['$'+(A.kpi.pasivo_riesgo/1e6).toFixed(2)+'M','Pasivo en riesgo','gold']]);
 const tg=n=>`<span class="tag t-${n}">${n}</span>`;
 document.getElementById('aVenc').innerHTML=A.vencimientos.map(v=>`<div class="it"><span><span class="exp" onclick="vf('${v.exp}')">${v.exp}</span> · ${v.materia}</span><span>${v.prox} · <b>${v.dias}d</b> ${tg(v.nivel)}</span></div>`).join('')||'<div class="it">Sin fechas futuras capturadas</div>';
 document.getElementById('aInact').innerHTML=A.inactividad.map(v=>`<div class="it"><span><span class="exp" onclick="vf('${v.exp}')">${v.exp}</span> · ${v.materia} · ${(v.abogado||'').split(' ')[0]}</span><span><b>${v.meses_sin_mov}m</b> sin mov. ${tg(v.nivel)}</span></div>`).join('');
 document.getElementById('aCont').innerHTML=A.contingente.map(v=>`<div class="it"><span><span class="exp" onclick="vf('${v.exp}')">${v.exp}</span> · ${v.dep||v.materia}</span><span>$${v.monto.toLocaleString('es-MX')} ${tg(v.nivel)}</span></div>`).join('');
 document.getElementById('aFichas').innerHTML=M.fichas.map(f=>`<div class="it"><span><span class="exp" onclick="vf('${f.exp}')">${f.exp}</span> · score ${f.score}</span><span>${tg(f.nivel)}</span></div>`).join('');
 window._F={};M.fichas.forEach(f=>window._F[f.exp]=f);
 const vbadge=v=>v==='verificado'?'<span style="background:#e6f6ee;color:#1f7a4d;border:1px solid #9fd9b8;border-radius:8px;padding:1px 8px;font-size:11px">✓ verificado en fuente oficial</span>':'<span class="warnbox">⚠ a confirmar en SJF</span>';
 const RI={'Bajo':'🟢','Medio':'🟡','Alto':'🔴','Crítico':'⚫'};
 const LP=(D.lecpro&&D.lecpro.tipos)||[];
 document.getElementById('lecCards').innerHTML=LP.map(t=>{const ri=RI[t.riesgo]||'🟡';
  const deps=t.deps.length?t.deps.map(d=>d[0].slice(0,24)+' ('+d[1]+')').join(' · '):'—';
  const abos=t.abogados.length?t.abogados.map(a=>(a[0]||'').split(' ').slice(0,2).join(' ')+' ('+a[1]+')').join(' · '):'—';
  const cau=t.causas_kb.length?'<ul style="margin:4px 0 0;padding-left:18px">'+t.causas_kb.map(c=>'<li>'+c+'</li>').join('')+'</ul>':'—';
  const nlp=t.causas_nlp.length?t.causas_nlp.map(c=>c[0]+' ('+c[1]+')').join(' · '):'sin indicios';
  return `<div class="lcard"><h4>${t.label} · ${t.n} asuntos &nbsp; ${ri} Riesgo ${t.riesgo} &nbsp; <span class="mtag">${t.clasif}</span> ${vbadge(t.verif)}</h4>`+
   `<div class="lrow"><b>Causa raíz (Ishikawa / 5 Why's):</b> ${cau}</div>`+
   `<div class="lrow"><b>Indicios NLP en el texto (a validar):</b> <span style="color:#64748b">${nlp}</span></div>`+
   `<div class="lrow"><b>Dependencias con mayor incidencia:</b> ${deps}</div>`+
   `<div class="lrow"><b>Abogados que intervinieron:</b> ${abos}</div>`+
   `<div class="lrow"><b>Impacto económico (piso parcial):</b> $${(t.impacto||0).toLocaleString('es-MX')} &nbsp;·&nbsp; <b>Prob. repetición:</b> ${t.rep} &nbsp;·&nbsp; <b>Evitabilidad:</b> ${t.evit} &nbsp;·&nbsp; <b>Factor:</b> ${t.factor}</div>`+
   `<div class="lrow" style="background:#f0fbf6;border:1px solid #cdeede;border-radius:7px;padding:7px 10px"><b>💡 Lección aprendida:</b> ${t.leccion}</div>`+
   `<div class="lrow" style="background:#fff8e6;border:1px solid #f0e0a8;border-radius:7px;padding:7px 10px"><b>🛡️ Acción preventiva:</b> ${t.accion}</div>`+
   `<div class="lrow"><b>Fundamento:</b> ${t.fund}</div></div>`;}).join('');
}
function vf(exp){const f=window._F&&window._F[exp];if(!f)return;
 const m=f.matriz;
 document.getElementById('mbody').innerHTML=`<h2 style="margin:0 0 4px;color:#00254a">Ficha de riesgo · ${f.exp} <span class="tag t-${f.nivel}">${f.nivel} · ${f.score}</span></h2>`+
  `<p style="color:#475569;font-size:13px">${f.resumen}</p>`+
  `<h3 style="color:#00254a;font-size:14px;margin:14px 0 6px">Matriz de riesgo</h3>`+
  `<div class="mtx">Probabilidad: <b>${m.probabilidad}</b> &nbsp;×&nbsp; Impacto: <b>${m.impacto}</b></div>`+
  `<h3 style="color:#00254a;font-size:14px;margin:14px 0 6px">Tres estrategias jurídicas (orientativas)</h3>`+
  f.estrategias.map((e,i)=>`<div class="estr"><b>${i+1}. ${e.estrategia}</b> <span class="mtag">prioridad ${e.prioridad}</span><div style="font-size:12.5px;margin-top:4px;color:#334155">${e.accion}</div></div>`).join('')+
  `<h3 style="color:#00254a;font-size:14px;margin:14px 0 6px">Trazabilidad</h3>`+
  f.trazabilidad.map(t=>`<div class="mtx">${t}</div>`).join('');
 document.getElementById('modal').classList.add('on');}
function cf(){document.getElementById('modal').classList.remove('on');}
document.getElementById('modal').onclick=e=>{if(e.target.id=='modal')cf();};
function conf(b){return b>=15?'🟢':b>=7?'🟡':b>0?'🔴':'—';}
function pct(v){return v===null?'<span style="color:#94a3b8">s/d</span>':v+'%';}
document.getElementById('tDesemp').innerHTML='<tr><th>Abogado</th><th>Vigentes</th><th>Total</th>'+
 '<th>T. estricta</th><th>T. ampliada</th><th>Base</th><th>Conf.</th></tr>'+
 dz.map(x=>`<tr><td>${x.abogado}</td><td><b>${x.vigentes}</b></td><td>${x.total}</td>`+
 `<td>${pct(x.tasa_estricta)}</td><td><b>${pct(x.tasa_ampliada)}</b></td><td>${x.base_ampliada}</td><td>${conf(x.base_ampliada)}</td></tr>`).join('');
// gobierno
const g=[['Filas en archivo origen','841'],['Filas canónicas (25 col)',D.meta.base_estructurada+' (deduplicadas)'],
 ['Filas corruptas recuperadas',D.meta.recuperados+' / '+D.meta.corruptas],['Universo consolidado',D.meta.universo],
 ['Codificación','ISO-8859-1 → UTF-8'],['Duplicados eliminados','16 expedientes'],
 ['Pasivo contingente (piso parcial)','$'+D.kpis.pasivo_contingente.toLocaleString('es-MX')+' ('+D.kpis.exp_con_monto+' exp)']];
document.getElementById('govt').innerHTML='<tr><th>Métrica</th><th>Valor</th></tr>'+g.map(r=>'<tr><td>'+r[0]+'</td><td><b>'+r[1]+'</b></td></tr>').join('');
nav();
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
})();</script><script>
/* Modo embebido (dentro del Centro Ejecutivo): oculta navbar/header y badge propios */
(function(){if(!/[?&]embed=1/.test(location.search))return;
 var st=document.createElement('style');st.textContent='header,.navbar{display:none!important}body{padding-top:0!important}';document.head.appendChild(st);
 function hideBadge(){var c=document.getElementById('__chg');if(c&&c.parentNode){c.parentNode.style.display='none';}}
 hideBadge();setTimeout(hideBadge,300);
})();
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
TPL=TPL.replace("__DATA__",DATA).replace("function do()=>0;","")
open("/Users/edithroque/Documents/CLAUDE/dashboard_SIGEJ.html","w",encoding="utf-8").write(TPL)
print("dashboard_SIGEJ.html OK -", len(TPL),"bytes")
