# -*- coding: utf-8 -*-
# MÓDULO: Gobierno Jurídico de la Investigación (Onda 2 · #2).
# SNII, PRODEP, cuerpos académicos, LGAC, conflictos de interés, bioética/bioseguridad, titularidad de resultados.
# Complementa (no duplica) el submódulo básico de Investigación de Conocimiento y Desarrollo; enlaza con Patrimonio Intangible (PI).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Gobierno de la Investigación'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','gobinv_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="gobinv_SIGEJ.html" class="act">🔬 Gobierno de la Investigación</a><a href="desarrollo_SIGEJ.html">📚 Conocimiento y Desarrollo</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="internacional_SIGEJ.html">🌎 Internacional</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Gobierno Jurídico de la Investigación</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:var(--azul);cursor:pointer;font-size:13px}
.collap>.bd2{padding:12px;display:none}.collap.open>.bd2{display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:9px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px}
textarea{min-height:50px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bw{background:var(--gold);color:#3a2c05;font-weight:700}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-580px;width:560px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
</style></head><body>
<header><h1>🔬 Gobierno Jurídico de la Investigación</h1><div class="s">SNII · PRODEP · cuerpos académicos · LGAC · conflictos de interés · bioética · titularidad de resultados</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 snii:['No','Candidato','Nivel I','Nivel II','Nivel III','Emérito'],
 prodep:['No','Perfil deseable vigente','En trámite'],
 grado:['En formación (CAEF)','En consolidación (CAEC)','Consolidado (CAC)'],
 fuente:['CONAHCYT / Secihti','PRODEP','Fondos internacionales','Industria / privado','Recursos propios UdeG','Gobierno estatal'],
 titular:['UdeG','Compartida','Del financiador','Del investigador','Por definir'],
 resConf:['Sin conflicto','Con medidas de mitigación','Impedimento / excusa','En revisión'],
 dictamen:['Aprobado','Aprobado con condiciones','En revisión','Rechazado','Vencido'],
 riesgoBio:['Mínimo','Moderado','Con seres humanos','Con animales','Material biológico peligroso'],
 estProy:['En diseño','Vigente','Concluido','Suspendido','Cancelado'],
 cu:['CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUCostaSur','CUSur','CUCiénega','CUAltos','CULagos','CUNorte','CUValles','CUTonalá','SEMS','Coord. Gral. de Investigación']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'g'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function INV(){return L('sigej_inv_investigadores');}
function CA(){return L('sigej_inv_cuerpos');}
function CF(){return L('sigej_inv_conflictos');}
function BIO(){return L('sigej_inv_bioetica');}
function PRY(){return L('sigej_inv_proyectos');}
function bit(a){if(window.__bitlog)__bitlog('Gobierno de la Investigación',a);}
function notif(t,f){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Gobierno de la Investigación',texto:t,folio:f||'',modulo:'Gobierno de la Investigación',leida:false});S('sigej_notificaciones',N);}
function seed(){if(localStorage.getItem('sigej_inv_investigadores'))return;
 S('sigej_inv_investigadores',[
  {id:uid(),folio:'INVR-001',nombre:'Dra. Ana Torres',cu:'CUCS',area:'Salud pública',snii:'Nivel II',sniiVig:'2027-12-31',prodep:'Perfil deseable vigente',prodepVig:'2028-06-30',ca:'Salud y sociedad',lgac:'Epidemiología',ipOblig:true,docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]},
  {id:uid(),folio:'INVR-002',nombre:'Dr. Luis Márquez',cu:'CUCEI',area:'Ingeniería',snii:'Nivel I',sniiVig:'2026-08-15',prodep:'En trámite',prodepVig:'',ca:'Materiales avanzados',lgac:'Nanotecnología',ipOblig:false,docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]}
 ]);
 S('sigej_inv_cuerpos',[{id:uid(),folio:'CA-001',nombre:'Salud y sociedad',cu:'CUCS',grado:'Consolidado (CAC)',lgac:'Epidemiología; políticas de salud',integrantes:6,resp:'Dra. Ana Torres'}]);
 S('sigej_inv_bioetica',[{id:uid(),folio:'BIO-001',titulo:'Estudio clínico fase II',investigador:'Dra. Ana Torres',riesgo:'Con seres humanos',dictamen:'Aprobado con condiciones',comite:'Comité de Ética CUCS',fdictamen:'2026-05-10',vigencia:'2026-08-10',obs:'Consentimiento informado revisado'}]);
 S('sigej_inv_conflictos',[]);
 S('sigej_inv_proyectos',[{id:uid(),folio:'PROY-001',titulo:'Vacuna candidata X',investigador:'Dra. Ana Torres',cu:'CUCS',fuente:'CONAHCYT / Secihti',monto:2500000,titular:'UdeG',piVinc:'',inicio:'2026-01-15',fin:'2027-12-31',estado:'Vigente',conflicto:false}]);
}

var TABS=[['t1','📊 Panel'],['t2','👩‍🔬 Investigadores (SNII/PRODEP)'],['t3','👥 Cuerpos académicos'],['t4','⚖️ Conflictos de interés'],['t5','🧪 Bioética'],['t6','📑 Proyectos y titularidad']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vInv();else if(VIEW==='t3')vCA();else if(VIEW==='t4')vCF();else if(VIEW==='t5')vBio();else vPry();}

function vPanel(){var I=INV(),ca=CA(),cf=CF(),bio=BIO(),pry=PRY();
 var snii=I.filter(function(x){return x.snii&&x.snii!=='No';}).length;
 var prodep=I.filter(function(x){return x.prodep==='Perfil deseable vigente';}).length;
 var venSnii=I.filter(function(x){var d=dr(x.sniiVig);return x.snii!=='No'&&d!==null&&d<=90;}).length;
 var imped=cf.filter(function(x){return /Impedimento/.test(x.resolucion);}).length;
 var revConf=cf.filter(function(x){return x.estado!=='Cerrado'&&/revisi/i.test(x.resolucion);}).length;
 var bioCond=bio.filter(function(x){return /condiciones|revisi/i.test(x.dictamen);}).length;
 var bioVen=bio.filter(function(x){var d=dr(x.vigencia);return d!==null&&d<0;}).length;
 var proyFin=pry.filter(function(x){return x.fuente;}).length;
 var sinIP=I.filter(function(x){return !x.ipOblig;}).length;
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+I.length+'</div><div class="l">Investigadores</div></div><div class="kpi g"><div class="n">'+snii+'</div><div class="l">Con SNII vigente</div></div><div class="kpi"><div class="n">'+prodep+'</div><div class="l">PRODEP vigente</div></div><div class="kpi"><div class="n">'+ca.length+'</div><div class="l">Cuerpos académicos</div></div><div class="kpi r"><div class="n">'+imped+'</div><div class="l">Impedimentos por conflicto</div></div><div class="kpi y"><div class="n">'+bioCond+'</div><div class="l">Bioética condicionada/en revisión</div></div><div class="kpi"><div class="n">'+proyFin+'</div><div class="l">Proyectos con financiamiento</div></div><div class="kpi r"><div class="n">'+sinIP+'</div><div class="l">Sin convenio de cesión de IP</div></div></div>';
 var ri=[];if(venSnii)ri.push(venSnii+' SNII por vencer (≤90d)');if(bioVen)ri.push(bioVen+' dictamen(es) de bioética vencidos');if(revConf)ri.push(revConf+' conflicto(s) en revisión');if(sinIP)ri.push(sinIP+' investigador(es) sin convenio de cesión de IP');
 var al=ri.length?'<div class="alert">🚨 <b>Atención jurídica:</b> '+ri.join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel de gobernanza de la investigación</h2><p class="lead">Estatus jurídico de investigadores, cuerpos académicos, conflictos de interés, bioética y titularidad de resultados.</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Investigadores por nivel SNII</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Cuerpos académicos por grado</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La verificación en línea ante el <b>SNII/Secihti y PRODEP</b> es integración de fase backend; aquí se administra el estatus, los conflictos de interés, la bioética y la <b>titularidad de resultados</b> (con enlace a Patrimonio Intangible para la PI generada).</div>';
 try{var s={};I.forEach(function(x){var k=x.snii||'No';s[k]=(s[k]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'bar',data:{labels:Object.keys(s),datasets:[{data:Object.values(s),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:9}}}}}});
  var g={};ca.forEach(function(x){var k=(x.grado||'').split(' ')[0]+' '+(x.grado||'').split(' ')[1];g[k]=(g[k]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'doughnut',data:{labels:Object.keys(g),datasets:[{data:Object.values(g),backgroundColor:['#e08e0b','#1aa39a','#1f9d6b']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});}catch(e){}
}
/* ---- Investigadores ---- */
function vInv(){var I=INV();var q=(val('iq')||'').toLowerCase();
 var form='<div class="collap" id="if"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar investigador — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre *</label><input id="v_nom"></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="v_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Área / disciplina</label><input id="v_area"></div>'+
  '<div class="f"><label>SNII</label><select id="v_snii">'+opt(D.snii,'No')+'</select></div>'+
  '<div class="f"><label>Vigencia SNII</label><input id="v_svig" type="date"></div>'+
  '<div class="f"><label>PRODEP</label><select id="v_prodep">'+opt(D.prodep,'No')+'</select></div>'+
  '<div class="f"><label>Cuerpo académico</label><input id="v_ca"></div>'+
  '<div class="f"><label>LGAC</label><input id="v_lgac"></div>'+
  '<div class="f"><label>Convenio de cesión de IP</label><select id="v_ip"><option>No</option><option>Sí</option></select></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addInv()">＋ Registrar</button> <span id="v_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var rows=I.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:6px 0"><input id="iq" value="'+esc(val('iq'))+'" placeholder="🔎 Buscar investigador…" oninput="render()" style="width:100%"></div><table><tr><th>Folio</th><th>Investigador</th><th>CU</th><th>SNII</th><th>PRODEP</th><th>IP</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var d=dr(x.sniiVig);return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b><br><span style="font-size:10px;color:#64748b">'+esc(x.area||'')+'</span></td><td style="font-size:11px">'+esc(x.cu)+'</td><td><span class="bdg '+(x.snii!=='No'?'g':'n')+'">'+esc(x.snii)+'</span>'+(x.snii!=='No'&&d!==null&&d<=90?' <span class="bdg y">'+(d<0?'vencido':d+'d')+'</span>':'')+'</td><td style="font-size:11px">'+esc(x.prodep)+'</td><td>'+(x.ipOblig?'<span class="bdg g">Sí</span>':'<span class="bdg r">No</span>')+'</td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin investigadores.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">👩‍🔬 Investigadores (SNII / PRODEP)</h2><p class="lead">Padrón con estatus jurídico: nivel SNII y vigencia, PRODEP, cuerpo académico, LGAC y convenio de cesión de propiedad intelectual.</p>'+form+tbl;
}
function addInv(){if(!val('v_nom')){el('v_msg').style.color='#c0392b';el('v_msg').textContent='Indica el nombre.';return;}
 var I=INV();var folio='INVR-'+String(I.length+1).padStart(3,'0');
 I.push({id:uid(),folio:folio,nombre:val('v_nom'),cu:val('v_cu'),area:val('v_area'),snii:val('v_snii'),sniiVig:val('v_svig'),prodep:val('v_prodep'),prodepVig:'',ca:val('v_ca'),lgac:val('v_lgac'),ipOblig:val('v_ip')==='Sí',docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de investigador'}]});
 S('sigej_inv_investigadores',I);bit('Alta de investigador '+folio);if(val('v_ip')!=='Sí')notif('Investigador '+val('v_nom')+' sin convenio de cesión de IP',folio);
 el('v_msg').style.color='#1f9d6b';el('v_msg').textContent='✓ '+folio+' registrado.';vInv();}
function ficha(i){var I=INV();var x=I[i];if(!x)return;
 var cf=CF().filter(function(c){return c.investigador===x.nombre;});
 var pry=PRY().filter(function(p){return p.investigador===x.nombre;});
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+esc(x.nombre)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+' · '+esc(x.cu)+' · '+esc(x.area||'')+'</div>'+
  '<div class="comp"><b>SNII:</b> '+esc(x.snii)+(x.sniiVig?' (vig. '+esc(x.sniiVig)+')':'')+'<br><b>PRODEP:</b> '+esc(x.prodep)+'<br><b>Cuerpo académico:</b> '+esc(x.ca||'—')+'<br><b>LGAC:</b> '+esc(x.lgac||'—')+'<br><b>Convenio de cesión de IP:</b> '+(x.ipOblig?'<span class="bdg g">Firmado</span>':'<span class="bdg r">Pendiente — riesgo de titularidad</span>')+'</div>'+
  '<div class="comp"><b>⚖️ Conflictos de interés ('+cf.length+')</b>'+(cf.length?cf.map(function(c){return '<div style="font-size:11.5px">• '+esc(c.tipo)+' — '+esc(c.resolucion)+'</div>';}).join(''):'<div style="color:#64748b;font-size:12px">Sin declaraciones.</div>')+'</div>'+
  '<div class="comp"><b>📑 Proyectos ('+pry.length+')</b>'+(pry.length?pry.map(function(p){return '<div style="font-size:11.5px">• '+esc(p.titulo)+' — '+esc(p.fuente)+' · titularidad '+esc(p.titular)+'</div>';}).join(''):'<div style="color:#64748b;font-size:12px">Sin proyectos.</div>')+'</div>'+
  '<div class="comp"><b>Actualizar IP:</b> <button class="bd mini" onclick="toggleIP('+i+')">'+(x.ipOblig?'Marcar pendiente':'Marcar convenio firmado')+'</button></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function toggleIP(i){var I=INV();I[i].ipOblig=!I[i].ipOblig;I[i].traza.push({ts:nowS(),usuario:P,accion:'Convenio de cesión de IP: '+(I[i].ipOblig?'firmado':'pendiente')});S('sigej_inv_investigadores',I);bit('IP de '+I[i].nombre+': '+(I[i].ipOblig?'firmado':'pendiente'));ficha(i);}
/* ---- Cuerpos académicos ---- */
function vCA(){var C=CA();
 var form='<div class="collap" id="cf2"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar cuerpo académico — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre *</label><input id="ca_nom"></div>'+
  '<div class="f"><label>CU</label><select id="ca_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Grado de consolidación</label><select id="ca_gr">'+opt(D.grado,'')+'</select></div>'+
  '<div class="f"><label>Integrantes</label><input id="ca_int" type="number" min="0"></div>'+
  '<div class="f"><label>Responsable</label><input id="ca_resp"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>LGAC</label><input id="ca_lgac"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addCA()">＋ Registrar</button> <span id="ca_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Cuerpo académico</th><th>CU</th><th>Grado</th><th>Integrantes</th><th>LGAC</th></tr>'+
  (C.length?C.map(function(x){var g=/Consolidado/.test(x.grado)?'g':/consolidación/.test(x.grado)?'y':'n';return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b></td><td>'+esc(x.cu)+'</td><td><span class="bdg '+g+'">'+esc(x.grado)+'</span></td><td>'+esc(x.integrantes||0)+'</td><td style="font-size:11px">'+esc(x.lgac||'')+'</td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin cuerpos académicos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">👥 Cuerpos académicos y LGAC</h2><p class="lead">Registro de cuerpos académicos, su grado de consolidación (CAEF/CAEC/CAC) y líneas de generación y aplicación del conocimiento.</p>'+form+tbl;
}
function addCA(){if(!val('ca_nom')){el('ca_msg').style.color='#c0392b';el('ca_msg').textContent='Indica el nombre.';return;}
 var C=CA();C.push({id:uid(),folio:'CA-'+String(C.length+1).padStart(3,'0'),nombre:val('ca_nom'),cu:val('ca_cu'),grado:val('ca_gr'),integrantes:+val('ca_int')||0,lgac:val('ca_lgac'),resp:val('ca_resp')});
 S('sigej_inv_cuerpos',C);bit('Alta de cuerpo académico '+val('ca_nom'));el('ca_msg').style.color='#1f9d6b';el('ca_msg').textContent='✓ registrado.';vCA();}
/* ---- Conflictos de interés ---- */
function vCF(){var C=CF();var iopt=INV().map(function(x){return '<option>'+esc(x.nombre)+'</option>';}).join('');
 var form='<div class="collap" id="cff"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar declaración de conflicto de interés — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Investigador</label><select id="k_inv">'+iopt+'</select></div>'+
  '<div class="f"><label>Proyecto / asunto</label><input id="k_proy"></div>'+
  '<div class="f"><label>Tipo</label><select id="k_tipo"><option>Económico</option><option>Familiar</option><option>Comercial / consultoría</option><option>Editorial / evaluación</option><option>Institucional</option><option>Otro</option></select></div>'+
  '<div class="f"><label>Resolución</label><select id="k_res">'+opt(D.resConf,'En revisión')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Descripción</label><input id="k_desc"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addCF()">＋ Registrar</button> <span id="k_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Investigador</th><th>Tipo</th><th>Proyecto/asunto</th><th>Resolución</th></tr>'+
  (C.length?C.map(function(x){var c=/Impedimento/.test(x.resolucion)?'r':/Sin conflicto/.test(x.resolucion)?'g':'y';return '<tr><td>'+esc(x.folio)+'</td><td>'+esc(x.investigador)+'</td><td>'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.proyecto||'')+'</td><td><span class="bdg '+c+'">'+esc(x.resolucion)+'</span></td></tr>';}).join(''):'<tr><td colspan="5" class="empty">Sin declaraciones de conflicto.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">⚖️ Conflictos de interés</h2><p class="lead">Declaraciones y resolución de conflictos de interés en la investigación (necesidad de excusa/impedimento, medidas de mitigación).</p>'+form+tbl;
}
function addCF(){if(!val('k_desc')){el('k_msg').style.color='#c0392b';el('k_msg').textContent='Describe el conflicto.';return;}
 var C=CF();var res=val('k_res');C.push({id:uid(),folio:'COI-'+String(C.length+1).padStart(3,'0'),investigador:val('k_inv'),proyecto:val('k_proy'),tipo:val('k_tipo'),desc:val('k_desc'),resolucion:res,fecha:hoy(),estado:/revisi/i.test(res)?'Abierto':'Cerrado'});
 S('sigej_inv_conflictos',C);bit('Conflicto de interés · '+val('k_inv'));if(/Impedimento/.test(res))notif('Impedimento por conflicto de interés: '+val('k_inv'),'');
 el('k_msg').style.color='#1f9d6b';el('k_msg').textContent='✓ registrado.';vCF();}
/* ---- Bioética ---- */
function vBio(){var Bb=BIO();
 var form='<div class="collap" id="bf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar protocolo de bioética / bioseguridad — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Título del protocolo *</label><input id="b_tit"></div>'+
  '<div class="f"><label>Investigador</label><input id="b_inv"></div>'+
  '<div class="f"><label>Nivel de riesgo</label><select id="b_riesgo">'+opt(D.riesgoBio,'')+'</select></div>'+
  '<div class="f"><label>Dictamen</label><select id="b_dic">'+opt(D.dictamen,'En revisión')+'</select></div>'+
  '<div class="f"><label>Comité de ética</label><input id="b_com"></div>'+
  '<div class="f"><label>Fecha dictamen</label><input id="b_fd" type="date"></div>'+
  '<div class="f"><label>Vigencia</label><input id="b_vig" type="date"></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Observaciones / condiciones</label><input id="b_obs"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addBio()">＋ Registrar</button> <span id="b_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Protocolo</th><th>Investigador</th><th>Riesgo</th><th>Dictamen</th><th>Vigencia</th></tr>'+
  (Bb.length?Bb.map(function(x){var d=dr(x.vigencia);var c=/Aprobado$/.test(x.dictamen)?'g':/Rechazado|Vencido/.test(x.dictamen)?'r':'y';return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.titulo)+'</b></td><td style="font-size:11px">'+esc(x.investigador)+'</td><td style="font-size:11px">'+esc(x.riesgo)+'</td><td><span class="bdg '+c+'">'+esc(x.dictamen)+'</span></td><td>'+esc(x.vigencia||'—')+(d!==null&&d<0?' <span class="bdg r">vencido</span>':'')+'</td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin protocolos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🧪 Bioética y bioseguridad</h2><p class="lead">Protocolos con dictamen del comité de ética/bioseguridad, nivel de riesgo (seres humanos, animales, material biológico) y vigencia.</p>'+form+tbl;
}
function addBio(){if(!val('b_tit')){el('b_msg').style.color='#c0392b';el('b_msg').textContent='Indica el título.';return;}
 var Bb=BIO();var dic=val('b_dic');Bb.push({id:uid(),folio:'BIO-'+String(Bb.length+1).padStart(3,'0'),titulo:val('b_tit'),investigador:val('b_inv'),riesgo:val('b_riesgo'),dictamen:dic,comite:val('b_com'),fdictamen:val('b_fd'),vigencia:val('b_vig'),obs:val('b_obs')});
 S('sigej_inv_bioetica',Bb);bit('Protocolo de bioética '+val('b_tit'));if(/condiciones|Rechazado/.test(dic))notif('Bioética: '+val('b_tit')+' → '+dic,'');
 el('b_msg').style.color='#1f9d6b';el('b_msg').textContent='✓ registrado.';vBio();}
/* ---- Proyectos y titularidad ---- */
function vPry(){var Pp=PRY();var iopt=INV().map(function(x){return '<option>'+esc(x.nombre)+'</option>';}).join('');
 var form='<div class="collap" id="pf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar proyecto de investigación — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Título *</label><input id="p_tit"></div>'+
  '<div class="f"><label>Investigador responsable</label><select id="p_inv">'+iopt+'</select></div>'+
  '<div class="f"><label>CU</label><select id="p_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Fuente de financiamiento</label><select id="p_fue">'+opt(D.fuente,'')+'</select></div>'+
  '<div class="f"><label>Monto (MXN)</label><input id="p_monto" type="number" min="0"></div>'+
  '<div class="f"><label>Titularidad de resultados</label><select id="p_tit2">'+opt(D.titular,'')+'</select></div>'+
  '<div class="f"><label>PI vinculada (folio Patrimonio)</label><input id="p_pi" placeholder="P-…"></div>'+
  '<div class="f"><label>Inicio</label><input id="p_ini" type="date"></div>'+
  '<div class="f"><label>Fin</label><input id="p_fin" type="date"></div>'+
  '<div class="f"><label>Estado</label><select id="p_est">'+opt(D.estProy,'Vigente')+'</select></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addPry()">＋ Registrar</button> <span id="p_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var tbl='<table><tr><th>Folio</th><th>Proyecto</th><th>Responsable</th><th>Fuente</th><th>Monto</th><th>Titularidad</th><th>Estado</th></tr>'+
  (Pp.length?Pp.map(function(x){var c=x.titular==='UdeG'?'g':/Por definir|financiador|investigador/.test(x.titular)?'y':'n';return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.titulo)+'</b></td><td style="font-size:11px">'+esc(x.investigador)+'</td><td style="font-size:11px">'+esc(x.fuente)+'</td><td>'+M(x.monto)+'</td><td><span class="bdg '+c+'">'+esc(x.titular)+'</span></td><td>'+esc(x.estado)+'</td></tr>';}).join(''):'<tr><td colspan="7" class="empty">Sin proyectos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📑 Proyectos y titularidad de resultados</h2><p class="lead">Proyectos con financiamiento, titularidad de la propiedad intelectual generada y vínculo con el módulo de Patrimonio Intangible.</p>'+form+tbl;
}
function addPry(){if(!val('p_tit')){el('p_msg').style.color='#c0392b';el('p_msg').textContent='Indica el título.';return;}
 var Pp=PRY();var tit=val('p_tit2');Pp.push({id:uid(),folio:'PROY-'+String(Pp.length+1).padStart(3,'0'),titulo:val('p_tit'),investigador:val('p_inv'),cu:val('p_cu'),fuente:val('p_fue'),monto:+val('p_monto')||0,titular:tit,piVinc:val('p_pi'),inicio:val('p_ini'),fin:val('p_fin'),estado:val('p_est'),conflicto:false});
 S('sigej_inv_proyectos',Pp);bit('Proyecto de investigación '+val('p_tit'));if(tit==='Por definir'||!tit)notif('Proyecto '+val('p_tit')+' con titularidad de resultados por definir','');
 el('p_msg').style.color='#1f9d6b';el('p_msg').textContent='✓ registrado.';vPry();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);function clean(){try{document.querySelectorAll('div[style*="99999"]').forEach(function(o){o.remove();});var b=document.querySelector('div[style*="bottom:12px"][style*="right:12px"]');if(b)b.style.display="none";}catch(e){}}clean();setTimeout(clean,200);setTimeout(clean,800);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"gobinv_SIGEJ.html","w",encoding="utf-8").write(out)
print("gobinv_SIGEJ.html OK -",len(out),"bytes")
