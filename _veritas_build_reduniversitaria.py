# -*- coding: utf-8 -*-
# MÓDULO: Enlace con la Red Universitaria — comunicación con los 19 CU + SEMS, numeralia oficial y Art. 219 RIAG (verbatim verificado).
import re, json
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Enlace con la Red'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','red_universitaria_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html" class="act">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="mensajeria_SIGEJ.html">💬 Mensajería</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a></div>'''

# ---- Datos oficiales verificados (SIE-UdeG / CGPE, ciclo 2024-2025, corte 31-jul-2025) ----
NUM=[["19","Centros Universitarios","7 metropolitanos · 12 regionales"],
     ["177","Planteles SEMS","76 escuelas · 101 módulos"],
     ["1","Universidad Virtual (SUV)","educación en línea"],
     ["339,508","Matrícula total","ciclo 2024-2025"],
     ["148,866","Educación superior","licenciatura y posgrado"],
     ["190,642","Educación media superior","bachillerato (SEMS)"],
     ["≈15,055","Personal académico","padrón 2024"],
     ["9,174","Personal administrativo","confianza 2,737 · sindicalizado 6,437"],
     ["2","Sindicatos","STAUdeG · SUTUdeG"],
     ["6,001","Estudiantes con discapacidad","inclusión"],
     ["2,997","Hablantes de lengua indígena","pertenencia étnica"]]

# ---- 19 Centros Universitarios (siglas + nombre + sede) — nombres verificados ----
CUS=[["CUAAD","Arte, Arquitectura y Diseño","Guadalajara"],
     ["CUCBA","Ciencias Biológicas y Agropecuarias","Zapopan"],
     ["CUCEA","Ciencias Económico Administrativas","Zapopan"],
     ["CUCEI","Ciencias Exactas e Ingenierías","Guadalajara"],
     ["CUCS","Ciencias de la Salud","Guadalajara"],
     ["CUCSH","Ciencias Sociales y Humanidades","Guadalajara"],
     ["CUTONALÁ","Tonalá","Tonalá"],
     ["CUTLAJOMULCO","Tlajomulco","Tlajomulco de Zúñiga"],
     ["CUGDL","Guadalajara","Guadalajara"],
     ["CUTLAQUEPAQUE","Tlaquepaque","San Pedro Tlaquepaque"],
     ["CUALTOS","Los Altos","Tepatitlán de Morelos"],
     ["CUCIÉNEGA","Ciénega","Ocotlán"],
     ["CUCOSTA","Costa","Puerto Vallarta"],
     ["CUCSUR","Costa Sur","Autlán de Navarro"],
     ["CULAGOS","Lagos","Lagos de Moreno"],
     ["CUNORTE","Norte","Colotlán"],
     ["CUSUR","Sur","Ciudad Guzmán"],
     ["CUVALLES","Valles","Ameca"],
     ["CUCHAPALA","Chapala","Chapala"]]

# ---- Art. 219 RIAG (Junio 2025) — transcripción textual verificada del PDF oficial ----
ART219=[
 "I. Coordinar la asesoría legal en materia de propiedad intelectual para el registro y protección jurídica del patrimonio intangible de la Universidad;",
 "II. Coordinar la asesoría legal en las ramas del derecho migratorio y derecho internacional privado, en asuntos que incumban a la Universidad;",
 "III. Coordinar la asesoría legal en que se brinde respecto de trámites consulares y aduanales que incumban a la Universidad de Guadalajara;",
 "IV. Coordinar la asesoría legal en la celebración de actos o la firma de documentos que impliquen obligaciones o derechos de la Universidad de Guadalajara;",
 "V. Coordinar la asesoría legal en el seguimiento de las adquisiciones, enajenaciones, fideicomisos, herencias, legados, donaciones y demás figuras jurídicas en que participe la Universidad de Guadalajara, vigilando que se realicen conforme a derecho;",
 "VI. Coordinar la producción, edición y difusión de contenidos, a través de publicaciones impresas o electrónicas, periódicas o no periódicas, tendientes a informar sobre los análisis e investigaciones jurídicas relacionados con disposiciones jurídicas aplicables a la Universidad de Guadalajara;",
 "VII. Diseñar la estrategia de implementación de tecnologías aplicadas al campo del Derecho, respecto de la asesoría jurídica que se brinda a la Red Universitaria;",
 "VIII. Diseñar los procesos de capacitación continua en los temas jurídicos que así lo requieran hacia las entidades de la Red Universitaria;",
 "IX. Coordinar a las instancias de asesoría jurídica que funcionen en los Centros Universitarios y en el Sistema de Educación Media Superior, y",
 "X. Las demás que se establezcan en la normatividad vigente y aquellas que por la naturaleza de sus atribuciones le correspondan."]

