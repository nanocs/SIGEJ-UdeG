# -*- coding: utf-8 -*-
# MÓDULO: Administración del Conocimiento y Desarrollo Institucional (Unidad de Capacitación, Investigación y Difusión).
# Art. 145 RIAG-UdeG · Dictamen IV/2021/498. Cliente, localStorage, self-contained. Interopera con Oficialía/Transparencia/Buscador.
# Submódulos: I Biblioteca · II Préstamos · III Gestión del Conocimiento · IV Capacitación · V Investigación · VI Difusión · VII Observatorio · VIII Innovación · IX Editorial.
import json, re
B="/Users/edithroque/Documents/CLAUDE/"

# --- Reusar el SNIP canónico (incluye perms + bitácora + UX guía/FAB + guarda sin-guardar + dedup datalist) ---
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Conocimiento y Desarrollo'")
# Conceder acceso a este módulo a perfiles JEFE y ABOG (la unidad responsable es una Jefatura)
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','desarrollo_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="desarrollo_SIGEJ.html" class="act">📚 Conocimiento y Desarrollo</a><a href="normatividad_SIGEJ.html">📖 Normatividad</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="buscador_SIGEJ.html">🔍 Buscador</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a></div>'''

DATA={
 "corte":"2026-06-30",
 "materias":["Constitucional","Administrativo","Laboral","Civil","Mercantil","Penal","Fiscal","Amparo","Internacional","Derechos Humanos","Propiedad Intelectual","Universitario","Electoral","Ambiental","Procesal","Anticorrupción"],
 "idiomas":["Español","Inglés","Francés","Portugués","Alemán","Italiano"],
 "paises":["México","España","Estados Unidos","Argentina","Colombia","Chile","Francia","Alemania","Reino Unido"],
 "editoriales":["Porrúa","Tirant lo Blanch","UNAM-IIJ","UdeG","Fondo de Cultura Económica","Oxford","Bosch","Civitas","Marcial Pons"],
 "estadoFis":["Nuevo","Bueno","Regular","Deteriorado","En reparación","Baja"],
 "tipoAcervo":["Libro físico","eBook","PDF","Revista","Legislación","Jurisprudencia","Manual","Protocolo","Guía","Base de datos"],
 "areas":["Coordinación de lo Contencioso","Coordinación de Enlace con la Red","Coordinación de Normatividad","Unidad de Instrumentos Jurídicos","Unidad de Patrimonio Intangible","Unidad de Asuntos Internacionales","Unidad de Capacitación, Investigación y Difusión","Oficialía de Partes","Área Contable","Área de Personal","Área de Sistemas","Secretaría General","CUCEA","CUCEI","CUCS","CUCSH","CUCBA","CUAAD","CUCEA","Rectoría General","SEMS","Centro Universitario (otro)"],
 "estPrest":["Prestado","Devuelto","Vencido","Renovado","Extraviado","Dañado"],
 "tipoCap":["Curso","Taller","Diplomado","Conferencia","Webinar","Seminario","Actualización jurídica","Capacitación especializada"],
 "modalidad":["Presencial","En línea","Híbrida"],
 "prioridad":["Alta","Media","Baja"],
 "claseCap":["Solicitud de capacitación","Curso programado","Material de repositorio","Aula virtual / grupo"],
 "estCap":["Solicitado","Programado","En curso","Concluido","Cancelado"],
 "tipoConoc":["Opinión jurídica","Dictamen","Investigación","Estudio","Tesis","Protocolo","Criterio","Jurisprudencia","Informe","Manual","Boletín","Presentación","Video","Podcast","Infografía","Curso"],
 "tipoInv":["Línea de investigación","Proyecto","Artículo","Capítulo","Libro","Dictamen","Estudio comparado","Revisión sistemática"],
 "estInv":["En diseño","En desarrollo","En revisión","Publicado","Suspendido"],
 "tipoDif":["Boletín","Newsletter","Podcast","Infografía","Micrositio","Revista","Video","Publicación"],
 "canalDif":["Portal institucional","Redes sociales","Correo masivo","Evento","Prensa"],
 "fuentesObs":["DOF","Congreso de la Unión","Congreso de Jalisco","SCJN","Tribunal Electoral","Corte Interamericana","Legislación estatal","Jurisprudencia"],
 "tipoInnov":["IA / Machine Learning","Automatización documental","Legal Design","Legal Tech","Ciencia de Datos","Visual Law","Chatbot","RPA / Robotic Process"],
 "estInnov":["Idea","Prototipo","Piloto","En producción","Descartado"],
 "tipoEdit":["Libro","Capítulo","Manual","Revista","Boletín","Dictamen"],
 "estEdit":["En dictaminación","En edición","En diseño","En imprenta","Publicado"]
}
DATAJ=json.dumps(DATA,ensure_ascii=False)

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Conocimiento y Desarrollo Institucional</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
/* HDR-UNIF */
header{background:linear-gradient(120deg,#00254a 0%,#0a4d8c 100%);color:#fff;padding:18px 24px}
header h1{margin:0;font-size:20px}header .s{opacity:.85;font-size:12.5px;margin-top:4px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;flex-wrap:wrap;gap:4px;padding:12px 18px 0;max-width:1280px;margin:auto}
.tab{padding:9px 13px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px;color:#334155}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:14px 18px 50px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:18px;min-height:300px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:13px;margin:0 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:10px 0 16px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:23px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.g .n{color:var(--ok)}.kpi.r .n{color:var(--red)}.kpi.y .n{color:var(--amber)}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:12px}
input,select,textarea{font-family:inherit;font-size:13px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;width:100%}
textarea{min-height:60px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:3px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:9px 14px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}
.bw{background:var(--gold);color:#3a2c05;font-weight:700}.mini{padding:6px 10px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px;margin-top:8px}
th{text-align:left;color:var(--mut);font-weight:600;border-bottom:2px solid var(--line);padding:7px 6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:7px 6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.chip{display:inline-block;background:#eef2f7;border:1px solid var(--line);border-radius:12px;padding:2px 9px;font-size:11px;margin:1px}
.bdg{padding:2px 9px;border-radius:11px;font-size:11px;font-weight:700}
.bdg.ok{background:#e6f6ee;color:#15803d}.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.n{background:#eef2f7;color:#475569}
.search{flex:1;min-width:180px}
.collap{border:1px solid var(--line);border-radius:10px;margin-bottom:12px;overflow:hidden}
.collap>.hd{background:#f8fafc;padding:10px 13px;font-weight:700;color:var(--azul);cursor:pointer;font-size:13.5px}
.collap>.bd2{padding:13px;display:none}.collap.open>.bd2{display:block}
.note{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:12px;margin:10px 0}
.ai{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:11px 13px;font-size:12.5px;margin:10px 0}
.drw{position:fixed;top:0;right:-560px;width:540px;max-width:94vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
.empty{color:var(--mut);font-size:13px;padding:18px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:10px}
/* LIGHT-UNIF */
body{background:var(--bg)!important;color:var(--ink)!important}
</style></head><body>
<header><h1>📚 Administración del Conocimiento y Desarrollo Institucional</h1>
<div class="s">Unidad de Capacitación, Investigación y Difusión de la Cultura Jurídica · Art. 145 RIAG-UdeG · Dictamen IV/2021/498 · corte __CORTE__</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<datalist id="dl_materias"></datalist><datalist id="dl_idiomas"></datalist><datalist id="dl_paises"></datalist><datalist id="dl_editoriales"></datalist><datalist id="dl_autores"></datalist><datalist id="dl_libros"></datalist>
<input type="file" id="fileIn" style="display:none">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
const D=__DATA__;const P=localStorage.getItem('sigej_perfil')||'(perfil)';
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function uid(){return 'x'+Math.abs((Date.now()^(performance.now()*1000|0))).toString(36);}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function dr(f){if(!f)return null;return Math.round((new Date(f+'T00:00:00')-new Date(D.corte+'T00:00:00'))/864e5);}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function opt(a,v){return a.map(function(x){return '<option'+(x===v?' selected':'')+'>'+x+'</option>';}).join('');}

/* ---- Configuración de submódulos (campos por captura) ---- */
const SUBS=[
 {k:'panel',ic:'📊',t:'Panel general'},
 {k:'bib',ic:'📚',t:'I · Biblioteca',store:'sigej_biblioteca',badge:'estado',
  fields:[['tipo','Tipo de acervo','sel','tipoAcervo'],['isbn','ISBN / ISSN'],['titulo','Título *'],['subtitulo','Subtítulo'],['autor','Autor','ds','autores'],['coautor','Coautor(es)'],['editorial','Editorial','ds','editoriales'],['anio','Año','num'],['edicion','Edición'],['pais','País','ds','paises'],['idioma','Idioma','ds','idiomas'],['materia','Materia','ds','materias'],['kw','Palabras clave'],['dewey','Clasificación Dewey'],['lc','Clasificación LC'],['inv','N.º de inventario'],['ubic','Ubicación física'],['estante','Estante'],['coleccion','Colección'],['estado','Estado físico','sel','estadoFis']],
  cols:[['titulo','Título'],['autor','Autor'],['materia','Materia'],['tipo','Tipo'],['estado','Estado']]},
 {k:'pre',ic:'🔄',t:'II · Préstamos',store:'sigej_prestamos',badge:'estado',
  fields:[['usuario','Usuario *'],['area','Área / Unidad / Coordinación','sel','areas'],['cargo','Cargo'],['libro','Libro (título)','ds','libros'],['fpres','Fecha del préstamo','date'],['flim','Fecha límite','date'],['fdev','Fecha de devolución','date'],['estado','Estado','sel','estPrest'],['renov','Renovaciones','num'],['multa','Multa interna (MXN)','num'],['obs','Observaciones','ta']],
  cols:[['libro','Libro'],['usuario','Usuario'],['flim','Vence'],['estado','Estado']]},
 {k:'con',ic:'🧠',t:'III · Conocimiento',store:'sigej_conocimiento',badge:null,
  fields:[['tipo','Tipo','sel','tipoConoc'],['titulo','Título *'],['autor','Autor / responsable','ds','autores'],['materia','Materia','ds','materias'],['anio','Año','num'],['kw','Palabras clave / etiquetas'],['resumen','Resumen','ta'],['fuente','Fuente / expediente origen']],
  cols:[['titulo','Título'],['tipo','Tipo'],['materia','Materia'],['anio','Año']]},
 {k:'cap',ic:'🎓',t:'IV · Capacitación',store:'sigej_capacitacion',badge:'estado',
  fields:[['clase','Clase','sel','claseCap'],['tema','Tema *'],['tipo','Tipo','sel','tipoCap'],['dep','Dependencia solicitante','sel','areas'],['part','N.º participantes','num'],['modalidad','Modalidad','sel','modalidad'],['prioridad','Prioridad','sel','prioridad'],['instructor','Instructor'],['fsol','Fecha solicitada','date'],['fprog','Fecha programada','date'],['horas','Horas','num'],['eval','Evaluación promedio (0-100)','num'],['estado','Estado','sel','estCap'],['justif','Justificación','ta']],
  cols:[['tema','Tema'],['clase','Clase'],['dep','Dependencia'],['estado','Estado']]},
 {k:'inv',ic:'🔬',t:'V · Investigación',store:'sigej_invest',badge:'estado',
  fields:[['tipo','Tipo','sel','tipoInv'],['titulo','Título / línea *'],['autor','Autor(es)','ds','autores'],['materia','Materia','ds','materias'],['estado','Estado','sel','estInv'],['fecha','Fecha','date'],['financ','Financiamiento'],['orcid','ORCID'],['pub','Publicación / DOI'],['resumen','Resumen','ta']],
  cols:[['titulo','Título / línea'],['tipo','Tipo'],['autor','Autor'],['estado','Estado']]},
 {k:'dif',ic:'📣',t:'VI · Difusión',store:'sigej_difusion',badge:'estado',
  fields:[['tipo','Tipo','sel','tipoDif'],['titulo','Título *'],['canal','Canal','sel','canalDif'],['fpub','Fecha de difusión','date'],['alcance','Alcance / vistas','num'],['interac','Interacciones','num'],['resp','Responsable'],['estado','Estado','sel','estCap'],['liga','Liga / micrositio'],['obs','Observaciones','ta']],
  cols:[['titulo','Título'],['tipo','Tipo'],['canal','Canal'],['alcance','Alcance']]},
 {k:'obs',ic:'🛰️',t:'VII · Observatorio',store:'sigej_observatorio',badge:'prioridad',
  fields:[['fuente','Fuente','sel','fuentesObs'],['titulo','Asunto / reforma *'],['materia','Materia','ds','materias'],['fecha','Fecha de publicación','date'],['prioridad','Prioridad / impacto','sel','prioridad'],['accion','Acción institucional sugerida','ta'],['liga','Liga oficial'],['resp','Responsable de seguimiento']],
  cols:[['titulo','Asunto'],['fuente','Fuente'],['materia','Materia'],['prioridad','Impacto']]},
 {k:'inno',ic:'💡',t:'VIII · Innovación',store:'sigej_innovacion',badge:'estado',
  fields:[['tipo','Categoría','sel','tipoInnov'],['titulo','Iniciativa *'],['estado','Estado','sel','estInnov'],['resp','Responsable'],['fecha','Fecha','date'],['impacto','Impacto esperado','ta'],['recursos','Recursos / herramientas']],
  cols:[['titulo','Iniciativa'],['tipo','Categoría'],['estado','Estado']]},
 {k:'edi',ic:'📖',t:'IX · Editorial',store:'sigej_editorial',badge:'estado',
  fields:[['tipo','Tipo','sel','tipoEdit'],['titulo','Título *'],['autor','Autor(es)','ds','autores'],['isbn','ISBN'],['doi','DOI'],['derechos','Derechos de autor / licencia'],['estado','Estado','sel','estEdit'],['fecha','Fecha','date'],['tiraje','Tiraje','num'],['obs','Observaciones','ta']],
  cols:[['titulo','Título'],['tipo','Tipo'],['estado','Estado']]}
];
function sub(k){return SUBS.filter(function(s){return s.k===k;})[0];}
let CUR='panel';

/* ---- Tabs ---- */
function buildTabs(){el('tabs').innerHTML=SUBS.map(function(s){return '<div class="tab'+(s.k===CUR?' on':'')+'" onclick="go(\''+s.k+'\')">'+s.ic+' '+s.t+'</div>';}).join('');}
function go(k){CUR=k;buildTabs();render();window.scrollTo(0,0);devFab();}
/* FAB «＋ Nuevo» propio del módulo (las pestañas son dinámicas; abre la captura de la pestaña activa) */
function devFab(){if(/[?&]embed=1/.test(location.search))return;var b=el('devNew');
 if(!b){b=document.createElement('button');b.id='devNew';b.type='button';b.textContent='＋ Nuevo';
  b.style.cssText='position:fixed;left:14px;bottom:56px;z-index:9001;border:none;border-radius:24px;padding:12px 20px;font-size:15px;font-weight:700;background:#1aa39a;color:#fff;cursor:pointer;box-shadow:0 5px 18px rgba(26,163,154,.45)';
  b.onclick=function(){var c=el('cap');if(!c)return;c.classList.add('open');c.scrollIntoView({behavior:'smooth',block:'center'});var f=c.querySelector('input,select,textarea');if(f)setTimeout(function(){try{f.focus();}catch(e){}},420);};
  document.body.appendChild(b);}
 b.style.display=(CUR==='panel')?'none':'block';}

/* ---- datalists ---- */
function fillDL(){
 el('dl_materias').innerHTML=D.materias.map(function(x){return '<option value="'+x+'">';}).join('');
 el('dl_idiomas').innerHTML=D.idiomas.map(function(x){return '<option value="'+x+'">';}).join('');
 el('dl_paises').innerHTML=D.paises.map(function(x){return '<option value="'+x+'">';}).join('');
 el('dl_editoriales').innerHTML=D.editoriales.map(function(x){return '<option value="'+x+'">';}).join('');
 var aut={},lib={};L('sigej_biblioteca').forEach(function(r){if(r.autor)aut[r.autor]=1;if(r.titulo)lib[r.titulo]=1;});
 L('sigej_invest').forEach(function(r){if(r.autor)aut[r.autor]=1;});
 el('dl_autores').innerHTML=Object.keys(aut).map(function(x){return '<option value="'+x+'">';}).join('');
 el('dl_libros').innerHTML=Object.keys(lib).map(function(x){return '<option value="'+x+'">';}).join('');
}

/* ---- Render genérico de submódulo ---- */
function render(){fillDL();if(CUR==='panel')return panel();var s=sub(CUR);var arr=L(s.store);
 var body='<h2 class="h">'+s.ic+' '+s.t.replace(/^[IVX]+ · /,'')+'</h2><p class="lead">Captura, expediente electrónico y búsqueda. Cada registro queda con trazabilidad y aparece en el Buscador / Transparencia General.</p>';
 body+=subKPI(s,arr);
 body+='<div class="collap" id="cap"><div class="hd" onclick="this.parentNode.classList.toggle(\'open\')">＋ Alta / Captura — clic para abrir/cerrar</div><div class="bd2">'+form(s)+'</div></div>';
 body+='<div class="bar"><input class="search" id="q" placeholder="🔎 Buscar en '+s.t.replace(/^[IVX]+ · /,'')+'… (título, autor, materia, palabra clave)" oninput="render()"><button class="bd mini" onclick="expCSV()">⬇️ CSV</button></div>';
 var q=norm(el('q')?el('q').value:'');
 var rows=arr.map(function(r,i){return {r:r,i:i};}).filter(function(o){return !q||norm(JSON.stringify(o.r)).indexOf(q)>=0;});
 body+=specialTop(s,arr);
 body+='<table><tr>'+s.cols.map(function(c){return '<th>'+c[1]+'</th>';}).join('')+'<th></th></tr>'+
  (rows.length?rows.map(function(o){return '<tr class="row" onclick="ficha(\''+s.k+'\','+o.i+')">'+s.cols.map(function(c){return '<td>'+cell(s,o.r,c[0])+'</td>';}).join('')+'<td style="text-align:right;color:#94a3b8">ver ›</td></tr>';}).join(''):'<tr><td colspan="'+(s.cols.length+1)+'" class="empty">Sin registros. Usa «Alta / Captura».</td></tr>')+'</table>';
 el('q')&&(body=body); el('panel').innerHTML=body;var qi=el('q');if(qi){qi.value=q?qi.value:'';}
 aiBox(s,arr);
}
function cell(s,r,k){var v=r[k];if(k===s.badge)return bdg(s,r);if(k==='flim'){var d=dr(v);return esc(v||'—')+(d!==null&&/Prestado|Vencido|Renovado/.test(r.estado||'')?(d<0?' <span class="bdg r">vencido</span>':d<=3?' <span class="bdg y">'+d+'d</span>':''):'');}return esc(v||'—');}
function bdg(s,r){var v=r[s.badge]||'—';var c='n';
 if(/Devuelto|Concluido|Publicado|Vigente|En producción|Bueno|Nuevo|Programado/.test(v))c='ok';
 else if(/Vencido|Extraviado|Dañado|Cancelado|Suspendido|Descartado|Deteriorado|Baja|Alta/.test(v))c=(v==='Alta'?'r':'r');
 else if(/Media|Regular|En curso|En desarrollo|En revisión|Prototipo|Piloto|En edición|En imprenta|Solicitado/.test(v))c='y';
 return '<span class="bdg '+c+'">'+esc(v)+'</span>';}

function form(s){return '<div class="grid">'+s.fields.map(function(f){
 var id='c_'+f[0];var ty=f[2]||'text';
 if(ty==='sel')return '<div class="f"><label>'+f[1]+'</label><select id="'+id+'">'+opt(D[f[3]],'')+'</select></div>';
 if(ty==='ds')return '<div class="f"><label>'+f[1]+'</label><input id="'+id+'" list="dl_'+f[3]+'"></div>';
 if(ty==='ta')return '<div class="f" style="grid-column:1/-1"><label>'+f[1]+'</label><textarea id="'+id+'"></textarea></div>';
 if(ty==='num')return '<div class="f"><label>'+f[1]+'</label><input id="'+id+'" type="number" min="0"></div>';
 if(ty==='date')return '<div class="f"><label>'+f[1]+'</label><input id="'+id+'" type="date"></div>';
 return '<div class="f"><label>'+f[1]+'</label><input id="'+id+'"></div>';
}).join('')+'</div><div style="margin-top:10px"><button class="b3" onclick="guardar(\''+s.k+'\')">＋ Registrar</button> <span id="msg" style="font-size:12px;color:var(--ok)"></span></div>';}

function guardar(k){var s=sub(k);var rec={id:uid(),autor_sis:P,fecha_alta:hoy(),docs:[]};
 var titKey=s.fields[0][0];var titF=s.fields.filter(function(f){return /\*/.test(f[1]);})[0];
 s.fields.forEach(function(f){var e=el('c_'+f[0]);rec[f[0]]=e?(e.value||'').trim():'';});
 var must=titF?titF[0]:null;if(must&&!rec[must]){el('msg').style.color='#c0392b';el('msg').textContent='Falta el campo obligatorio (*).';return;}
 var arr=L(s.store);
 // folio legible
 var pref={bib:'BIB',pre:'PRE',con:'CON',cap:'CAP',inv:'INV',dif:'DIF',obs:'OBS',inno:'INN',edi:'EDI'}[k]||'REG';
 rec.folio=pref+'-'+(new Date().getFullYear())+'-'+String(arr.length+1).padStart(4,'0');
 rec.traza=[{ts:nowS(),accion:'Alta de registro',usuario:P}];
 arr.push(rec);S(s.store,arr);
 if(window.__bitlog)__bitlog('Acción','Alta '+s.t+': '+(rec[titKey]||rec.folio));
 stub(k,rec);
 s.fields.forEach(function(f){var e=el('c_'+f[0]);if(e)e.value='';});
 el('msg').style.color='#1f9d6b';el('msg').textContent='✓ '+rec.folio+' registrado.';render();
}
/* Interoperabilidad: deja antecedente en notificaciones para préstamos por vencer y observatorio prioritario */
function stub(k,rec){try{
 if(k==='obs'&&rec.prioridad==='Alta'){pushNotif('Observatorio jurídico','⚠️ '+rec.titulo+' ('+rec.fuente+') — impacto Alto',rec.folio);}
 if(k==='cap'&&rec.clase==='Solicitud de capacitación'){pushNotif('Capacitación','Nueva solicitud: '+rec.tema+' — '+rec.dep,rec.folio);}
}catch(e){}}
function pushNotif(area,txt,folio){var N=L('sigej_notificaciones');N.push({ts:nowS(),area:area,texto:txt,folio:folio,modulo:'Conocimiento y Desarrollo',leida:false});S('sigej_notificaciones',N);}

/* ---- KPIs por submódulo ---- */
function subKPI(s,arr){var K=[];
 if(s.k==='bib'){var fis=arr.filter(function(r){return r.tipo==='Libro físico';}).length;K=[['',arr.length,'Acervo total',''],['',fis,'Físicos',''],['',arr.length-fis,'Digitales','g'],['',new Set(arr.map(function(r){return r.materia;})).size,'Materias','y']];}
 else if(s.k==='pre'){var venc=arr.filter(function(r){var d=dr(r.flim);return /Prestado|Vencido|Renovado/.test(r.estado)&&d!==null&&d<0;}).length;var prox=arr.filter(function(r){var d=dr(r.flim);return /Prestado|Renovado/.test(r.estado)&&d!==null&&d>=0&&d<=3;}).length;var act=arr.filter(function(r){return /Prestado|Renovado|Vencido/.test(r.estado);}).length;K=[['',act,'Préstamos activos',''],['',venc,'Vencidos','r'],['',prox,'Por vencer (≤3d)','y'],['',arr.filter(function(r){return /Extraviado|Dañado/.test(r.estado);}).length,'Extraviados/dañados','r']];}
 else if(s.k==='cap'){var sol=arr.filter(function(r){return r.clase==='Solicitud de capacitación';}).length;var hrs=arr.reduce(function(a,r){return a+(+r.horas||0);},0);var pa=arr.reduce(function(a,r){return a+(+r.part||0);},0);K=[['',arr.length,'Registros',''],['',sol,'Solicitudes','y'],['',pa,'Participantes','g'],['',hrs,'Horas de capacitación','']];}
 else{K=[['',arr.length,'Registros',''],['',new Set(arr.map(function(r){return r.materia||r.tipo;})).size,'Categorías',''],['',arr.filter(function(r){return /Publicado|Concluido|En producción|Vigente/.test(r.estado||'');}).length,'Concluidos/publicados','g']];}
 return '<div class="kpis">'+K.map(function(k){return '<div class="kpi '+k[3]+'"><div class="n">'+k[1]+'</div><div class="l">'+k[2]+'</div></div>';}).join('')+'</div>';}

/* ---- Encabezados especiales (alertas préstamos) ---- */
function specialTop(s,arr){if(s.k!=='pre')return '';
 var al=arr.filter(function(r){var d=dr(r.flim);return /Prestado|Renovado|Vencido/.test(r.estado)&&d!==null&&d<=3;});
 if(!al.length)return '';
 return '<div class="note">⏰ <b>Alertas de préstamo:</b> '+al.map(function(r){var d=dr(r.flim);return esc(r.libro)+' ('+esc(r.usuario)+') '+(d<0?'<b>vencido '+(-d)+'d</b>':'vence en '+d+'d');}).join(' · ')+'</div>';}

/* ---- Asistente IA (heurístico, honesto) ---- */
function aiBox(s,arr){var box=document.createElement('div');box.className='ai';var msg='';
 if(s.k==='bib'){var m={};arr.forEach(function(r){if(r.materia)m[r.materia]=(m[r.materia]||0)+1;});var top=Object.keys(m).sort(function(a,b){return m[b]-m[a];})[0];msg='🤖 <b>Recomendación (heurística):</b> '+(top?('la materia con más acervo es <b>'+top+'</b>; el motor sugeriría bibliografía relacionada por coincidencia de materia/palabras clave.'):'captura acervo para generar recomendaciones.');}
 else if(s.k==='pre'){var v=arr.filter(function(r){var d=dr(r.flim);return /Prestado|Renovado|Vencido/.test(r.estado)&&d!==null&&d<0;}).length;msg='🤖 <b>Detección:</b> '+v+' préstamo(s) vencido(s) → el motor generaría recordatorios automáticos al usuario y a su área.';}
 else if(s.k==='cap'){var t={};arr.forEach(function(r){if(r.tema)t[r.tema]=(t[r.tema]||0)+1;});var top=Object.keys(t).sort(function(a,b){return t[b]-t[a];})[0];msg='🤖 <b>Necesidades de capacitación:</b> el tema más solicitado es <b>'+(top||'—')+'</b>; con histórico el motor propondría rutas de aprendizaje y calendario.';}
 else{msg='🤖 <b>IA (fase backend):</b> recomendación de contenidos, resúmenes automáticos y detección de tendencias se generarán con el motor semántico del servidor; aquí se aplican reglas básicas sobre los datos capturados.';}
 box.innerHTML=msg+' <span style="opacity:.7">— El OCR de imagen/PDF y la búsqueda semántica/IA real son fase backend.</span>';el('panel').appendChild(box);}

/* ---- Ficha / drawer con todos los campos + expediente + OCR ---- */
function ficha(k,i){var s=sub(k);var arr=L(s.store);var r=arr[i];if(!r)return;
 var det=s.fields.map(function(f){var v=r[f[0]];return v?('<b>'+f[1].replace(' *','')+':</b> '+esc(v)):null;}).filter(Boolean).join('<br>');
 var qr=(r.inv||r.folio||'')?'<img src="https://api.qrserver.com/v1/create-qr-code/?size=88x88&data='+encodeURIComponent((r.folio||'')+'|'+(r.inv||r.titulo||''))+'" style="width:88px;height:88px" onerror="this.style.display=\'none\'">':'';
 var docs=(r.docs||[]).length?(r.docs||[]).map(function(d,j){return '<div style="font-size:11.5px">📎 '+esc(d.cat||'Doc')+' · '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b;font-size:12px">Sin archivos.</span>';
 var tz=(r.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 var extra='';
 if(k==='pre')extra='<div style="margin-top:8px;display:flex;gap:6px;flex-wrap:wrap"><button class="bd mini" onclick="prestAcc(\''+r.id+'\',\'Renovado\')">🔁 Renovar</button><button class="b3 mini" onclick="prestAcc(\''+r.id+'\',\'Devuelto\')">✔ Devolver</button><button class="bd mini" style="background:#5a2330;color:#fff" onclick="prestAcc(\''+r.id+'\',\'Extraviado\')">⚠ Extraviado</button></div>';
 if(k==='cap'&&/Curso|Concluido|En curso/.test(r.estado))extra='<div style="margin-top:8px"><button class="bw mini" onclick="constancia(\''+r.id+'\')">📄 Constancia (Word)</button></div>';
 el('drwBody').innerHTML='<h2 style="margin:0 0 4px;color:#0a4d8c">'+esc(r.folio||'')+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+s.ic+' '+s.t+' · alta '+esc(r.fecha_alta||'')+' · '+esc(r.autor_sis||'')+'</div>'+
  '<div class="comp" style="display:flex;gap:12px;align-items:flex-start"><div style="flex:1">'+det+'</div>'+qr+'</div>'+
  extra+
  '<div class="comp"><b>📎 Expediente electrónico</b> <button class="bd mini" onclick="adj(\''+k+'\',\''+r.id+'\')">Adjuntar archivo</button> <button class="bw mini" onclick="ocr(\''+k+'\',\''+r.id+'\')">🔎 OCR / extraer datos</button><div style="margin-top:6px">'+docs+'</div></div>'+
  '<div class="comp"><b>🧾 Trazabilidad</b><div style="margin-top:5px">'+tz+'</div></div>'+
  '<div style="margin-top:10px"><button class="bd" onclick="closeDrw()">Cerrar</button> <button class="bd" style="background:#fdeaea;color:#c0392b" onclick="elimina(\''+k+'\',\''+r.id+'\')">🗑 Eliminar</button></div>';
 el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
function recById(store,id){var a=L(store);for(var i=0;i<a.length;i++)if(a[i].id===id)return {a:a,i:i,r:a[i]};return null;}
function prestAcc(id,estado){var o=recById('sigej_prestamos',id);if(!o)return;o.r.estado=estado;if(estado==='Devuelto')o.r.fdev=hoy();if(estado==='Renovado')o.r.renov=(+o.r.renov||0)+1;o.r.traza=o.r.traza||[];o.r.traza.push({ts:nowS(),accion:'Préstamo → '+estado,usuario:P});S('sigej_prestamos',o.a);if(window.__bitlog)__bitlog('Acción','Préstamo '+o.r.libro+' → '+estado);closeDrw();render();}
function elimina(k,id){if(!confirm('¿Eliminar este registro? Queda constancia en la bitácora a nombre de '+P+'.'))return;var s=sub(k);var a=L(s.store).filter(function(x){return x.id!==id;});S(s.store,a);if(window.__bitlog)__bitlog('Acción','Eliminó registro de '+s.t);closeDrw();render();}

/* ---- Expediente: adjuntar + OCR heurístico ---- */
let _AT=null;
function adj(k,id){_AT={k:k,id:id};el('fileIn').value='';el('fileIn').click();}
el('fileIn').onchange=function(){var f=this.files[0];if(!f||!_AT)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var s=sub(_AT.k);var o=recById(s.store,_AT.id);var rd=new FileReader();rd.onload=function(){o.r.docs=o.r.docs||[];o.r.docs.push({nombre:f.name,tipo:f.type,cat:'Documento',data:rd.result,fecha:hoy(),por:P});o.r.traza.push({ts:nowS(),accion:'Adjuntó '+f.name,usuario:P});S(s.store,o.a);ficha(_AT.k,o.i);};rd.readAsDataURL(f);};
function ocr(k,id){var s=sub(k);var o=recById(s.store,id);if(!o)return;var txt=prompt('Pega el TEXTO del documento (OCR de imagen real = fase backend). Se extraen ISBN/año/materia y se llena el primer campo vacío:');if(txt==null)return;
 var isbn=(txt.match(/\b97[89][\d\- ]{9,16}\b/)||[])[0];var anio=(txt.match(/\b(19|20)\d{2}\b/)||[])[0];
 var mat=D.materias.filter(function(m){return norm(txt).indexOf(norm(m))>=0;})[0];
 if(isbn&&!o.r.isbn)o.r.isbn=isbn.replace(/\s/g,'');if(anio&&!o.r.anio)o.r.anio=anio;if(mat&&!o.r.materia)o.r.materia=mat;
 var filled=[];['titulo','tema','resumen','obj','accion','impacto'].some(function(c){if(s.fields.some(function(f){return f[0]===c;})&&!o.r[c]){o.r[c]=txt.split(/\n|\. /)[0].slice(0,120);filled.push(c);return true;}return false;});
 o.r.docs=o.r.docs||[];o.r.docs.push({nombre:'OCR_'+(o.r.folio||'')+'.txt',tipo:'text/plain',cat:'OCR / extracción',data:'data:text/plain;base64,'+btoa(unescape(encodeURIComponent(txt.slice(0,4000)))),fecha:hoy(),por:P});
 o.r.traza.push({ts:nowS(),accion:'OCR/extracción (reglas)',usuario:P});S(s.store,o.a);
 alert('Extracción por reglas: '+[isbn?'ISBN':'',anio?'año':'',mat?'materia':'',filled.length?'campo '+filled[0]:''].filter(Boolean).join(', ')+'. OCR de imagen real = fase backend.');ficha(k,o.i);}

/* ---- Constancia de capacitación (Word) ---- */
function constancia(id){var o=recById('sigej_capacitacion',id);if(!o)return;var r=o.r;
 var html='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria"><div style="text-align:center"><h2>UNIVERSIDAD DE GUADALAJARA</h2><h3>Oficina de la Abogacía General</h3><p>Unidad de Capacitación, Investigación y Difusión de la Cultura Jurídica</p><h2>CONSTANCIA</h2><p>otorga la presente a las dependencias y personas participantes en</p><h3>'+esc(r.tema)+'</h3><p>'+esc(r.tipo||'')+' · '+esc(r.modalidad||'')+' · '+(r.horas||0)+' horas</p><p>Dependencia: '+esc(r.dep||'')+' · Instructor: '+esc(r.instructor||'')+'</p><p>Folio: '+esc(r.folio)+' · '+esc(r.fprog||r.fsol||hoy())+'</p></div></body></html>';
 var b=new Blob(['﻿'+html],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='Constancia_'+r.folio+'.doc';a.click();}

/* ---- CSV export ---- */
function expCSV(){var s=sub(CUR);if(!s.store)return;var arr=L(s.store);if(!arr.length){alert('Sin datos.');return;}
 var cols=s.fields.map(function(f){return f[0];});var head=['folio'].concat(cols);
 var rows=arr.map(function(r){return head.map(function(c){return '"'+String(r[c]==null?'':r[c]).replace(/"/g,'""')+'"';}).join(',');});
 var csv=head.join(',')+'\n'+rows.join('\n');var b=new Blob(['﻿'+csv],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=s.k+'_'+hoy()+'.csv';a.click();}

/* ---- Panel general ---- */
function panel(){var c={};SUBS.forEach(function(s){if(s.store)c[s.k]=L(s.store).length;});
 var totalAcervo=c.bib||0;var prest=L('sigej_prestamos');var venc=prest.filter(function(r){var d=dr(r.flim);return /Prestado|Renovado|Vencido/.test(r.estado)&&d!==null&&d<0;}).length;
 var hrs=L('sigej_capacitacion').reduce(function(a,r){return a+(+r.horas||0);},0);
 var html='<h2 class="h">📊 Panel general — Conocimiento y Desarrollo</h2><p class="lead">Visión integral de los nueve submódulos. Equivalente funcional (prototipo) a Koha/Alma/Moodle/Power BI; las integraciones externas (Teams, Moodle, Zotero, ORCID, DOF) y la IA semántica son fase backend.</p>';
 html+='<div class="kpis">'+
  kpi(totalAcervo,'Acervo bibliográfico','')+kpi((c.con||0),'Activos de conocimiento','')+kpi((c.cap||0),'Capacitación','y')+kpi(hrs,'Horas de capacitación','g')+
  kpi((c.inv||0),'Investigaciones','')+kpi((c.dif||0),'Productos de difusión','')+kpi((c.obs||0),'Alertas observatorio','y')+kpi(venc,'Préstamos vencidos','r')+
  '</div>';
 html+='<div class="grid" style="grid-template-columns:1fr 1fr"><div class="comp"><b>Acervo por materia</b><canvas id="ch1" height="150"></canvas></div><div class="comp"><b>Registros por submódulo</b><canvas id="ch2" height="150"></canvas></div></div>';
 html+='<div class="ai">🤖 <b>Resumen ejecutivo (heurístico):</b> '+totalAcervo+' títulos en biblioteca, '+(c.cap||0)+' acciones de capacitación ('+hrs+' h), '+venc+' préstamo(s) vencido(s). El motor de IA generaría boletines automáticos, rutas de aprendizaje y detección de tendencias jurídicas a partir de estos datos.</div>';
 el('panel').innerHTML=html;
 try{var m={};L('sigej_biblioteca').forEach(function(r){if(r.materia)m[r.materia]=(m[r.materia]||0)+1;});
  new Chart(el('ch1'),{type:'doughnut',data:{labels:Object.keys(m),datasets:[{data:Object.values(m),backgroundColor:['#0a4d8c','#1aa39a','#d4a32c','#1f9d6b','#c0392b','#7c8ba1','#e08e0b','#5b8def','#8e6fd4']}]},options:{plugins:{legend:{position:'right',labels:{font:{size:9}}}}}});
  new Chart(el('ch2'),{type:'bar',data:{labels:SUBS.filter(function(s){return s.store;}).map(function(s){return s.t.replace(/^[IVX]+ · /,'');}),datasets:[{data:SUBS.filter(function(s){return s.store;}).map(function(s){return L(s.store).length;}),backgroundColor:'#0a4d8c'}]},options:{plugins:{legend:{display:false}},scales:{x:{ticks:{font:{size:8}}}}}});
 }catch(e){}
}
function kpi(n,l,c){return '<div class="kpi '+(c||'')+'"><div class="n">'+n+'</div><div class="l">'+l+'</div></div>';}

buildTabs();render();setTimeout(devFab,120);
</script>
__SNIP__
</body></html>"""

out=TPL.replace("__DATA__",DATAJ).replace("__NAV__",NAV).replace("__SNIP__",SNIP).replace("__CORTE__",DATA["corte"])
open(B+"desarrollo_SIGEJ.html","w",encoding="utf-8").write(out)
print("desarrollo_SIGEJ.html OK -",len(out),"bytes")
