# -*- coding: utf-8 -*-
# SUBMÓDULO (embebido en Contencioso): Recomendaciones y quejas de Derechos Humanos.
# CNDH, CEDHJ (Jalisco), CEAV/CEEAV (víctimas), organismos internacionales. Captura, revisión, búsqueda y trazabilidad a Transparencia.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_actuaciones.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Actuaciones Externas'","modulo:'Recomendaciones DH'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','derechoshumanos_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="contencioso_SIGEJ.html">⚔️ Asuntos Contenciosos</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Recomendaciones de Derechos Humanos</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;--dh:#5b3a8e;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#3a2160,#5b3a8e);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.92;font-size:12px;margin-top:3px}
.navbar{background:#2c1a49;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#dccff0;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:var(--dh);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:300px}
h2.h{margin:0 0 4px;color:var(--dh);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--dh)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:var(--dh);cursor:pointer;font-size:13px}
.collap>.bd2{padding:12px;display:none}.collap.open>.bd2{display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:9px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bw{background:var(--gold);color:#3a2c05;font-weight:700}.mini{padding:6px 10px;font-size:12px}
.bdh{background:var(--dh);color:#fff;font-weight:700}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}.bdg.dh{background:#efe6fb;color:#5b3a8e}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-600px;width:580px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.pt{border:1px solid var(--line);border-radius:8px;padding:8px;margin:5px 0;font-size:12px;display:flex;justify-content:space-between;gap:8px;align-items:center}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🕊️ Recomendaciones y quejas de Derechos Humanos</h1><div class="s">CNDH · CEDHJ (Jalisco) · CEAV/CEEAV (víctimas) · organismos internacionales · captura, revisión, seguimiento y trazabilidad a Transparencia</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 organismo:['CNDH — Comisión Nacional de los Derechos Humanos','CEDHJ — Comisión Estatal de Derechos Humanos Jalisco','CEAV — Comisión Ejecutiva de Atención a Víctimas (federal)','CEEAV Jalisco — Comisión Estatal de Atención a Víctimas','Organismo internacional (CIDH / ONU-DH)','Otro'],
 tipo:['Queja','Recomendación','Medida cautelar','Propuesta de conciliación','Solicitud de informe','Vista / colaboración','Inscripción en Registro de Víctimas'],
 derecho:['Igualdad y no discriminación','Debido proceso / legalidad','Integridad y seguridad personal','Educación','Salud','Libertad de expresión','Protección de datos personales','Trabajo','Acceso a la información','Vida libre de violencia','Derechos de las mujeres','Otro'],
 estado:['En trámite','Propuesta de conciliación','Recomendación emitida','Aceptada','Aceptada parcialmente','No aceptada','En cumplimiento','Cumplida','Concluida','Seguimiento'],
 area:['Rectoría General','Secretaría General','Coordinación de lo Contencioso','CUCS','CUCEA','CUCEI','CUCSH','CUCBA','CUAAD','SEMS','CGRH / Personal','Otra dependencia'],
 estPunto:['Pendiente','En cumplimiento','Cumplido']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'dh'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function DH(){return L('sigej_derechoshumanos');}
function bit(a){if(window.__bitlog)__bitlog('Recomendaciones DH',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Derechos Humanos',texto:t,folio:f||'',modulo:'Recomendaciones DH',leida:false});S('sigej_notificaciones',N);}
function orgCorto(o){return o.split(' — ')[0].split(' (')[0].split(' /')[0];}
function estClass(e){return /Cumplida|Aceptada$|Concluida/.test(e)?'g':/No aceptada/.test(e)?'r':/emitida|cumplimiento|conciliaci|Aceptada parcial|Seguimiento/.test(e)?'y':'n';}
function seed(){if(localStorage.getItem('sigej_derechoshumanos'))return;S('sigej_derechoshumanos',[
 {id:uid(),folio:'DH-2026-001',organismo:'CEDHJ — Comisión Estatal de Derechos Humanos Jalisco',tipo:'Queja',numero:'Q/XXXX/2026',derecho:'Debido proceso / legalidad',quejoso:'Quejoso 1 (anonimizado)',area:'Coordinación de lo Contencioso',hechos:'Inconformidad por presunta dilación en procedimiento (anonimizado).',estado:'En trámite',puntos:[],fRecep:'2026-05-01',fLimite:'2026-07-20',resp:'Área jurídica',reparacion:'',expVinc:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:uid(),folio:'DH-2026-002',organismo:'CNDH — Comisión Nacional de los Derechos Humanos',tipo:'Recomendación',numero:'REC/XX/2026',derecho:'Igualdad y no discriminación',quejoso:'Colectivo (anonimizado)',area:'Rectoría General',hechos:'Recomendación por medidas de inclusión (anonimizado).',estado:'Aceptada parcialmente',puntos:[{texto:'Emitir protocolo de no discriminación',estado:'En cumplimiento'},{texto:'Capacitación al personal',estado:'Pendiente'}],fRecep:'2026-03-10',fLimite:'2026-09-10',resp:'Abogacía General',reparacion:'',expVinc:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
 {id:uid(),folio:'DH-2026-003',organismo:'CEEAV Jalisco — Comisión Estatal de Atención a Víctimas',tipo:'Inscripción en Registro de Víctimas',numero:'RUV-JAL-XXXX',derecho:'Vida libre de violencia',quejoso:'Víctima (anonimizada · datos sensibles)',area:'CGRH / Personal',hechos:'Solicitud de medidas de reparación integral (anonimizado).',estado:'En cumplimiento',puntos:[{texto:'Medida de ayuda inmediata',estado:'Cumplido'},{texto:'Reparación integral',estado:'En cumplimiento'}],fRecep:'2026-04-05',fLimite:'',resp:'Abogacía General',reparacion:'Medidas de rehabilitación y no repetición',expVinc:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
]);}

var TABS=[['t1','📊 Panel'],['t2','🕊️ Casos (captura / revisión / búsqueda)'],['t3','📤 Reportes']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vCasos();else vRep();}

function vPanel(){var A=DH();
 var quejas=A.filter(function(x){return x.tipo==='Queja';}).length;
 var recs=A.filter(function(x){return /Recomendaci/.test(x.tipo);}).length;
 var acept=A.filter(function(x){return /^Aceptada|parcial/.test(x.estado);}).length;
 var noAcept=A.filter(function(x){return x.estado==='No aceptada';}).length;
 var cumpl=A.filter(function(x){return /cumplimiento|Cumplida/.test(x.estado);}).length;
 var vict=A.filter(function(x){return /CEAV|CEEAV|Víctimas/.test(x.organismo);}).length;
 var ptsPend=A.reduce(function(a,x){return a+(x.puntos||[]).filter(function(p){return p.estado!=='Cumplido';}).length;},0);
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+A.length+'</div><div class="l">Casos DH</div></div><div class="kpi"><div class="n">'+quejas+'</div><div class="l">Quejas</div></div><div class="kpi"><div class="n">'+recs+'</div><div class="l">Recomendaciones</div></div><div class="kpi g"><div class="n">'+acept+'</div><div class="l">Aceptadas</div></div><div class="kpi r"><div class="n">'+noAcept+'</div><div class="l">No aceptadas</div></div><div class="kpi y"><div class="n">'+cumpl+'</div><div class="l">En cumplimiento</div></div><div class="kpi"><div class="n">'+vict+'</div><div class="l">Atención a víctimas</div></div><div class="kpi r"><div class="n">'+ptsPend+'</div><div class="l">Puntos pendientes</div></div></div>';
 var venc=A.filter(function(x){var d=dr(x.fLimite);return !/Cumplida|Concluida|No aceptada/.test(x.estado)&&d!==null&&d<=15;});
 var al=venc.length?'<div class="alert">⏰ <b>Plazos por vencer:</b> '+venc.map(function(x){var d=dr(x.fLimite);return esc(x.folio)+' ('+orgCorto(x.organismo)+') '+(d<0?'<b>vencido</b>':d+'d');}).join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de Derechos Humanos</h2><p class="lead">Quejas y recomendaciones ante organismos de derechos humanos y comisiones de víctimas, con seguimiento de puntos recomendatorios y cumplimiento.</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#5b3a8e">Casos por organismo</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#5b3a8e">Casos por estado</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">🔒 Los casos de DH suelen contener <b>datos personales sensibles</b>: el quejoso/víctima se registra <b>anonimizado</b>. La versión pública de las recomendaciones (Art. 8 fr. VII de la Ley de Transparencia) se difunde con datos protegidos. La integración con los sistemas de CNDH/CEDHJ/CEAV es fase backend. Cada acción queda en la <b>bitácora de Transparencia General</b>.</div>';
 try{var o={};A.forEach(function(x){o[orgCorto(x.organismo)]=(o[orgCorto(x.organismo)]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(o),datasets:[{data:Object.values(o),backgroundColor:['#5b3a8e','#8e6fd4','#d4a32c','#1aa39a','#c0392b','#6b7280']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var e={};A.forEach(function(x){e[x.estado]=(e[x.estado]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:Object.keys(e),datasets:[{data:Object.values(e),backgroundColor:'#5b3a8e'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
function vCasos(){var A=DH();var q=(val('dq')||'').toLowerCase(),fo=val('dfo'),fe=val('dfe'),fd=val('dfd');
 var form='<div class="collap" id="df"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Capturar caso de Derechos Humanos — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Organismo *</label><select id="d_org">'+opt(D.organismo,'')+'</select></div>'+
  '<div class="f"><label>Tipo</label><select id="d_tipo">'+opt(D.tipo,'')+'</select></div>'+
  '<div class="f"><label>Número (queja/recomendación)</label><input id="d_num"></div>'+
  '<div class="f"><label>Derecho vulnerado</label><select id="d_der">'+opt(D.derecho,'')+'</select></div>'+
  '<div class="f"><label>Quejoso / víctima (anonimizado)</label><input id="d_quej"></div>'+
  '<div class="f"><label>Área / dependencia señalada</label><select id="d_area">'+opt(D.area,'')+'</select></div>'+
  '<div class="f"><label>Fecha de recepción</label><input id="d_frec" type="date"></div>'+
  '<div class="f"><label>Fecha límite</label><input id="d_flim" type="date"></div>'+
  '<div class="f"><label>Estado</label><select id="d_est">'+opt(D.estado,'En trámite')+'</select></div>'+
  '<div class="f"><label>Responsable jurídico</label><input id="d_resp"></div>'+
  '<div class="f"><label>Expediente contencioso vinculado</label><input id="d_exp"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Hechos (resumen, sin datos sensibles)</label><input id="d_hechos"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addCaso()">＋ Registrar</button> <span id="d_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="dq" value="'+esc(val('dq'))+'" placeholder="🔎 Buscar (folio, organismo, derecho, área, hechos)…" oninput="render()" style="flex:1;min-width:170px"><select id="dfo" onchange="render()" style="max-width:150px"><option value="">Todo organismo</option>'+opt(D.organismo.map(orgCorto),fo)+'</select><select id="dfe" onchange="render()" style="max-width:150px"><option value="">Todo estado</option>'+opt(D.estado,fe)+'</select><select id="dfd" onchange="render()" style="max-width:150px"><option value="">Todo derecho</option>'+opt(D.derecho,fd)+'</select></div>';
 var rows=A.map(function(x,i){return {x:x,i:i};}).filter(function(o){return (!q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0)&&(!fo||orgCorto(o.x.organismo)===fo)&&(!fe||o.x.estado===fe)&&(!fd||o.x.derecho===fd);});
 var tbl='<table><tr><th>Folio</th><th>Organismo</th><th>Tipo</th><th>Derecho</th><th>Área señalada</th><th>Estado</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var d=dr(x.fLimite);return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+(d!==null&&d<=15&&!/Cumplida|Concluida|No aceptada/.test(x.estado)?' <span class="bdg y">'+(d<0?'venc':d+'d')+'</span>':'')+'</td><td><b>'+esc(orgCorto(x.organismo))+'</b></td><td style="font-size:11px">'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.derecho)+'</td><td style="font-size:11px">'+esc(x.area||'—')+'</td><td><span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin casos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🕊️ Casos de Derechos Humanos</h2><p class="lead">Captura, revisión y búsqueda de quejas, recomendaciones y atención a víctimas.</p>'+form+ctrl+tbl;
}
function addCaso(){if(!val('d_org')){el('d_msg').style.color='#c0392b';el('d_msg').textContent='Indica el organismo.';return;}
 var A=DH();var folio='DH-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(3,'0');
 var c={id:uid(),folio:folio,organismo:val('d_org'),tipo:val('d_tipo'),numero:val('d_num'),derecho:val('d_der'),quejoso:val('d_quej'),area:val('d_area'),hechos:val('d_hechos'),estado:val('d_est'),puntos:[],fRecep:val('d_frec'),fLimite:val('d_flim'),resp:val('d_resp'),reparacion:'',expVinc:val('d_exp'),docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta ('+val('d_tipo')+')'}]};
 A.push(c);S('sigej_derechoshumanos',A);bit('Alta caso DH '+folio+' · '+orgCorto(val('d_org')));
 notif('Nuevo caso de Derechos Humanos ('+orgCorto(val('d_org'))+'): '+val('d_tipo'),folio);
 var dd=dr(val('d_flim'));if(dd!==null&&dd<=15)notif('Caso DH '+folio+' con plazo próximo',folio);
 el('d_msg').style.color='#1f9d6b';el('d_msg').textContent='✓ '+folio+' registrado.';render();}
function ficha(i){var A=DH();var x=A[i];if(!x)return;
 var pts=(x.puntos||[]).map(function(p,j){var c=p.estado==='Cumplido'?'g':p.estado==='En cumplimiento'?'y':'n';return '<div class="pt"><span>'+esc(p.texto)+'</span><span><span class="bdg '+c+'">'+esc(p.estado)+'</span> <span class="lk" style="cursor:pointer;color:#5b3a8e" onclick="ptCiclo('+i+','+j+')">↻</span></span></div>';}).join('')||'<span style="color:#64748b;font-size:12px">Sin puntos recomendatorios.</span>';
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos.</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#5b3a8e">'+esc(x.folio)+' · '+esc(x.tipo)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.organismo)+' <span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></div>'+
  '<div class="comp"><b>N.º:</b> '+esc(x.numero||'—')+' · <b>Derecho:</b> '+esc(x.derecho)+'<br><b>Quejoso/víctima:</b> '+esc(x.quejoso||'—')+' <span class="bdg dh">anonimizado</span><br><b>Área señalada:</b> '+esc(x.area||'—')+' · <b>Responsable:</b> '+esc(x.resp||'—')+'<br><b>Recepción:</b> '+esc(x.fRecep||'—')+' · <b>Límite:</b> '+esc(x.fLimite||'—')+(x.expVinc?'<br><b>Expediente vinculado:</b> '+esc(x.expVinc):'')+'<br><b>Hechos:</b> '+esc(x.hechos||'—')+(x.reparacion?'<br><b>Reparación:</b> '+esc(x.reparacion):'')+'</div>'+
  '<div class="comp"><b>📋 Puntos recomendatorios / medidas</b> <button class="bd mini" onclick="addPt('+i+')">＋ Agregar</button><div style="margin-top:6px">'+pts+'</div></div>'+
  '<div class="comp"><b>Estado del caso</b><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+D.estado.map(function(e){return '<button class="bd mini" onclick="setEstado('+i+',\''+e+'\')">'+e+'</button>';}).join('')+'</div></div>'+
  '<div class="comp"><b>🗂️ Expediente</b> <button class="bd mini" onclick="dhAdj('+i+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bw mini" onclick="dhWord('+i+')">📄 Ficha (Word)</button> <button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function addPt(i){var A=DH();var t=prompt('Punto recomendatorio / medida:','');if(!t)return;A[i].puntos=A[i].puntos||[];A[i].puntos.push({texto:t.trim(),estado:'Pendiente'});A[i].traza.push({ts:nowS(),usuario:P,accion:'Punto agregado'});S('sigej_derechoshumanos',A);bit('Punto en '+A[i].folio);ficha(i);}
function ptCiclo(i,j){var A=DH();var p=A[i].puntos[j];var o=['Pendiente','En cumplimiento','Cumplido'];p.estado=o[(o.indexOf(p.estado)+1)%3];A[i].traza.push({ts:nowS(),usuario:P,accion:'Punto → '+p.estado});S('sigej_derechoshumanos',A);ficha(i);}
function setEstado(i,e){var A=DH();var x=A[i];if(x.estado===e)return;var antes=x.estado;x.estado=e;x.traza.push({ts:nowS(),usuario:P,accion:'Estado: '+antes+' → '+e});S('sigej_derechoshumanos',A);bit(x.folio+' → '+e);if(/emitida|No aceptada|Cumplida/.test(e))notif('Caso DH '+x.folio+' → '+e,x.folio);ficha(i);}
var _AT=null;
function dhAdj(i){_AT=i;el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría (Queja / Recomendación / Informe de autoridad / Aceptación / Evidencia de cumplimiento / Otro):','Recomendación')||'Documento';var r=new FileReader();r.onload=function(){var A=DH();A[_AT].docs=A[_AT].docs||[];A[_AT].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});A[_AT].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat});S('sigej_derechoshumanos',A);ficha(_AT);};r.readAsDataURL(f);};el('fileIn').click();}
function dhWord(i){var x=DH()[i];var pts=(x.puntos||[]).map(function(p){return '<li>'+esc(p.texto)+' — '+esc(p.estado)+'</li>';}).join('');
 var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Ficha de caso de Derechos Humanos — '+esc(x.folio)+'</h3><p><b>Organismo:</b> '+esc(x.organismo)+'<br><b>Tipo:</b> '+esc(x.tipo)+' · <b>N.º:</b> '+esc(x.numero)+'<br><b>Derecho:</b> '+esc(x.derecho)+'<br><b>Área señalada:</b> '+esc(x.area)+' · <b>Responsable:</b> '+esc(x.resp)+'<br><b>Recepción:</b> '+esc(x.fRecep)+' · <b>Límite:</b> '+esc(x.fLimite)+'<br><b>Estado:</b> '+esc(x.estado)+'</p><p><b>Hechos:</b> '+esc(x.hechos)+'</p>'+(pts?'<p><b>Puntos recomendatorios / medidas:</b></p><ul>'+pts+'</ul>':'')+'<p style="font-size:8pt;color:#555">Datos de la persona quejosa/víctima protegidos (anonimizado). Documento generado por SIGEJ-UdeG.</p></body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='CasoDH_'+x.folio+'.doc';a.click();}
function vRep(){var A=DH();
 el('panel').innerHTML='<h2 class="h">📤 Reportes</h2><p class="lead">Matriz de casos de Derechos Humanos (con datos personales protegidos).</p><div style="display:flex;gap:8px;margin-bottom:12px"><button class="b1 mini" onclick="expCSV()">⬇️ Matriz CSV</button></div>'+
  '<table><tr><th>Folio</th><th>Organismo</th><th>Tipo</th><th>Derecho</th><th>Área</th><th>Límite</th><th>Estado</th><th>Puntos</th></tr>'+A.map(function(x){var pc=(x.puntos||[]).filter(function(p){return p.estado==='Cumplido';}).length;return '<tr><td>'+esc(x.folio)+'</td><td style="font-size:11px">'+esc(orgCorto(x.organismo))+'</td><td>'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.derecho)+'</td><td style="font-size:11px">'+esc(x.area||'—')+'</td><td>'+esc(x.fLimite||'—')+'</td><td>'+esc(x.estado)+'</td><td>'+pc+'/'+(x.puntos||[]).length+'</td></tr>';}).join('')+'</table>';
}
function expCSV(){var A=DH();var rows=[['Folio','Organismo','Tipo','Numero','Derecho','AreaSenalada','Recepcion','Limite','Estado','PuntosCumplidos','PuntosTotal','Responsable']].concat(A.map(function(x){var pc=(x.puntos||[]).filter(function(p){return p.estado==='Cumplido';}).length;return [x.folio,x.organismo,x.tipo,x.numero,x.derecho,x.area,x.fRecep,x.fLimite,x.estado,pc,(x.puntos||[]).length,x.resp];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='derechos_humanos_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"derechoshumanos_SIGEJ.html","w",encoding="utf-8").write(out)
print("derechoshumanos_SIGEJ.html OK -",len(out),"bytes")
