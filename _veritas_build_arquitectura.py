# -*- coding: utf-8 -*-
# PÁGINA DE REFERENCIA: Especificación técnica — Capa backend, seguridad e integraciones del SIGEJ (para el Área de Sistemas).
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Arquitectura/Backend'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','arquitectura_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="transparencia_general_SIGEJ.html">📊 Transparencia General</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Especificación técnica (backend e integraciones)</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#0b2540,#24476f);color:#fff;padding:18px 24px}
header h1{margin:0;font-size:20px}header .s{opacity:.85;font-size:12.5px;margin-top:4px}
.navbar{background:#081a30;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.wrap{max-width:1080px;margin:auto;padding:18px 22px 50px}
.bar{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:12px}
.toc{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-bottom:16px;font-size:12.5px;columns:2;column-gap:24px}
.toc a{color:var(--azul2);text-decoration:none;display:block;margin:2px 0}
.doc{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px 26px;box-shadow:0 1px 3px rgba(2,40,90,.06)}
.doc h2{color:var(--azul);font-size:17px;border-bottom:2px solid var(--line);padding-bottom:6px;margin:22px 0 10px}
.doc h3{color:var(--azul2);font-size:14px;margin:16px 0 6px}
.doc p,.doc li{font-size:13px;line-height:1.65;color:#243244}
.doc table{width:100%;border-collapse:collapse;font-size:12px;margin:8px 0}
.doc th{background:#f1f5f9;text-align:left;padding:6px 8px;border:1px solid var(--line);color:#334155;font-size:11px}
.doc td{padding:6px 8px;border:1px solid #eef2f7;vertical-align:top}
.pill{display:inline-block;border-radius:10px;padding:1px 8px;font-size:10.5px;font-weight:700}
.p-a{background:#fdeaea;color:#c0392b}.p-m{background:#fef3e2;color:#b45309}.p-b{background:#e6f6ee;color:#15803d}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:12px;margin:10px 0}
.b1{background:var(--azul2);color:#fff;font-weight:700;border:none;border-radius:9px;padding:9px 16px;cursor:pointer;font-size:13px}
.layer{border:1px solid var(--line);border-left:5px solid var(--teal);border-radius:9px;padding:9px 12px;margin:6px 0;font-size:12.5px}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:16px}
</style></head><body>
<header><h1>🏗️ SIGEJ-UdeG · Especificación técnica — Capa backend, seguridad e integraciones</h1><div class="s">Documento de arquitectura para el Área de Sistemas · de prototipo cliente a plataforma institucional de Legal Governance</div></header>
__NAV__
<div class="wrap">
 <div class="bar"><div style="font-size:12.5px;color:#64748b">Versión de trabajo · generado por SIGEJ-UdeG (Lexa &amp; Veritas). Ajústese con el Área de Sistemas.</div><button class="b1" onclick="wordDoc()">📄 Descargar especificación (Word)</button></div>
 <div class="toc" id="toc"></div>
 <div class="doc" id="doc">

<h2 id="s1">1. Resumen ejecutivo y estado actual</h2>
<p>El SIGEJ es hoy un <b>prototipo funcional del lado del cliente</b>: ~30 módulos HTML autocontenidos que persisten en <code>localStorage</code> del navegador, con control de acceso por perfil en la capa de interfaz. Esto valida procesos, flujos, indicadores y reglas de negocio, pero <b>no constituye un sistema de producción</b>: los datos viven en cada equipo, no hay autenticación real ni integración con los sistemas institucionales.</p>
<p>Esta especificación define la <b>capa de backend, seguridad e integraciones</b> necesaria para convertir el prototipo en una <b>plataforma institucional</b>, conservando la lógica y la experiencia ya construidas.</p>
<div class="note">Principio rector: <b>no reescribir lo validado</b>. El frontend actual (HTML/JS) puede conservarse conectándolo a una API; la lógica de negocio ya probada se traslada al servidor con el mismo modelo de datos.</div>

<h2 id="s2">2. Arquitectura objetivo (capas)</h2>
<div class="layer"><b>Presentación</b> — Frontend actual (HTML/JS) servido por el backend o migrado a SPA (React); mismos módulos y flujos. Consume API por HTTPS.</div>
<div class="layer"><b>API</b> — REST/GraphQL (Node.js/.NET/Python) con API Gateway; una API por dominio (contencioso, instrumentos, patrimonio, IAM, transparencia, etc.).</div>
<div class="layer"><b>Servicios de dominio</b> — Reglas de negocio (turnado, trazabilidad, alertas, cálculo de indicadores) migradas del cliente al servidor.</div>
<div class="layer"><b>Datos</b> — Base relacional (PostgreSQL/SQL Server); <b>almacén de objetos</b> (S3/Azure Blob) para documentos (hoy en base64); motor de <b>búsqueda</b> (OpenSearch/Elastic) + <b>base vectorial</b> para IA.</div>
<div class="layer"><b>Identidad</b> — OAuth2/OIDC con <b>SSO institucional</b> (Microsoft Entra ID / Google Workspace) + el módulo IAM como capa de RBAC/ABAC.</div>
<div class="layer"><b>Integración</b> — Conectores a sistemas UdeG y externos (ver §5) vía API Gateway / bus de eventos.</div>
<div class="layer"><b>Analítica</b> — Power BI / Microsoft Fabric embebido para tableros ejecutivos.</div>
<div class="layer"><b>Observabilidad y seguridad</b> — Bitácora inalterable, monitoreo, respaldos, cifrado, WAF.</div>

<h2 id="s3">3. Modelo de datos (inventario de módulos → tablas)</h2>
<p>Cada arreglo <code>localStorage</code> corresponde a una o varias tablas. Migración: exportar el JSON actual e importarlo al esquema relacional.</p>
<table><tr><th>Módulo</th><th>Claves localStorage (origen)</th><th>Tablas destino (sugerido)</th></tr>
<tr><td>Asuntos Contenciosos</td><td>juicios.tab (base 821 exp), sigej_masc, sigej_resp, sigej_asesoria, sigej_proyectos, sigej_actuaciones, sigej_derechoshumanos</td><td>expedientes, masc, responsabilidades, asesorias, proyectos, actuaciones, dh_recomendaciones</td></tr>
<tr><td>Instrumentos Jurídicos (CLM)</td><td>sigej_instrumentos, sigej_portal_dep/_contra</td><td>instrumentos, dependencias, contrapartes</td></tr>
<tr><td>Patrimonio Intangible</td><td>sigej_patrimonio, sigej_patrimonio_pub, sigej_ott</td><td>propiedad_intelectual, publicaciones, transferencia_tec</td></tr>
<tr><td>Patrimonio Inmobiliario</td><td>sigej_inmuebles, sigej_muebles_reg, sigej_contratos_inm</td><td>inmuebles, bienes_muebles, contratos_inmobiliarios</td></tr>
<tr><td>Asuntos Internacionales</td><td>sigej_internacional, sigej_int_movilidad</td><td>internacional, movilidad</td></tr>
<tr><td>Normatividad</td><td>sigej_normatividad, sigej_norma_repo/_resp/_bienes</td><td>normatividad, repositorio_normativo, resp_universitarias, desincorporacion</td></tr>
<tr><td>Conocimiento y Desarrollo</td><td>sigej_biblioteca, _prestamos, _conocimiento, _capacitacion, _invest, _difusion, _observatorio, _innovacion, _editorial</td><td>biblioteca, prestamos, conocimiento, capacitacion, investigacion, difusion, observatorio, innovacion, editorial</td></tr>
<tr><td>Gobierno de la Investigación</td><td>sigej_inv_investigadores/_cuerpos/_conflictos/_bioetica/_proyectos</td><td>investigadores, cuerpos_academicos, conflictos_interes, bioetica, inv_proyectos</td></tr>
<tr><td>Administración</td><td>sigej_adm_contable/_bienes/_personal/_viaticos/_papeleria/_requis/_proveedores; sigej_log_comisiones/_choferes/_vehiculos</td><td>contable, bienes, personal, viaticos, papeleria, requisiciones, proveedores, comisiones, choferes, vehiculos</td></tr>
<tr><td>Oficialía de Partes</td><td>sigej_oficialia, sigej_oficios</td><td>oficialia_recepcion, oficios</td></tr>
<tr><td>Transparencia</td><td>sigej_uti, sigej_transp_oblig, sigej_bitacora</td><td>solicitudes_uti, obligaciones_transp, bitacora_auditoria</td></tr>
<tr><td>Help Desk / IAM</td><td>sigej_helpdesk, _hd_cmdb/_sw/_kb/_sec; sigej_usuarios, _usuarios_audit, _iam_cupos/_lic/_seg, _exp_asig/_reasig</td><td>tickets, cmdb, software, kb, seguridad; usuarios, auditoria_usuarios, cupos, licencias, politicas_seg, asignaciones, reasignaciones</td></tr>
<tr><td>Mensajería</td><td>sigej_canales, _mensajes, _avisos, _msg_audit</td><td>canales, mensajes, avisos, mensajeria_audit</td></tr>
<tr><td>Sostenibilidad</td><td>sigej_sost_oblig/_cert/_proy</td><td>amb_obligaciones, amb_certificados, sost_proyectos</td></tr>
<tr><td>Hospitales y Salud</td><td>sigej_hosp_est/_conv/_resp</td><td>establecimientos_salud, convenios_salud, responsabilidad_sanitaria</td></tr>
<tr><td>Laboratorios</td><td>sigej_lab/_lab_mat/_lab_bio</td><td>laboratorios, materiales_peligrosos, bioseguridad</td></tr>
<tr><td>Programas Académicos · Servicio Social · Auditorías</td><td>sigej_programas, sigej_serviciosocial, sigej_auditorias</td><td>programas, ss_convenios, auditorias/observaciones</td></tr>
<tr><td>Transversales</td><td>sigej_notificaciones, sigej_perfil, sigej_bipdi_metas</td><td>notificaciones, sesiones, metas_pdi</td></tr>
</table>
<div class="note">Los <b>documentos</b> hoy se guardan como <code>data:base64</code> dentro del registro (límite 2 MB). En producción: subir a <b>almacén de objetos</b> y guardar solo la URL/metadatos + antivirus.</div>

<h2 id="s4">4. Seguridad e identidad (backend del módulo IAM)</h2>
<p>El módulo <b>Administración Central de Usuarios y Seguridad</b> ya define la política (usuarios, roles, matriz de 17 privilegios, cupos, licencias, auditoría). Falta su <b>enforcement real en el servidor</b>:</p>
<ul>
<li><b>Contraseñas</b>: hash con Argon2/bcrypt + salt; nunca en claro (hoy solo se marca <code>passSet</code>).</li>
<li><b>SSO + 2FA</b>: OIDC contra Microsoft Entra ID; segundo factor TOTP/push obligatorio para administradores.</li>
<li><b>Sesiones</b>: JWT de corta vida + refresh; <b>cierre remoto</b> real; expiración por inactividad; registro de dispositivos.</li>
<li><b>RBAC/ABAC</b>: la matriz de privilegios y la <b>segregación por adscripción</b> (coordinación/unidad/CU) se validan en cada endpoint, no solo se ocultan en el menú.</li>
<li><b>Bitácora inalterable</b>: append-only con encadenamiento por hash (o WORM); IP, equipo, navegador reales.</li>
<li><b>Restricciones</b>: por IP/rango, horario y ubicación (hoy parámetros; aplicarlas en el gateway).</li>
<li><b>Cupos y licencias</b>: validación de límites por módulo/sistema del lado servidor al crear usuarios.</li>
</ul>
<p><b>Normas de referencia</b>: ISO/IEC 27001 e ISO 27002, NIST Cybersecurity Framework, OWASP ASVS. <b>Datos personales</b>: LGPDPPSO / Ley de Protección de Datos de Jalisco — atención especial a <b>datos sensibles</b> (salud, víctimas/DH, biométricos): cifrado en reposo y en tránsito, minimización, anonimización (ya aplicada en DH y Hospitales) y control de acceso estricto.</p>

<h2 id="s5">5. Integraciones (priorizadas)</h2>
<table><tr><th>Sistema / servicio</th><th>Módulos SIGEJ</th><th>Propósito</th><th>Prioridad</th></tr>
<tr><td><b>SIIAU</b> (académico)</td><td>Legal por CU, Programas, Movilidad, BI PDI, Servicio Social</td><td>Catálogo de CU, matrícula, planes de estudio, personal</td><td><span class="pill p-a">Alta</span></td></tr>
<tr><td><b>SSO institucional</b> (Entra ID / Google)</td><td>IAM / todos</td><td>Autenticación única y 2FA</td><td><span class="pill p-a">Alta</span></td></tr>
<tr><td><b>Firma electrónica</b> (e.firma / institucional)</td><td>Instrumentos, Oficialía, Contratos, DH, Programas</td><td>Firma de convenios, oficios, acuses, resoluciones</td><td><span class="pill p-a">Alta</span></td></tr>
<tr><td><b>Plataforma Nacional de Transparencia (PNT/SIPOT)</b></td><td>Transparencia (Art. 8/14-Bis), UTI</td><td>Publicación y respuesta de obligaciones y solicitudes</td><td><span class="pill p-a">Alta</span></td></tr>
<tr><td><b>Power BI / Microsoft Fabric</b></td><td>Centro Ejecutivo, BI PDI, tableros</td><td>Tableros ejecutivos por rol/CU/eje PDI</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td><b>Microsoft 365 / Teams / correo</b></td><td>Mensajería, Notificaciones</td><td>Entrega de avisos, correo, chat, calendario</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td><b>COPLADI / indicadores PDI</b></td><td>BI PDI</td><td>Metas 2028/2031 y línea base oficiales</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td>serviciosocial.udg.mx</td><td>Servicio Social</td><td>Padrón y solicitud de convenios</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td>INDAUTOR / SEGOB</td><td>Publicaciones y Editorial</td><td>Reserva de derechos y licitud de título/contenido</td><td><span class="pill p-b">Baja</span></td></tr>
<tr><td>RPP / Catastro</td><td>Patrimonio Inmobiliario</td><td>Folios reales, certificados de gravamen</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td>COFEPRIS / SEMARNAT / PROFEPA / CONAGUA / SEDENA / CONBIOÉTICA / CNSNS</td><td>Sostenibilidad, Hospitales, Laboratorios</td><td>Licencias, permisos, RPBI, precursores, bioseguridad</td><td><span class="pill p-b">Baja</span></td></tr>
<tr><td>ASF / ASEJ / Contraloría</td><td>Auditorías</td><td>Observaciones y solventación</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td>CNDH / CEDHJ / CEAV / CEEAV</td><td>Recomendaciones DH</td><td>Quejas, recomendaciones, registro de víctimas</td><td><span class="pill p-m">Media</span></td></tr>
<tr><td>SNII-Secihti / PRODEP</td><td>Gobierno de la Investigación</td><td>Estatus de investigadores</td><td><span class="pill p-b">Baja</span></td></tr>
<tr><td>INM / SRE / consulados</td><td>Internacional / Movilidad</td><td>Visas, condición de estancia</td><td><span class="pill p-b">Baja</span></td></tr>
<tr><td>Archivo General / Repositorio institucional</td><td>Oficialía, Transparencia, Conocimiento</td><td>Gestión documental (ISO 15489) y disposición</td><td><span class="pill p-m">Media</span></td></tr>
</table>

<h2 id="s6">6. Inteligencia artificial y OCR</h2>
<p>Hoy el sistema aplica <b>heurísticas por reglas</b> (extracción por patrones, recomendaciones simples, predicción de vencimientos). En backend se sustituyen por servicios reales:</p>
<table><tr><th>Capacidad</th><th>Estado actual</th><th>Servicio backend</th></tr>
<tr><td>OCR de imágenes/PDF</td><td>Por reglas sobre texto pegado</td><td>Azure Document Intelligence / AWS Textract / Google Document AI</td></tr>
<tr><td>Búsqueda semántica</td><td>Palabras clave + filtros</td><td>Embeddings + base vectorial (pgvector / OpenSearch KNN)</td></tr>
<tr><td>Clasificación documental / extracción</td><td>Reglas</td><td>LLM + modelos entrenados</td></tr>
<tr><td>Generación/revisión de contratos</td><td>Cláusuloteca manual</td><td>LLM + cláusuloteca (RAG) con revisión humana</td></tr>
<tr><td>Predicción (vencimientos, riesgo, consumo)</td><td>Heurística</td><td>Modelos predictivos / Power BI + ML</td></tr>
<tr><td>Asistente jurídico</td><td>Chat sobre datos</td><td>RAG sobre el acervo con control de acceso</td></tr>
</table>
<div class="note">Toda IA sobre datos sensibles (salud, DH, personales) debe respetar el <b>control de acceso</b> y la <b>protección de datos</b>; no exponer datos personales a modelos externos sin base jurídica y anonimización.</div>

<h2 id="s7">7. Plan de migración por fases</h2>
<table><tr><th>Fase</th><th>Alcance</th><th>Resultado</th></tr>
<tr><td>0 · Cimientos</td><td>Esquema de base de datos desde el inventario (§3), almacén de objetos, entorno DevSecOps</td><td>Persistencia central</td></tr>
<tr><td>1 · Identidad</td><td>SSO OIDC + 2FA + IAM enforcement (RBAC/ABAC), bitácora inalterable</td><td>Acceso seguro y auditable</td></tr>
<tr><td>2 · API por dominio</td><td>Migrar la lógica de cada módulo a servicios + endpoints; conectar el frontend</td><td>Multiusuario real</td></tr>
<tr><td>3 · Documentos y búsqueda</td><td>Migrar base64 → objetos + antivirus; buscador + índice</td><td>Expediente electrónico institucional</td></tr>
<tr><td>4 · Integraciones prioritarias</td><td>SIIAU, Firma-e, PNT, Power BI, M365</td><td>Interoperabilidad núcleo</td></tr>
<tr><td>5 · Integraciones sectoriales</td><td>RPP, ASF/ASEJ, CNDH/CEDHJ, COFEPRIS/SEMARNAT/SEDENA, INDAUTOR, etc.</td><td>Cobertura completa</td></tr>
<tr><td>6 · IA</td><td>OCR real, búsqueda semántica, asistentes, predicción</td><td>Automatización</td></tr>
</table>

<h2 id="s8">8. Requisitos no funcionales y cumplimiento</h2>
<ul>
<li><b>Seguridad</b>: ISO 27001/27002, NIST CSF, OWASP ASVS; cifrado en reposo y tránsito; WAF; gestión de vulnerabilidades.</li>
<li><b>Protección de datos</b>: LGPDPPSO y Ley estatal; avisos de privacidad; datos sensibles cifrados y con acceso restringido; anonimización.</li>
<li><b>Gestión documental</b>: ISO 15489; catálogo de disposición y archivo (Art. 8 fr. XIII); versionamiento y trazabilidad.</li>
<li><b>Gobierno de TI</b>: COBIT; servicio ITIL v4 (ya modelado en Help Desk); BPMN 2.0 para los flujos.</li>
<li><b>Disponibilidad</b>: respaldos, recuperación ante desastres, alta disponibilidad; monitoreo y alertas.</li>
<li><b>Accesibilidad y calidad</b>: ISO 9001; accesibilidad web; auditoría de accesos y cambios.</li>
</ul>
<p style="font-size:11px;color:#64748b;margin-top:16px">Documento generado por SIGEJ-UdeG · Oficina de la Abogacía General · Coordinación de Enlace con la Red (Lexa &amp; Veritas). Es una guía de arquitectura; la selección de tecnologías y la calendarización corresponden al Área de Sistemas.</p>
 </div>
</div>
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
/* Tabla de contenido automática */
(function(){var hs=document.querySelectorAll('#doc h2');var t='';hs.forEach(function(h){t+='<a href="#'+h.id+'">'+h.textContent+'</a>';});document.getElementById('toc').innerHTML='<b style="color:#00254a;font-size:12px">Contenido</b>'+t;})();
function wordDoc(){var c=document.getElementById('doc').innerHTML;var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><meta charset="utf-8"><body style="font-family:Cambria">'+
 '<div style="text-align:center"><h2>UNIVERSIDAD DE GUADALAJARA · Oficina de la Abogacía General</h2><h3>SIGEJ · Especificación técnica — Capa backend, seguridad e integraciones</h3></div>'+c+'</body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='SIGEJ_Especificacion_Backend_Integraciones.doc';a.click();}
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"arquitectura_SIGEJ.html","w",encoding="utf-8").write(out)
print("arquitectura_SIGEJ.html OK -",len(out),"bytes")
