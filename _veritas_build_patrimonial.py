# -*- coding: utf-8 -*-
# MÓDULO: Gestión Jurídica del Patrimonio Inmobiliario, Bienes y Recintos Culturales (Onda 2).
# Control registral de inmuebles (escrituras/RPP), inmuebles sin escritura, bienes muebles registrados, recintos culturales,
# y contratos inmobiliarios (arrendamientos, comodatos, permutas). NO duplica Patrimonio Intangible (IP) ni el inventario admin de bienes.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Patrimonio Inmobiliario'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','patrimonial_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="patrimonial_SIGEJ.html" class="act">🏢 Patrimonio Inmobiliario</a><a href="patrimonio_SIGEJ.html">🧩 Patrimonio Intangible</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Patrimonio Inmobiliario, Bienes y Recintos</title>
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
.rec{background:#fff;border:1px solid var(--line);border-left:5px solid var(--gold);border-radius:12px;padding:13px;margin-bottom:10px;cursor:pointer}
.rec:hover{box-shadow:0 4px 14px rgba(2,40,90,.12)}
.note{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.alert{background:#fdeaea;border:1px solid #e7a0a0;color:#a02020;border-radius:9px;padding:9px 12px;font-size:12.5px;margin-bottom:10px}
.drw{position:fixed;top:0;right:-600px;width:580px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:20px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>🏢 Patrimonio Inmobiliario, Bienes y Recintos Culturales</h1><div class="s">Control registral de inmuebles (escrituras · RPP) · bienes muebles registrados · recintos culturales · arrendamientos, comodatos y permutas</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D={
 tipoInm:['Edificio','Terreno','Recinto cultural','Local comercial','Bodega','Casa','Estacionamiento','Área común','Predio rústico','Otro'],
 uso:['Académico','Administrativo','Cultural','Investigación','Salud','Deportivo','Comercial','Reserva','Mixto'],
 regimen:['Propiedad UdeG','Donación recibida','Comodato recibido','Arrendado (UdeG inquilino)','Fideicomiso','Posesión sin título'],
 estReg:['Escriturado e inscrito en RPP','Escriturado sin inscribir','Sin escritura','En regularización','En litigio','Por verificar'],
 cu:['CUCEA','CUCEI','CUCS','CUCSH','CUCBA','CUAAD','CUCosta','CUCostaSur','CUSur','CUCiénega','CUAltos','CULagos','CUNorte','CUValles','CUTonalá','CUTlaquepaque','CUTlajomulco','CUChapala','CUGuadalajara','SEMS','CGEDC / Cultura UdeG','Administración General / Red'],
 tipoCont:['Arrendamiento (UdeG arrendador)','Arrendamiento (UdeG arrendatario)','Comodato otorgado','Comodato recibido','Permuta','Usufructo','Donación'],
 estCont:['Vigente','Por vencer','Vencido','En trámite','Terminado','Rescindido']
};
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function uid(){return 'p'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(hoy()+'T00:00:00'))/864e5);}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}
const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function INM(){return L('sigej_inmuebles');}
function MUE(){return L('sigej_muebles_reg');}
function CON(){return L('sigej_contratos_inm');}
function bit(a){if(window.__bitlog)__bitlog('Patrimonio inmobiliario',a);}
function regClass(e){if(/inscrito en RPP/.test(e))return 'g';if(/Sin escritura|litigio/i.test(e))return 'r';if(/regulariz|sin inscribir/i.test(e))return 'y';return 'n';}
function seed(){if(localStorage.getItem('sigej_inmuebles'))return;
 var rec=[['MUSA · Museo de las Artes','CUAAD','Av. Juárez 975, Guadalajara'],['Teatro Diana','CGEDC / Cultura UdeG','Av. 16 de Septiembre 710, Guadalajara'],['Auditorio Telmex','CGEDC / Cultura UdeG','Av. Obispo Pedro Loza / Zona Belenes, Zapopan'],['Conjunto de Artes Escénicas (Santander)','CGEDC / Cultura UdeG','Periférico Nte., Zapopan'],['Cineteca FICG','CGEDC / Cultura UdeG','Guadalajara'],['Pabellón Cultural de la República','CGEDC / Cultura UdeG','Zapopan'],['Librería Carlos Fuentes','CGEDC / Cultura UdeG','Av. Chapultepec, Guadalajara']];
 var arr=rec.map(function(r,i){return {id:uid(),folio:'INM-REC-'+String(i+1).padStart(3,'0'),nombre:r[0],tipo:'Recinto cultural',uso:'Cultural',cu:r[1],direccion:r[2],municipio:'',superficie:0,valor:0,regimen:'Propiedad UdeG',reg:{escritura:'Por verificar',escNum:'',notario:'',escFecha:'',rpp:'Por verificar',folioReal:'',distrito:'',rppFecha:'',estatus:'Por verificar'},gravamen:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (recinto cultural · plantilla, capturar situación registral real)'}]};});
 // dos inmuebles demo con estatus registral variado
 arr.push({id:uid(),folio:'INM-2026-001',nombre:'Edificio administrativo (demo)',tipo:'Edificio',uso:'Administrativo',cu:'Administración General / Red',direccion:'(demo)',municipio:'Guadalajara',superficie:1200,valor:45000000,regimen:'Propiedad UdeG',reg:{escritura:'Sí',escNum:'12,345',notario:'Notaría 5 GDL',escFecha:'2008-05-10',rpp:'Inscrito',folioReal:'FR-000123',distrito:'Distrito 1',rppFecha:'2008-06-01',estatus:'Escriturado e inscrito en RPP'},gravamen:'Libre de gravamen',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]});
 arr.push({id:uid(),folio:'INM-2026-002',nombre:'Predio en regularización (demo)',tipo:'Terreno',uso:'Reserva',cu:'CUCosta',direccion:'(demo)',municipio:'Puerto Vallarta',superficie:5000,valor:8000000,regimen:'Donación recibida',reg:{escritura:'En trámite',escNum:'',notario:'',escFecha:'',rpp:'No inscrito',folioReal:'',distrito:'',rppFecha:'',estatus:'En regularización'},gravamen:'',docs:[],traza:[{ts:nowS(),usuario:'Sistema',accion:'Alta (demo)'}]});
 S('sigej_inmuebles',arr);
}

var TABS=[['t1','📊 Panel'],['t2','🏢 Inmuebles y registro'],['t3','🎭 Recintos culturales'],['t4','📄 Arrendamientos · Comodatos · Permutas'],['t5','📦 Bienes muebles registrados'],['t6','📤 Reportes']];
var VIEW='t1';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){seed();if(VIEW==='t1')vPanel();else if(VIEW==='t2')vInm();else if(VIEW==='t3')vRec();else if(VIEW==='t4')vCont();else if(VIEW==='t5')vMue();else vRep();}

/* ---- Panel ---- */
function vPanel(){var I=INM();var C=CON();
 var insc=I.filter(function(x){return /inscrito en RPP/.test(x.reg.estatus);}).length;
 var sinEsc=I.filter(function(x){return /Sin escritura|Posesión sin título/i.test(x.reg.estatus)||x.regimen==='Posesión sin título';}).length;
 var regu=I.filter(function(x){return /regulariz|sin inscribir/i.test(x.reg.estatus);}).length;
 var verif=I.filter(function(x){return /Por verificar/.test(x.reg.estatus);}).length;
 var rec=I.filter(function(x){return x.tipo==='Recinto cultural';}).length;
 var vig=C.filter(function(x){return x.estado==='Vigente';}).length;
 var venc=C.filter(function(x){var d=dr(x.fin);return /Vigente|Por vencer/.test(x.estado)&&d!==null&&d<=30;}).length;
 var sup=I.reduce(function(a,x){return a+(+x.superficie||0);},0);
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+I.length+'</div><div class="l">Inmuebles</div></div><div class="kpi g"><div class="n">'+insc+'</div><div class="l">Escriturados e inscritos (RPP)</div></div><div class="kpi r"><div class="n">'+sinEsc+'</div><div class="l">Sin escritura / posesión</div></div><div class="kpi y"><div class="n">'+regu+'</div><div class="l">En regularización</div></div><div class="kpi n"><div class="n">'+verif+'</div><div class="l">Sin dato registral (por verificar)</div></div><div class="kpi"><div class="n">'+rec+'</div><div class="l">Recintos culturales</div></div><div class="kpi"><div class="n">'+vig+'</div><div class="l">Contratos vigentes</div></div><div class="kpi y"><div class="n">'+venc+'</div><div class="l">Contratos por vencer (≤30d)</div></div></div>';
 var riesgo=[];if(sinEsc)riesgo.push(sinEsc+' inmueble(s) sin escritura/título');if(regu)riesgo.push(regu+' en regularización');if(venc)riesgo.push(venc+' contrato(s) por vencer');
 var al=riesgo.length?'<div class="alert">🚨 <b>Riesgo patrimonial:</b> '+riesgo.join(' · ')+'.</div>':'';
 el('panel').innerHTML='<h2 class="h">📊 Panel patrimonial</h2><p class="lead">Situación registral del patrimonio inmobiliario y estado de contratos. Superficie registrada: '+sup.toLocaleString('es-MX')+' m².</p>'+al+kp+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><b style="color:#0a4d8c">Inmuebles por situación registral</b><canvas id="c1" height="150"></canvas></div><div class="card"><b style="color:#0a4d8c">Contratos por tipo</b><canvas id="c2" height="150"></canvas></div></div>'+
  '<div class="note">ℹ️ La <b>consulta directa ante el Registro Público de la Propiedad y Catastro</b> (folios reales, certificados de libertad de gravamen) es integración de <b>fase backend</b>; aquí se registra, controla y alerta sobre la situación registral capturada. El <b>resguardo administrativo</b> de bienes muebles vive en <b>Administración → Inventario y bienes</b> (aquí se lleva su control registral/jurídico).</div>';
 try{var e={};I.forEach(function(x){var k=x.reg.estatus||'Por verificar';e[k]=(e[k]||0)+1;});if(window.__c1)__c1.destroy();window.__c1=new Chart(el('c1'),{type:'doughnut',data:{labels:Object.keys(e),datasets:[{data:Object.values(e),backgroundColor:['#1f9d6b','#e08e0b','#c0392b','#d4a32c','#6b7280','#94a3b8']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  var t={};C.forEach(function(x){var k=x.tipo.replace(/ \(.*/,'');t[k]=(t[k]||0)+1;});if(window.__c2)__c2.destroy();window.__c2=new Chart(el('c2'),{type:'bar',data:{labels:Object.keys(t),datasets:[{data:Object.values(t),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});}catch(e){}
}
/* ---- Inmuebles ---- */
function vInm(){var I=INM();var q=(val('iq')||'').toLowerCase(),fe=val('ife');
 var form='<div class="collap" id="if"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar inmueble — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Nombre / identificación *</label><input id="i_nom"></div>'+
  '<div class="f"><label>Tipo</label><select id="i_tipo">'+opt(D.tipoInm,'')+'</select></div>'+
  '<div class="f"><label>Uso</label><select id="i_uso">'+opt(D.uso,'')+'</select></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="i_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Dirección</label><input id="i_dir"></div>'+
  '<div class="f"><label>Municipio</label><input id="i_mun"></div>'+
  '<div class="f"><label>Superficie (m²)</label><input id="i_sup" type="number" min="0"></div>'+
  '<div class="f"><label>Valor (MXN)</label><input id="i_val" type="number" min="0"></div>'+
  '<div class="f"><label>Régimen</label><select id="i_reg">'+opt(D.regimen,'')+'</select></div>'+
  '<div class="f"><label>Situación registral</label><select id="i_est">'+opt(D.estReg,'Por verificar')+'</select></div>'+
  '<div class="f"><label>Escritura (núm.)</label><input id="i_escn"></div>'+
  '<div class="f"><label>Notario</label><input id="i_not"></div>'+
  '<div class="f"><label>Folio real (RPP)</label><input id="i_fr"></div>'+
  '<div class="f"><label>Fecha inscripción RPP</label><input id="i_frf" type="date"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addInm()">＋ Registrar inmueble</button> <span id="i_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var ctrl='<div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px"><input id="iq" value="'+esc(val('iq'))+'" placeholder="🔎 Buscar inmueble…" oninput="render()" style="flex:1;min-width:160px"><select id="ife" onchange="render()" style="max-width:230px"><option value="">Toda situación registral</option>'+opt(D.estReg,fe)+'</select></div>';
 var rows=I.map(function(x,i){return {x:x,i:i};}).filter(function(o){return (!q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0)&&(!fe||o.x.reg.estatus===fe);});
 var tbl='<table><tr><th>Folio</th><th>Inmueble</th><th>Tipo</th><th>CU</th><th>Régimen</th><th>Situación registral</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.nombre)+'</b></td><td>'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.cu)+'</td><td style="font-size:11px">'+esc(x.regimen)+'</td><td><span class="bdg '+regClass(x.reg.estatus)+'">'+esc(x.reg.estatus)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin inmuebles.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">🏢 Inmuebles y situación registral</h2><p class="lead">Registro de bienes inmuebles con su estatus ante el RPP: escriturados e inscritos, escriturados sin inscribir, sin escritura o en regularización.</p>'+form+ctrl+tbl;
}
function addInm(){if(!val('i_nom')){el('i_msg').style.color='#c0392b';el('i_msg').textContent='Indica el nombre.';return;}
 var I=INM();var folio='INM-'+(new Date().getFullYear())+'-'+String(I.length+1).padStart(3,'0');
 I.push({id:uid(),folio:folio,nombre:val('i_nom'),tipo:val('i_tipo'),uso:val('i_uso'),cu:val('i_cu'),direccion:val('i_dir'),municipio:val('i_mun'),superficie:+val('i_sup')||0,valor:+val('i_val')||0,regimen:val('i_reg'),reg:{escritura:val('i_escn')?'Sí':'Por verificar',escNum:val('i_escn'),notario:val('i_not'),escFecha:'',rpp:val('i_fr')?'Inscrito':'Por verificar',folioReal:val('i_fr'),distrito:'',rppFecha:val('i_frf'),estatus:val('i_est')},gravamen:'',docs:[],traza:[{ts:nowS(),usuario:P,accion:'Alta de inmueble'}]});
 S('sigej_inmuebles',I);bit('Alta de inmueble '+folio);el('i_msg').style.color='#1f9d6b';el('i_msg').textContent='✓ '+folio+' registrado.';vInm();}
function ficha(i){var I=INM();var x=I[i];if(!x)return;var r=x.reg;
 var cont=CON().filter(function(c){return c.inm===x.id;});
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin documentos (escritura, avalúo, plano, certificado de gravamen).</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+esc(x.nombre)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.folio)+' · '+esc(x.tipo)+' · '+esc(x.cu)+' · <span class="bdg '+regClass(r.estatus)+'">'+esc(r.estatus)+'</span></div>'+
  '<div class="comp"><b>📍 Datos:</b> '+esc(x.direccion||'—')+(x.municipio?', '+esc(x.municipio):'')+'<br><b>Uso:</b> '+esc(x.uso)+' · <b>Superficie:</b> '+(x.superficie||0).toLocaleString('es-MX')+' m² · <b>Valor:</b> '+M(x.valor)+'<br><b>Régimen:</b> '+esc(x.regimen)+'</div>'+
  '<div class="comp"><b>📜 Situación registral</b><br><b>Escritura:</b> '+esc(r.escritura)+(r.escNum?' núm. '+esc(r.escNum):'')+(r.notario?' · '+esc(r.notario):'')+(r.escFecha?' · '+esc(r.escFecha):'')+'<br><b>Registro Público:</b> '+esc(r.rpp)+(r.folioReal?' · folio real '+esc(r.folioReal):'')+(r.rppFecha?' · '+esc(r.rppFecha):'')+'<br><b>Estatus:</b> <span class="bdg '+regClass(r.estatus)+'">'+esc(r.estatus)+'</span> '+
   '<div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+D.estReg.map(function(e){return '<button class="bd mini" onclick="setEstReg('+i+',\''+e+'\')">'+e.split(' ')[0]+(/inscrito/.test(e)?' inscrito':/sin inscribir/.test(e)?' s/inscribir':/Sin escritura/.test(e)?' s/escritura':'')+'</button>';}).join('')+'</div></div>'+
  '<div class="comp"><b>📄 Contratos vinculados ('+cont.length+')</b> <button class="bd mini" onclick="goV(\'t4\')">+ nuevo en pestaña</button><div style="margin-top:5px">'+(cont.length?cont.map(function(c){var d=dr(c.fin);return '<div style="font-size:11.5px">• '+esc(c.tipo)+' · '+esc(c.contraparte)+' · '+esc(c.estado)+(d!==null&&d<=30&&/Vigente|Por vencer/.test(c.estado)?' <span class="bdg y">vence '+d+'d</span>':'')+'</div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin contratos.</span>')+'</div></div>'+
  '<div class="comp"><b>🗂️ Expediente (escritura, avalúo, plano, certificado de gravamen)</b> <button class="bd mini" onclick="inmAdj('+i+')">Adjuntar</button><div style="margin-top:5px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bw mini" onclick="inmWord('+i+')">📄 Ficha registral (Word)</button> <button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEstReg(i,est){var I=INM();I[i].reg.estatus=est;I[i].traza.push({ts:nowS(),usuario:P,accion:'Situación registral → '+est});S('sigej_inmuebles',I);bit('Inmueble '+I[i].folio+' → '+est);
 if(/Sin escritura|litigio/i.test(est)){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:'Patrimonio inmobiliario',texto:'Riesgo registral: '+I[i].nombre+' → '+est,folio:I[i].folio,modulo:'Patrimonio Inmobiliario',leida:false});S('sigej_notificaciones',N);}
 ficha(i);}
var _AT=null;
function inmAdj(i){_AT=i;el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var cat=prompt('Categoría del documento (Escritura / Avalúo / Plano / Certificado de gravamen / Otro):','Escritura')||'Documento';var r=new FileReader();r.onload=function(){var I=INM();I[_AT].docs=I[_AT].docs||[];I[_AT].docs.push({nombre:f.name,tipo:f.type,cat:cat,data:r.result,fecha:hoy()});I[_AT].traza.push({ts:nowS(),usuario:P,accion:'Adjuntó '+cat+': '+f.name});S('sigej_inmuebles',I);ficha(_AT);};r.readAsDataURL(f);};el('fileIn').click();}
function inmWord(i){var x=INM()[i];var r=x.reg;var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><h2>Universidad de Guadalajara · Oficina de la Abogacía General</h2><h3>Ficha registral de inmueble — '+esc(x.folio)+'</h3><p><b>Inmueble:</b> '+esc(x.nombre)+'<br><b>Tipo/Uso:</b> '+esc(x.tipo)+' / '+esc(x.uso)+'<br><b>Ubicación:</b> '+esc(x.direccion)+' '+esc(x.municipio)+'<br><b>CU/Dependencia:</b> '+esc(x.cu)+'<br><b>Superficie:</b> '+(x.superficie||0)+' m² · <b>Valor:</b> '+M(x.valor)+'<br><b>Régimen:</b> '+esc(x.regimen)+'</p><h4>Situación registral</h4><p><b>Escritura:</b> '+esc(r.escritura)+' '+esc(r.escNum)+' '+esc(r.notario)+'<br><b>RPP:</b> '+esc(r.rpp)+' folio real '+esc(r.folioReal)+'<br><b>Estatus:</b> '+esc(r.estatus)+'</p></body></html>';var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='FichaRegistral_'+x.folio+'.doc';a.click();}
/* ---- Recintos culturales ---- */
function vRec(){var R=INM().map(function(x,i){return {x:x,i:i};}).filter(function(o){return o.x.tipo==='Recinto cultural';});
 var cards=R.map(function(o){var x=o.x;var cont=CON().filter(function(c){return c.inm===x.id;});return '<div class="rec" onclick="ficha('+o.i+')"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><b style="font-size:14px;color:#0a4d8c">🎭 '+esc(x.nombre)+'</b><span class="bdg '+regClass(x.reg.estatus)+'">'+esc(x.reg.estatus)+'</span></div><div style="font-size:12px;color:#475569;margin-top:4px">'+esc(x.cu)+' · '+esc(x.direccion||'')+'</div><div style="font-size:11.5px;color:#64748b;margin-top:4px">📄 '+cont.length+' contrato(s) · '+(x.docs||[]).length+' documento(s)</div></div>';}).join('');
 el('panel').innerHTML='<h2 class="h">🎭 Recintos culturales</h2><p class="lead">MUSA, Teatro Diana, Auditorio Telmex, Conjunto Santander, Cineteca, Pabellón Cultural, Librería Carlos Fuentes. Clic para ver/capturar su situación registral y contratos.</p>'+cards+
  '<div class="note">Los recintos están precargados como <b>plantilla</b>; su situación registral aparece como «Por verificar» — captura la escritura, folio real y contratos reales en cada ficha. No se inventaron números de escritura.</div>';
}
/* ---- Contratos inmobiliarios ---- */
function vCont(){var C=CON();var I=INM();
 var iopt=I.map(function(x){return '<option value="'+x.id+'">'+esc(x.nombre)+'</option>';}).join('');
 var form='<div class="collap" id="cf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar contrato (arrendamiento / comodato / permuta) — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Tipo</label><select id="c_tipo">'+opt(D.tipoCont,'')+'</select></div>'+
  '<div class="f"><label>Inmueble</label><select id="c_inm">'+iopt+'</select></div>'+
  '<div class="f"><label>Contraparte</label><input id="c_cp"></div>'+
  '<div class="f"><label>Inicio</label><input id="c_ini" type="date"></div>'+
  '<div class="f"><label>Vigencia (fin)</label><input id="c_fin" type="date"></div>'+
  '<div class="f"><label>Renta / valor (MXN)</label><input id="c_renta" type="number" min="0"></div>'+
  '<div class="f"><label>Garantía</label><input id="c_gar"></div>'+
  '<div class="f"><label>Estado</label><select id="c_est">'+opt(D.estCont,'Vigente')+'</select></div>'+
  '<div class="f" style="grid-column:1/-1"><label>Objeto / observaciones</label><input id="c_obs"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addCont()">＋ Registrar contrato</button> <span id="c_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var prox=C.filter(function(c){var d=dr(c.fin);return /Vigente|Por vencer/.test(c.estado)&&d!==null&&d<=30;});
 var al=prox.length?'<div class="alert">⏰ <b>Contratos por vencer / vencidos:</b> '+prox.map(function(c){var d=dr(c.fin);return esc(c.tipo.replace(/ \(.*/,''))+' · '+esc(c.contraparte)+' '+(d<0?'<b>vencido '+(-d)+'d</b>':'en '+d+'d');}).join(' · ')+'</div>':'';
 var tbl='<table><tr><th>Folio</th><th>Tipo</th><th>Inmueble</th><th>Contraparte</th><th>Vigencia</th><th>Renta/Valor</th><th>Estado</th></tr>'+
  (C.length?C.map(function(c){var inm=I.filter(function(x){return x.id===c.inm;})[0];var d=dr(c.fin);var cls=c.estado==='Vigente'?'g':/Vencido|Rescindido/.test(c.estado)?'r':c.estado==='Por vencer'?'y':'n';return '<tr><td>'+esc(c.folio)+'</td><td style="font-size:11.5px">'+esc(c.tipo)+'</td><td style="font-size:11px">'+esc(inm?inm.nombre:'—')+'</td><td style="font-size:11px">'+esc(c.contraparte)+'</td><td>'+esc(c.fin||'—')+(d!==null&&d<=30&&/Vigente|Por vencer/.test(c.estado)?' <span class="bdg y">'+(d<0?'vencido':d+'d')+'</span>':'')+'</td><td>'+(c.renta?M(c.renta):'—')+'</td><td><span class="bdg '+cls+'">'+esc(c.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="7" class="empty">Sin contratos.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📄 Arrendamientos, comodatos y permutas</h2><p class="lead">Contratos sobre inmuebles del patrimonio: arrendamientos (activo/pasivo), comodatos otorgados/recibidos, permutas, usufructo y donaciones. Vinculados al inmueble y al RPP. Complementa el CLM general de <b>Instrumentos Jurídicos</b>.</p>'+al+form+tbl;
}
function addCont(){if(!val('c_cp')){el('c_msg').style.color='#c0392b';el('c_msg').textContent='Indica la contraparte.';return;}
 var C=CON();var folio='CTI-'+(new Date().getFullYear())+'-'+String(C.length+1).padStart(3,'0');
 C.push({id:uid(),folio:folio,tipo:val('c_tipo'),inm:val('c_inm'),contraparte:val('c_cp'),ini:val('c_ini'),fin:val('c_fin'),renta:+val('c_renta')||0,garantia:val('c_gar'),estado:val('c_est'),obs:val('c_obs'),docs:[]});
 S('sigej_contratos_inm',C);bit('Contrato inmobiliario '+folio+' ('+val('c_tipo')+')');el('c_msg').style.color='#1f9d6b';el('c_msg').textContent='✓ '+folio+' registrado.';vCont();}
/* ---- Bienes muebles registrados ---- */
function vMue(){var Mm=MUE();var q=(val('mq')||'').toLowerCase();
 var form='<div class="collap" id="mf"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">➕ Registrar bien mueble (registral/jurídico) — clic para abrir/cerrar</div><div class="bd2"><div class="grid">'+
  '<div class="f"><label>Descripción *</label><input id="m_desc"></div>'+
  '<div class="f"><label>Tipo</label><select id="m_tipo"><option>Vehículo</option><option>Obra de arte / acervo cultural</option><option>Equipo de alto valor</option><option>Semoviente</option><option>Maquinaria</option><option>Otro</option></select></div>'+
  '<div class="f"><label>N.º de registro / serie</label><input id="m_reg"></div>'+
  '<div class="f"><label>CU / dependencia</label><select id="m_cu">'+opt(D.cu,'')+'</select></div>'+
  '<div class="f"><label>Valor (MXN)</label><input id="m_val" type="number" min="0"></div>'+
  '<div class="f"><label>Régimen</label><select id="m_reg2"><option>Propiedad UdeG</option><option>Donación recibida</option><option>Comodato recibido</option><option>Arrendado</option></select></div>'+
  '<div class="f"><label>Documento acreditante</label><input id="m_doc" placeholder="Factura / registro / título"></div>'+
  '</div><div style="margin-top:8px"><button class="b3" onclick="addMue()">＋ Registrar bien mueble</button> <span id="m_msg" style="font-size:12px;color:#1f9d6b"></span></div></div></div>';
 var rows=Mm.map(function(x,i){return {x:x,i:i};}).filter(function(o){return !q||JSON.stringify(o.x).toLowerCase().indexOf(q)>=0;});
 var tbl='<div style="margin:6px 0"><input id="mq" value="'+esc(val('mq'))+'" placeholder="🔎 Buscar…" oninput="render()" style="width:100%"></div><table><tr><th>Folio</th><th>Descripción</th><th>Tipo</th><th>Registro/Serie</th><th>CU</th><th>Valor</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;return '<tr><td>'+esc(x.folio)+'</td><td><b>'+esc(x.desc)+'</b></td><td>'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.reg||'—')+'</td><td style="font-size:11px">'+esc(x.cu)+'</td><td>'+M(x.valor)+'</td></tr>';}).join(''):'<tr><td colspan="6" class="empty">Sin bienes muebles registrados.</td></tr>')+'</table>';
 el('panel').innerHTML='<h2 class="h">📦 Bienes muebles registrados (control jurídico)</h2><p class="lead">Control registral/jurídico de bienes muebles con documento de propiedad (vehículos, acervo cultural, equipo de alto valor). El <b>resguardo e inventario administrativo</b> se lleva en <b>Administración → Inventario y bienes</b>.</p>'+form+tbl;
}
function addMue(){if(!val('m_desc')){el('m_msg').style.color='#c0392b';el('m_msg').textContent='Indica la descripción.';return;}
 var Mm=MUE();var folio='MUE-'+(new Date().getFullYear())+'-'+String(Mm.length+1).padStart(3,'0');
 Mm.push({id:uid(),folio:folio,desc:val('m_desc'),tipo:val('m_tipo'),reg:val('m_reg'),cu:val('m_cu'),valor:+val('m_val')||0,regimen:val('m_reg2'),doc:val('m_doc'),alta:hoy()});
 S('sigej_muebles_reg',Mm);bit('Alta de bien mueble '+folio);el('m_msg').style.color='#1f9d6b';el('m_msg').textContent='✓ '+folio+' registrado.';vMue();}
/* ---- Reportes ---- */
function vRep(){var I=INM();
 el('panel').innerHTML='<h2 class="h">📤 Reportes</h2><p class="lead">Matriz registral de inmuebles y padrón patrimonial.</p><div style="display:flex;gap:8px;margin-bottom:12px"><button class="b1 mini" onclick="expCSV()">⬇️ Matriz registral (CSV)</button></div>'+
  '<table><tr><th>Folio</th><th>Inmueble</th><th>Tipo</th><th>CU</th><th>Régimen</th><th>Escritura</th><th>RPP</th><th>Estatus</th></tr>'+I.map(function(x){return '<tr><td>'+esc(x.folio)+'</td><td>'+esc(x.nombre)+'</td><td>'+esc(x.tipo)+'</td><td style="font-size:11px">'+esc(x.cu)+'</td><td style="font-size:11px">'+esc(x.regimen)+'</td><td>'+esc(x.reg.escritura)+'</td><td>'+esc(x.reg.rpp)+'</td><td><span class="bdg '+regClass(x.reg.estatus)+'">'+esc(x.reg.estatus)+'</span></td></tr>';}).join('')+'</table>';
}
function expCSV(){var I=INM();var rows=[['Folio','Inmueble','Tipo','Uso','CU','Direccion','Municipio','Superficie','Valor','Regimen','Escritura','EscNum','Notario','RPP','FolioReal','Estatus']].concat(I.map(function(x){var r=x.reg;return [x.folio,x.nombre,x.tipo,x.uso,x.cu,x.direccion,x.municipio,x.superficie,x.valor,x.regimen,r.escritura,r.escNum,r.notario,r.rpp,r.folioReal,r.estatus];}));
 var csv=rows.map(function(r){return r.map(function(c){return '"'+String(c==null?'':c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='patrimonio_inmobiliario_'+hoy()+'.csv';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"patrimonial_SIGEJ.html","w",encoding="utf-8").write(out)
print("patrimonial_SIGEJ.html OK -",len(out),"bytes")
