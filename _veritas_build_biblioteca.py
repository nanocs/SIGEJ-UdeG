# -*- coding: utf-8 -*-
# BIBLIOTECA JURÍDICA · Submódulo del Módulo Operativo — CONSULTA y SOLICITUD DE PRÉSTAMO para usuarios generales.
# Usuarios generales: solo consultar catálogo, ver ficha y solicitar préstamo (y ver si un ejemplar está prestado, a quién y de qué área).
# Alta/edición/baja del acervo, autorización de préstamos y registro de devoluciones: SOLO 'Bibliotecario' / Administrador / Help Desk.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Biblioteca Jurídica'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','biblioteca_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="operativo_SIGEJ.html">🧰 Módulo Operativo</a><a href="biblioteca_SIGEJ.html" class="act">📚 Biblioteca</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Biblioteca Jurídica</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:15px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 44px}
.searchbar{position:sticky;top:0;z-index:20;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);margin-bottom:12px}
.searchbar input.q{width:100%;font-size:15px;padding:11px 14px;border:2px solid var(--azul2);border-radius:12px}
.filters{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:7px;margin-top:8px}
.filters select,.filters input{width:100%;font-size:12.5px;padding:7px;border:1px solid var(--line);border-radius:8px;background:#fff}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:12px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul2)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.bk{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px;display:flex;gap:10px;cursor:pointer;transition:.12s}
.bk:hover{box-shadow:0 6px 18px rgba(2,40,90,.12);transform:translateY(-2px)}
.bk .cov{width:56px;height:78px;border-radius:6px;flex:none;display:flex;align-items:center;justify-content:center;font-size:26px;color:#fff;background:linear-gradient(150deg,#0a4d8c,#1aa39a)}
.bk .t{font-weight:700;font-size:13.5px;color:#0a2f4f;line-height:1.25}
.bk .a{font-size:11.5px;color:#64748b;margin-top:2px}
.bk .m{font-size:11px;color:#94a3b8;margin-top:4px}
.disp{display:inline-block;font-size:10px;font-weight:700;border-radius:10px;padding:2px 8px;margin-top:6px}
.disp.d{background:#e7f7ee;color:#128c4a}.disp.p{background:#fdeaea;color:#c0392b}.disp.r{background:#fef3e2;color:#b45309}
.btn{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:8px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bg{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
.drawer{position:fixed;inset:0;background:rgba(8,20,38,.5);display:none;z-index:9000}
.drawer.on{display:block}
.panel{position:absolute;top:0;right:0;width:560px;max-width:96vw;height:100%;background:#fff;overflow:auto;padding:18px 20px;box-shadow:-8px 0 30px rgba(0,0,0,.3)}
.panel .x{position:absolute;top:12px;right:16px;cursor:pointer;font-size:18px;color:#64748b}
.fichacov{width:96px;height:132px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:44px;color:#fff;background:linear-gradient(150deg,#0a4d8c,#1aa39a)}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:7px 6px;vertical-align:top}
.kv{font-size:12.5px;line-height:1.9}.kv b{color:#0a2f4f}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.warn{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
.tabs{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:12px}
.tab{padding:8px 13px;border:1px solid var(--line);border-radius:9px;background:#fff;cursor:pointer;font-size:12.5px}
.tab.on{background:#0a4d8c;color:#fff;font-weight:700}
</style></head><body>
<header><h1>📚 Biblioteca Jurídica · Oficina de la Abogacía General</h1><div class="s">Consulta del acervo y solicitud de préstamos · UdeG</div></header>
__NAV__
<div class="wrap">
 <div class="tabs" id="tabs"></div>
 <div id="pane"></div>
</div>
<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwc"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function S(k,v){localStorage.setItem(k,JSON.stringify(v));}
function ec(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function nowT(){return new Date().toISOString().slice(0,16).replace('T',' ');}
var PERFIL=localStorage.getItem('sigej_perfil')||'(perfil)';
var SES=J('sigej_sesion')||{};
/* Personal autorizado de la Biblioteca (admin del acervo y de préstamos) */
var BIBAD=['Bibliotecario','Responsable de Biblioteca','Administrador','Sistemas','Jefe del Área de Sistemas','Jefe de Unidad de Capacitación, Investigación y Difusión'];
function esBibliotecario(){return BIBAD.indexOf(PERFIL)>=0;}
/* adscripción del usuario (para registrar en la solicitud) */
function miAdscr(){var code=SES.code;var U=J('sigej_usuarios');if(code&&Array.isArray(U)){for(var i=0;i<U.length;i++){if(String(U[i].numEmp||'').toLowerCase()===String(code).toLowerCase())return U[i].unidad||U[i].coord||'';}}return localStorage.getItem('sigej_op_adscr')||'';}
var TIPOS=['Libro','Revista','Tesis','Manual','Legislación','Jurisprudencia','Obra de consulta','Código comentado','Formulario'];
function blog(t,a){try{var L=J('sigej_bitacora')||[];L.push({ts:new Date().toISOString().slice(0,19).replace('T',' '),perfil:PERFIL,modulo:'Biblioteca Jurídica',tipo:t,accion:String(a||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);S('sigej_bitacora',L);}catch(e){}if(window.__bitlog){try{window.__bitlog(t,a);}catch(e){}}}
/* ===== acervo (seed) ===== */
function seed(){if(J('sigej_biblioteca_acervo'))return;S('sigej_biblioteca_acervo',[
 {id:'BIB-0001',titulo:'Constitución Política de los Estados Unidos Mexicanos comentada',autor:'IIJ-UNAM',materia:'Derecho Constitucional',editorial:'UNAM',anio:2023,isbn:'978-607-30-0001-1',clas:'KGF2921',tipo:'Legislación',kw:'constitución, amparo, derechos humanos',resumen:'Texto constitucional con comentarios doctrinales artículo por artículo.',ubic:'Estante A-1',ejemplares:3},
 {id:'BIB-0002',titulo:'Ley Orgánica de la Universidad de Guadalajara — texto y reformas',autor:'Secretaría General UdeG',materia:'Normatividad Universitaria',editorial:'UdeG',anio:2022,isbn:'',clas:'UDG-LO-01',tipo:'Legislación',kw:'ley orgánica, gobierno universitario, CGU',resumen:'Compilación de la Ley Orgánica y sus reformas.',ubic:'Estante U-1',ejemplares:5},
 {id:'BIB-0003',titulo:'Derecho Administrativo',autor:'Gabino Fraga',materia:'Derecho Administrativo',editorial:'Porrúa',anio:2021,isbn:'978-970-07-0002-2',clas:'KGF-DA-114',tipo:'Libro',kw:'acto administrativo, procedimiento, nulidad',resumen:'Obra clásica del derecho administrativo mexicano.',ubic:'Estante B-3',ejemplares:2},
 {id:'BIB-0004',titulo:'Contratos civiles',autor:'Rafael Rojina Villegas',materia:'Derecho Civil',editorial:'Porrúa',anio:2020,isbn:'978-970-07-0003-3',clas:'KGF-DC-220',tipo:'Libro',kw:'contratos, obligaciones, convenios',resumen:'Teoría y práctica de los contratos civiles.',ubic:'Estante B-4',ejemplares:1},
 {id:'BIB-0005',titulo:'Propiedad intelectual y transferencia de tecnología',autor:'Varios',materia:'Propiedad Intelectual',editorial:'Tirant lo Blanch',anio:2023,isbn:'978-84-1113-004-4',clas:'PI-TT-050',tipo:'Obra de consulta',kw:'patentes, marcas, derechos de autor, licencias',resumen:'Marco jurídico de la PI y la transferencia tecnológica universitaria.',ubic:'Estante C-1',ejemplares:2},
 {id:'BIB-0006',titulo:'Semanario Judicial de la Federación — jurisprudencia laboral',autor:'SCJN',materia:'Derecho Laboral',editorial:'SCJN',anio:2024,isbn:'',clas:'SJF-LAB',tipo:'Jurisprudencia',kw:'jurisprudencia, laboral, reinstalación',resumen:'Tesis y jurisprudencia en materia laboral.',ubic:'Estante D-2',ejemplares:4},
 {id:'BIB-0007',titulo:'Manual de Oficialía de Partes y gestión documental',autor:'AGN',materia:'Archivística',editorial:'AGN',anio:2022,isbn:'978-607-00-0007-7',clas:'ARCH-OP-10',tipo:'Manual',kw:'oficialía, correspondencia, archivo, CADIDO',resumen:'Buenas prácticas de recepción, turnado y archivo.',ubic:'Estante E-1',ejemplares:2}
]);}
seed();
function ACE(){return J('sigej_biblioteca_acervo')||[];}
function saveACE(a){S('sigej_biblioteca_acervo',a);}
function PRE(){return J('sigej_biblioteca_prestamos')||[];}
function savePRE(a){S('sigej_biblioteca_prestamos',a);}
/* préstamos activos de un libro */
function activos(libId){return PRE().filter(function(p){return p.libId===libId&&['Entregada','Autorizada'].indexOf(p.estado)>=0;});}
function pendientes(libId){return PRE().filter(function(p){return p.libId===libId&&p.estado==='Pendiente';});}
function disponibles(b){var pr=activos(b.id).length;return Math.max(0,(b.ejemplares||0)-pr);}
function dispEstado(b){var d=disponibles(b);if(d>0)return {k:'d',t:'Disponible ('+d+'/'+(b.ejemplares||0)+')'};if(pendientes(b.id).length)return {k:'r',t:'Reservado'};return {k:'p',t:'Prestado'};}
/* ===== TABS ===== */
function tabsList(){var t=[['cat','🔎 Consulta del acervo'],['mis','📋 Mis solicitudes']];if(esBibliotecario())t.push(['adm','🛠️ Administración (Biblioteca)']);return t;}
var cur='cat';
function drawTabs(){el('tabs').innerHTML=tabsList().map(function(t){return '<button class="tab'+(t[0]===cur?' on':'')+'" onclick="go(\''+t[0]+'\')">'+t[1]+'</button>';}).join('');}
function go(id){cur=id;drawTabs();render();window.scrollTo(0,0);}
function render(){if(cur==='cat')catalogo();else if(cur==='mis')misSolicitudes();else if(cur==='adm')admin();}
/* ===== 1. CONSULTA DEL CATÁLOGO + 4. BÚSQUEDA RÁPIDA ===== */
function uniq(key){var s={};ACE().forEach(function(b){if(b[key])s[b[key]]=1;});return Object.keys(s).sort();}
function catalogo(){
 var A=ACE();var total=A.length;var disp=A.filter(function(b){return disponibles(b)>0;}).length;
 el('pane').innerHTML='<div class="searchbar"><input class="q" id="q" placeholder="🔎 Búsqueda rápida: título, autor, materia, ISBN, palabras clave…" oninput="lista()">'+
  '<div class="filters">'+
   '<input id="f_tit" placeholder="Título" oninput="lista()">'+
   '<input id="f_aut" placeholder="Autor" oninput="lista()">'+
   '<select id="f_mat" onchange="lista()"><option value="">Materia (todas)</option>'+uniq('materia').map(function(x){return '<option>'+ec(x)+'</option>';}).join('')+'</select>'+
   '<select id="f_edi" onchange="lista()"><option value="">Editorial (todas)</option>'+uniq('editorial').map(function(x){return '<option>'+ec(x)+'</option>';}).join('')+'</select>'+
   '<input id="f_anio" placeholder="Año" oninput="lista()">'+
   '<input id="f_isbn" placeholder="ISBN" oninput="lista()">'+
   '<input id="f_clas" placeholder="Clasificación" oninput="lista()">'+
   '<select id="f_tipo" onchange="lista()"><option value="">Tipo de material</option>'+TIPOS.map(function(x){return '<option>'+ec(x)+'</option>';}).join('')+'</select>'+
   '<select id="f_disp" onchange="lista()"><option value="">Disponibilidad</option><option>Disponible</option><option>Prestado</option><option>Reservado</option></select>'+
  '</div></div>'+
  '<div class="kpis"><div class="kpi"><div class="n">'+total+'</div><div class="l">Títulos en el acervo</div></div><div class="kpi"><div class="n">'+disp+'</div><div class="l">Con ejemplares disponibles</div></div><div class="kpi"><div class="n" id="kres">'+total+'</div><div class="l">Resultados</div></div></div>'+
  '<div class="cards" id="cards"></div>';
 lista();}
function filtra(){var A=ACE();var q=norm((el('q')||{}).value||'');
 var ft=norm((el('f_tit')||{}).value||''),fa=norm((el('f_aut')||{}).value||''),fm=(el('f_mat')||{}).value||'',fe=(el('f_edi')||{}).value||'',fy=((el('f_anio')||{}).value||'').trim(),fi=norm((el('f_isbn')||{}).value||''),fc=norm((el('f_clas')||{}).value||''),fp=(el('f_tipo')||{}).value||'',fd=(el('f_disp')||{}).value||'';
 return A.filter(function(b){
   if(ft&&norm(b.titulo).indexOf(ft)<0)return false;
   if(fa&&norm(b.autor).indexOf(fa)<0)return false;
   if(fm&&b.materia!==fm)return false;if(fe&&b.editorial!==fe)return false;
   if(fy&&String(b.anio||'')!==fy)return false;if(fi&&norm(b.isbn).indexOf(fi)<0)return false;
   if(fc&&norm(b.clas).indexOf(fc)<0)return false;if(fp&&b.tipo!==fp)return false;
   if(fd){var de=dispEstado(b).k;if(fd==='Disponible'&&de!=='d')return false;if(fd==='Prestado'&&de!=='p')return false;if(fd==='Reservado'&&de!=='r')return false;}
   if(q){var blob=norm(b.titulo+' '+b.autor+' '+b.materia+' '+b.editorial+' '+b.isbn+' '+b.clas+' '+b.tipo+' '+(b.kw||'')+' '+(b.resumen||''));if(blob.indexOf(q)<0)return false;}
   return true;}).sort(function(a,b){return norm(a.titulo).localeCompare(norm(b.titulo));});}
function lista(){var rows=filtra();if(el('kres'))el('kres').textContent=rows.length;
 el('cards').innerHTML=rows.length?rows.map(function(b){var d=dispEstado(b);return '<div class="bk" onclick="ficha(\''+b.id+'\')"><div class="cov">'+(b.tipo==='Jurisprudencia'?'⚖️':b.tipo==='Legislación'?'📜':b.tipo==='Revista'?'📰':'📕')+'</div><div><div class="t">'+ec(b.titulo)+'</div><div class="a">'+ec(b.autor)+' · '+ec(b.anio||'')+'</div><div class="m">'+ec(b.materia)+' · '+ec(b.tipo)+'</div><span class="disp '+d.k+'">'+d.t+'</span></div></div>';}).join(''):'<div class="warn">Sin resultados con esos filtros.</div>';}
/* ===== 2. FICHA + 3. SOLICITUD DE PRÉSTAMO ===== */
function ficha(id){var b=ACE().filter(function(x){return x.id===id;})[0];if(!b)return;var d=dispEstado(b);var act=activos(b.id);var esAdmin=esBibliotecario();
 var prestadoInfo=act.length?('<div class="warn"><b>Ejemplar(es) en préstamo:</b><table style="margin-top:4px"><tr><th>Persona</th><th>Área / Coord. / Unidad</th><th>Desde</th><th>Estado</th></tr>'+act.map(function(p){return '<tr><td>'+ec(p.solicitante)+'</td><td>'+ec(p.adscripcion||'—')+'</td><td style="font-size:11px">'+ec(p.fEntrega||p.fSolicitud||'')+'</td><td><span class="disp '+(p.estado==='Entregada'?'p':'r')+'">'+ec(p.estado)+'</span></td></tr>';}).join('')+'</table></div>'):'';
 var histBtn=esAdmin?'<div style="margin-top:10px"><b>Historial de préstamos (personal autorizado):</b><table style="margin-top:4px"><tr><th>Persona</th><th>Área</th><th>Solicitud</th><th>Estado</th></tr>'+PRE().filter(function(p){return p.libId===b.id;}).slice(-20).reverse().map(function(p){return '<tr><td>'+ec(p.solicitante)+'</td><td style="font-size:11px">'+ec(p.adscripcion||'—')+'</td><td style="font-size:11px">'+ec(p.fSolicitud)+'</td><td>'+ec(p.estado)+'</td></tr>';}).join('')+'</table></div>':'';
 var puedeSolicitar=disponibles(b)>0;
 el('drwc').innerHTML='<div style="display:flex;gap:16px"><div class="fichacov">'+(b.tipo==='Jurisprudencia'?'⚖️':b.tipo==='Legislación'?'📜':'📘')+'</div><div style="flex:1"><h2 style="margin:0 0 4px;color:#00254a;font-size:17px">'+ec(b.titulo)+'</h2><div style="color:#64748b;font-size:12.5px">'+ec(b.autor)+'</div><span class="disp '+d.k+'" style="margin-top:6px">'+d.t+'</span></div></div>'+
  '<div class="kv" style="margin-top:12px"><b>Materia:</b> '+ec(b.materia)+'<br><b>Tipo:</b> '+ec(b.tipo)+'<br><b>Editorial:</b> '+ec(b.editorial||'—')+'<br><b>Año:</b> '+ec(b.anio||'—')+'<br><b>ISBN:</b> '+ec(b.isbn||'—')+'<br><b>Clasificación:</b> '+ec(b.clas||'—')+'<br><b>Ubicación física:</b> '+ec(b.ubic||'—')+'<br><b>Ejemplares:</b> '+(b.ejemplares||0)+' · <b>Disponibles:</b> '+disponibles(b)+'<br><b>Palabras clave:</b> '+ec(b.kw||'—')+'</div>'+
  '<div class="note" style="margin-top:8px"><b>Resumen:</b> '+ec(b.resumen||'—')+'</div>'+
  prestadoInfo+histBtn+
  '<div style="margin-top:14px">'+(puedeSolicitar?'<button class="bg" onclick="solicitar(\''+b.id+'\')">📖 Solicitar préstamo</button>':'<button class="bd" disabled>Sin ejemplares disponibles</button>')+' <button class="bd" onclick="closeDrw()">Cerrar</button></div>'+
  '<div class="note" style="margin-top:10px;font-size:11px">🔒 Como usuario general solo puedes <b>consultar</b> y <b>solicitar préstamo</b>. La administración del acervo, la autorización de préstamos y el registro de devoluciones corresponden al personal autorizado de la Biblioteca.</div>';
 el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
function solicitar(id){var b=ACE().filter(function(x){return x.id===id;})[0];if(!b)return;if(disponibles(b)<=0){alert('No hay ejemplares disponibles.');return;}
 var adsc=miAdscr();if(!adsc){adsc=prompt('Indica tu Área / Coordinación / Unidad:','');if(adsc===null)return;}
 var P=PRE();var folio='PRE-'+new Date().getFullYear()+'-'+String(P.length+1).padStart(4,'0');
 P.push({id:'PR-'+Date.now().toString(36),folio:folio,libId:b.id,titulo:b.titulo,solicitante:SES.nombre||PERFIL,perfil:PERFIL,adscripcion:adsc,fSolicitud:nowT(),estado:'Pendiente',hist:[{ts:nowT(),usuario:PERFIL,accion:'Solicitud de préstamo'}]});
 savePRE(P);blog('Acción','Solicitud de préstamo '+folio+' · '+b.titulo);
 /* notificación automática al responsable de la Biblioteca (canal SIGEJ) */
 try{var N=J('sigej_notificaciones')||[];N.push({id:'NT-'+Date.now().toString(36),ts:nowT(),tipo:'Biblioteca',folio:folio,asunto:'Solicitud de préstamo',para:'Responsable de Biblioteca',rol:'Biblioteca',canal:'SIGEJ',mensaje:(SES.nombre||PERFIL)+' ('+adsc+') solicita: '+b.titulo,link:'biblioteca_SIGEJ.html',leido:false,origen:'Biblioteca Jurídica'});S('sigej_notificaciones',N);}catch(e){}
 alert('✅ Solicitud '+folio+' enviada al responsable de la Biblioteca para su autorización.');closeDrw();go('mis');}
/* ===== Mis solicitudes (usuario) ===== */
function misSolicitudes(){var mias=PRE().filter(function(p){return p.perfil===PERFIL||p.solicitante===(SES.nombre||PERFIL);}).slice().reverse();
 el('pane').innerHTML='<div class="note">Aquí ves el estado de <b>tus</b> solicitudes de préstamo. El responsable de la Biblioteca las autoriza, entrega y registra la devolución.</div><div class="card" style="background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px;overflow:auto"><table><thead><tr><th>Folio</th><th>Libro</th><th>Solicitud</th><th>Estado</th></tr></thead><tbody>'+(mias.length?mias.map(function(p){return '<tr><td><b>'+ec(p.folio)+'</b></td><td>'+ec(p.titulo)+'</td><td style="font-size:11px">'+ec(p.fSolicitud)+'</td><td><span class="disp '+(p.estado==='Devuelta'?'d':p.estado==='Cancelada'?'p':'r')+'">'+ec(p.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="4" style="text-align:center;color:#64748b;padding:14px">Aún no tienes solicitudes.</td></tr>')+'</tbody></table></div>';}
/* ===== 5. Administración (SOLO personal autorizado) ===== */
function admin(){if(!esBibliotecario()){el('pane').innerHTML='<div class="warn">Acceso reservado al personal autorizado de la Biblioteca.</div>';return;}
 var P=PRE().slice().reverse();
 el('pane').innerHTML='<div class="note">🛠️ Panel del <b>personal autorizado</b>: autoriza/entrega préstamos, registra devoluciones y administra el acervo.</div>'+
  '<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px;margin-bottom:12px"><h3 style="margin:0 0 6px;font-size:14px;color:#0a4d8c">➕ Alta de material al acervo</h3><div class="filters">'+
   '<input id="a_tit" placeholder="Título *"><input id="a_aut" placeholder="Autor"><input id="a_mat" placeholder="Materia"><input id="a_edi" placeholder="Editorial"><input id="a_anio" placeholder="Año"><input id="a_isbn" placeholder="ISBN"><input id="a_clas" placeholder="Clasificación"><select id="a_tipo">'+TIPOS.map(function(x){return '<option>'+ec(x)+'</option>';}).join('')+'</select><input id="a_ubic" placeholder="Ubicación física"><input id="a_ej" type="number" min="1" value="1" placeholder="Ejemplares"><input id="a_kw" placeholder="Palabras clave"></div><textarea id="a_res" placeholder="Resumen" style="width:100%;margin-top:6px;padding:7px;border:1px solid var(--line);border-radius:8px"></textarea><div style="margin-top:6px"><button class="bg" onclick="altaLibro()">Guardar en acervo</button> <span id="a_msg" style="font-size:12px"></span></div></div>'+
  '<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px;overflow:auto"><h3 style="margin:0 0 6px;font-size:14px;color:#0a4d8c">📋 Solicitudes de préstamo</h3><table><thead><tr><th>Folio</th><th>Libro</th><th>Solicitante</th><th>Área</th><th>Estado</th><th>Acciones</th></tr></thead><tbody>'+(P.length?P.map(function(p){return '<tr><td><b>'+ec(p.folio)+'</b></td><td style="font-size:11.5px">'+ec(p.titulo)+'</td><td style="font-size:11.5px">'+ec(p.solicitante)+'</td><td style="font-size:11px">'+ec(p.adscripcion||'—')+'</td><td><span class="disp '+(p.estado==='Devuelta'?'d':p.estado==='Cancelada'?'p':'r')+'">'+ec(p.estado)+'</span></td><td style="white-space:nowrap">'+accionesPre(p)+'</td></tr>';}).join(''):'<tr><td colspan="6" style="text-align:center;color:#64748b;padding:14px">Sin solicitudes.</td></tr>')+'</tbody></table></div>';}
function accionesPre(p){var b='';if(p.estado==='Pendiente')b+='<button class="btn mini bg" onclick="preEstado(\''+p.id+'\',\'Autorizada\')">Autorizar</button> <button class="btn mini bd" onclick="preEstado(\''+p.id+'\',\'Cancelada\')">Cancelar</button>';else if(p.estado==='Autorizada')b+='<button class="btn mini b1" onclick="preEstado(\''+p.id+'\',\'Entregada\')">Entregar</button>';else if(p.estado==='Entregada')b+='<button class="btn mini bg" onclick="preEstado(\''+p.id+'\',\'Devuelta\')">Registrar devolución</button>';else b+='—';return b;}
function preEstado(id,est){if(!esBibliotecario())return;var P=PRE();var p=P.filter(function(x){return x.id===id;})[0];if(!p)return;
 if(est==='Entregada'){p.fEntrega=nowT();}if(est==='Devuelta'){p.fDevol=nowT();}
 p.estado=est;(p.hist=p.hist||[]).push({ts:nowT(),usuario:PERFIL,accion:'Estado → '+est});savePRE(P);blog('Acción','Préstamo '+p.folio+' → '+est);
 try{var N=J('sigej_notificaciones')||[];N.push({id:'NT-'+Date.now().toString(36),ts:nowT(),tipo:'Biblioteca',folio:p.folio,asunto:'Préstamo '+est,para:p.solicitante,rol:'Solicitante',canal:'SIGEJ',mensaje:'Tu solicitud de «'+p.titulo+'» está: '+est,link:'biblioteca_SIGEJ.html',leido:false,origen:'Biblioteca Jurídica'});S('sigej_notificaciones',N);}catch(e){}
 admin();}
function altaLibro(){if(!esBibliotecario())return;var tit=(el('a_tit').value||'').trim();if(!tit){el('a_msg').style.color='#c0392b';el('a_msg').textContent='El título es obligatorio.';return;}
 var A=ACE();A.push({id:'BIB-'+String(A.length+1).padStart(4,'0'),titulo:tit,autor:(el('a_aut').value||'').trim(),materia:(el('a_mat').value||'').trim(),editorial:(el('a_edi').value||'').trim(),anio:(el('a_anio').value||'').trim(),isbn:(el('a_isbn').value||'').trim(),clas:(el('a_clas').value||'').trim(),tipo:el('a_tipo').value,ubic:(el('a_ubic').value||'').trim(),ejemplares:+el('a_ej').value||1,kw:(el('a_kw').value||'').trim(),resumen:(el('a_res').value||'').trim()});saveACE(A);blog('Acción','Alta de material: '+tit);el('a_msg').style.color='#128c4a';el('a_msg').textContent='✓ Guardado.';admin();}
/* init */
drawTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{background:#fff!important}.wrap{padding-top:6px!important}";document.head.appendChild(st);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"biblioteca_SIGEJ.html","w",encoding="utf-8").write(out)
print("biblioteca_SIGEJ.html OK -",len(out),"bytes")
