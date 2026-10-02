# -*- coding: utf-8 -*-
# MÓDULO: Legal por Centro Universitario (vista transversal · Onda 1 del roadmap de Legal Governance).
# NO duplica captura: consolida la cartera jurídica por CU reusando datos existentes (litigios reales + índices localStorage).
import json,re
B="/Users/edithroque/Documents/CLAUDE/"
EXPJ=open(B+"_legalcu_exp.json",encoding="utf-8").read()   # 749 litigios reales (slim)
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Legal por CU'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','legalcu_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="legalcu_SIGEJ.html" class="act">🏛️ Legal por CU</a><a href="contencioso_SIGEJ.html">⚔️ Contencioso</a><a href="instrumentos_SIGEJ.html">📜 Instrumentos</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Legal por Centro Universitario</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.wrap{max-width:1280px;margin:auto;padding:16px 18px 44px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;box-shadow:0 1px 3px rgba(2,40,90,.06)}
.kpi .n{font-size:23px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.r .n{color:var(--red)}.kpi.g .n{color:var(--ok)}.kpi.y .n{color:var(--amber)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}
.cu{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;cursor:pointer;transition:.15s;border-left:5px solid var(--teal)}
.cu:hover{transform:translateY(-3px);box-shadow:0 6px 18px rgba(2,40,90,.14)}
.cu.r{border-left-color:var(--red)}.cu.y{border-left-color:var(--amber)}
.cu h3{margin:0 0 6px;font-size:14px;color:var(--azul)}
.cu .row{display:flex;justify-content:space-between;font-size:12px;color:#475569;margin:2px 0}
.cu .tot{font-size:22px;font-weight:800;color:var(--azul2);margin-top:6px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:14px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
.note{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:12px 0}
.back{color:#0a4d8c;cursor:pointer;font-size:13px}
.sec{font-weight:700;color:#0a4d8c;font-size:13px;margin:14px 0 4px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:14px}
</style></head><body>
<header><h1>🏛️ Legal por Centro Universitario</h1><div class="s">Cartera jurídica consolidada por CU · Red Universitaria (19 CU + SEMS) · vista transversal (Legal Governance)</div></header>
__NAV__
<div class="wrap" id="wrap"></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const EXP=__EXP__;
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function M(v){return '$'+Number(v||0).toLocaleString('es-MX');}
/* Catálogo canónico de la Red (infografía 2025) + patrones de normalización */
const CU=[
 {k:'CUCEA',n:'CUCEA · Económico Administrativas',p:/cucea/},
 {k:'CUCEI',n:'CUCEI · Exactas e Ingenierías',p:/cucei/},
 {k:'CUCS',n:'CUCS · Ciencias de la Salud',p:/\bcucs\b/},
 {k:'CUCSH',n:'CUCSH · Sociales y Humanidades',p:/cucsh/},
 {k:'CUCBA',n:'CUCBA · Biológico Agropecuarias',p:/cucba/},
 {k:'CUAAD',n:'CUAAD · Arte, Arquitectura y Diseño',p:/cuaad/},
 {k:'CUCostaSur',n:'CUCostaSur · Costa Sur',p:/cucsur|cucostasur|costa sur/},
 {k:'CUCosta',n:'CUCosta · Costa',p:/cucosta|cu costa|\bcosta\b/},
 {k:'CUSur',n:'CUSur · Sur',p:/\bcusur\b|centro universitario del sur/},
 {k:'CUCienega',n:'CUCiénega · Ciénega',p:/cucienega|cienega/},
 {k:'CUAltos',n:'CUAltos · Altos',p:/cualtos|de los altos/},
 {k:'CULagos',n:'CULagos · Lagos',p:/culagos|de los lagos/},
 {k:'CUNorte',n:'CUNorte · Norte',p:/cunorte|del norte/},
 {k:'CUValles',n:'CUValles · Valles',p:/cuvalles|de los valles/},
 {k:'CUTonala',n:'CUTonalá · Tonalá',p:/cutonala|tonala/},
 {k:'CUTlaquepaque',n:'CUTlaquepaque',p:/tlaquepaque/},
 {k:'CUTlajomulco',n:'CUTlajomulco',p:/tlajomulco/},
 {k:'CUChapala',n:'CUChapala',p:/chapala/},
 {k:'CUG',n:'CUGuadalajara',p:/cuguadalajara|\bcug\b|guadalajara \(cug\)/},
 {k:'SEMS',n:'SEMS · Media Superior',p:/sems|preparatoria|prepa\b|politecnica|politécnica|media superior|bachillerato/},
 {k:'RED',n:'Administración General / Red',p:/coordinacion|coordinación|rectoria|rectoría|operadora|universidad de guadalajara|pensiones|jubilaciones|region\b|administrativa|general/}
];
function cuDe(txt,cat){var t=norm(txt||'');for(var i=0;i<CU.length;i++){if(CU[i].p.test(t))return CU[i].k;}
 var c=norm(cat||'');if(c.indexOf('sems')>=0||c.indexOf('media')>=0)return 'SEMS';if(c.indexOf('administrativa')>=0||c.indexOf('rectoria')>=0)return 'RED';return 'OTRAS';}
function cuName(k){var f=CU.filter(function(x){return x.k===k;})[0];return f?f.n:(k==='OTRAS'?'Otras dependencias / sin clasificar':k);}
/* Fuentes capturadas (localStorage) atribuibles por dependencia/CU */
function capturados(){var out=[];
 L('sigej_instrumentos').forEach(function(e){out.push({fuente:'Convenio/Contrato',folio:e.folio,tit:(e.tipo||'')+' · '+(e.obj||''),est:e.estado,cu:cuDe((e.dep||'')+' '+(e.contra||''),'')});});
 L('sigej_patrimonio').forEach(function(e){out.push({fuente:'Propiedad intelectual',folio:e.folio,tit:e.titulo||e.tipo,est:e.estado,cu:cuDe((e.cu||e.dep||'')+' '+(e.autor||''),'')});});
 L('sigej_internacional').forEach(function(e){out.push({fuente:'Internacional',folio:e.folio,tit:e.titulo,est:e.estado,cu:cuDe((e.cu||e.dep||''),'')});});
 L('sigej_capacitacion').forEach(function(e){out.push({fuente:'Capacitación',folio:e.folio,tit:e.tema,est:e.estado,cu:cuDe((e.dep||''),'')});});
 L('sigej_masc').forEach(function(e){out.push({fuente:'MASC',folio:e.exp||e.num||'',tit:e.tipo||'Convenio',est:e.cumplimiento||e.estado,cu:cuDe((e.demandado||'')+' '+(e.actor||''),'')});});
 return out;}
/* Agregado por CU */
function agg(){var g={};function slot(k){if(!g[k])g[k]={litigios:0,activos:0,riesgo:0,pasivo:0,cap:0};return g[k];}
 EXP.forEach(function(e){var k=cuDe(e.d,e.c);var s=slot(k);s.litigios++;if(e.ac)s.activos++;if(/Alto|Crítico|Critico/.test(e.r||''))s.riesgo++;s.pasivo+=(+e.pa||0);});
 capturados().forEach(function(c){slot(c.cu).cap++;});
 return g;}

let CURCU=null;
function render(){if(CURCU)return detalle(CURCU);panorama();}
function panorama(){var g=agg();
 var totL=EXP.length,totR=EXP.filter(function(e){return /Alto|Crítico|Critico/.test(e.r||'');}).length,totP=EXP.reduce(function(a,e){return a+(+e.pa||0);},0);
 var nCU=Object.keys(g).filter(function(k){return k!=='OTRAS'&&g[k].litigios+g[k].cap>0;}).length;
 var kpi='<div class="kpis"><div class="kpi"><div class="n">'+totL+'</div><div class="l">Litigios (base real)</div></div><div class="kpi"><div class="n">'+nCU+'</div><div class="l">CU/sedes con cartera</div></div><div class="kpi r"><div class="n">'+totR+'</div><div class="l">Alto riesgo / críticos</div></div><div class="kpi y"><div class="n" style="font-size:17px">'+M(totP)+'</div><div class="l">Pasivo contingente (doc.)</div></div></div>';
 var orden=Object.keys(g).sort(function(a,b){return (g[b].litigios+g[b].cap)-(g[a].litigios+g[a].cap);});
 var cards=orden.map(function(k){var s=g[k];var tot=s.litigios+s.cap;if(!tot)return '';var cls=s.riesgo>=8?' r':s.riesgo>=3?' y':'';return '<div class="cu'+cls+'" onclick="abrir(\''+k+'\')"><h3>'+esc(cuName(k))+'</h3><div class="tot">'+tot+'</div><div class="row"><span>⚖️ Litigios</span><b>'+s.litigios+'</b></div><div class="row"><span>🟢 Activos</span><b>'+s.activos+'</b></div><div class="row"><span>🔴 Alto riesgo</span><b>'+s.riesgo+'</b></div><div class="row"><span>📄 Convenios/PI/otros</span><b>'+s.cap+'</b></div><div class="row"><span>💰 Pasivo</span><b>'+M(s.pasivo)+'</b></div></div>';}).join('');
 el('wrap').innerHTML='<h2 class="h">Panorama de la Red Universitaria</h2><p class="lead">Clic en un Centro Universitario para ver su cartera jurídica consolidada. Reúne litigios (base real), convenios, propiedad intelectual, asuntos internacionales, capacitación y MASC atribuidos por dependencia.</p>'+kpi+
  '<div class="card"><b style="color:#0a4d8c">Litigios por CU/sede</b><canvas id="ch" height="120"></canvas></div>'+
  '<div class="grid">'+cards+'</div>'+
  '<div class="note">ℹ️ La atribución de litigios por CU se deriva del campo <b>dependencia</b> de cada expediente (heurística de normalización); los convenios, PI, etc. se atribuyen por su dependencia capturada. Los expedientes sin CU identificable se agrupan en «Otras dependencias». Cifras de litigios = base documentada (juicios.tab, corte 2026-06-18).</div>';
 try{var top=orden.filter(function(k){return g[k].litigios>0;}).slice(0,14);if(window.__c)window.__c.destroy();window.__c=new Chart(el('ch'),{type:'bar',data:{labels:top.map(function(k){return k;}),datasets:[{label:'Litigios',data:top.map(function(k){return g[k].litigios;}),backgroundColor:'#0a4d8c'},{label:'Alto riesgo',data:top.map(function(k){return g[k].riesgo;}),backgroundColor:'#c0392b'}]},options:{scales:{x:{ticks:{font:{size:9}}}}}});}catch(e){}
}
function abrir(k){CURCU=k;window.scrollTo(0,0);render();}
function volver(){CURCU=null;render();}
function detalle(k){var lit=EXP.filter(function(e){return cuDe(e.d,e.c)===k;});var cap=capturados().filter(function(c){return c.cu===k;});
 var act=lit.filter(function(e){return e.ac;}).length,ri=lit.filter(function(e){return /Alto|Crítico|Critico/.test(e.r||'');}).length,pa=lit.reduce(function(a,e){return a+(+e.pa||0);},0);
 var kpi='<div class="kpis"><div class="kpi"><div class="n">'+lit.length+'</div><div class="l">Litigios</div></div><div class="kpi g"><div class="n">'+act+'</div><div class="l">Activos</div></div><div class="kpi r"><div class="n">'+ri+'</div><div class="l">Alto riesgo</div></div><div class="kpi y"><div class="n" style="font-size:16px">'+M(pa)+'</div><div class="l">Pasivo</div></div><div class="kpi"><div class="n">'+cap.length+'</div><div class="l">Convenios/PI/otros</div></div></div>';
 function rb(r){var c=/Crítico|Critico/.test(r)?'r':/Alto/.test(r)?'r':/Medio/.test(r)?'y':'g';return '<span class="bdg '+c+'">'+esc(r||'—')+'</span>';}
 var tL=lit.length?'<table><tr><th>Expediente</th><th>Materia</th><th>Dependencia</th><th>Estado</th><th>Riesgo</th><th>Responsable</th><th>Pasivo</th></tr>'+lit.slice(0,400).map(function(e){return '<tr><td>'+esc(e.n)+'</td><td>'+esc(e.m)+'</td><td style="font-size:11px">'+esc((e.d||'').slice(0,28))+'</td><td>'+esc(e.e)+'</td><td>'+rb(e.r)+'</td><td style="font-size:11px">'+esc(e.resp)+'</td><td>'+M(e.pa)+'</td></tr>';}).join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin litigios atribuidos.</div>';
 var tC=cap.length?'<table><tr><th>Fuente</th><th>Folio</th><th>Asunto</th><th>Estado</th></tr>'+cap.map(function(c){return '<tr><td>'+esc(c.fuente)+'</td><td>'+esc(c.folio)+'</td><td>'+esc((c.tit||'').slice(0,50))+'</td><td>'+esc(c.est||'')+'</td></tr>';}).join('')+'</table>':'<div style="color:#64748b;font-size:12px">Sin convenios/PI/otros capturados para este CU.</div>';
 el('wrap').innerHTML='<div class="back" onclick="volver()">← Volver al panorama de la Red</div><h2 class="h" style="margin-top:8px">'+esc(cuName(k))+'</h2><p class="lead">Cartera jurídica consolidada del Centro Universitario.</p>'+kpi+
  '<div style="display:flex;gap:8px;margin-bottom:10px"><button class="bd mini" onclick="expCU(\''+k+'\')">⬇️ Exportar CSV</button></div>'+
  '<div class="card"><div class="sec">⚖️ Litigios ('+lit.length+')</div>'+tL+'</div>'+
  '<div class="card"><div class="sec">📄 Convenios · Propiedad intelectual · Internacional · Capacitación · MASC ('+cap.length+')</div>'+tC+'</div>';
}
function expCU(k){var lit=EXP.filter(function(e){return cuDe(e.d,e.c)===k;});var rows=[['Expediente','Materia','Dependencia','Estado','Riesgo','Responsable','Pasivo']].concat(lit.map(function(e){return [e.n,e.m,e.d,e.e,e.r,e.resp,e.pa];}));
 var csv=rows.map(function(r){return r.map(function(x){return '"'+String(x==null?'':x).replace(/"/g,'""')+'"';}).join(',');}).join('\n');
 var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='LegalCU_'+k+'.csv';a.click();}
render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;background:#fff!important}";document.head.appendChild(st);function clean(){try{document.querySelectorAll('div[style*="99999"]').forEach(function(o){o.remove();});var b=document.querySelector('div[style*="bottom:12px"][style*="right:12px"]');if(b)b.style.display="none";}catch(e){}}clean();setTimeout(clean,200);setTimeout(clean,800);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__EXP__",EXPJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"legalcu_SIGEJ.html","w",encoding="utf-8").write(out)
print("legalcu_SIGEJ.html OK -",len(out),"bytes")
