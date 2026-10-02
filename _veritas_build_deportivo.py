# -*- coding: utf-8 -*-
# SUBMÓDULO: Derecho Deportivo (parte jurídica) — dentro de Gestión Jurídica Especializada.
# Asuntos jurídicos del deporte universitario + discapacidad y grupos prioritarios + DDHH (demandas, denuncias, quejas, recomendaciones).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Derecho Deportivo'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','deportivo_SIGEJ','gestion_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="deportivo_SIGEJ.html" class="act">🏅 Derecho Deportivo</a><a href="contencioso_SIGEJ.html">⚔️ Contencioso</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Derecho Deportivo</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00382b,#0a6b52);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00241c;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2e8dc;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:#0a6b52;color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:#0a6b52;font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f2fbf7;border:1px solid #cdeade;border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:#0a6b52}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:9px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:#0a6b52;color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f2fbf7}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}
.note{background:#eefaf5;border:1px solid #bfe6d4;color:#0a6b52;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.leg{font-size:12.5px;line-height:1.6}.leg li{margin-bottom:6px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f7fbfa;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.chip{display:inline-block;background:#eefaf5;border:1px solid #bfe6d4;color:#0a6b52;border-radius:20px;font-size:10.5px;padding:2px 9px;margin:2px}
.enl{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}
.enl a{display:block;text-decoration:none;background:#f7fbfa;border:1px solid var(--line);border-radius:12px;padding:13px;color:#0a6b52}
.enl a:hover{background:#eefaf5}.enl b{display:block;font-size:13.5px}.enl span{font-size:11px;color:var(--mut)}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
</style></head><body>
<header><h1>🏅 Derecho Deportivo · parte jurídica</h1><div class="s">Asuntos jurídicos del deporte universitario · discapacidad y grupos prioritarios · demandas, denuncias, quejas y recomendaciones DDHH — submódulo de Gestión Jurídica Especializada</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 tipo:['Demanda','Denuncia','Queja','Recomendación DDHH','Consulta / asesoría','Convenio / responsabilidad'],
 ambito:['Deporte universitario','Discapacidad y grupos prioritarios','Ambos'],
 entidad:['Club Deportivo UDG','Leones Negros (marca/club)','CUCS · Cultura Física y Deportes','Coordinación de Cultura Física','Centro Universitario (disciplina deportiva)','SEMS (deporte)','Carrera Leones Negros','Otra entidad UdeG'],
 organismo:['—','CNDH (nacional)','CEDHJ (Jalisco)','CONADIS','DIF Jalisco','Órgano interno de control','Autoridad judicial','Autoridad administrativa'],
 estado:['Recibido','En análisis jurídico','En trámite','Atendido','Concluido','Improcedente']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'd'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function AV(){return L('sigej_deportivo');}
function bit(a){if(window.__bitlog)__bitlog('Derecho Deportivo',a);}
function estClass(e){return /Atendido|Concluido/.test(e)?'g':/Improcedente/.test(e)?'r':/análisis|trámite|Recibido/.test(e)?'y':'n';}
function seed(){if(localStorage.getItem('sigej_deportivo'))return;S('sigej_deportivo',[
 {id:uid(),folio:'DEP-2026-001',tipo:'Recomendación DDHH',ambito:'Discapacidad y grupos prioritarios',entidad:'Centro Universitario (disciplina deportiva)',organismo:'CEDHJ (Jalisco)',numero:'—',derecho:'Accesibilidad e inclusión',estado:'En análisis jurídico',fecha:hoy(),resp:'Área de DDHH',hechos:'(demo) Presunta falta de accesibilidad en instalación deportiva para persona con discapacidad.',traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:uid(),folio:'DEP-2026-002',tipo:'Convenio / responsabilidad',ambito:'Deporte universitario',entidad:'Club Deportivo UDG',organismo:'—',numero:'—',derecho:'',estado:'En trámite',fecha:hoy(),resp:'Instrumentos Jurídicos',hechos:'(demo) Convenio de uso de instalaciones y cobertura de seguro de deportistas.',traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
]);}

var TABS=[['t1','🏅 Panel'],['t2','⚖️ Asuntos jurídicos'],['t3','♿ Discapacidad y grupos prioritarios'],['t4','📚 Marco normativo y enlaces']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vAsuntos();else if(VIEW==='t3')vDisc();else vNorm();}

function vPanel(){var A=AV();
 var dem=A.filter(function(x){return /Demanda|Denuncia|Queja|Recomendación/.test(x.tipo);}).length;
 var disc=A.filter(function(x){return /Discapacidad/.test(x.ambito);}).length;
 var abiertos=A.filter(function(x){return !/Atendido|Concluido|Improcedente/.test(x.estado);}).length;
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+A.length+'</div><div class="l">Asuntos jurídicos</div></div><div class="kpi r"><div class="n">'+dem+'</div><div class="l">Demandas/denuncias/quejas/recom.</div></div><div class="kpi y"><div class="n">'+abiertos+'</div><div class="l">En trámite</div></div><div class="kpi"><div class="n">'+disc+'</div><div class="l">Discapacidad y grupos prioritarios</div></div></div>';
 el('panel').innerHTML='<h2 class="h">🏅 Panel de asuntos jurídico-deportivos</h2><p class="lead">Parte jurídica del deporte universitario y de discapacidad/grupos prioritarios: demandas, denuncias, quejas y recomendaciones de derechos humanos.</p>'+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a6b52">Asuntos por tipo</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a6b52">Asuntos por ámbito</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">🔗 Trazabilidad con Oficialía de Partes, Contencioso y Archivo. El deporte universitario se gestiona a través de entidades como el Club Deportivo UDG, Leones Negros y la Coordinación de Cultura Física; aquí se concentra únicamente la <b>dimensión jurídica</b>.</div>';
 try{var s={};A.forEach(function(x){s[x.tipo]=(s[x.tipo]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'bar',data:{labels:Object.keys(s),datasets:[{data:Object.values(s),backgroundColor:'#0a6b52'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});
  var g={};A.forEach(function(x){g[x.ambito]=(g[x.ambito]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'doughnut',data:{labels:Object.keys(g),datasets:[{data:Object.values(g),backgroundColor:['#0a6b52','#d4a32c','#0a4d8c']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});}catch(e){}
}
function form(){return '<div class="grid">'+
  '<div class="f"><label>Tipo de asunto *</label><select id="a_tipo">'+opt(D.tipo,'')+'</select></div>'+
  '<div class="f"><label>Ámbito</label><select id="a_amb">'+opt(D.ambito,'')+'</select></div>'+
  '<div class="f"><label>Entidad deportiva / universitaria</label><select id="a_ent">'+opt(D.entidad,'')+'</select></div>'+
  '<div class="f"><label>Organismo (para recomendaciones/quejas)</label><select id="a_org">'+opt(D.organismo,'')+'</select></div>'+
  '<div class="f"><label>No. de oficio / expediente / recomendación</label><input id="a_num"></div>'+
  '<div class="f"><label>Derecho involucrado</label><input id="a_der" placeholder="p. ej. no discriminación, accesibilidad"></div>'+
  '<div class="f"><label>Fecha</label><input id="a_fec" type="date"></div>'+
  '<div class="f"><label>Responsable</label><input id="a_resp"></div>'+
  '<div class="f"><label>Estado</label><select id="a_est">'+opt(D.estado,'')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Hechos / objeto</label><textarea id="a_hechos" rows="2"></textarea></div>'+
  '</div>';}
function vAsuntos(){var A=AV().map(function(x,i){return {x:x,i:i};});var q=norm(val('q')),ft=val('ft');
 var rows=A.filter(function(o){return (!q||norm(JSON.stringify(o.x)).indexOf(q)>=0)&&(!ft||o.x.tipo===ft);});
 var fm='<div class="card"><b style="color:#0a6b52">➕ Registrar asunto jurídico</b>'+form()+'<div style="margin-top:8px"><button class="b1" onclick="addAsunto()">＋ Registrar</button> <span id="msg" style="font-size:12px;color:#0a6b52"></span></div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="q" value="'+esc(val('q'))+'" placeholder="🔎 Buscar" oninput="render()" style="flex:1;min-width:180px"><select id="ft" onchange="render()" style="max-width:200px"><option value="">Todo tipo</option>'+opt(D.tipo,ft)+'</select></div>';
 var tbl='<table><tr><th>Folio</th><th>Tipo</th><th>Ámbito</th><th>Entidad</th><th>Organismo</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td>'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.ambito)+'</td><td style="font-size:11px">'+esc(x.entidad)+'</td><td style="font-size:11px">'+esc(x.organismo||'—')+'</td><td><span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" style="text-align:center;color:#64748b;padding:16px">Sin asuntos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">⚖️ Asuntos jurídicos deportivos y de grupos prioritarios</h2><p class="lead">Registro de demandas, denuncias, quejas, recomendaciones DDHH y convenios/responsabilidad del ámbito deportivo y de discapacidad.</p>'+fm+ctrl+tbl;
}
function addAsunto(){if(!val('a_tipo')){el('msg').textContent='Indica el tipo.';return;}
 var A=AV();var folio='DEP-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 var o={id:uid(),folio:folio,tipo:val('a_tipo'),ambito:val('a_amb'),entidad:val('a_ent'),organismo:val('a_org'),numero:val('a_num'),derecho:val('a_der'),fecha:val('a_fec')||hoy(),resp:val('a_resp'),estado:val('a_est')||'Recibido',hechos:val('a_hechos'),traza:[{ts:nowS(),usuario:P,accion:'Alta'}]};
 A.push(o);S('sigej_deportivo',A);bit('Alta asunto '+folio+' · '+val('a_tipo'));el('msg').textContent='✓ '+folio+' registrado.';render();}
function ficha(i){var A=AV();var x=A[i];if(!x)return;
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a6b52">'+esc(x.folio)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.tipo)+' · '+esc(x.ambito)+' <span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></div>'+
  '<div class="comp"><b>Entidad:</b> '+esc(x.entidad)+'<br><b>Organismo:</b> '+esc(x.organismo||'—')+' · <b>No.:</b> '+esc(x.numero||'—')+'<br><b>Derecho involucrado:</b> '+esc(x.derecho||'—')+'<br><b>Fecha:</b> '+esc(x.fecha||'—')+' · <b>Responsable:</b> '+esc(x.resp||'—')+'</div>'+
  '<div class="comp"><b>Hechos / objeto:</b><br>'+esc(x.hechos||'—')+'</div>'+
  '<div class="comp"><b>Estado</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+D.estado.map(function(e){return '<button class="bd mini" onclick="setEst('+i+',\''+e+'\')">'+e+'</button>';}).join('')+'</div></div>'+
  '<div class="comp" style="border-left:4px solid #0a6b52"><b>📝 Seguimiento (notas del equipo)</b><div style="margin-top:4px">'+((x.seguimiento||[]).length?(x.seguimiento||[]).slice().reverse().map(function(s){return '<div style="font-size:11.5px;color:#334155;border-bottom:1px solid #eef2f7;padding:4px 0"><b style="color:#0a6b52">'+esc(s.usuario)+'</b> <span style="color:#94a3b8;font-size:10px">'+esc(s.ts)+'</span><br>'+esc(s.texto)+'</div>';}).join(''):'<span style="color:#94a3b8;font-size:12px">Sin notas.</span>')+'</div><div style="margin-top:6px"><textarea id="seg_'+i+'" rows="2" placeholder="Nota de seguimiento del asunto…"></textarea><button class="b1 mini" style="margin-top:5px" onclick="addSegD('+i+')">＋ Agregar nota</button></div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function addSegD(i){var A=AV();var x=A[i];var t=val('seg_'+i);if(!t){alert('Escribe la nota.');return;}x.seguimiento=x.seguimiento||[];x.seguimiento.push({ts:nowS(),usuario:P,texto:t});S('sigej_deportivo',A);bit(x.folio+' · nota de seguimiento');ficha(i);}
function setEst(i,e){var A=AV();var x=A[i];if(x.estado===e)return;x.estado=e;x.traza.push({ts:nowS(),usuario:P,accion:'Estado → '+e});S('sigej_deportivo',A);bit(x.folio+' → '+e);ficha(i);}
function closeDrw(){el('drw').classList.remove('on');}
function vDisc(){el('panel').innerHTML='<h2 class="h">♿ Discapacidad y grupos de atención prioritaria</h2><p class="lead">Inclusión, accesibilidad y no discriminación en el ámbito universitario y deportivo. Toda queja, denuncia o recomendación se registra en «Asuntos jurídicos».</p>'+
  '<div class="card"><b style="color:#0a6b52">Marco de referencia (verificado)</b><ul class="leg">'+
   '<li><b>Convención sobre los Derechos de las Personas con Discapacidad</b> (ONU) y su Protocolo Facultativo.</li>'+
   '<li><b>Ley General para la Inclusión de las Personas con Discapacidad</b> (federal).</li>'+
   '<li><b>Ley para la Inclusión y Desarrollo Integral de las Personas con Discapacidad del Estado de Jalisco</b>.</li>'+
   '<li>Art. 1º constitucional — igualdad y <b>no discriminación</b>; Ley Federal para Prevenir y Eliminar la Discriminación.</li>'+
   '<li>Instancias: <b>CONADIS</b> (nacional), <b>DIF Jalisco</b>, <b>CNDH</b> y <b>CEDHJ</b> (derechos humanos / recomendaciones).</li>'+
  '</ul></div>'+
  '<div class="card"><b style="color:#0a6b52">✅ Verificación jurídica de accesibilidad (checklist de apoyo)</b><ul class="leg" style="margin-top:4px">'+
   '<li>Ajustes razonables y accesibilidad física en instalaciones deportivas.</li>'+
   '<li>No discriminación en el acceso a disciplinas, becas y programas deportivos.</li>'+
   '<li>Consentimiento informado y protección de datos personales sensibles (salud).</li>'+
   '<li>Cobertura de seguro y responsabilidad respecto del deportista con discapacidad.</li>'+
   '<li>Atención y canalización de quejas ante CEDHJ/CNDH y seguimiento de recomendaciones.</li>'+
  '</ul></div>'+
  '<div class="note">📌 Los grupos de atención prioritaria incluyen personas con discapacidad, entre otros. El detalle de derechos y de los mecanismos de queja se rige por las leyes citadas; su redacción textual debe consultarse en la fuente oficial.</div>';
}
function vNorm(){el('panel').innerHTML='<h2 class="h">📚 Marco normativo y enlaces institucionales</h2><p class="lead">Fundamento jurídico del deporte universitario y de discapacidad/grupos prioritarios (nombres de ley verificados; el texto de cada artículo debe consultarse en la fuente oficial).</p>'+
  '<div class="card"><b style="color:#0a6b52">🏅 Deporte</b><ul class="leg">'+
   '<li><b>Ley General de Cultura Física y Deporte</b> (federal) y su Reglamento.</li>'+
   '<li><b>Ley de Cultura Física y Deporte del Estado de Jalisco</b>.</li>'+
   '<li>Normatividad universitaria de la UdeG aplicable a la actividad deportiva y a las entidades productivas/deportivas.</li>'+
   '<li>Propiedad intelectual de marca deportiva (p. ej. «Leones Negros») — enlace con Patrimonio Intangible.</li>'+
  '</ul></div>'+
  '<div class="card"><b style="color:#0a6b52">♿ Discapacidad, grupos prioritarios y DDHH</b><ul class="leg">'+
   '<li>Convención ONU sobre los Derechos de las Personas con Discapacidad.</li>'+
   '<li>Ley General para la Inclusión de las Personas con Discapacidad (federal).</li>'+
   '<li>Ley para la Inclusión y Desarrollo Integral de las Personas con Discapacidad del Estado de Jalisco.</li>'+
   '<li>CNDH y CEDHJ — quejas y recomendaciones de derechos humanos.</li>'+
  '</ul></div>'+
  '<div class="card"><b style="color:#0a6b52">🔗 Enlaces institucionales (deporte UdeG)</b><div class="enl" style="margin-top:6px">'+
   '<a href="https://pdu.udg.mx/" target="_blank" rel="noopener"><b>PDU · UdeG</b><span>pdu.udg.mx</span></a>'+
   '<a href="http://pregrado.udg.mx/Centros/Tem%C3%A1ticos/CUCS/cultura-fisica-y-deportes" target="_blank" rel="noopener"><b>CUCS · Cultura Física y Deportes</b><span>pregrado.udg.mx</span></a>'+
   '<a href="https://clubdeportivoudg.com/" target="_blank" rel="noopener"><b>Club Deportivo UDG</b><span>clubdeportivoudg.com</span></a>'+
   '<a href="https://leonesnegrosudg.mx/" target="_blank" rel="noopener"><b>Leones Negros UdeG</b><span>leonesnegrosudg.mx</span></a>'+
   '<a href="https://carreraleonesnegros.udg.mx/" target="_blank" rel="noopener"><b>Carrera Leones Negros</b><span>carreraleonesnegros.udg.mx</span></a>'+
  '</div></div>'+
  '<div class="card"><b style="color:#0a6b52">♿ Referencias de discapacidad</b><div class="enl" style="margin-top:6px">'+
   '<a href="https://www.gob.mx/issste/articulos/hablemos-de-discapacidad" target="_blank" rel="noopener"><b>ISSSTE · Hablemos de discapacidad</b><span>gob.mx/issste</span></a>'+
   '<a href="https://info.jalisco.gob.mx/grupos-de-atencion/personas-con-discapacidad" target="_blank" rel="noopener"><b>Jalisco · Personas con discapacidad</b><span>info.jalisco.gob.mx</span></a>'+
  '</div></div>'+
  '<div class="note">⚖️ <b>Regla:</b> cuando se cite un artículo específico, su redacción debe tomarse del texto oficial vigente; este módulo referencia los ordenamientos, no reproduce su articulado.</div>';
}
buildTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"deportivo_SIGEJ.html","w",encoding="utf-8").write(out)
print("deportivo_SIGEJ.html OK -",len(out),"bytes")