numHTML="".join(f'<div class="kpi"><div class="n">{v}</div><div class="l">{l}</div><div class="sub">{s}</div></div>' for v,l,s in NUM)
cuHTML="".join(f'<tr><td class="sig">{sig}</td><td>Centro Universitario de {nom}</td><td>{sede}</td><td><a class="mini" href="mensajeria_SIGEJ.html">💬 Canal</a> <a class="mini" href="oficialia_SIGEJ.html">📨 Turnar</a></td></tr>' for sig,nom,sede in CUS)
art219HTML="".join(f'<li>{f}</li>' for f in ART219)

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Enlace con la Red Universitaria</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--line:#e2e8f0;--bg:#eef2f7;--mut:#5b6b82}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:#0a1f3c}
header{background:linear-gradient(120deg,#0b2540,#24476f);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.wrap{max-width:1240px;margin:auto;padding:18px}
.card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:16px;box-shadow:0 3px 12px rgba(10,37,74,.06)}
.card h2{margin:0 0 4px;font-size:16px;color:var(--azul)}
.card .cap{font-size:11.5px;color:var(--mut);margin-bottom:12px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.kpi{background:#f6f9fc;border:1px solid var(--line);border-radius:12px;padding:13px}
.kpi .n{font-size:24px;font-weight:800;color:var(--azul2)}.kpi .l{font-size:11.5px;color:#334155;margin-top:2px}.kpi .sub{font-size:10px;color:#8090a5;margin-top:3px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}
th{background:#f1f5fb;color:#334155;font-size:11.5px}
td.sig{font-weight:700;color:var(--azul2);white-space:nowrap}
a.mini{display:inline-block;font-size:11px;text-decoration:none;color:var(--azul2);background:#eef6ff;border:1px solid #cfe0f5;border-radius:6px;padding:2px 7px;margin:1px}
.leg{list-style:none;padding:0;margin:0}.leg li{padding:8px 0;border-bottom:1px dashed #d8e2ee;font-size:12.5px;line-height:1.5}
.leg li:last-child{border-bottom:none}
.chan{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.chan a{display:block;text-decoration:none;background:#f6f9fc;border:1px solid var(--line);border-radius:12px;padding:14px;color:var(--azul)}
.chan a:hover{background:#eef6ff}.chan b{display:block;font-size:14px}.chan span{font-size:11.5px;color:var(--mut)}
.src{font-size:11px;color:var(--mut);margin-top:8px}.src a{color:var(--azul2)}.src code{background:#eef2f7;padding:1px 5px;border-radius:4px}
.form{display:grid;gap:8px;max-width:640px}
.form input,.form textarea{width:100%;padding:9px 11px;border:1px solid var(--line);border-radius:9px;font-size:13px;font-family:inherit}
.form textarea{resize:vertical}
.form .btns{display:flex;gap:8px;flex-wrap:wrap}
.form button{border:none;border-radius:9px;padding:10px 16px;font-size:12.5px;font-weight:600;cursor:pointer}
.form .b1{background:var(--azul2);color:#fff}.form .b2{background:#eef6ff;color:var(--azul2);border:1px solid #cfe0f5}
.form .out{font-size:12px;margin-top:2px}.form .out.ok{color:#0b7a6f}.form .out.warn{color:#b45309}.form .out a{color:var(--azul2)}
.badge{display:inline-block;background:#e6f7f4;color:#0b7a6f;border:1px solid #bfe9e2;border-radius:20px;font-size:10.5px;padding:2px 9px;margin-left:6px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:10px}
</style></head><body>
<header><h1>🌐 Coordinación de Enlace con la Red Universitaria</h1><div class="s">Comunicación jurídica con los 19 Centros Universitarios, el SEMS y la Universidad Virtual · Art. 219 RIAG-UdeG</div></header>
__NAV__
<div class="wrap">

 <div class="card">
  <h2>📊 Estadística Institucional · Red Universitaria de Jalisco</h2>
  <div class="cap">Cifras oficiales verificadas. Fuente: Sistema Institucional de Estadísticas (SIE-UdeG) / CGPE, ciclo 2024-2025, corte 31-jul-2025.</div>
  <div class="kpis">__NUM__</div>
 </div>

 <div class="card">
  <h2>👥 Personal de la Red y representación sindical</h2>
  <div class="cap">Composición del personal administrativo (corte 2025) y los dos sindicatos titulares de los contratos colectivos de la Universidad.</div>
  <table><thead><tr><th>Categoría</th><th>Personas</th><th>Nota</th></tr></thead><tbody>
   <tr><td><b>Personal administrativo (total)</b></td><td>9,174</td><td>suma de confianza + sindicalizado</td></tr>
   <tr><td>· De confianza</td><td>2,737</td><td>dirección, inspección, vigilancia y fiscalización</td></tr>
   <tr><td>· Sindicalizado</td><td>6,437</td><td>representado por el SUTUdeG</td></tr>
   <tr><td>· Mandos medios y superiores</td><td><span style="color:#8090a5">subconjunto de confianza</span></td><td>puestos directivos (detalle por puesto en el Tabulador/Plantilla 2025; no publicado como total fijo)</td></tr>
   <tr><td>Personal académico</td><td>≈15,055</td><td>representado por el STAUdeG</td></tr>
  </tbody></table>
  <div class="chan" style="margin-top:12px">
   <a href="https://sutudeg.net/" target="_blank" rel="noopener"><b>🛠️ SUTUdeG</b><span>Sindicato Único de Trabajadores de la Universidad de Guadalajara — personal administrativo.</span></a>
   <a href="https://www.staudeg.org/" target="_blank" rel="noopener"><b>🎓 STAUdeG</b><span>Sindicato de Trabajadores Académicos de la Universidad de Guadalajara — personal académico.</span></a>
  </div>
  <div class="src">Fuentes: Coordinación General de Recursos Humanos / Coordinación de Transparencia (UdeG), «Resumen Personal Confianza-Sindicalizado 2025» y Tabulador/Plantilla 2025. Totales de administrativo validados por suma de dependencias. Mandos medios y superiores forman parte del personal de confianza; su conteo exacto no se publica como total consolidado (se detalla por puesto).</div>
 </div>

 <div class="card">
  <h2>🏛️ Directorio de la Red · Enlace jurídico por entidad</h2>
  <div class="cap">Canal de comunicación jurídica con cada Centro Universitario. Usa <b>Canal</b> (mensajería institucional) o <b>Turnar</b> (Oficialía de Partes) para dar trazabilidad a cada asunto.</div>
  <input id="cuBuscar" placeholder="🔍 Buscar centro universitario por sigla, nombre o sede…" oninput="filtrarCU()" style="width:100%;padding:9px 12px;border:1px solid var(--line);border-radius:9px;font-size:13px;margin-bottom:10px">
  <table><thead><tr><th>Sigla</th><th>Centro Universitario</th><th>Sede</th><th>Comunicación</th></tr></thead><tbody id="cuBody">__CUS__</tbody></table>
  <div id="cuVacio" style="display:none;font-size:12px;color:var(--mut);padding:8px 2px">Sin coincidencias.</div>
  <div class="src">19 Centros Universitarios (7 metropolitanos · 12 regionales, según agregado SIE). La clasificación metropolitano/regional de los centros de creación reciente puede variar entre fuentes oficiales; el directorio lista los 19 con su sede verificada.</div>
 </div>

 <div class="chan card">
  <h2>📡 Sistema de Educación Media Superior (SEMS) y Universidad Virtual</h2>
  <div class="cap" style="grid-column:1/-1">Además de los Centros Universitarios, la Coordinación enlaza al SEMS (177 planteles: 76 escuelas + 101 módulos) y al Sistema de Universidad Virtual.</div>
  <a href="mensajeria_SIGEJ.html"><b>🎓 SEMS · 177 planteles</b><span>Enlace jurídico con las preparatorias y módulos del bachillerato universitario.</span></a>
  <a href="mensajeria_SIGEJ.html"><b>💻 Universidad Virtual (SUV)</b><span>Enlace jurídico con la educación en línea de la Red.</span></a>
  <a href="gestion_SIGEJ.html"><b>🗂️ Gestión especializada</b><span>Investigación, programas, laboratorios y hospitales de la Red.</span></a>
 </div>

 <div class="card">
  <h2>⚖️ Fundamento normativo · Art. 219 RIAG-UdeG <span class="badge">verbatim verificado</span></h2>
  <div class="cap">Reglamento Interno de la Administración General de la Universidad de Guadalajara (versión Junio 2025). <b>Artículo 219.</b> Son atribuciones de la Coordinación de Enlace con la Red, las siguientes:</div>
  <ol class="leg" style="list-style:none">__ART219__</ol>
  <div class="src">Transcripción textual del PDF oficial: <a href="https://secgral.udg.mx/sites/default/files/Normatividad_especifica/RIAG%20(Junio%202025)_0.pdf" target="_blank" rel="noopener">RIAG (Junio 2025)</a>. La fracción <b>IX</b> es la base para coordinar a las instancias de asesoría jurídica de los Centros Universitarios y del SEMS. La Oficina de la Abogacía General se integra por 13 instancias (Art. 214 RIAG), entre ellas esta Coordinación.</div>
 </div>

 <div class="card">
  <h2>🌐 Canal externo · Dependencias y contrapartes</h2>
  <div class="cap">La Coordinación de Enlace <b>amplía su canal</b> más allá de la Red interna: las dependencias externas, contrapartes y ciudadanía se comunican y dan seguimiento a su <b>trámite autorizado</b> a través del <b>Portal de Seguimiento para usuarios externos</b> (por folio, sin usuario ni contraseña). El Portal de dependencias y contrapartes se movió aquí desde la pantalla de acceso.</div>
  <div class="chan">
   <a href="seguimiento_SIGEJ.html"><b>🌐 Portal de Seguimiento externo</b><span>Dependencias y contrapartes consultan el avance de su trámite por folio, sin contraseña.</span></a>
   <a href="instrumentos_SIGEJ.html"><b>🏢 Portal de dependencias y contrapartes</b><span>Alta y gestión de convenios e instrumentos con dependencias y contrapartes.</span></a>
   <a href="solicitud_convenios_SIGEJ.html"><b>📝 Solicitud de convenio</b><span>Portal externo de solicitud de convenios con carga de documentos (confidencial).</span></a>
  </div>
 </div>

 <div class="card">
  <h2>✉️ Contacto y solicitud de asesoría a la Coordinación</h2>
  <div class="cap">Contacta a la <b>Coordinación de Enlace con la Red</b> por <b>portal</b> (queda registrado con folio y trazabilidad) o por <b>correo</b> a <a href="mailto:abogral@udg.mx">abogral@udg.mx</a>. La búsqueda de centros está en el directorio de arriba.</div>
  <div class="form">
   <input id="ctNom" placeholder="Nombre y cargo">
   <input id="ctEnt" placeholder="Dependencia / Centro Universitario">
   <input id="ctMail" type="email" placeholder="Correo de contacto">
   <input id="ctAsu" placeholder="Asunto">
   <textarea id="ctMsg" rows="3" placeholder="Describe tu solicitud de asesoría jurídica…"></textarea>
   <div class="btns">
    <button class="b1" onclick="enviarPortal()">📨 Enviar por el portal (con folio)</button>
    <button class="b2" onclick="enviarCorreo()">✉️ Enviar por correo</button>
   </div>
   <div id="ctOut" class="out"></div>
  </div>
  <div class="src">El envío por portal se registra localmente (prototipo, clave <code>sigej_red_contacto</code>) y es trazable en Oficialía y Transparencia. El correo institucional de la Coordinación es <b>abogral@udg.mx</b>; la entrega/notificación automática se realiza en el backend.</div>
 </div>

 <div class="chan card">
  <h2>🔗 Trazabilidad y comunicación</h2>
  <div class="cap" style="grid-column:1/-1">Todo intercambio con la Red queda registrado para dar certeza jurídica.</div>
  <a href="oficialia_SIGEJ.html"><b>📨 Oficialía de Partes</b><span>Turnado y radicación de documentos hacia/desde cada CU y prepa, con folio.</span></a>
  <a href="mensajeria_SIGEJ.html"><b>💬 Mensajería institucional</b><span>Canales por centro universitario, con acuse de lectura y auditoría.</span></a>
  <a href="transparencia_general_SIGEJ.html"><b>📊 Transparencia General</b><span>Bitácora consolidada y rendición de cuentas de la Red.</span></a>
 </div>

</div>
<script>
function filtrarCU(){var q=(document.getElementById('cuBuscar').value||'').toLowerCase().trim();
 var rows=document.querySelectorAll('#cuBody tr');var vis=0;
 rows.forEach(function(r){var t=r.textContent.toLowerCase();var ok=!q||t.indexOf(q)>=0;r.style.display=ok?'':'none';if(ok)vis++;});
 document.getElementById('cuVacio').style.display=vis?'none':'block';}
function J(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function _v(id){return (document.getElementById(id).value||'').trim();}
function enviarPortal(){var nom=_v('ctNom'),ent=_v('ctEnt'),mail=_v('ctMail'),asu=_v('ctAsu'),msg=_v('ctMsg');
 var out=document.getElementById('ctOut');
 if(!nom||!asu||!msg){out.className='out warn';out.textContent='⚠️ Completa al menos nombre, asunto y mensaje.';return;}
 var arr=J('sigej_red_contacto');var d=new Date();
 var folio='RED-'+String(arr.length+1).padStart(4,'0')+'/'+d.getFullYear();
 arr.push({folio:folio,nombre:nom,entidad:ent,correo:mail,asunto:asu,mensaje:msg,fecha:d.toISOString().slice(0,10),estado:'Recibido'});
 localStorage.setItem('sigej_red_contacto',JSON.stringify(arr));
 out.className='out ok';out.innerHTML='✅ <b>Solicitud registrada</b> — Folio <b>'+folio+'</b>. Queda trazable ante la Coordinación de Enlace. Da seguimiento en el <a href="seguimiento_SIGEJ.html?folio='+encodeURIComponent(folio)+'">portal de seguimiento</a>.';
 ['ctNom','ctEnt','ctMail','ctAsu','ctMsg'].forEach(function(i){document.getElementById(i).value='';});}
function enviarCorreo(){var nom=_v('ctNom'),ent=_v('ctEnt'),asu=_v('ctAsu'),msg=_v('ctMsg');
 var out=document.getElementById('ctOut');
 var sub=encodeURIComponent('[Enlace con la Red] '+(asu||'Solicitud de asesoría'));
 var body=encodeURIComponent('Nombre y cargo: '+nom+'\nDependencia/CU: '+ent+'\n\n'+msg);
 // Correo institucional de la Coordinación de Enlace con la Red / Oficina de la Abogacía General.
 window.location.href='mailto:abogral@udg.mx?subject='+sub+'&body='+body;
 out.className='out ok';out.innerHTML='✉️ Se abrió tu gestor de correo con el mensaje prellenado, dirigido a <b>abogral@udg.mx</b> (Coordinación de Enlace con la Red).';}
</script>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
__SNIP__
</body></html>"""
out=(TPL.replace("__NAV__",NAV).replace("__NUM__",numHTML).replace("__CUS__",cuHTML)
        .replace("__ART219__",art219HTML).replace("__SNIP__",SNIP))
open(B+"red_universitaria_SIGEJ.html","w",encoding="utf-8").write(out)
print("red_universitaria_SIGEJ.html OK -",len(out),"bytes | CU:",len(CUS),"| frac219:",len(ART219))
