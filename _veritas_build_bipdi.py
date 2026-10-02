# -*- coding: utf-8 -*-
# MÓDULO: BI Estratégico · Gobernanza Jurídica alineada al PDI 2025-2031 (Onda 1 · #3).
# Consolida indicadores de TODOS los módulos SIGEJ y los mapea a los 5 ejes del PDI, con metodología línea base 2025 → metas 2028/2031.
import re,json
B="/Users/edithroque/Documents/CLAUDE/"
KPIJ=json.dumps(json.load(open(B+"inicio_kpi.json",encoding="utf-8")),ensure_ascii=False)  # KPIs reales del litigio
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'BI Estratégico PDI'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','bipdi_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="bipdi_SIGEJ.html" class="act">🎯 BI Estratégico PDI</a><a href="legalcu_SIGEJ.html">🏛️ Legal por CU</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · BI Estratégico PDI 2025-2031</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.vsel{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);border-radius:20px;padding:5px 10px;font-size:12px;color:#fff}
.vsel select{background:transparent;border:none;color:#fff;font-size:12px}.vsel select option{color:#0a1f3c}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12px}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:320px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.ejes{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-bottom:14px}
.eje{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;cursor:pointer;border-top:5px solid var(--teal);transition:.15s}
.eje:hover{transform:translateY(-3px);box-shadow:0 6px 18px rgba(2,40,90,.14)}
.eje.e1{border-top-color:#0a4d8c}.eje.e2{border-top-color:#1aa39a}.eje.e3{border-top-color:#d4a32c}.eje.e4{border-top-color:#8e6fd4}.eje.e5{border-top-color:#1f9d6b}
.eje h3{margin:0 0 6px;font-size:13.5px;color:var(--azul)}
.eje .cov{font-size:22px;font-weight:800;color:var(--azul2)}
.eje .l{font-size:11px;color:var(--mut)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px;vertical-align:middle}
td input{width:90px;padding:5px;border:1px solid var(--line);border-radius:6px;font-size:12px}
.bar{height:9px;background:#eef2f7;border-radius:6px;overflow:hidden;min-width:80px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--teal),var(--azul2))}
.tag{display:inline-block;background:#eef2f7;border:1px solid var(--line);border-radius:10px;padding:1px 7px;font-size:10px;margin:1px}
.gap{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:12px;margin:8px 0}
.opp{color:#b45309;font-weight:700}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.back{color:#0a4d8c;cursor:pointer;font-size:13px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
</style></head><body>
<header><div><h1>🎯 BI Estratégico · Gobernanza Jurídica</h1><div class="s">Alineado al Plan de Desarrollo Institucional 2025-2031 · 5 ejes · metodología línea base → metas 2028/2031</div></div>
<div class="vsel">👁️ Vista: <select id="vista" onchange="render()"><option>Institucional (Rectora / Secretario / Abogado General)</option><option>Por Coordinación</option><option>Por Centro Universitario</option><option>Por Dependencia</option></select></div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const KPI=__KPI__;
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function LO(k){try{return JSON.parse(localStorage.getItem(k)||'{}');}catch(e){return {};}}
function S(k,v){localStorage.setItem(k,JSON.stringify(v));}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
function pct(v){return (v==null?'—':v+'%');}
function metas(){return LO('sigej_bipdi_metas');}
function setMeta(id,y,v){var m=metas();m[id]=m[id]||{};m[id][y]=v;S('sigej_bipdi_metas',m);}

/* Los 5 ejes del PDI 2025-2031 (verificados del documento) */
const EJES=[
 {k:'e1',n:'Formación de calidad para la vida'},
 {k:'e2',n:'Generar conocimiento'},
 {k:'e3',n:'De la mano con la sociedad'},
 {k:'e4',n:'Cultura que nos une'},
 {k:'e5',n:'Gestión que construye'}
];
function sum(k,f){return L(k).reduce(function(a,x){return a+(+(f(x))||0);},0);}
/* Indicadores: valor REAL desde SIGEJ; meta = editable (del PDI / Abogado General) */
const IND=[
 // Eje 1 · Formación
 {e:'e1',id:'i_capac',n:'Acciones de capacitación jurídica',u:'acciones',t:'▲',src:['Conocimiento y Desarrollo'],v:function(){return L('sigej_capacitacion').length;}},
 {e:'e1',id:'i_hrs',n:'Horas de capacitación impartidas',u:'horas',t:'▲',src:['Conocimiento'],v:function(){return sum('sigej_capacitacion',function(x){return x.horas;});}},
 {e:'e1',id:'i_part',n:'Participantes capacitados',u:'personas',t:'▲',src:['Conocimiento'],v:function(){return sum('sigej_capacitacion',function(x){return x.part;});}},
 {e:'e1',id:'i_prog',n:'Programas académicos con dictamen jurídico',u:'programas',t:'▲',src:[],gap:'Módulo de Gestión Jurídica de Programas Académicos (Onda 2)',v:function(){return 0;}},
 // Eje 2 · Conocimiento
 {e:'e2',id:'i_pi',n:'Registros de propiedad intelectual',u:'registros',t:'▲',src:['Patrimonio Intangible'],v:function(){return L('sigej_patrimonio').length;}},
 {e:'e2',id:'i_inv',n:'Proyectos / productos de investigación con cobertura jurídica',u:'proyectos',t:'▲',src:['Conocimiento→Investigación'],v:function(){return L('sigej_invest').length;}},
 {e:'e2',id:'i_edi',n:'Productos editoriales (ISBN/ISSN, cesiones)',u:'productos',t:'▲',src:['Conocimiento→Editorial'],v:function(){return L('sigej_editorial').length;}},
 {e:'e2',id:'i_bib',n:'Acervo bibliográfico jurídico administrado',u:'títulos',t:'▲',src:['Conocimiento→Biblioteca'],v:function(){return L('sigej_biblioteca').length;}},
 {e:'e2',id:'i_intl',n:'Convenios/asuntos de internacionalización y movilidad',u:'asuntos',t:'▲',src:['Asuntos Internacionales'],v:function(){return L('sigej_internacional').length;}},
 // Eje 3 · Sociedad
 {e:'e3',id:'i_conv',n:'Convenios y contratos con la sociedad / dependencias',u:'instrumentos',t:'▲',src:['Instrumentos Jurídicos'],v:function(){return L('sigej_instrumentos').length;}},
 {e:'e3',id:'i_masc',n:'Asuntos resueltos por MASC (conciliaciones)',u:'asuntos',t:'▲',src:['Contencioso→MASC'],v:function(){return L('sigej_masc').length;}},
 {e:'e3',id:'i_dif',n:'Productos de difusión de la cultura jurídica',u:'productos',t:'▲',src:['Conocimiento→Difusión'],v:function(){return L('sigej_difusion').length;}},
 {e:'e3',id:'i_ases',n:'Asesorías y consultas jurídicas atendidas',u:'consultas',t:'▲',src:['Contencioso→Asesoría'],v:function(){return L('sigej_asesoria').length;}},
 // Eje 4 · Cultura
 {e:'e4',id:'i_difc',n:'Acciones de difusión cultural con soporte jurídico',u:'acciones',t:'▲',src:['Conocimiento→Difusión'],v:function(){return L('sigej_difusion').length;}},
 {e:'e4',id:'i_recinto',n:'Recintos culturales con contrato/póliza vigente',u:'recintos',t:'▲',src:[],gap:'Módulo de Gestión Jurídica del Patrimonio Cultural (MUSA, Diana, Telmex…) (Onda 2)',v:function(){return 0;}},
 {e:'e4',id:'i_event',n:'Eventos institucionales con contrato jurídico',u:'eventos',t:'▲',src:[],gap:'Se cubre al construir Patrimonio Cultural (Onda 2)',v:function(){return 0;}},
 // Eje 5 · Gestión
 {e:'e5',id:'i_litact',n:'Litigios activos bajo gestión',u:'expedientes',t:'▼',src:['Contencioso'],v:function(){return KPI.activos;}},
 {e:'e5',id:'i_tasa',n:'Tasa de éxito en litigios',u:'%',t:'▲',src:['Contencioso'],v:function(){return KPI.tasa;}},
 {e:'e5',id:'i_pasivo',n:'Pasivo contingente documentado',u:'MXN',t:'▼',money:true,src:['Contencioso'],v:function(){return KPI.pasivo_doc;}},
 {e:'e5',id:'i_riesgo',n:'Expedientes de alto riesgo / críticos',u:'expedientes',t:'▼',src:['Contencioso'],v:function(){return KPI.alto_riesgo;}},
 {e:'e5',id:'i_audit',n:'Observaciones de auditoría solventadas',u:'%',t:'▲',src:['Auditorías'],v:function(){var o=[];L('sigej_auditorias').forEach(function(a){(a.obs||[]).forEach(function(x){o.push(x);});});return o.length?Math.round(100*o.filter(function(x){return x.estado==='Solventada';}).length/o.length):0;}},
 {e:'e5',id:'i_transp',n:'Solicitudes de transparencia (UTI) registradas',u:'solicitudes',t:'▲',src:['Transparencia'],v:function(){return L('sigej_uti').length;}},
 {e:'e5',id:'i_resp',n:'Responsabilidades administrativas en proceso',u:'procedimientos',t:'▼',src:['Contencioso→Responsabilidades'],v:function(){return L('sigej_resp').length;}},
 {e:'e5',id:'i_norm',n:'Instrumentos normativos gestionados',u:'normas',t:'▲',src:['Normatividad'],v:function(){return L('sigej_normatividad').length;}}
];
function indEje(k){return IND.filter(function(x){return x.e===k;});}
function fmtV(ind){var v=ind.v();return ind.money?M(v):(ind.u==='%'?v+'%':Number(v).toLocaleString('es-MX'));}
function avance(ind){var m=metas()[ind.id];var v=ind.v();if(!m||!m['2031'])return null;var meta=+m['2031'];if(!meta)return null;
 if(ind.t==='▼')return Math.max(0,Math.min(100,Math.round(100*(1-(v-meta)/(v||1)))));// para descendentes, avance = cercanía a meta menor
 return Math.min(100,Math.round(100*v/meta));}
function cobertura(k){var is=indEje(k);var con=is.filter(function(i){return i.v()>0;}).length;return {con:con,tot:is.length,pct:Math.round(100*con/is.length)};}

var VIEW='panorama';
var TABS=[['panorama','🗺️ Panorama']].concat(EJES.map(function(e,i){return [e.k,'Eje '+(i+1)];}));
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){buildTabs();if(VIEW==='panorama')vPanorama();else vEje(VIEW);}

function vPanorama(){var vista=el('vista')?el('vista').value:'';
 var cards=EJES.map(function(e,i){var c=cobertura(e.k);return '<div class="eje '+e.k+'" onclick="goV(\''+e.k+'\')"><h3>Eje '+(i+1)+' · '+esc(e.n)+'</h3><div class="cov">'+c.con+'/'+c.tot+'</div><div class="l">indicadores con dato en SIGEJ</div><div class="bar" style="margin-top:8px"><i style="width:'+c.pct+'%"></i></div></div>';}).join('');
 el('panel').innerHTML='<h2 class="h">🗺️ Panorama de gobernanza por eje del PDI</h2><p class="lead">Cobertura del jurídico en cada eje del Plan de Desarrollo Institucional 2025-2031. Clic en un eje para ver sus indicadores, metas y avance. Vista actual: <b>'+esc(vista)+'</b>.</p>'+
  '<div class="ejes">'+cards+'</div>'+
  '<div class="card"><b style="color:#0a4d8c">Cobertura jurídica por eje (radar)</b><canvas id="radar" height="150"></canvas></div>'+
  '<div class="note">ℹ️ La <b>vista por rol/CU/dependencia</b> aplica el filtro de datos correspondiente; la segregación fina y la alimentación automática desde <b>SIIAU/CGPE/Power BI</b> son fase backend. Los <b>valores son reales del SIGEJ</b> (corte vigente); las <b>metas 2028/2031</b> las captura el Abogado General o se alimentan del PDI.</div>';
 try{if(window.__r)window.__r.destroy();window.__r=new Chart(el('radar'),{type:'radar',data:{labels:EJES.map(function(e,i){return 'Eje '+(i+1);}),datasets:[{label:'Cobertura %',data:EJES.map(function(e){return cobertura(e.k).pct;}),backgroundColor:'rgba(10,77,140,.2)',borderColor:'#0a4d8c',pointBackgroundColor:'#0a4d8c'}]},options:{scales:{r:{beginAtZero:true,max:100,ticks:{font:{size:8}}}}}});}catch(e){}
}
function vEje(k){var e=EJES.filter(function(x){return x.k===k;})[0];var idx=EJES.map(function(x){return x.k;}).indexOf(k)+1;var is=indEje(k);var m=metas();
 var rows=is.map(function(ind){var v=ind.v();var mm=m[ind.id]||{};var av=avance(ind);var gap=ind.v()===0&&ind.gap;
  return '<tr'+(gap?' style="background:#fffdf5"':'')+'><td><b>'+esc(ind.n)+'</b><br><span style="font-size:10px;color:#64748b">'+ind.src.map(function(s){return '<span class="tag">'+esc(s)+'</span>';}).join('')+(gap?' <span class="opp">⚑ oportunidad</span>':'')+'</td>'+
   '<td style="font-weight:700;color:#0a4d8c">'+fmtV(ind)+' <span style="font-size:10px;color:#64748b">'+esc(ind.u)+'</span></td>'+
   '<td><input type="number" value="'+(mm['2028']||'')+'" onchange="setMeta(\''+ind.id+'\',\'2028\',this.value)" placeholder="—"></td>'+
   '<td><input type="number" value="'+(mm['2031']||'')+'" onchange="setMeta(\''+ind.id+'\',\'2031\',this.value);render()" placeholder="—"></td>'+
   '<td>'+(av!=null?'<div style="display:flex;align-items:center;gap:6px"><div class="bar"><i style="width:'+av+'%"></i></div><span style="font-size:11px">'+av+'%</span></div>':'<span style="color:#94a3b8;font-size:11px">define meta</span>')+'</td>'+
   '<td style="text-align:center;font-size:14px">'+ind.t+'</td></tr>';}).join('');
 var gaps=is.filter(function(i){return i.gap&&i.v()===0;});
 var gapHtml=gaps.length?'<div class="gap">⚑ <b>Oportunidades de módulo para este eje:</b><ul style="margin:4px 0 0 16px;padding:0">'+gaps.map(function(g){return '<li>'+esc(g.n)+' → '+esc(g.gap)+'</li>';}).join('')+'</ul></div>':'';
 el('panel').innerHTML='<div class="back" onclick="goV(\'panorama\')">← Panorama</div><h2 class="h" style="margin-top:8px">Eje '+idx+' · '+esc(e.n)+'</h2><p class="lead">Indicadores del jurídico que aportan a este eje del PDI. Valores reales del SIGEJ; captura la meta 2028/2031 (▲ deseable subir · ▼ deseable bajar).</p>'+
  '<div class="card"><table><tr><th>Indicador</th><th>Valor actual</th><th>Meta 2028</th><th>Meta 2031</th><th>Avance</th><th>Tend.</th></tr>'+rows+'</table></div>'+gapHtml+
  '<div class="note">Metodología PDI: línea base 2025 (valor actual del SIGEJ) → meta 2028 → meta 2031 → tendencia deseable. Las metas se guardan en el sistema; la alimentación oficial provendría del PDI/COPLADI (backend).</div>';
}
buildTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);function clean(){try{document.querySelectorAll('div[style*="99999"]').forEach(function(o){o.remove();});var b=document.querySelector('div[style*="bottom:12px"][style*="right:12px"]');if(b)b.style.display="none";}catch(e){}}clean();setTimeout(clean,200);setTimeout(clean,800);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__KPI__",KPIJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"bipdi_SIGEJ.html","w",encoding="utf-8").write(out)
print("bipdi_SIGEJ.html OK -",len(out),"bytes")
