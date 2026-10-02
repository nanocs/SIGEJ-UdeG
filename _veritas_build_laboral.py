# -*- coding: utf-8 -*-
# SUBMÓDULO DE PERMISOS, LICENCIAS, INCIDENCIAS Y DESCANSOS — Compliance by Design (CCT Personal Administrativo UdeG / SUTUdeG).
# Motor de Reglas del Contrato Colectivo (BRE) parametrizable, administrado por RH / Oficina de la Abogacía General.
# IMPORTANTE (regla de responsabilidad): el sistema NO presume articulado; el fundamento (cláusula del CCT) lo captura RH/Abogacía en el
# editor del Motor de Reglas. Solo se sembraron como referencia las cláusulas que la usuaria citó expresamente (34 y 59, estímulo por puntualidad).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Permisos, Licencias e Incidencias'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','laboral_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="laboral_SIGEJ.html" class="act">🧑‍⚖️ Permisos y Licencias</a><a href="operativo_SIGEJ.html">🧰 Módulo Operativo</a><a href="administracion_SIGEJ.html">🗂️ Administración</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="cumplimiento_SIGEJ.html">⚖️ Cumplimiento</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Permisos, Licencias, Incidencias y Descansos</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:15px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.14);color:#fff}
.tabs{display:flex;gap:5px;flex-wrap:wrap;padding:12px 18px 0;max-width:1340px;margin:auto}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px}
.tab.on{background:#0a4d8c;color:#fff;font-weight:700}
.wrap{max-width:1340px;margin:auto;padding:14px 18px 46px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:12px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px}
.kpi .n{font-size:22px;font-weight:800;color:var(--azul2)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.card h3{margin:0 0 8px;font-size:14px;color:var(--azul)}
.grid{display:grid;gap:8px}
label.lb{font-size:11px;color:#64748b;display:block;margin-bottom:2px;font-weight:600}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:8px;border:1px solid var(--line);border-radius:8px;background:#fff}
textarea{min-height:46px;resize:vertical}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:12.5px;padding:8px 12px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.bo{background:var(--amber);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.bg{background:var(--ok);color:#fff;font-weight:700}.br{background:var(--red);color:#fff;font-weight:700}.mini{padding:5px 9px;font-size:11.5px}
table{width:100%;border-collapse:collapse;font-size:12px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:7px 6px;vertical-align:top}
.st{padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;white-space:nowrap}
.st.b{background:#eef6ff;color:#0a4d8c}.st.y{background:#fef3e2;color:#b45309}.st.v{background:#e7f7ee;color:#128c4a}.st.r{background:#fdeaea;color:#c0392b}.st.g{background:#f1f5f9;color:#475569}
.dict{border:1px solid var(--line);border-left:4px solid var(--azul2);border-radius:8px;padding:10px 12px;font-size:12px;background:#f8fbff;margin-top:8px}
.dict.ok{border-left-color:#1f9d6b;background:#f2fbf6}.dict.no{border-left-color:#c0392b;background:#fdf5f4}
.ficha{border:1px solid #cfe0f5;border-radius:9px;padding:10px 12px;font-size:12px;background:#eef6ff;margin-top:6px;line-height:1.6}
.chk{font-size:12px;margin:2px 0}.chk .ico{font-weight:800}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.warn{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.drawer{position:fixed;inset:0;background:rgba(8,20,38,.5);display:none;z-index:9000}.drawer.on{display:block}
.panel{position:absolute;top:0;right:0;width:620px;max-width:96vw;height:100%;background:#fff;overflow:auto;padding:18px 20px;box-shadow:-8px 0 30px rgba(0,0,0,.3)}
.panel .x{position:absolute;top:12px;right:16px;cursor:pointer;font-size:18px;color:#64748b}
.tl{border-left:2px solid #cbd5e1;margin-left:6px;padding-left:14px}.tl .ev{position:relative;padding:6px 0;font-size:12px}.tl .ev:before{content:'';position:absolute;left:-21px;top:10px;width:9px;height:9px;border-radius:50%;background:#0a4d8c}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
</style></head><body>
<header><h1>🧑‍⚖️ Permisos, Licencias, Incidencias y Descansos</h1><div class="s">Compliance by Design · Contrato Colectivo de Trabajo (Personal Administrativo UdeG) · Motor de Reglas parametrizable</div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div id="pane"></div></div>
<div class="drawer" id="drw"><div class="panel"><span class="x" onclick="closeDrw()">✕</span><div id="drwc"></div></div></div>
<footer>Oficina de la Abogacía General · Coordinación con Recursos Humanos · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function S(k,v){localStorage.setItem(k,JSON.stringify(v));}
function ec(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function nowT(){return new Date().toISOString().slice(0,16).replace('T',' ');}
function nowFull(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function today(){return new Date().toISOString().slice(0,10);}
var PERFIL=localStorage.getItem('sigej_perfil')||'(perfil)';
var SES=J('sigej_sesion')||{};
/* Roles administradores (RH / Abogacía / jefe): autorizan y administran el BRE */
var RH=['Administrador','Sistemas','Jefe del Área de Personal','Coordinador Jurídico','Abogado General','Coordinador de Enlace con la Red'];
function esRH(){return RH.indexOf(PERFIL)>=0;}
var BREADMIN=['Administrador','Sistemas','Jefe del Área de Personal','Coordinador Jurídico','Abogado General','Coordinador de Normatividad'];
function esBREadmin(){return BREADMIN.indexOf(PERFIL)>=0;}
function blog(t,a){try{var L=J('sigej_bitacora')||[];L.push({ts:nowFull(),perfil:PERFIL,modulo:'Permisos y Licencias',tipo:t,accion:String(a||'').slice(0,90)});if(L.length>3000)L=L.slice(-3000);S('sigej_bitacora',L);}catch(e){}if(window.__bitlog){try{window.__bitlog(t,a);}catch(e){}}}
/* datos del trabajador (de la sesión / IAM); antigüedad y nombramiento parametrizables */
function trabajador(){var U=J('sigej_usuarios');var u=null;if(SES.code&&Array.isArray(U)){for(var i=0;i<U.length;i++){if(String(U[i].numEmp||'').toLowerCase()===String(SES.code).toLowerCase())u=U[i];}}
 return {nombre:(u&&u.nombre)||SES.nombre||PERFIL,numEmp:(u&&u.numEmp)||SES.code||'',adscripcion:(u&&(u.unidad||u.coord))||localStorage.getItem('sigej_op_adscr')||'',antiguedadMeses:+(localStorage.getItem('sigej_lab_antig')||36),nombramiento:localStorage.getItem('sigej_lab_nombra')||'Administrativo de base'};}
/* ===== MOTOR DE REGLAS (BRE) — catálogo parametrizable ===== */
/* fundamento 'por capturar' salvo el que la usuaria citó (cláusulas 34 y 59, puntualidad). NO se inventa articulado. */
var NOMBRAM=['Administrativo de base','Administrativo de confianza','Interinato','Contrato por obra','Todos'];
function seedBRE(){if(localStorage.getItem('sigej_bre_ver')==='cct2024v1')return;var R=[
 mk('001','Permiso por fallecimiento de familiar',4,'habiles',0,'Cláusula 65 CCT 2024-2026 (permisos por motivos familiares y civiles, con goce de sueldo íntegro): fallecimiento de familiar directo —padres, hijos o cónyuge—, 4 días hábiles.',['Constancia de defunción'],'Jefe inmediato / RH','Familiar directo (padres, hijos o cónyuge). Solicitud por escrito con al menos 4 días hábiles de anticipación, salvo deceso imprevisto.',true,true,['incapacidad']),
 mk('002','Permiso por matrimonio',8,'habiles',0,'Cláusula 65 CCT 2024-2026: matrimonio civil, 8 días hábiles con goce de sueldo; vigencia de un año a partir de la fecha del matrimonio.',['Constancia/acta de matrimonio'],'RH','Vigencia de 1 año desde el matrimonio. Solicitud por escrito con al menos 4 días hábiles de anticipación.',true,true,[]),
 mk('003','Permiso económico',29,'dias',0,'Cláusula 65, fracción VI, CCT 2024-2026: permiso económico (sin goce de sueldo), hasta por 29 días, previa autorización del titular de la dependencia.',[],'Titular de la dependencia','Hasta 29 días; SIN goce de sueldo; autoriza el titular de la dependencia.',false,true,['incapacidad']),
 mk('004','Licencia sin goce de sueldo',0,'dias',12,'Cláusula 65, fracción IX, CCT 2024-2026: licencia por motivos personales (sin goce), de 1 mes hasta 1 año; requiere antigüedad mayor a un año; se solicita al Rector General con al menos 2 semanas de anticipación (respuesta en máximo 15 días hábiles).',['Solicitud fundada dirigida al Rector General'],'Rector General','De 1 mes a 1 año; antigüedad mayor a 1 año; solicitar con 2 semanas de anticipación; sin goce de sueldo.',false,true,['permiso_economico']),
 mk('005','Descanso por puntualidad',1,'dias',0,'Cláusula 34 CCT 2024-2026 (estímulo por puntualidad): 1 día de descanso por mes calendario laborado sin usar tolerancias; se disfruta en el mes inmediato siguiente, notificando por escrito al superior con al menos 3 días hábiles de anticipación.',[],'Jefe inmediato','Sin usar tolerancias en el mes; disfrute en el mes siguiente; aviso por escrito con 3 días hábiles de anticipación.',true,true,['incapacidad']),
 mk('006','Compensación por guardias',0,'dias',0,'Cláusula por capturar (CCT) — compensación por guardias en periodo vacacional. RH/Abogacía debe capturar el fundamento.',['Oficio de designación'],'RH','Por capturar conforme al CCT.',true,false,[]),
 mk('007','Permiso sindical',0,'dias',0,'Cláusula por capturar (CCT) — permiso sindical. RH/Abogacía debe capturar el fundamento.',['Oficio del sindicato'],'RH','Por capturar conforme al CCT.',true,false,['licencia_medica']),
 mk('008','Incapacidad (IMSS)',0,'naturales',0,'Cláusula 65-I CCT 2024-2026 / Ley del Seguro Social: incapacidad médica según determine el IMSS (días naturales); dar aviso a más tardar el día hábil siguiente y entregar el certificado del IMSS en máximo 3 días.',['Certificado de incapacidad del IMSS'],'RH','Aviso a más tardar el día hábil siguiente; certificado del IMSS en máximo 3 días.',true,true,['permiso_economico','descanso_puntualidad']),
 mk('009','Permiso de paternidad',20,'habiles',0,'Cláusula 65 CCT 2024-2026: paternidad (nacimiento o adopción), 20 días hábiles; no acumulable a vacaciones ni genera suplencia.',['Acta de nacimiento / resolución de adopción'],'RH','No acumulable a vacaciones ni genera suplencia.',true,true,[]),
 mk('010','Permiso de maternidad',90,'naturales',0,'Cláusula 66 CCT 2024-2026: maternidad, 90 días naturales; solicitud por escrito al jefe inmediato con copia a Recursos Humanos, adjuntando certificado médico oficial.',['Certificado médico oficial'],'RH','Solicitud por escrito con copia a Recursos Humanos.',true,true,[]),
 mk('011','Lactancia',0,'dias',0,'Cláusula 88-XV CCT 2024-2026: lactancia, dos periodos de 30 minutos diarios durante los primeros 6 meses de edad del menor, a elección de la trabajadora.',[],'RH / Jefe inmediato','Dos periodos de 30 minutos diarios durante los primeros 6 meses.',true,true,[]),
 mk('012','Consulta médica IMSS',0,'dias',0,'Cláusula 88-XIV CCT 2024-2026: consultas médicas, permiso por el tiempo de la jornada para asistir al IMSS; se comprueba con la constancia correspondiente.',['Constancia / pase del IMSS'],'Jefe inmediato','Comprobar con la constancia del IMSS.',true,true,[]),
 mk('013','Enfermedad de hijo menor',3,'habiles',0,'Cláusula 65 CCT 2024-2026: enfermedad de hijos menores, 3 días hábiles; requiere constancia médica que lo justifique.',['Constancia médica'],'Jefe inmediato / RH','Cuando sea necesaria la atención/cuidado del menor.',true,true,[]),
 mk('014','Cirugía de familiar',5,'habiles',0,'Cláusula 65 CCT 2024-2026: cirugía de familiar directo (padres, hijos o cónyuge), 5 días hábiles; constancia médica; no acumulable a vacaciones.',['Constancia médica'],'RH','Familiar directo; no acumulable a vacaciones.',true,true,[]),
 mk('015','Adaptación en guardería',3,'habiles',0,'Cláusula 65 CCT 2024-2026: adaptación en guarderías, 3 días hábiles para el periodo de adaptación del menor.',[],'Jefe inmediato','Para el periodo de adaptación del menor.',true,true,[]),
 mk('016','Licencia académica',0,'dias',36,'Cláusula 44 CCT 2024-2026 (licencias para estudios): licencia con goce de sueldo para posgrados escolarizados (máximo 30 autorizaciones); personal con más de 3 años de antigüedad; entregar constancia de calificaciones en término no mayor a 30 días tras iniciar el ciclo.',['Constancia de inscripción / calificaciones'],'RH / Abogado General','Antigüedad mayor a 3 años; máximo 30 autorizaciones; constancia de calificaciones en 30 días.',true,true,[]),
 mk('017','Descarga horaria',0,'dias',36,'Cláusula 44 CCT 2024-2026 (licencias para estudios): descarga horaria de hasta el 50% de la jornada para licenciatura o posgrado; personal con más de 3 años de antigüedad; presentar trámite ante el Sindicato y acreditar ser alumno regular.',['Trámite ante el Sindicato','Constancia de alumno regular'],'RH','Antigüedad mayor a 3 años; hasta 50% de la jornada; alumno regular.',true,true,[]),
 mk('018','Licencia prolongada',0,'dias',0,'Cláusula por capturar (CCT) — licencia prolongada. RH/Abogacía debe capturar el fundamento.',['Solicitud fundada'],'RH / Abogado General','Por capturar conforme al CCT.',true,false,[])
];S('sigej_bre_reglas',R);localStorage.setItem('sigej_bre_ver','cct2024v1');}
function mk(num,tipo,dias,base,antig,fund,docs,autoridad,restric,goce,verif,incompat){return {id:'BRE-'+num,num:'Regla '+num,tipo:tipo,key:norm(tipo),fundamento:fund,dias:dias,base:base,antiguedad:antig,nombramientos:['Todos'],docs:docs||[],incompat:incompat||[],autoridad:autoridad||'RH',vigencia:'CCT 2024-2026',restricciones:restric||'',goceSueldo:goce!==false,acumula:false,estado:'Vigente',version:1,fEntrada:'2024',fConclusion:'',verif:{ok:!!verif,fuente:'CCT Personal Administrativo UdeG 2024-2026 (documento proporcionado)'},hist:[{version:1,fecha:today(),usuario:'seed',fundamento:fund,nota:verif?'Cláusula del CCT (verificada del documento)':'Alta inicial (parametrizar con el CCT)'}],activo:true};}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,'_').replace(/^_|_$/g,'');}
seedBRE();
function BRE(){return J('sigej_bre_reglas')||[];}
function reglaDe(tipo){var R=BRE();for(var i=0;i<R.length;i++){if(R[i].tipo===tipo&&R[i].estado==='Vigente'&&R[i].activo!==false)return R[i];}return null;}
/* ===== Motor de evaluación (árbol de decisiones) → dictamen motivado ===== */
function evaluar(sol){var r=reglaDe(sol.tipo);var pasos=[];function chk(ok,label){pasos.push({ok:!!ok,label:label});return !!ok;}
 var t=sol.trabajador||{};var faltan=[];
 if(!r){return {cumple:false,reglaId:null,pasos:[{ok:false,label:'No existe regla vigente para «'+sol.tipo+'» en el Motor de Reglas'}],faltantes:['Regla no configurada'],fundamento:'—'};}
 chk(true,'Relación laboral vigente (nombramiento '+(t.nombramiento||'—')+')');
 var nomOk=r.nombramientos.indexOf('Todos')>=0||r.nombramientos.indexOf(t.nombramiento)>=0;chk(nomOk,'Tipo de nombramiento aplicable');if(!nomOk)faltan.push('Nombramiento no aplicable');
 var antOk=(t.antiguedadMeses||0)>=(r.antiguedad||0);chk(antOk,'Antigüedad requerida ('+(r.antiguedad||0)+' meses; tiene '+(t.antiguedadMeses||0)+')');if(!antOk)faltan.push('Antigüedad insuficiente');
 var docsOk=(r.docs||[]).every(function(d){return (sol.docs||[]).some(function(x){return x.docReq===d||norm(x.nombre).indexOf(norm(d).slice(0,6))>=0;})||(sol.docsDeclarados||[]).indexOf(d)>=0;});chk(docsOk||!(r.docs||[]).length,'Documentación obligatoria'+((r.docs||[]).length?' ('+r.docs.join(', ')+')':' — no requiere'));if(!docsOk&&(r.docs||[]).length)faltan.push('Faltan documentos: '+r.docs.join(', '));
 var diasOk=!r.dias||!sol.dias||sol.dias<=r.dias;chk(diasOk,'Días dentro del máximo del CCT'+(r.dias?' ('+r.dias+' '+r.base+')':' — parametrizar'));if(!diasOk)faltan.push('Excede los días autorizados ('+r.dias+')');
 /* incompatibilidades: otra solicitud activa incompatible en el periodo */
 var activas=(J('sigej_laboral_solicitudes')||[]).filter(function(s){return s.id!==sol.id&&(s.trabajador||{}).numEmp===t.numEmp&&['Autorizada','En RH','En jefe','Enviada'].indexOf(s.estado)>=0;});
 var incompat=activas.filter(function(s){return (r.incompat||[]).indexOf(norm(s.tipo))>=0;});
 chk(incompat.length===0,'Sin incompatibilidades vigentes'+(incompat.length?' (choca con: '+incompat.map(function(s){return s.tipo;}).join(', ')+')':''));if(incompat.length)faltan.push('Incompatibilidad con: '+incompat.map(function(s){return s.tipo;}).join(', '));
 var cumple=faltan.length===0;
 var texto=(cumple?'PROCEDE':'NO PROCEDE')+' la solicitud de «'+sol.tipo+'» conforme al Motor de Reglas del CCT. Fundamento: '+r.fundamento+'. '+(cumple?'Se cumplen los requisitos; continúa el flujo de autorización.':'Requisitos no satisfechos: '+faltan.join('; ')+'.');
 return {cumple:cumple,reglaId:r.id,reglaNum:r.num,pasos:pasos,faltantes:faltan,fundamento:r.fundamento,autoridad:r.autoridad,texto:texto};}
/* ===== TABS ===== */
function tabsList(){var t=[['t1','📝 Solicitar (trabajador)'],['t2','📋 Mis solicitudes'],['t5','📅 Calendario Vacacional']];
 if(esRH())t.splice(2,0,['t3','✅ Autorización (RH/Jefe)']);
 t.push(['t6','⭐ Estímulo por puntualidad']);
 if(esBREadmin())t.push(['t4','⚖️ Motor de Reglas (BRE)']);
 if(esRH())t.push(['t7','📊 Panel ejecutivo']);
 return t;}
var cur='t1';
function drawTabs(){el('tabs').innerHTML=tabsList().map(function(t){return '<button class="tab'+(t[0]===cur?' on':'')+'" onclick="go(\''+t[0]+'\')">'+t[1]+'</button>';}).join('');}
function go(id){cur=id;drawTabs();render();window.scrollTo(0,0);}
function render(){if(cur==='t1')solicitar();else if(cur==='t2')mis();else if(cur==='t3')autoriza();else if(cur==='t4')bre();else if(cur==='t5')calendario();else if(cur==='t6')puntualidad();else if(cur==='t7')panel();}
function SOL(){return J('sigej_laboral_solicitudes')||[];}
function saveSOL(a){S('sigej_laboral_solicitudes',a);}
/* ===== 1. SOLICITAR (trabajador) — ficha jurídica + validación BRE previa ===== */
var selTipo='';var curDocs=[];
function solicitar(){var R=BRE().filter(function(x){return x.estado==='Vigente'&&x.activo!==false;});
 el('pane').innerHTML='<div class="note">El trabajador <b>solo genera</b> solicitudes; nunca las aprueba. Antes de enviar, el <b>Motor de Reglas</b> muestra la ficha jurídica y valida el cumplimiento; si no procede, <b>impide el envío</b>. Las <b>vacaciones no se solicitan</b> (ver Calendario Vacacional Institucional).</div>'+
  '<div class="card"><h3>📝 Nueva solicitud</h3><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">'+
   '<div><label class="lb">Tipo de permiso / licencia *</label><select id="s_tipo" onchange="fichaTipo()"><option value="">— Selecciona —</option>'+R.map(function(x){return '<option>'+ec(x.tipo)+'</option>';}).join('')+'</select></div>'+
   '<div><label class="lb">Fecha inicio</label><input id="s_ini" type="date"></div>'+
   '<div><label class="lb">Fecha fin</label><input id="s_fin" type="date"></div>'+
   '<div><label class="lb">Días solicitados</label><input id="s_dias" type="number" min="0" value="1"></div>'+
  '</div><div style="margin-top:6px"><label class="lb">Motivo / justificación</label><textarea id="s_motivo"></textarea></div>'+
  '<div id="s_ficha"></div><div id="s_docs"></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="validarSol()">🔎 Validar con el Motor de Reglas</button> <button class="bg" onclick="enviarSol()" id="s_send" style="display:none">📨 Enviar solicitud</button> <span id="s_msg" style="font-size:12px;margin-left:6px"></span></div>'+
  '<div id="s_dict"></div></div>';}
function fichaTipo(){var tipo=el('s_tipo').value;selTipo=tipo;curDocs=[];var r=reglaDe(tipo);el('s_send').style.display='none';el('s_dict').innerHTML='';
 if(!r){el('s_ficha').innerHTML='';el('s_docs').innerHTML='';return;}
 el('s_ficha').innerHTML='<div class="ficha"><b>⚖️ Ficha jurídica ('+ec(r.num)+')</b>'+(r.verif&&r.verif.ok?' <span class="st v">✓ CCT verificado</span>':' <span class="st y">cláusula por capturar</span>')+'<br><b>Fundamento:</b> '+ec(r.fundamento)+'<br><b>Días autorizados:</b> '+(r.dias?r.dias+' '+ec(r.base):'según CCT (parametrizar)')+' · <b>Goce de sueldo:</b> '+(r.goceSueldo?'sí':'no')+'<br><b>Antigüedad requerida:</b> '+(r.antiguedad||0)+' meses · <b>Autoridad competente:</b> '+ec(r.autoridad)+'<br><b>Documentación obligatoria:</b> '+((r.docs||[]).join(', ')||'—')+'<br><b>Restricciones:</b> '+ec(r.restricciones)+'</div>';
 el('s_docs').innerHTML='<div style="margin-top:8px"><label class="lb">📎 Adjunta tus documentos / constancias (PDF, imagen o Word · máx. 1.9 MB c/u)</label>'+((r.docs||[]).length?r.docs.map(function(d,i){return '<div style="margin:4px 0;font-size:12px">'+ec(d)+' <span style="color:#c0392b">*</span><br><input type="file" id="sf_'+i+'" accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" onchange="fileAdd('+i+',this)"></div>';}).join(''):'<div style="font-size:11.5px;color:#64748b">Esta cláusula no exige documento; puedes adjuntar soporte opcional.</div>')+'<div style="margin-top:6px"><label class="lb">Otros documentos de soporte (opcional)</label><input type="file" id="sf_otros" multiple accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" onchange="fileAdd(-1,this)"></div><div id="s_doclist" style="margin-top:6px;font-size:11.5px"></div></div>';renderDocList();}
function fileAdd(i,inp){var r=reglaDe(el('s_tipo').value);var reqName=(i>=0&&r&&r.docs[i])?r.docs[i]:'Otro documento';var files=inp.files;for(var k=0;k<files.length;k++){(function(f){if(f.size>1.9e6){alert('Máximo 1.9 MB por archivo: '+f.name);return;}var rd=new FileReader();rd.onload=function(){if(i>=0)curDocs=curDocs.filter(function(x){return x.slot!==i;});curDocs.push({slot:(i>=0?i:'otro'),docReq:reqName,nombre:f.name,tipo:f.type,data:rd.result,fecha:today()});renderDocList();};rd.readAsDataURL(f);})(files[k]);}}
function renderDocList(){var box=el('s_doclist');if(!box)return;box.innerHTML=curDocs.length?('<b>Adjuntos ('+curDocs.length+'):</b> '+curDocs.map(function(d,i){return '📎 '+ec(d.docReq)+': '+ec(d.nombre)+' <span style="color:#c0392b;cursor:pointer" onclick="delDoc('+i+')">✕</span>';}).join(' &nbsp;·&nbsp; ')):'<span style="color:#94a3b8">Sin adjuntos aún.</span>';}
function delDoc(i){curDocs.splice(i,1);renderDocList();}
function solFromForm(){var docsDecl=[];curDocs.forEach(function(x){if(x.slot!=='otro'&&docsDecl.indexOf(x.docReq)<0)docsDecl.push(x.docReq);});
 return {id:'SOL-'+Date.now().toString(36),tipo:el('s_tipo').value,trabajador:trabajador(),fechaInicio:el('s_ini').value,fechaFin:el('s_fin').value,dias:+el('s_dias').value||0,motivo:(el('s_motivo').value||'').trim(),docsDeclarados:docsDecl,docs:curDocs.slice()};}
function validarSol(){if(!el('s_tipo').value){el('s_msg').style.color='#c0392b';el('s_msg').textContent='Selecciona el tipo.';return;}
 var sol=solFromForm();var d=evaluar(sol);
 el('s_dict').innerHTML='<div class="dict '+(d.cumple?'ok':'no')+'"><b>'+(d.cumple?'✅ PROCEDE':'⛔ NO PROCEDE')+' — Dictamen del Motor de Reglas</b><div style="margin-top:5px">'+d.pasos.map(function(p){return '<div class="chk"><span class="ico" style="color:'+(p.ok?'#128c4a':'#c0392b')+'">'+(p.ok?'✓':'✗')+'</span> '+ec(p.label)+'</div>';}).join('')+'</div><div style="margin-top:6px;font-size:11.5px;color:#334155">'+ec(d.texto)+'</div></div>';
 el('s_send').style.display=d.cumple?'':'none';el('s_msg').textContent='';window.__lastDict=d;}
function enviarSol(){var sol=solFromForm();var d=evaluar(sol);if(!d.cumple){el('s_msg').style.color='#c0392b';el('s_msg').textContent='El Motor de Reglas impide el envío (no procede).';return;}
 sol.folio='PL-'+new Date().getFullYear()+'-'+String(SOL().length+1).padStart(4,'0');sol.estado='Enviada';sol.dictamen=d;sol.fechaSolicitud=nowT();sol.creadoPor=PERFIL;sol.ts=nowT();
 sol.flujo=[{etapa:'Trabajador',usuario:PERFIL,accion:'Solicitud enviada',fecha:nowT(),nota:sol.motivo}];sol.bitacora=[{ts:nowFull(),usuario:PERFIL,accion:'Alta de solicitud '+sol.folio}];
 var A=SOL();A.push(sol);saveSOL(A);blog('Acción','Solicitud '+sol.folio+' · '+sol.tipo);
 try{var N=J('sigej_notificaciones')||[];N.push({id:'NT-'+Date.now().toString(36),ts:nowT(),tipo:'Laboral',folio:sol.folio,asunto:'Nueva solicitud '+sol.tipo,para:'Jefe inmediato / RH',rol:'Autorizador',canal:'SIGEJ',mensaje:sol.trabajador.nombre+' solicita '+sol.tipo,link:'laboral_SIGEJ.html',leido:false,origen:'Permisos y Licencias'});S('sigej_notificaciones',N);}catch(e){}
 el('s_msg').style.color='#128c4a';el('s_msg').textContent='✓ '+sol.folio+' enviada al flujo de autorización.';el('s_dict').innerHTML='';el('s_send').style.display='none';curDocs=[];go('t2');}
/* ===== 2. MIS SOLICITUDES ===== */
function mis(){var t=trabajador();var A=SOL().filter(function(s){return (s.trabajador||{}).numEmp===t.numEmp||s.creadoPor===PERFIL;}).slice().reverse();
 el('pane').innerHTML='<div class="card" style="overflow:auto"><h3>📋 Mis solicitudes</h3><table><thead><tr><th>Folio</th><th>Tipo</th><th>Fechas</th><th>Días</th><th>Estado</th><th>Dictamen</th></tr></thead><tbody>'+(A.length?A.map(function(s){return '<tr class="rowc" onclick="ficha(\''+s.id+'\')" style="cursor:pointer"><td><b>'+ec(s.folio)+'</b></td><td>'+ec(s.tipo)+'</td><td style="font-size:11px">'+ec(s.fechaInicio||'')+(s.fechaFin?' → '+ec(s.fechaFin):'')+'</td><td>'+ec(s.dias||'')+'</td><td><span class="st '+stColor(s.estado)+'">'+ec(s.estado)+'</span></td><td>'+(s.dictamen&&s.dictamen.cumple?'✅':'—')+'</td></tr>';}).join(''):'<tr><td colspan="6" style="text-align:center;color:#64748b;padding:14px">Aún no tienes solicitudes.</td></tr>')+'</tbody></table></div>';}
function stColor(s){if(['Autorizada'].indexOf(s)>=0)return 'v';if(['Negada','Cancelada'].indexOf(s)>=0)return 'r';if(['Requiere info','Devuelta'].indexOf(s)>=0)return 'y';if(['Enviada','En jefe','En RH'].indexOf(s)>=0)return 'b';return 'g';}
/* ===== ficha de una solicitud (drawer) ===== */
function solById(id){return SOL().filter(function(s){return s.id===id;})[0];}
function ficha(id){var s=solById(id);if(!s)return;var d=s.dictamen||{};
 var flujo=(s.flujo||[]).map(function(f){return '<div class="ev"><b>'+ec(f.etapa)+' · '+ec(f.accion)+'</b> <span style="color:#94a3b8">'+ec(f.fecha)+' · '+ec(f.usuario)+'</span>'+(f.nota?'<br><span style="color:#475569">'+ec(f.nota)+'</span>':'')+'</div>';}).join('');
 var acc='';if(esRH()&&['Enviada','En jefe','En RH','Requiere info','Devuelta'].indexOf(s.estado)>=0){acc='<div class="card"><h3>Acción de autorización</h3><textarea id="a_nota" placeholder="Observación / fundamento"></textarea><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap"><button class="bg mini" onclick="accion(\''+s.id+'\',\'Autorizada\')">✅ Autorizar</button><button class="br mini" onclick="accion(\''+s.id+'\',\'Negada\')">⛔ Negar</button><button class="bo mini" onclick="accion(\''+s.id+'\',\'Requiere info\')">📄 Requerir info</button><button class="bd mini" onclick="accion(\''+s.id+'\',\'Devuelta\')">↩️ Devolver</button><button class="bd mini" onclick="accion(\''+s.id+'\',\'Cancelada\')">🚫 Cancelar</button></div><div class="warn" style="margin-top:6px">La modificación de una solicitud solo procede con fundamento legal; nada se elimina (expediente inalterable).</div></div>';}
 el('drwc').innerHTML='<h2 style="margin:0 0 3px;color:#00254a;font-size:17px">'+ec(s.folio)+' <span class="st '+stColor(s.estado)+'">'+ec(s.estado)+'</span></h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+ec(s.tipo)+'</div>'+
  '<div class="card"><b>Trabajador:</b> '+ec((s.trabajador||{}).nombre)+' ('+ec((s.trabajador||{}).numEmp)+')<br><b>Adscripción:</b> '+ec((s.trabajador||{}).adscripcion||'—')+'<br><b>Nombramiento:</b> '+ec((s.trabajador||{}).nombramiento||'—')+' · <b>Antigüedad:</b> '+((s.trabajador||{}).antiguedadMeses||0)+' meses<br><b>Fechas:</b> '+ec(s.fechaInicio||'—')+(s.fechaFin?' → '+ec(s.fechaFin):'')+' · <b>Días:</b> '+ec(s.dias||'—')+'<br><b>Motivo:</b> '+ec(s.motivo||'—')+'<br><b>Documentos declarados:</b> '+((s.docsDeclarados||[]).join(', ')||'—')+'</div>'+((s.docs&&s.docs.length)?'<div class="card"><h3>📎 Documentos adjuntos ('+s.docs.length+')</h3>'+s.docs.map(function(d){return '<div style="margin:3px 0;font-size:12px">📄 <b>'+ec(d.docReq||'Documento')+':</b> <a href="'+d.data+'" download="'+ec(d.nombre)+'" style="color:#0a4d8c">'+ec(d.nombre)+'</a> <span style="color:#94a3b8;font-size:10.5px">'+ec(d.fecha||'')+'</span></div>';}).join('')+'</div>':'')+
  (d.texto?'<div class="dict '+(d.cumple?'ok':'no')+'"><b>🧾 Dictamen automatizado ('+ec(d.reglaNum||'')+')</b><div style="margin-top:4px">'+ec(d.texto)+'</div><div style="margin-top:4px;font-size:11px;color:#64748b">Fundamento: '+ec(d.fundamento||'—')+'</div></div>':'')+
  acc+
  '<div class="card"><h3>🧾 Flujo y expediente (inalterable)</h3><div class="tl">'+(flujo||'<div class="ev">—</div>')+'</div></div>';
 el('drw').classList.add('on');}
function closeDrw(){el('drw').classList.remove('on');}
function accion(id,estado){if(!esRH())return;var A=SOL();var s=A.filter(function(x){return x.id===id;})[0];if(!s)return;var nota=(el('a_nota')?el('a_nota').value:'').trim();
 if((estado==='Negada'||estado==='Requiere info')&&!nota){alert('La resolución debe estar motivada (captura la observación/fundamento).');return;}
 s.estado=estado;var etapa=esRH()&&(PERFIL==='Jefe del Área de Personal'||PERFIL==='Administrador')?'Recursos Humanos':(PERFIL==='Abogado General'?'Abogado General':'Jefe inmediato');
 (s.flujo=s.flujo||[]).push({etapa:etapa,usuario:PERFIL,accion:estado,fecha:nowT(),nota:nota});(s.bitacora=s.bitacora||[]).push({ts:nowFull(),usuario:PERFIL,accion:estado+(nota?': '+nota:'')});
 saveSOL(A);blog('Acción','Solicitud '+s.folio+' → '+estado);
 try{var N=J('sigej_notificaciones')||[];N.push({id:'NT-'+Date.now().toString(36),ts:nowT(),tipo:'Laboral',folio:s.folio,asunto:'Solicitud '+estado,para:(s.trabajador||{}).nombre,rol:'Trabajador',canal:'SIGEJ',mensaje:'Tu solicitud de '+s.tipo+' está: '+estado,link:'laboral_SIGEJ.html',leido:false,origen:'Permisos y Licencias'});
 if(estado==='Autorizada')N.push({id:'NT-'+Date.now().toString(36)+'a',ts:nowT(),tipo:'Laboral',folio:s.folio,asunto:'Autorización laboral (conocimiento)',para:'Abogado General',rol:'Conocimiento',canal:'SIGEJ',mensaje:'Autorizada '+s.tipo+' de '+(s.trabajador||{}).nombre,link:'centro_ejecutivo_SIGEJ.html',leido:false,origen:'Permisos y Licencias'});
 S('sigej_notificaciones',N);}catch(e){}
 ficha(id);}
/* ===== 3. AUTORIZACIÓN (bandeja RH/Jefe) ===== */
function autoriza(){if(!esRH()){el('pane').innerHTML='<div class="warn">Acceso reservado a RH, jefe inmediato, coordinador o Abogado General.</div>';return;}
 var A=SOL().slice().reverse();var pend=A.filter(function(s){return ['Enviada','En jefe','En RH','Requiere info','Devuelta'].indexOf(s.estado)>=0;});
 el('pane').innerHTML='<div class="kpis"><div class="kpi"><div class="n">'+pend.length+'</div><div class="l">Pendientes de autorización</div></div><div class="kpi"><div class="n">'+A.filter(function(s){return s.estado==='Autorizada';}).length+'</div><div class="l">Autorizadas</div></div><div class="kpi"><div class="n">'+A.filter(function(s){return s.estado==='Negada';}).length+'</div><div class="l">Negadas</div></div></div>'+
  '<div class="note">Flujo obligatorio: <b>Trabajador → Jefe inmediato → Recursos Humanos → Notificación al Abogado General (Centro Ejecutivo) → Archivo → Expediente laboral</b>. No se omiten etapas; el expediente es inalterable.</div>'+
  '<div class="card" style="overflow:auto"><table><thead><tr><th>Folio</th><th>Trabajador</th><th>Tipo</th><th>Días</th><th>Dictamen BRE</th><th>Estado</th></tr></thead><tbody>'+(A.length?A.map(function(s){return '<tr class="rowc" onclick="ficha(\''+s.id+'\')" style="cursor:pointer"><td><b>'+ec(s.folio)+'</b></td><td style="font-size:11.5px">'+ec((s.trabajador||{}).nombre)+'<br><span style="color:#94a3b8">'+ec((s.trabajador||{}).adscripcion||'')+'</span></td><td>'+ec(s.tipo)+'</td><td>'+ec(s.dias||'')+'</td><td>'+(s.dictamen?(s.dictamen.cumple?'<span class="st v">procede</span>':'<span class="st r">no procede</span>'):'—')+'</td><td><span class="st '+stColor(s.estado)+'">'+ec(s.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="6" style="text-align:center;color:#64748b;padding:14px">Sin solicitudes.</td></tr>')+'</tbody></table></div>';}
/* ===== 4. MOTOR DE REGLAS (BRE) — admin ===== */
function bre(){if(!esBREadmin()){el('pane').innerHTML='<div class="warn">El Motor de Reglas lo administran Recursos Humanos y la Oficina de la Abogacía General.</div>';return;}
 var R=BRE();var verif=R.filter(function(x){return !/por capturar/i.test(x.fundamento);}).length;
 el('pane').innerHTML='<div class="note">Catálogo de reglas del CCT <b>parametrizable sin tocar código</b>. Cada regla cita su <b>fundamento</b> (cláusula), que <b>RH/Abogacía captura del CCT</b> — el sistema <b>no presume articulado</b>. Versionamiento: las reglas no se borran (Vigente/Derogada/Suspendida/Sustituida).</div>'+
  '<div class="kpis"><div class="kpi"><div class="n">'+R.length+'</div><div class="l">Reglas</div></div><div class="kpi"><div class="n" style="color:#128c4a">'+verif+'</div><div class="l">Con fundamento capturado</div></div><div class="kpi"><div class="n" style="color:#b45309">'+(R.length-verif)+'</div><div class="l">Cláusula por capturar</div></div></div>'+
  '<div class="card" style="overflow:auto"><table><thead><tr><th>Regla</th><th>Tipo</th><th>Fundamento (CCT)</th><th>Días</th><th>Antig.</th><th>Docs</th><th>Estado</th><th></th></tr></thead><tbody>'+R.map(function(r,i){return '<tr><td><b>'+ec(r.num)+'</b></td><td>'+ec(r.tipo)+'</td><td style="font-size:11px;color:'+(/por capturar/i.test(r.fundamento)?'#b45309':'#128c4a')+'">'+ec(r.fundamento)+'</td><td>'+(r.dias||'—')+' '+ec(r.dias?r.base:'')+'</td><td>'+(r.antiguedad||0)+'m</td><td style="font-size:11px">'+((r.docs||[]).join(', ')||'—')+'</td><td><span class="st '+(r.estado==='Vigente'?'v':'g')+'">'+ec(r.estado)+' v'+r.version+'</span></td><td style="white-space:nowrap"><button class="bd mini" onclick="editRegla('+i+')">✏️</button> <button class="bd mini" onclick="verReglaHist('+i+')">🧾</button></td></tr>';}).join('')+'</tbody></table></div>';}
function editRegla(i){if(!esBREadmin())return;var R=BRE();var r=R[i];if(!r)return;
 var fu=prompt('Fundamento / cláusula del CCT (captura el texto conforme al CCT):',r.fundamento);if(fu===null)return;
 var dd=prompt('Días autorizados (0 = parametrizar):',r.dias);if(dd===null)return;var nd=parseInt(dd,10);if(isNaN(nd))nd=r.dias;
 var an=prompt('Antigüedad requerida (meses):',r.antiguedad);if(an===null)return;var na=parseInt(an,10);if(isNaN(na))na=r.antiguedad;
 var doc=prompt('Documentos obligatorios (separa con ;):',(r.docs||[]).join('; '));if(doc===null)return;
 var res=prompt('Restricciones / observaciones:',r.restricciones);if(res===null)return;
 r.version=(r.version||1)+1;r.fundamento=fu.trim();r.dias=nd;r.antiguedad=na;r.docs=doc.split(';').map(function(s){return s.trim();}).filter(Boolean);r.restricciones=res.trim();
 (r.hist=r.hist||[]).push({version:r.version,fecha:today(),usuario:PERFIL,fundamento:fu.trim(),nota:'Parametrización'});
 S('sigej_bre_reglas',R);blog('Acción','Parametriza regla BRE '+r.num);bre();}
function verReglaHist(i){var r=BRE()[i];if(!r)return;alert('🧾 '+r.num+' · '+r.tipo+'\nEstado: '+r.estado+' (v'+r.version+')\nFundamento vigente: '+r.fundamento+'\nAutoridad: '+r.autoridad+'\nIncompatibilidades: '+((r.incompat||[]).join(', ')||'—')+'\n\nVERSIONAMIENTO:\n'+(r.hist||[]).map(function(h){return '• v'+h.version+' ('+h.fecha+', '+h.usuario+'): '+h.fundamento+' — '+h.nota;}).join('\n'));}
/* ===== 5. CALENDARIO VACACIONAL INSTITUCIONAL (RH admin; trabajador solo lectura) ===== */
function CAL(){return J('sigej_laboral_calendario')||[];}
function seedCal(){if(J('sigej_laboral_calendario'))return;S('sigej_laboral_calendario',[
 {id:'C1',tipo:'Vacacional',periodo:'Primer periodo 2026',fInicio:'2026-07-20',fFin:'2026-07-31',desc:'Periodo vacacional oficial (Calendario Universitario)'},
 {id:'C2',tipo:'Suspensión',periodo:'Suspensión de labores',fInicio:'2026-12-24',fFin:'2027-01-06',desc:'Suspensión oficial de labores'},
 {id:'C3',tipo:'Descanso obligatorio',periodo:'Día de descanso obligatorio',fInicio:'2026-09-16',fFin:'2026-09-16',desc:'Conforme a la LFT y el CCT'}
]);}
seedCal();
function calendario(){var C=CAL();var adm=esRH();
 el('pane').innerHTML='<div class="note">Las <b>vacaciones son un derecho previamente calendarizado</b> (CCT + Calendario Universitario): <b>no se solicitan</b>. El trabajador solo <b>visualiza</b>; solo Recursos Humanos administra este calendario.</div>'+
  (adm?'<div class="card"><h3>➕ Agregar periodo (Recursos Humanos)</h3><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))"><select id="c_tipo"><option>Vacacional</option><option>Suspensión</option><option>Descanso obligatorio</option><option>Guardia</option></select><input id="c_periodo" placeholder="Periodo / nombre"><input id="c_ini" type="date"><input id="c_fin" type="date"><input id="c_desc" placeholder="Descripción / fundamento"></div><div style="margin-top:6px"><button class="bg" onclick="addCal()">Guardar</button></div></div>':'')+
  '<div class="card" style="overflow:auto"><table><thead><tr><th>Tipo</th><th>Periodo</th><th>Inicio</th><th>Fin</th><th>Descripción</th></tr></thead><tbody>'+(C.length?C.map(function(x){var col=x.tipo==='Vacacional'?'v':x.tipo==='Guardia'?'y':x.tipo==='Suspensión'?'b':'g';return '<tr><td><span class="st '+col+'">'+ec(x.tipo)+'</span></td><td><b>'+ec(x.periodo)+'</b></td><td>'+ec(x.fInicio)+'</td><td>'+ec(x.fFin)+'</td><td style="font-size:11.5px">'+ec(x.desc||'')+'</td></tr>';}).join(''):'<tr><td colspan="5" style="text-align:center;color:#64748b;padding:12px">Sin periodos.</td></tr>')+'</tbody></table></div>'+
  '<div class="warn">🛡️ No existe botón «Solicitar vacaciones» (prohibido por el pliego). La excepción es <b>Compensación por Guardias Vacacionales</b>: si te designan oficialmente para cubrir guardias en vacaciones, solicítala en la pestaña «Solicitar» (tipo «Compensación por guardias»).</div>';}
function addCal(){if(!esRH())return;var p=(el('c_periodo').value||'').trim();if(!p){alert('Indica el periodo.');return;}var C=CAL();C.push({id:'C-'+Date.now().toString(36),tipo:el('c_tipo').value,periodo:p,fInicio:el('c_ini').value,fFin:el('c_fin').value,desc:(el('c_desc').value||'').trim()});S('sigej_laboral_calendario',C);blog('Acción','RH agrega periodo vacacional/guardia: '+p);calendario();}
/* ===== 6. ESTÍMULO POR PUNTUALIDAD (cláusulas 34 y 59, citadas por el área) ===== */
function puntualidad(){var P=J('sigej_laboral_puntualidad')||[];var t=trabajador();
 el('pane').innerHTML='<div class="note">Motor de <b>estímulo por puntualidad</b> conforme a las <b>cláusulas 34 y 59 del CCT</b> (citadas por el área; el texto exacto se captura y verifica). Al cierre de mes se evalúa la asistencia; si el trabajador cumple, se habilita el descanso o —si la Universidad lo determina y el trabajador acepta— la compensación económica prevista en el CCT.</div>'+
  '<div class="card"><h3>Simulación de cierre de mes</h3><div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))"><div><label class="lb">Retardos del mes</label><input id="p_ret" type="number" min="0" value="0"></div><div><label class="lb">Faltas</label><input id="p_fal" type="number" min="0" value="0"></div><div><label class="lb">Incidencias/permisos</label><input id="p_inc" type="number" min="0" value="0"></div></div><div style="margin-top:6px"><button class="b1" onclick="evalPunt()">Evaluar puntualidad</button> <span id="p_msg" style="font-size:12px;margin-left:6px"></span></div><div id="p_res"></div></div>'+
  '<div class="card" style="overflow:auto"><h3>Estímulos generados</h3><table><thead><tr><th>Fecha</th><th>Trabajador</th><th>Modalidad</th><th>Estado</th></tr></thead><tbody>'+(P.length?P.slice().reverse().map(function(x){return '<tr><td style="font-size:11px">'+ec(x.ts)+'</td><td>'+ec(x.trabajador)+'</td><td>'+ec(x.modalidad)+'</td><td><span class="st '+(x.estado==='Descanso elegido'?'v':'y')+'">'+ec(x.estado)+'</span></td></tr>';}).join(''):'<tr><td colspan="4" style="text-align:center;color:#64748b;padding:12px">Sin estímulos.</td></tr>')+'</tbody></table></div>';}
function evalPunt(){var ret=+el('p_ret').value||0,fal=+el('p_fal').value||0,inc=+el('p_inc').value||0;var t=trabajador();
 /* parámetros del estímulo (configurables): sin faltas, retardos dentro de tolerancia */
 var TOL=+(localStorage.getItem('sigej_punt_tolerancia')||3);
 var cumple=fal===0&&ret<=TOL;
 el('p_res').innerHTML='<div class="dict '+(cumple?'ok':'no')+'" style="margin-top:8px">'+(cumple?'✅ <b>Estímulo por Puntualidad Disponible</b> — cumple los requisitos (sin faltas; retardos '+ret+' ≤ tolerancia '+TOL+'). Cláusulas 34 y 59 del CCT. Elige tu día de descanso dentro del mes siguiente (sujeto a autorización del jefe y a no afectar la operación).':'⛔ No cumple los requisitos del estímulo este mes (faltas: '+fal+', retardos: '+ret+', tolerancia: '+TOL+').')+'</div>'+(cumple?'<div style="margin-top:6px"><input id="p_dia" type="date" style="max-width:200px"> <button class="bg mini" onclick="genPunt(\'Descanso elegido\')">Elegir día de descanso</button> <button class="bd mini" onclick="genPunt(\'Compensación económica\')">Aceptar compensación económica</button></div>':'');}
function genPunt(mod){var t=trabajador();var P=J('sigej_laboral_puntualidad')||[];P.push({id:'PU-'+Date.now().toString(36),ts:nowT(),trabajador:t.nombre,numEmp:t.numEmp,modalidad:mod,dia:(el('p_dia')?el('p_dia').value:''),estado:mod==='Descanso elegido'?'Descanso elegido':'Compensación aceptada',fundamento:'Cláusulas 34 y 59 del CCT'});S('sigej_laboral_puntualidad',P);blog('Acción','Estímulo puntualidad ('+mod+') '+t.nombre);
 try{var N=J('sigej_notificaciones')||[];N.push({id:'NT-'+Date.now().toString(36),ts:nowT(),tipo:'Laboral',folio:'PUNT',asunto:'Estímulo por puntualidad',para:'Jefe inmediato / RH',rol:'Autorizador',canal:'SIGEJ',mensaje:t.nombre+': '+mod+' (cl. 34/59 CCT)',link:'laboral_SIGEJ.html',leido:false,origen:'Permisos y Licencias'});N.push({id:'NT-'+Date.now().toString(36)+'a',ts:nowT(),tipo:'Laboral',folio:'PUNT',asunto:'Estímulo (conocimiento)',para:'Abogado General',rol:'Conocimiento',canal:'SIGEJ',mensaje:t.nombre+' · estímulo por puntualidad',link:'centro_ejecutivo_SIGEJ.html',leido:false,origen:'Permisos y Licencias'});S('sigej_notificaciones',N);}catch(e){}
 el('p_res').innerHTML='<div class="dict ok" style="margin-top:8px">✓ Registrado ('+ec(mod)+'). Notificado al jefe inmediato, RH y al Abogado General para conocimiento.</div>';puntualidad();}
/* ===== 7. PANEL EJECUTIVO ===== */
function panel(){var A=SOL();var P=J('sigej_laboral_puntualidad')||[];
 function ct(f){return A.filter(f).length;}
 var byDep={};A.forEach(function(s){var d=(s.trabajador||{}).adscripcion||'(sin adscripción)';byDep[d]=(byDep[d]||0)+1;});
 var noProc=A.filter(function(s){return s.dictamen&&!s.dictamen.cumple;}).length;
 el('pane').innerHTML='<div class="note">Panel para conocimiento del <b>Abogado General</b> (se refleja también en el Centro Ejecutivo). Indicadores en tiempo real de incidencias y cumplimiento del CCT.</div>'+
  '<div class="kpis"><div class="kpi"><div class="n">'+A.length+'</div><div class="l">Solicitudes totales</div></div><div class="kpi"><div class="n" style="color:#0a4d8c">'+ct(function(s){return ['Enviada','En jefe','En RH'].indexOf(s.estado)>=0;})+'</div><div class="l">Pendientes</div></div><div class="kpi"><div class="n" style="color:#128c4a">'+ct(function(s){return s.estado==='Autorizada';})+'</div><div class="l">Autorizadas</div></div><div class="kpi"><div class="n" style="color:#c0392b">'+ct(function(s){return s.estado==='Negada';})+'</div><div class="l">Negadas</div></div><div class="kpi"><div class="n" style="color:#b45309">'+ct(function(s){return s.tipo==='Incapacidad (IMSS)';})+'</div><div class="l">Incapacidades</div></div><div class="kpi"><div class="n">'+ct(function(s){return s.tipo==='Permiso sindical';})+'</div><div class="l">Permisos sindicales</div></div><div class="kpi"><div class="n">'+P.length+'</div><div class="l">Estímulos puntualidad</div></div><div class="kpi '+(noProc?'':'')+'"><div class="n" style="color:'+(noProc?'#c0392b':'#1f9d6b')+'">'+noProc+'</div><div class="l">Alertas de posible incumplimiento</div></div></div>'+
  '<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><h3>Incidencias por dependencia</h3><table>'+(Object.keys(byDep).length?Object.keys(byDep).sort(function(a,b){return byDep[b]-byDep[a];}).map(function(k){return '<tr><td>'+ec(k)+'</td><td style="text-align:right"><b>'+byDep[k]+'</b></td></tr>';}).join(''):'<tr><td style="color:#94a3b8">Sin datos.</td></tr>')+'</table></div>'+
  '<div class="card"><h3>Cumplimiento del CCT (Motor de Reglas)</h3><div style="font-size:12.5px;line-height:1.9">Reglas configuradas: <b>'+BRE().length+'</b><br>Con fundamento capturado: <b>'+BRE().filter(function(x){return !/por capturar/i.test(x.fundamento);}).length+'</b><br>Solicitudes que no procedían (bloqueadas): <b>'+noProc+'</b><br>Dictámenes automatizados emitidos: <b>'+A.filter(function(s){return s.dictamen;}).length+'</b></div><div class="note" style="margin-top:6px">Toda autorización quedó dictaminada y con expediente inalterable.</div></div></div>';}
/* init */
var __vm=(location.search.match(/[?&]vista=([a-z]+)/)||[])[1];
if(__vm==='panel'&&esRH())cur='t7';else if(__vm==='calendario')cur='t5';else if(__vm==='autoriza'&&esRH())cur='t3';
drawTabs();render();
</script>
<script>(function(){if(!/[?&]embed=1/.test(location.search))return;var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{background:#fff!important}.wrap{padding-top:6px!important}";document.head.appendChild(st);})();</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"laboral_SIGEJ.html","w",encoding="utf-8").write(out)
print("laboral_SIGEJ.html OK -",len(out),"bytes | reglas seed:",out.count("mk('0"))
