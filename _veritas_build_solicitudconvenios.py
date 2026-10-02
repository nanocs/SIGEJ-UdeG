# -*- coding: utf-8 -*-
# PORTAL EXTERNO · Solicitud de Convenios — dependencias y contrapartes solicitan un convenio y suben documentos.
# CONFIDENCIAL: los documentos y la solicitud SOLO se ven en este módulo (no se indexan en Buscador/Transparencia/Archivo).
# TRAZABILIDAD (metadatos, sin exponer documentos): Oficialía de Partes, Instrumentos Jurídicos, Convenios de Servicio Social.
B="/Users/edithroque/Documents/CLAUDE/"
HTML=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Solicitud de Convenios (portal externo)</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px}
header h1{margin:0;font-size:19px}header .s{opacity:.9;font-size:12px;margin-top:3px}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;gap:4px;padding:12px 18px 0;max-width:1100px;margin:auto;flex-wrap:wrap}
.tab{padding:9px 12px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1100px;margin:auto;padding:14px 18px 44px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);padding:20px;min-height:300px}
h2.h{margin:0 0 4px;color:var(--azul);font-size:18px}.lead{color:var(--mut);font-size:12.5px;margin:0 0 14px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px}
.f label{font-size:11px;color:var(--mut);display:block;margin-bottom:2px}
input,select,textarea{width:100%;font-family:inherit;font-size:13px;padding:9px;border:1px solid var(--line);border-radius:8px}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:9px 14px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;color:var(--mut);border-bottom:2px solid var(--line);padding:6px;font-size:11px}
td{border-bottom:1px solid #f1f5f9;padding:6px}tr.row{cursor:pointer}tr.row:hover{background:#f8fafc}
.bdg{padding:2px 8px;border-radius:10px;font-size:10.5px;font-weight:700}
.bdg.r{background:#fdeaea;color:#c0392b}.bdg.y{background:#fef3e2;color:#b45309}.bdg.g{background:#e6f6ee;color:#15803d}.bdg.n{background:#eef2f7;color:#475569}
.note{background:#eef6ff;border:1px solid #cfe0f5;color:#0a4d8c;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.conf{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:10px 0}
.ok{background:#e6f6ee;border:1px solid #b7e4c7;color:#15803d;border-radius:10px;padding:12px 14px;font-size:13px;margin-top:10px}
.drw{position:fixed;top:0;right:-620px;width:600px;max-width:96vw;height:100vh;background:#fff;box-shadow:-8px 0 30px rgba(0,0,0,.2);transition:.25s;overflow:auto;z-index:9500;padding:20px}
.drw.on{right:0}.drw .x{float:right;cursor:pointer;font-size:20px;color:#94a3b8}
.comp{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:11px;margin:8px 0;font-size:12.5px;line-height:1.6}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:12px}
input[type=file]{display:none}
</style></head><body>
<header><h1>📝 Solicitud de Convenios · Portal para dependencias y contrapartes</h1><div class="s">Presenta tu solicitud de convenio y adjunta la documentación. Uso externo · Oficina de la Abogacía General · UdeG</div></header>
<div class="navbar"><a href="acceso_SIGEJ.html">🔐 Acceso</a><a href="seguimiento_SIGEJ.html">🌐 Seguimiento de trámites</a><a href="solicitud_convenios_SIGEJ.html" class="act">📝 Solicitud de Convenios</a></div>
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<div class="drw" id="drw"><span class="x" onclick="closeDrw()">✕</span><div id="drwBody"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function val(i){var e=el(i);return e?(e.value||'').trim():'';}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
function hoy(){return new Date().toISOString().slice(0,10);}
function nowS(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function uid(){return 'sc'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
var PERFIL=localStorage.getItem('sigej_perfil')||'';
var INTERNO=!!PERFIL;
function SC(){return L('sigej_solicitud_convenios');}
var D={tipo:['Convenio general','Convenio específico','Convenio de colaboración','Convenio de servicio social','Convenio de prácticas profesionales','Intercambio académico','Intercambio estudiantil','Otro'],
 cu:['Rectoría General','Secretaría General','CUAAD','CUCBA','CUCEA','CUCEI','CUCS','CUCSH','CUCiénega','CUCosta','CUCostaSur','CUAltos','CULagos','CUNorte','CUSur','CUValles','CUTonalá','CUTlajomulco','SEMS','UDG Virtual','Otra dependencia UdeG']};

var TABS=INTERNO?[['nueva','📝 Nueva solicitud'],['consulta','🔎 Consultar folio'],['bandeja','📥 Bandeja (interno)']]:[['nueva','📝 Nueva solicitud'],['consulta','🔎 Consultar mi solicitud']];
var VIEW='nueva';
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;buildTabs();render();window.scrollTo(0,0);}
function render(){if(VIEW==='nueva')vNueva();else if(VIEW==='consulta')vConsulta();else vBandeja();}

function vNueva(){el('panel').innerHTML='<h2 class="h">📝 Nueva solicitud de convenio</h2><p class="lead">Completa los datos y adjunta la documentación. Al enviar recibirás un <b>folio</b> para dar seguimiento.</p>'+
  '<div class="conf">🔒 <b>Confidencialidad:</b> la información y los documentos de esta solicitud se resguardan <b>únicamente en este portal de Solicitud de Convenios</b>; no son visibles desde otros módulos del sistema.</div>'+
  '<div class="grid">'+
   '<div class="f"><label>Dependencia / institución solicitante *</label><input id="s_dep"></div>'+
   '<div class="f"><label>Contraparte / representante</label><input id="s_contra"></div>'+
   '<div class="f"><label>Tipo de convenio</label><select id="s_tipo">'+D.tipo.map(function(x){return '<option>'+x+'</option>';}).join('')+'</select></div>'+
   '<div class="f"><label>Dependencia UdeG involucrada</label><select id="s_cu">'+D.cu.map(function(x){return '<option>'+x+'</option>';}).join('')+'</select></div>'+
   '<div class="f"><label>Nombre de contacto *</label><input id="s_nom"></div>'+
   '<div class="f"><label>Correo de contacto *</label><input id="s_mail" type="email"></div>'+
   '<div class="f"><label>Teléfono</label><input id="s_tel"></div>'+
   '<div class="f" style="grid-column:1/-1"><label>Objeto / propósito del convenio *</label><textarea id="s_obj" rows="2"></textarea></div>'+
  '</div>'+
  '<div class="card" style="margin-top:10px"><b style="color:#0a4d8c">📎 Documentos adjuntos</b> <button class="bd mini" onclick="adj()">Adjuntar documento</button><div id="docList" style="margin-top:6px;font-size:12px;color:#64748b">Sin documentos aún (proyecto de convenio, acta constitutiva, poder, identificación, etc.).</div></div>'+
  '<div style="margin-top:10px"><button class="b3" onclick="enviar()">📨 Enviar solicitud</button> <span id="s_msg" style="font-size:12.5px"></span></div>'+
  '<div id="s_out"></div>';
 renderDocs();
}
var DOCS=[];
function adj(){el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>1.6e6){alert('Máximo 1.6 MB por archivo.');return;}var r=new FileReader();r.onload=function(){DOCS.push({nombre:f.name,tipo:f.type,data:r.result,fecha:hoy()});renderDocs();};r.readAsDataURL(f);};el('fileIn').click();}
function renderDocs(){var b=el('docList');if(!b)return;b.innerHTML=DOCS.length?DOCS.map(function(d,i){return '<div>📎 '+esc(d.nombre)+' <a href="#" onclick="DOCS.splice('+i+',1);renderDocs();return false;" style="color:#c0392b">quitar</a></div>';}).join(''):'Sin documentos aún.';}
function enviar(){var dep=val('s_dep'),nom=val('s_nom'),mail=val('s_mail'),obj=val('s_obj');
 var m=el('s_msg');if(!dep||!nom||!mail||!obj){m.style.color='#c0392b';m.textContent='Completa dependencia, contacto, correo y objeto.';return;}
 var A=SC();var folio='SOLC-'+(new Date().getFullYear())+'-'+String(A.length+1).padStart(4,'0');
 var o={id:uid(),folio:folio,dependencia:dep,contraparte:val('s_contra'),tipo:val('s_tipo'),cu:val('s_cu'),objeto:obj,
  contacto:{nombre:nom,correo:mail,tel:val('s_tel')},docs:DOCS.slice(),estado:'Recibida',fecha:nowS(),
  refs:{oficialia:'',instrumento:'',serviciosocial:''},traza:[{ts:nowS(),usuario:'Externo',accion:'Solicitud recibida'}]};
 A.push(o);S('sigej_solicitud_convenios',A);DOCS=[];
 el('s_out').innerHTML='<div class="ok">✅ <b>Solicitud enviada.</b> Tu folio de seguimiento es <b>'+folio+'</b>. Consérvalo para consultar el estado en la pestaña «Consultar». Te contactaremos al correo '+esc(mail)+'.<div style="margin-top:8px"><button class="b1 mini" onclick="acuse(\''+folio+'\')">🧾 Ver / imprimir acuse de recibo (con QR y sello)</button></div></div>';
 m.textContent='';el('s_dep').value='';el('s_nom').value='';el('s_mail').value='';el('s_obj').value='';el('s_contra').value='';el('s_tel').value='';renderDocs();
}
function vConsulta(){el('panel').innerHTML='<h2 class="h">🔎 Consultar mi solicitud</h2><p class="lead">Ingresa el folio que recibiste al enviar tu solicitud (formato SOLC-AAAA-####).</p>'+
  '<div style="display:flex;gap:8px;flex-wrap:wrap;max-width:520px"><input id="cq" placeholder="SOLC-2026-0001"><button class="b1" onclick="consultar()">Consultar</button></div><div id="c_out" style="margin-top:12px"></div>';}
function consultar(){var f=norm(val('cq'));var A=SC();var o=A.filter(function(x){return norm(x.folio)===f;})[0];var out=el('c_out');
 if(!o){out.innerHTML='<div class="note">No se encontró una solicitud con ese folio. Verifica el dato.</div>';return;}
 out.innerHTML='<div class="card"><b>'+esc(o.folio)+'</b> <span class="bdg '+estClass(o.estado)+'">'+esc(o.estado)+'</span><div style="margin-top:6px;font-size:12.5px"><b>Dependencia:</b> '+esc(o.dependencia)+'<br><b>Tipo:</b> '+esc(o.tipo)+'<br><b>Objeto:</b> '+esc(o.objeto)+'<br><b>Recibida:</b> '+esc(o.fecha)+'<br><b>Documentos adjuntos:</b> '+(o.docs||[]).length+'</div>'+
  '<div style="margin-top:8px"><b>Seguimiento:</b>'+ (o.traza||[]).map(function(t){return '<div style="font-size:11.5px;color:#64748b">'+t.ts+' — '+esc(t.accion)+'</div>';}).join('')+'</div>'+
  '<div style="margin-top:8px"><button class="b1 mini" onclick="acuse(\''+esc(o.folio)+'\')">🧾 Ver / imprimir acuse (con QR)</button></div></div>';}
function estClass(e){return /Aprob|Convertida|Atendida/.test(e)?'g':/Rechaz|Improceden/.test(e)?'r':/revisi|trámite|turnad/i.test(e)?'y':'n';}

/* ===== Bandeja interna + trazabilidad ===== */
function vBandeja(){var A=SC().map(function(x,i){return {x:x,i:i};});var q=norm(val('bq'));
 var rows=A.filter(function(o){return !q||norm(JSON.stringify(o.x)).indexOf(q)>=0;});
 el('panel').innerHTML='<h2 class="h">📥 Bandeja de solicitudes (interno)</h2><p class="lead">Revisión de solicitudes de convenio y su documentación (visible solo aquí). Turna a Oficialía o conviértela en instrumento / convenio de servicio social.</p>'+
  '<div style="display:flex;gap:8px;margin:6px 0 10px;flex-wrap:wrap"><input id="bq" value="'+esc(val('bq'))+'" placeholder="🔎 Buscar" oninput="render()" style="flex:1;min-width:180px"><button class="bd mini" onclick="acuseLista()">📄 Acuse por listado (Word)</button></div>'+
  '<table><tr><th>Folio</th><th>Dependencia</th><th>Tipo</th><th>Docs</th><th>Estado</th><th>Trazas</th></tr>'+
  (rows.length?rows.map(function(o){var x=o.x;var r=[];if(x.refs&&x.refs.oficialia)r.push('OF');if(x.refs&&x.refs.instrumento)r.push('INSTR');if(x.refs&&x.refs.serviciosocial)r.push('SS');return '<tr class="row" onclick="ficha('+o.i+')"><td>'+esc(x.folio)+'</td><td><b>'+esc(x.dependencia)+'</b></td><td style="font-size:11px">'+esc(x.tipo)+'</td><td>'+(x.docs||[]).length+'</td><td><span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></td><td style="font-size:10px;color:#0a4d8c">'+r.join(' · ')+'</td></tr>';}).join(''):'<tr><td colspan="6" style="text-align:center;color:#64748b;padding:16px">Sin solicitudes.</td></tr>')+'</table>';}
function ficha(i){var A=SC();var x=A[i];if(!x)return;
 var docs=(x.docs||[]).length?(x.docs||[]).map(function(d){return '<div style="font-size:11.5px">📎 '+esc(d.nombre)+' <a href="'+d.data+'" download="'+esc(d.nombre)+'">descargar</a></div>';}).join(''):'<span style="color:#64748b">Sin documentos.</span>';
 var tz=(x.traza||[]).map(function(t){return '<div style="font-size:11px;color:#64748b">'+t.ts+' · '+esc(t.usuario)+' — '+esc(t.accion)+'</div>';}).join('');
 var refs=x.refs||{};
 el('drwBody').innerHTML='<h2 style="margin:0 0 2px;color:#0a4d8c">'+esc(x.folio)+'</h2><div style="color:#64748b;font-size:12px;margin-bottom:8px">'+esc(x.tipo)+' <span class="bdg '+estClass(x.estado)+'">'+esc(x.estado)+'</span></div>'+
  '<div class="comp"><b>Dependencia:</b> '+esc(x.dependencia)+'<br><b>Contraparte:</b> '+esc(x.contraparte||'—')+'<br><b>Dependencia UdeG:</b> '+esc(x.cu||'—')+'<br><b>Contacto:</b> '+esc(x.contacto&&x.contacto.nombre||'—')+' · '+esc(x.contacto&&x.contacto.correo||'—')+' · '+esc(x.contacto&&x.contacto.tel||'—')+'<br><b>Objeto:</b> '+esc(x.objeto)+'</div>'+
  '<div class="comp"><b>📎 Documentos (confidenciales, solo aquí)</b><div style="margin-top:4px">'+docs+'</div></div>'+
  '<div class="comp"><b>🔗 Trazabilidad</b><div style="margin-top:6px;display:flex;gap:6px;flex-wrap:wrap">'+
   '<button class="bd mini" onclick="turnarOf('+i+')">📨 Turnar a Oficialía'+(refs.oficialia?' ✓':'')+'</button>'+
   '<button class="bd mini" onclick="aInstrumento('+i+')">📜 Convertir a Instrumento'+(refs.instrumento?' ✓':'')+'</button>'+
   '<button class="bd mini" onclick="aServicio('+i+')">🤝 Convertir a Convenio SS'+(refs.serviciosocial?' ✓':'')+'</button></div>'+
   '<div style="font-size:11px;color:#64748b;margin-top:5px">Se comparte solo el <b>metadato</b> (folio, dependencia, tipo, objeto); los documentos permanecen confidenciales en este portal.</div></div>'+
  '<div class="comp"><b>Estado</b> <span style="font-size:11px;color:#64748b">(Aprobada / Rechazada / Con requisitos → notifica al contacto por correo)</span><div style="margin-top:6px;display:flex;gap:5px;flex-wrap:wrap">'+['Recibida','En revisión jurídica','Con requisitos','Aprobada','Rechazada'].map(function(e){return '<button class="bd mini" onclick="setEst('+i+',\''+e+'\')">'+e+'</button>';}).join('')+'</div>'+(x.requisitos?'<div style="font-size:11.5px;color:#b45309;margin-top:5px"><b>Requisitos:</b> '+esc(x.requisitos)+'</div>':'')+'</div>'+
  '<div class="comp"><b>📄 Acuse</b> <button class="bd mini" onclick="acuse(\''+esc(x.folio)+'\')">🧾 Acuse de recibo (imprimible · QR y sello)</button> <span style="font-size:11px;color:#64748b">se abre para imprimir / guardar PDF</span></div>'+
  '<div class="comp"><b>🧾 Seguimiento</b><div style="margin-top:4px">'+tz+'</div></div>'+
  '<div style="margin-top:8px"><button class="bd" onclick="closeDrw()">Cerrar</button></div>';
 el('drw').classList.add('on');
}
function setEst(i,e){var A=SC();var x=A[i];var req='';
 if(e==='Con requisitos'){req=prompt('Requisitos / observaciones que debe subsanar el solicitante:','');if(req===null)return;x.requisitos=req;}
 x.estado=e;x.traza.push({ts:nowS(),usuario:PERFIL||'interno',accion:'Estado → '+e+(req?' ('+req+')':'')});
 // Trazabilidad a Oficialía de Partes (si está radicada)
 if(x.refs&&x.refs.oficialia){var O=L('sigej_oficios');for(var k=0;k<O.length;k++){if(O[k].folio===x.refs.oficialia){O[k].estatus=(e==='Aprobada'?'Concluido':e==='Rechazada'?'Cancelado':'En proceso');(O[k].traza=O[k].traza||[]).push({ts:nowS(),accion:'Solicitud '+x.folio+' → '+e,usuario:PERFIL||'interno',nota:req||''});break;}}S('sigej_oficios',O);}
 S('sigej_solicitud_convenios',A);
 if(/Aprobada|Rechazada|Con requisitos/.test(e))notificar(i,e,req);
 ficha(i);render();}
function notificar(i,e,req){var A=SC();var x=A[i];var correo=(x.contacto&&x.contacto.correo)||'';
 var estMsg=e==='Aprobada'?'ha sido APROBADA':e==='Rechazada'?'ha sido RECHAZADA':'requiere REQUISITOS / información adicional';
 x.traza.push({ts:nowS(),usuario:PERFIL||'interno',accion:'Notificación por correo a '+(correo||'(sin correo)')+' — '+e});S('sigej_solicitud_convenios',A);
 if(!correo){alert('El solicitante no registró correo; no se pudo notificar automáticamente.');return;}
 var body='Estimado(a) '+((x.contacto&&x.contacto.nombre)||'solicitante')+':\n\nSu solicitud de convenio con folio '+x.folio+' ('+x.dependencia+') '+estMsg+'.'+(req?'\n\nRequisitos / observaciones: '+req:'')+'\n\nPuede dar seguimiento con su folio en el portal de Solicitud de Convenios de la UdeG.\n\nCoordinación de Enlace con la Red · Oficina de la Abogacía General · Universidad de Guadalajara';
 window.location.href='mailto:'+correo+'?subject='+encodeURIComponent('[OAG-UdeG] Su solicitud de convenio '+x.folio+': '+e)+'&body='+encodeURIComponent(body);}
function acuse(folio){var A=SC();var x=null;for(var i=0;i<A.length;i++){if(A[i].folio===folio){x=A[i];break;}}if(!x){alert('Solicitud no encontrada.');return;}
 var of=(x.refs&&x.refs.oficialia)?x.refs.oficialia:'';
 var qr='SIGEJ|ACUSE|'+x.folio+'|'+x.dependencia+'|'+(x.fecha||'')+(of?'|OF:'+of:'');
 var sello=x.fecha||nowS();
 var rows=[['Folio de la solicitud',x.folio],['Fecha y hora de recepción',x.fecha||'—'],['Dependencia / institución solicitante',x.dependencia],['Contraparte / representante',x.contraparte||'—'],['Tipo de convenio',x.tipo],['Dependencia UdeG involucrada',x.cu||'—'],['Objeto',x.objeto],['Contacto',((x.contacto&&x.contacto.nombre)||'—')+' · '+((x.contacto&&x.contacto.correo)||'—')+' · '+((x.contacto&&x.contacto.tel)||'—')],['Documentos adjuntos',(x.docs||[]).length],['Estado actual',x.estado],['Radicado en Oficialía de Partes',of||'—']];
 if(x.requisitos)rows.push(['Requisitos indicados',x.requisitos]);
 var tr=rows.map(function(r){return '<tr><th style="width:38%">'+esc(r[0])+'</th><td>'+esc(String(r[1]))+'</td></tr>';}).join('');
 var w=window.open('','_blank','width=820,height=1000');if(!w){alert('Permite ventanas emergentes para ver/imprimir el acuse.');return;}
 var doc='<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Acuse '+esc(x.folio)+'</title>'+
  '<scr'+'ipt src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></scr'+'ipt>'+
  '<style>body{font-family:Cambria,Georgia,serif;color:#111;margin:0;padding:26px}.hoja{border:3px solid #00254a;border-radius:8px;padding:22px;max-width:730px;margin:auto}h1{font-size:15pt;text-align:center;color:#00254a;margin:0}h2{font-size:10.5pt;text-align:center;margin:2px 0 12px;font-weight:normal}.tit{text-align:center;font-size:12pt;font-weight:bold;color:#00254a;margin:6px 0}table{width:100%;border-collapse:collapse;font-size:10.5pt;margin-top:8px}th,td{border:1px solid #999;padding:5px 8px;text-align:left;vertical-align:top}th{background:#eef2f7;color:#00254a}.leg{text-align:justify;font-size:9.5pt;margin-top:12px;color:#333}.foot{display:flex;justify-content:space-between;align-items:center;margin-top:16px;gap:14px;flex-wrap:wrap}.qr{text-align:center}.qr .code{font-family:monospace;font-size:8pt;margin-top:3px;word-break:break-all;max-width:150px}.sello{border:3px double #0a6b52;color:#0a6b52;border-radius:10px;padding:8px 14px;text-align:center;transform:rotate(-7deg);font-weight:bold;font-size:11pt;line-height:1.3}.sello small{font-weight:normal;font-size:8pt;display:block}.firma{text-align:center;font-size:9pt}.pie{font-size:8pt;color:#555;text-align:center;margin-top:12px}button{margin:14px auto;display:block;padding:8px 18px;border:none;border-radius:8px;background:#0a4d8c;color:#fff;font-size:12pt;cursor:pointer}@media print{button{display:none}body{padding:0}}</style></head><body>'+
  '<button onclick="window.print()">🖨️ Imprimir / Guardar como PDF</button>'+
  '<div class="hoja"><h1>UNIVERSIDAD DE GUADALAJARA</h1><h2>Oficina de la Abogacía General · Coordinación de Enlace con la Red</h2>'+
  '<div class="tit">ACUSE DE RECIBO — SOLICITUD DE CONVENIO</div>'+
  '<table>'+tr+'</table>'+
  '<div class="leg">Se hace constar que la Oficina de la Abogacía General de la Universidad de Guadalajara <b>tiene por recibida</b> la solicitud de convenio antes referida, para su análisis jurídico. El presente acuse no prejuzga sobre la procedencia de la solicitud.</div>'+
  '<div class="foot"><div class="qr"><div id="qr"></div><div class="code">'+esc(qr)+'</div></div>'+
  '<div class="sello">RECIBIDO<small>Oficina de la Abogacía General · UdeG</small><small>Coordinación de Enlace con la Red</small><small>'+esc(sello)+'</small></div>'+
  '<div class="firma">_____________________<br>Recibió (nombre y firma)</div></div>'+
  '<div class="pie">Documento generado por SIGEJ-UdeG · '+nowS()+'. Verifique el folio mediante el código QR. Consulte el estado con su folio en el portal de Solicitud de Convenios.</div></div>'+
  '<scr'+'ipt>try{new QRCode(document.getElementById("qr"),{text:'+JSON.stringify(qr)+',width:112,height:112,correctLevel:QRCode.CorrectLevel.M});}catch(e){document.getElementById("qr").textContent="[QR: "+'+JSON.stringify(x.folio)+'+"]";}</scr'+'ipt>'+
  '</body></html>';
 w.document.write(doc);w.document.close();
 (function(){var B=SC();for(var i=0;i<B.length;i++){if(B[i].folio===folio){B[i].traza=B[i].traza||[];B[i].traza.push({ts:nowS(),usuario:PERFIL||'externo',accion:'Acuse de recibo generado (QR + sello de recepción)'});S('sigej_solicitud_convenios',B);break;}}})();}
function acuseLista(){var A=SC();if(!A.length){alert('No hay solicitudes registradas.');return;}
 var rows=A.map(function(x,i){return '<tr><td>'+(i+1)+'</td><td>'+esc(x.folio)+'</td><td>'+esc(x.dependencia)+'</td><td>'+esc(x.tipo)+'</td><td>'+esc((x.fecha||'').slice(0,10))+'</td><td>'+esc(x.estado)+'</td><td>'+esc((x.refs&&x.refs.oficialia)||'—')+'</td><td>'+((x.docs||[]).length)+'</td></tr>';}).join('');
 var head='<div style="text-align:center"><div style="font-size:13pt;font-weight:bold">UNIVERSIDAD DE GUADALAJARA</div><div style="font-size:11pt">Oficina de la Abogacía General · Coordinación de Enlace con la Red</div><div style="font-size:11.5pt;font-weight:bold;margin-top:6px">RELACIÓN DE SOLICITUDES DE CONVENIO RECIBIDAS</div></div>';
 var th='<tr style="background:#0a4d8c;color:#fff"><th>No.</th><th>Folio</th><th>Dependencia</th><th>Tipo</th><th>Fecha</th><th>Estado</th><th>Oficialía</th><th>Docs</th></tr>';
 var h='<html xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><style>body{font-family:Cambria,serif;font-size:10pt}table{border-collapse:collapse;width:100%;font-size:9pt}th,td{border:1px solid #999;padding:3px 5px;text-align:left}</style></head><body>'+head+'<hr><p style="font-size:10pt"><b>Fecha:</b> '+hoy()+' &nbsp; <b>Total:</b> '+A.length+' solicitud(es).</p><table>'+th+rows+'</table><br><br><table style="width:100%;border:none;font-size:10pt"><tr><td style="border:none;text-align:center">_____________________________<br>Coordinación de Enlace con la Red · Oficina de la Abogacía General</td></tr></table></body></html>';
 var b=new Blob(['﻿'+h],{type:'application/msword'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='relacion_solicitudes_convenio_'+hoy()+'.doc';a.click();}
function closeDrw(){el('drw').classList.remove('on');}
function turnarOf(i){var A=SC();var x=A[i];if(x.refs.oficialia){alert('Ya turnada a Oficialía: '+x.refs.oficialia);return;}
 var O=L('sigej_oficios');var of='OFI-'+(new Date().getFullYear())+'-'+String(O.length+1).padStart(4,'0');
 var yy=String(new Date().getFullYear());var verif='SC-'+Date.now().toString(36).toUpperCase();
 O.push({folio:of,verif:verif,serie:'USS',anio:yy,consec:O.length+1,via:'Recibido',tipo:'Solicitud de convenio',demi:x.dependencia,ddest:'Oficina de la Abogacía General',dest:'Coordinación de Enlace con la Red',cargo:'',area:'Coordinación de Enlace con la Red',capt:PERFIL||'interno',resp:'',asunto:'Solicitud de convenio · '+x.dependencia+' — '+(x.objeto||'').slice(0,60),desc:x.objeto||'',exp:[x.folio],prio:'Ordinaria',conf:'Confidencial',clas:'Solicitud de convenio',obs:'Origen: portal externo de Solicitud de Convenios ('+x.folio+'). Documentos confidenciales en ese portal.',kw:['convenio','solicitud'],fecha:hoy(),hora:'',sla:'',flimite:'',estatus:'Capturado',estHist:[{est:'Capturado',ts:nowS(),usuario:PERFIL||'interno'}],acuse:null,cc:[],turno:'',relaciones:[],docs:[],versiones:[],riesgos:[],ref:x.folio,traza:[{ts:nowS(),accion:'Ingreso desde Solicitud de Convenios',usuario:PERFIL||'interno',nota:x.folio}]});
 S('sigej_oficios',O);x.refs.oficialia=of;x.estado='Turnada a Oficialía';x.traza.push({ts:nowS(),usuario:PERFIL||'interno',accion:'Turnada a Oficialía ('+of+')'});S('sigej_solicitud_convenios',A);
 alert('📨 Turnada a Oficialía de Partes con folio '+of+' (solo metadatos; documentos confidenciales aquí).');ficha(i);render();}
function aInstrumento(i){var A=SC();var x=A[i];if(x.refs.instrumento){alert('Ya convertida en instrumento: '+x.refs.instrumento);return;}
 var I=L('sigej_instrumentos');var fo='INSTR-'+(new Date().getFullYear())+'-'+String(I.length+1).padStart(3,'0');
 I.push({folio:fo,fam:'Convenios',tipo:x.tipo||'Convenio',area:'OAG',dep:x.cu||x.dependencia,contra:x.dependencia,obj:x.objeto,monto:0,fuente:'No aplica',firma:'',ini:'',fin:'',estado:'Solicitud',resp:'',oblig:[],versiones:[{v:1,autor:PERFIL||'interno',fecha:hoy(),nota:'Alta desde Solicitud de Convenios ('+x.folio+')'}],bitacora:[{ts:nowS(),accion:'Creado desde Solicitud de Convenios '+x.folio,usuario:PERFIL||'interno'}],score:15,nivel:'Bajo',refSolicitud:x.folio});
 S('sigej_instrumentos',I);x.refs.instrumento=fo;x.traza.push({ts:nowS(),usuario:PERFIL||'interno',accion:'Convertida a Instrumento ('+fo+')'});S('sigej_solicitud_convenios',A);
 alert('📜 Instrumento '+fo+' creado (familia Convenios). Los documentos permanecen confidenciales en este portal.');ficha(i);render();}
function aServicio(i){var A=SC();var x=A[i];if(x.refs.serviciosocial){alert('Ya convertida en convenio SS: '+x.refs.serviciosocial);return;}
 var Y=L('sigej_serviciosocial');var fo='CSS-'+(new Date().getFullYear())+'-'+String(Y.length+1).padStart(3,'0');
 Y.push({id:uid(),folio:fo,dependencia:x.dependencia,sector:'Por clasificar',tipo:'Servicio social',cu:x.cu||'Red Universitaria',objeto:x.objeto,ini:'',fin:'',plazas:0,modalidad:'',resp:x.contacto&&x.contacto.nombre||'',respons:'',estado:'Solicitud',origen:'Solicitud de Convenios ('+x.folio+')',docs:[],traza:[{ts:nowS(),usuario:PERFIL||'interno',accion:'Alta desde Solicitud de Convenios '+x.folio}]});
 S('sigej_serviciosocial',Y);x.refs.serviciosocial=fo;x.traza.push({ts:nowS(),usuario:PERFIL||'interno',accion:'Convertida a Convenio SS ('+fo+')'});S('sigej_solicitud_convenios',A);
 alert('🤝 Convenio de Servicio Social '+fo+' creado. Los documentos permanecen confidenciales en este portal.');ficha(i);render();}
buildTabs();render();
</script>

<script>
/* SIGEJ · PWA + RWD (responsive, Mobile First) + modo oscuro — capa universal */
(function(){try{
var isEmbed=/[?&]embed=1/.test(location.search);
/* --- PWA: manifest + meta + service worker (instalable en iOS/iPadOS/Android sin tienda) --- */
if(!isEmbed){
 function meta(n,c){var m=document.createElement('meta');m.name=n;m.content=c;document.head.appendChild(m);}
 if(!document.querySelector('link[rel="manifest"]')){var l=document.createElement('link');l.rel='manifest';l.href='sigej.webmanifest';document.head.appendChild(l);}
 meta('theme-color','#00254a');meta('mobile-web-app-capable','yes');meta('apple-mobile-web-app-capable','yes');meta('apple-mobile-web-app-status-bar-style','black-translucent');meta('apple-mobile-web-app-title','SIGEJ');
 var al=document.createElement('link');al.rel='apple-touch-icon';al.href='sigej_icon.svg';document.head.appendChild(al);
 if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('sigej_sw.js').catch(function(){});});}
}
/* --- RWD: endurecimiento responsivo universal (no altera la maqueta de escritorio) --- */
var css=document.createElement('style');css.setAttribute('data-sigej','rwd');
css.textContent=[
 'img,video,canvas{max-width:100%;height:auto}',
 'html{-webkit-text-size-adjust:100%}',
 '@media (max-width:768px){',
 '  .navbar{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch}',
 '  .navbar a{white-space:nowrap}',
 '  button,.tb,.tab,.ootb,.navbar a{min-height:40px}',
 '  table{display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;white-space:nowrap}',
 '  .kpis,.cards,.apps{grid-template-columns:1fr!important}',
 '  .grid[style*="1fr 1fr"],.grid[style*="1.3fr"],.grid[style*="1.4fr"]{grid-template-columns:1fr!important}',
 '  .panel{width:100%!important}',
 '}',
 '@media (max-width:480px){ header h1{font-size:16px!important} .wrap{padding-left:10px!important;padding-right:10px!important} }',
 /* modo oscuro global por inversión controlada (se re-invierte multimedia para no dañar imágenes/QR/iframes) */
 'html.sigej-dark{filter:invert(0.92) hue-rotate(180deg);background:#0e1626}',
 'html.sigej-dark img,html.sigej-dark canvas,html.sigej-dark iframe,html.sigej-dark video,html.sigej-dark svg,html.sigej-dark .cov,html.sigej-dark .fichacov,html.sigej-dark .acuse .q img{filter:invert(1) hue-rotate(180deg)}',
 '#sigejDark{position:fixed;left:16px;bottom:16px;z-index:99990;background:#0a4d8c;color:#fff;border:none;border-radius:50%;width:42px;height:42px;font-size:18px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.3)}'
].join('\n');
document.head.appendChild(css);
if(localStorage.getItem('sigej_dark')==='1')document.documentElement.classList.add('sigej-dark');
if(!isEmbed){
 var db=document.createElement('button');db.id='sigejDark';db.type='button';db.title='Modo claro / oscuro';db.textContent=localStorage.getItem('sigej_dark')==='1'?'☀️':'🌙';
 db.onclick=function(){var on=document.documentElement.classList.toggle('sigej-dark');localStorage.setItem('sigej_dark',on?'1':'0');db.textContent=on?'☀️':'🌙';};
 if(document.body)document.body.appendChild(db);
}
}catch(e){}})();
</script>

<script>
/* SIGEJ · Panel universal "Normativa aplicable" (asistente jurídico normativo por pantalla) */
(function(){try{
if(/[?&]embed=1/.test(location.search))return;
var pk=(location.pathname.split('/').pop()||'x').replace('.html','')||'x';
if(/^(index|acceso_SIGEJ|SIGEJ_inicio)$/.test(pk))return;if(!document.body)return;
function J(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function ec(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
var DEF=[
 {amb:'Interna',cat:'Contratos',nombre:'Normatividad de Contratos',url:'https://secgral.udg.mx/normatividad/contratos',mods:['instrumentos_SIGEJ']},
 {amb:'Interna',cat:'Contratos',nombre:'Empresa Universitaria',url:'https://secgral.udg.mx/normatividad/contratos/empresa-universitaria',mods:['instrumentos_SIGEJ','patrimonio_SIGEJ']},
 {amb:'Interna',cat:'Acuerdos',nombre:'Acuerdos de Rectoría General',url:'https://secgral.udg.mx/acuerdos/rectoria-general',mods:[]},
 {amb:'Interna',cat:'Acuerdos',nombre:'Acuerdos Comisión de Hacienda',url:'https://secgral.udg.mx/acuerdos/comision-de-hacienda',mods:['instrumentos_SIGEJ','administracion_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Comisión de Hacienda',url:'https://secgral.udg.mx/circulares/comision-de-hacienda',mods:['administracion_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Comisión de Responsabilidades y Sanciones',url:'https://secgral.udg.mx/circulares/comision-de-responsabilidades-y-sanciones',mods:['contencioso_SIGEJ','resp_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Rectoría General',url:'https://secgral.udg.mx/circulares/rectoria-general',mods:[]},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Secretaría General',url:'https://secgral.udg.mx/circulares/secretaria-general',mods:['oficialia_SIGEJ']},
 {amb:'Interna',cat:'Circulares',nombre:'Circulares Anuales',url:'https://secgral.udg.mx/circulares-anuales',mods:[]},
 {amb:'Interna',cat:'Normatividad',nombre:'Normatividad General',url:'https://secgral.udg.mx/normatividad/general',mods:['normatividad_SIGEJ','instrumentos_SIGEJ','contencioso_SIGEJ']},
 {amb:'Interna',cat:'Normatividad',nombre:'Normatividad Específica',url:'https://secgral.udg.mx/normatividad/especifica',mods:['normatividad_SIGEJ']},
 {amb:'Interna',cat:'Órganos colegiados',nombre:'Sesiones del CGU',url:'http://www.hcgu.udg.mx/sesioneshcgu',mods:['normatividad_SIGEJ']},
 {amb:'Interna',cat:'Órganos colegiados',nombre:'Dictámenes del CGU',url:'http://www.hcgu.udg.mx/dictamenes',mods:['normatividad_SIGEJ','instrumentos_SIGEJ']},
 {amb:'Interna',cat:'Órganos colegiados',nombre:'Sesiones de Comisiones',url:'http://www.hcgu.udg.mx/sesiones-de-comisiones',mods:['normatividad_SIGEJ']},
 {amb:'Externa',cat:'Federal',nombre:'Legislación Federal (Diputados)',url:'https://www.diputados.gob.mx/LeyesBiblio/index.htm',mods:['instrumentos_SIGEJ','contencioso_SIGEJ','internacional_SIGEJ','patrimonio_SIGEJ']},
 {amb:'Externa',cat:'Federal',nombre:'Reglamentos Federales',url:'https://www.diputados.gob.mx/LeyesBiblio/regla.htm',mods:['instrumentos_SIGEJ','contencioso_SIGEJ']},
 {amb:'Externa',cat:'Estatal',nombre:'Legislación de Jalisco',url:'https://congresoweb.congresojal.gob.mx/BibliotecaVirtual/LeyesEstatales.cfm',mods:['contencioso_SIGEJ','instrumentos_SIGEJ','oficialia_SIGEJ']},
 {amb:'Externa',cat:'NOM',nombre:'Normas Oficiales Mexicanas',url:'https://platiica.economia.gob.mx/normalizacion/normas-oficiales-mexicanas/',mods:['patrimonio_SIGEJ','internacional_SIGEJ']}
];
function REPO(){var r=J('sigej_repo_normativo');return Array.isArray(r)&&r.length?r:DEF;}
var base=pk;
var rel=REPO().filter(function(x){return (x.mods||[]).indexOf(base)>=0;});
var gen=REPO().filter(function(x){return !(x.mods||[]).length&&x.amb==='Interna';});
var b=document.createElement('div');b.textContent='📖 Normativa';
b.style.cssText='position:fixed;right:16px;bottom:100px;background:#5a2e8c;color:#fff;padding:9px 14px;border-radius:22px;font:600 12.5px system-ui,sans-serif;cursor:pointer;z-index:99994;box-shadow:0 4px 14px rgba(0,0,0,.25)';
var p=document.createElement('div');
p.style.cssText='position:fixed;right:16px;bottom:146px;width:360px;max-width:94vw;max-height:74vh;background:#fff;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 12px 34px rgba(0,0,0,.3);z-index:99995;display:none;flex-direction:column;overflow:hidden';
document.body.appendChild(b);document.body.appendChild(p);
function link(x){return '<a href="'+ec(x.url)+'" target="_blank" rel="noopener" style="display:flex;gap:7px;align-items:center;padding:7px 9px;border:1px solid #eef2f7;border-radius:8px;margin-bottom:5px;text-decoration:none;color:#0a2f4f;font:12px system-ui,sans-serif"><span>'+(x.amb==='Interna'?'🏛️':'🌐')+'</span><span>'+ec(x.nombre)+'</span><span style="margin-left:auto;font-size:10px;color:#94a3b8">↗</span></a>';}
function render(){p.innerHTML='<div style="background:#5a2e8c;color:#fff;padding:9px 12px;font:700 13px system-ui,sans-serif;display:flex;justify-content:space-between;align-items:center"><span>📖 Normativa aplicable</span><span id="__nx" style="cursor:pointer;font-size:16px">✕</span></div><div style="overflow:auto;padding:10px 12px;flex:1">'+
 (rel.length?'<div style="font:600 11px system-ui,sans-serif;color:#5a2e8c;margin-bottom:5px">RELACIONADA CON ESTE MÓDULO</div>'+rel.map(link).join(''):'<div style="font:12px system-ui,sans-serif;color:#94a3b8;margin-bottom:6px">Sin normas mapeadas específicamente a este módulo.</div>')+
 '<div style="font:600 11px system-ui,sans-serif;color:#5a2e8c;margin:8px 0 5px">NORMATIVIDAD INSTITUCIONAL</div>'+gen.slice(0,5).map(link).join('')+
 '<a href="cumplimiento_SIGEJ.html" style="display:block;text-align:center;margin-top:8px;background:#0a4d8c;color:#fff;border-radius:8px;padding:8px;text-decoration:none;font:600 12px system-ui,sans-serif">⚖️ Abrir Motor de Cumplimiento</a>'+
 '<div style="font:10.5px system-ui,sans-serif;color:#64748b;margin-top:8px">Repositorio administrado por la Coordinación de Normatividad. Términos y plazos conforme a la ley aplicable.</div></div>';
 p.querySelector('#__nx').onclick=function(){p.style.display='none';};}
b.onclick=function(){var o=p.style.display!=='none';if(o){p.style.display='none';}else{render();p.style.display='flex';}};
}catch(e){}})();
</script>
</body></html>"""
open(B+"solicitud_convenios_SIGEJ.html","w",encoding="utf-8").write(HTML)
print("solicitud_convenios_SIGEJ.html OK -",len(HTML),"bytes")
