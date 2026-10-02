# -*- coding: utf-8 -*-
# MÓDULO: Chat y Mensajería interna del SIGEJ (Teams/Slack/Mattermost-like, sector público).
# Directos, canales por coordinación/unidad/expediente/módulo, avisos institucionales con acuse, adjuntos, auditoría.
# Usa el directorio de usuarios del IAM (sigej_usuarios). Cliente, localStorage, self-contained.
import re
B="/Users/edithroque/Documents/CLAUDE/"
_src=open(B+"_veritas_build_administracion.py",encoding="utf-8").read()
SNIP=re.search(r'SNIP=r"""(.*?)"""',_src,re.S).group(1)
SNIP=SNIP.replace("modulo:'Administración OAG'","modulo:'Mensajería'")
SNIP=SNIP.replace("'oficialia_SIGEJ',","'oficialia_SIGEJ','mensajeria_SIGEJ',")

NAV='''<div class="navbar"><a href="SIGEJ_inicio.html">🏠 Inicio</a><a href="archivo_SIGEJ.html">🗄️ Archivo</a><a href="seguimientos_SIGEJ.html">🧭 Seguimientos</a><a href="red_universitaria_SIGEJ.html">🌐 Enlace con la Red</a><a href="gestion_SIGEJ.html">🗂️ Gestión</a><a href="centro_ejecutivo_SIGEJ.html">🧭 Centro Ejecutivo</a><a href="mensajeria_SIGEJ.html" class="act">💬 Mensajería</a><a href="notificaciones_SIGEJ.html">📬 Notificaciones</a><a href="helpdesk_SIGEJ.html">🛠️ Help Desk</a><a href="oficialia_SIGEJ.html">📨 Oficialía</a><a href="buscador_SIGEJ.html">🔍 Buscador</a></div>'''

TPL=r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SIGEJ-UdeG · Mensajería institucional</title>
<style>
:root{--azul:#00254a;--azul2:#0a4d8c;--teal:#1aa39a;--gold:#d4a32c;--ok:#1f9d6b;--amber:#e08e0b;--red:#c0392b;--ink:#0a1f3c;--mut:#64748b;--line:#e2e8f0;--bg:#eef2f7;}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--ink)}
header{background:linear-gradient(120deg,#00254a,#0a4d8c);color:#fff;padding:16px 22px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px}
header h1{margin:0;font-size:19px}header .s{opacity:.85;font-size:12px;margin-top:3px}
.me{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);border-radius:20px;padding:5px 10px;font-size:12px;color:#fff}
.me select{background:transparent;border:none;color:#fff;font-size:12px}
.me select option{color:#0a1f3c}
.navbar{background:#00203f;display:flex;flex-wrap:wrap;gap:2px;padding:6px 14px}
.navbar a{color:#c2d2e8;text-decoration:none;font-size:12.5px;padding:6px 10px;border-radius:7px}
.navbar a:hover,.navbar a.act{background:rgba(255,255,255,.12);color:#fff}
.tabs{display:flex;gap:4px;padding:10px 16px 0;max-width:1280px;margin:auto;flex-wrap:wrap}
.tab{padding:8px 13px;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;background:#fff;cursor:pointer;font-size:12.5px}
.tab.on{background:var(--azul2);color:#fff;font-weight:700}
.wrap{max-width:1280px;margin:auto;padding:0 16px 40px}
.panel{background:#fff;border-radius:0 12px 12px 12px;box-shadow:0 1px 3px rgba(2,40,90,.07);min-height:440px}
.chatwrap{display:grid;grid-template-columns:270px 1fr;min-height:440px}
.side{border-right:1px solid var(--line);padding:10px;overflow:auto;max-height:560px}
.side h4{margin:8px 4px 4px;font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}
.conv{padding:8px 10px;border-radius:9px;cursor:pointer;font-size:13px;display:flex;justify-content:space-between;align-items:center;gap:6px}
.conv:hover{background:#f1f5f9}.conv.on{background:#e6f0fb}
.conv .b{background:var(--red);color:#fff;border-radius:10px;font-size:10px;padding:0 6px;font-weight:700}
.thread{display:flex;flex-direction:column;max-height:560px}
.thead{padding:11px 14px;border-bottom:1px solid var(--line);font-weight:700;color:var(--azul);display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.msgs{flex:1;overflow:auto;padding:14px;background:#f8fafc;min-height:280px}
.msg{max-width:74%;margin:6px 0;padding:9px 12px;border-radius:12px;font-size:13px;line-height:1.5;box-shadow:0 1px 2px rgba(2,40,90,.08)}
.msg.mine{background:#d9f0ea;margin-left:auto}.msg.other{background:#fff}
.msg .meta{font-size:10px;color:var(--mut);margin-top:4px}
.msg .who{font-size:11px;font-weight:700;color:var(--azul2);margin-bottom:2px}
.chip{display:inline-block;background:#eef2f7;border:1px solid var(--line);border-radius:11px;padding:1px 8px;font-size:10.5px;margin:1px}
.compose{border-top:1px solid var(--line);padding:10px;display:flex;flex-direction:column;gap:6px}
.compose .row{display:flex;gap:6px;flex-wrap:wrap}
.compose input,.compose textarea,.compose select{border:1px solid var(--line);border-radius:8px;padding:8px;font-size:13px;font-family:inherit}
.compose textarea{flex:1;min-height:44px;resize:vertical}
button{font-family:inherit;cursor:pointer;border:none;border-radius:8px;font-size:13px;padding:8px 13px}
.b1{background:var(--azul2);color:#fff;font-weight:700}.b3{background:var(--ok);color:#fff;font-weight:700}.bd{background:#e2e8f0;color:#0a1f3c}.mini{padding:6px 10px;font-size:12px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;padding:16px}
.kpi{background:#f8fafc;border:1px solid var(--line);border-radius:11px;padding:13px}
.kpi .n{font-size:23px;font-weight:800;color:var(--azul)}.kpi .l{font-size:11px;color:var(--mut);margin-top:2px}
.kpi.g .n{color:var(--ok)}.kpi.r .n{color:var(--red)}.kpi.y .n{color:var(--amber)}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin:14px}
.aviso{border-left:5px solid var(--azul2);background:#f8fafc;border-radius:10px;padding:11px 13px;margin:10px 14px;font-size:13px}
.aviso.urg{border-left-color:var(--red)}.aviso.obl{border-left-color:var(--amber)}
.pill{font-size:10px;font-weight:700;border-radius:10px;padding:1px 8px}.pill.r{background:#fdeaea;color:#c0392b}.pill.g{background:#e6f6ee;color:#15803d}.pill.y{background:#fef3e2;color:#b45309}
.note{background:#fff8e6;border:1px solid #e7c66b;color:#8a6d1a;border-radius:9px;padding:9px 12px;font-size:11.5px;margin:12px 14px}
.empty{color:var(--mut);font-size:13px;padding:30px;text-align:center}
footer{background:#e8731c;color:#fff;border-top:3px solid #c75e10;text-align:center;font-size:11.5px;padding:14px;margin-top:14px}
input[type=file]{display:none}
</style></head><body>
<header><div><h1>💬 Mensajería institucional SIGEJ</h1><div class="s">Comunicación segura, segmentada y trazable · necesidad de conocer · confidencialidad · Oficina de la Abogacía General</div></div>
<div class="me">👤 Yo: <select id="meSel" onchange="setMe()"></select></div></header>
__NAV__
<div class="tabs" id="tabs"></div>
<div class="wrap"><div class="panel" id="panel"></div></div>
<input type="file" id="fileIn">
<footer>Oficina de la Abogacía General · Coordinación de Enlace con la Red · abogral@udg.mx · (Lexa &amp; Veritas)</footer>
<script>
function el(i){return document.getElementById(i);}
function L(k){try{return JSON.parse(localStorage.getItem(k)||'[]');}catch(e){return [];}}
function S(k,a){localStorage.setItem(k,JSON.stringify(a));}
function uid(){return 'm'+Math.abs(Date.now()^(performance.now()*1000|0)).toString(36);}
function now(){return new Date().toISOString().slice(0,19).replace('T',' ');}
function hoy(){return new Date().toISOString().slice(0,10);}
function esc(s){return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
/* Directorio: usa los usuarios del IAM (sigej_usuarios); si no hay, sintetiza desde el perfil */
function users(){var U=L('sigej_usuarios').filter(function(u){return u.estado==='Activo';});if(!U.length){U=[{id:'self',nombre:localStorage.getItem('sigej_perfil')||'Usuario',rol:localStorage.getItem('sigej_perfil')||'Usuario',tipo:'Interno OAG',coord:'OAG',area:'—'}];}return U;}
function userById(id){var u=users().filter(function(x){return x.id===id;})[0];return u||{id:id,nombre:'(usuario)',rol:''};}
function meId(){var id=localStorage.getItem('sigej_msg_me');var U=users();if(id&&U.some(function(u){return u.id===id;}))return id;
 var p=localStorage.getItem('sigej_perfil');var m=U.filter(function(u){return u.rol===p;})[0]||U[0];localStorage.setItem('sigej_msg_me',m.id);return m.id;}
function ME(){return userById(meId());}
function setMe(){localStorage.setItem('sigej_msg_me',el('meSel').value);CUR=null;render();}
function fillMe(){var m=meId();el('meSel').innerHTML=users().map(function(u){return '<option value="'+u.id+'"'+(u.id===m?' selected':'')+'>'+esc(u.nombre)+' — '+esc(u.rol)+'</option>';}).join('');}
/* Permisos de envío (Art. III) */
function puedeAviso(u){return /Administrador|^Sistemas$|Jefe del Área de Sistemas|Jefe del Área de Personal|Director|Coordinador|Jefe|Abogado General|Secretaría/.test(u.rol||'');}
function puedeCanal(u){return puedeAviso(u);}
/* Canales (Art. IV): se siembran por coordinación/módulo */
function seedCanales(){if(localStorage.getItem('sigej_canales'))return;var U=users();
 function miembros(f){return U.filter(f).map(function(u){return u.id;});}
 var admins=function(u){return /Administrador|Jefe del Área de Sistemas/.test(u.rol);};
 var C=[
  {id:'c_gen',nombre:'📣 General OAG',desc:'Canal institucional para todo el personal',confid:'Institucional',modulo:'',admin:'Administrador',miembros:U.map(function(u){return u.id;})},
  {id:'c_cont',nombre:'⚔️ Coordinación de lo Contencioso',desc:'Asuntos contenciosos y litigio',confid:'Restringido',modulo:'contencioso',admin:'Coordinador Jurídico',miembros:miembros(function(u){return /Contencioso|Litig|Laboral|Civil/.test((u.coord||'')+(u.area||''))||admins(u);})},
  {id:'c_hd',nombre:'🛠️ Help Desk',desc:'Soporte técnico y sistemas',confid:'Restringido',modulo:'helpdesk',admin:'Jefe del Área de Sistemas',miembros:miembros(function(u){return /Sistemas|Help Desk/.test((u.area||'')+(u.tipo||''))||admins(u);})},
  {id:'c_inst',nombre:'📜 Instrumentos Jurídicos',desc:'Convenios y contratos',confid:'Restringido',modulo:'instrumentos',admin:'Jefe de Unidad de Instrumentos Jurídicos',miembros:miembros(admins)}
 ];S('sigej_canales',C);}
function canales(){return L('sigej_canales');}
function misCanales(){var id=meId();return canales().filter(function(c){return (c.miembros||[]).indexOf(id)>=0;});}
/* Auditoría de comunicación (Art. XI) */
function msgAudit(accion,detalle){var A=L('sigej_msg_audit');A.push({ts:now(),actor:ME().nombre,accion:accion,detalle:(detalle||'').slice(0,120)});S('sigej_msg_audit',A);if(window.__bitlog)__bitlog('Comunicación',accion+': '+(detalle||''));}

var TABS=[['conv','💬 Conversaciones'],['avisos','📢 Avisos institucionales'],['buscar','🔎 Búsqueda'],['tablero','📊 Tablero']];
var VIEW='conv',CUR=null;
function buildTabs(){el('tabs').innerHTML=TABS.map(function(t){return '<div class="tab'+(t[0]===VIEW?' on':'')+'" onclick="goV(\''+t[0]+'\')">'+t[1]+'</div>';}).join('');}
function goV(v){VIEW=v;CUR=null;buildTabs();render();}
function render(){seedCanales();fillMe();if(VIEW==='conv')vConv();else if(VIEW==='avisos')vAvisos();else if(VIEW==='buscar')vBuscar();else vTablero();}

/* ---------- Conversaciones ---------- */
function dmKey(a,b){return [a,b].sort().join('~');}
function msgs(){return L('sigej_mensajes').filter(function(m){return !m.borrado;});}
function convList(){var id=meId();var list=[];
 misCanales().forEach(function(c){var unread=msgs().filter(function(m){return m.canal===c.id&&m.from!==id&&(m.leidoPor||[]).indexOf(id)<0;}).length;list.push({k:'canal:'+c.id,nombre:c.nombre,unread:unread,tipo:'canal'});});
 var dms={};msgs().forEach(function(m){if(m.tipo!=='dm')return;if(m.from!==id&&(m.to||[]).indexOf(id)<0)return;var other=m.from===id?(m.to||[])[0]:m.from;if(!other)return;dms[other]=dms[other]||{unread:0};if(m.from!==id&&(m.leidoPor||[]).indexOf(id)<0)dms[other].unread++;});
 Object.keys(dms).forEach(function(o){list.push({k:'dm:'+o,nombre:'💬 '+userById(o).nombre,unread:dms[o].unread,tipo:'dm'});});
 return list;}
function vConv(){var id=meId();var me=ME();if(!CUR){var mc=misCanales();CUR=mc.length?('canal:'+mc[0].id):null;}
 var cl=convList();
 var side='<h4>Canales</h4>'+misCanales().map(function(c){var un=cl.filter(function(x){return x.k==='canal:'+c.id;})[0];var u=un?un.unread:0;return '<div class="conv'+(CUR==='canal:'+c.id?' on':'')+'" onclick="openConv(\'canal:'+c.id+'\')"><span>'+esc(c.nombre)+'</span>'+(u?'<span class="b">'+u+'</span>':'')+'</div>';}).join('');
 side+='<h4>Directos</h4>'+cl.filter(function(x){return x.tipo==='dm';}).map(function(x){return '<div class="conv'+(CUR===x.k?' on':'')+'" onclick="openConv(\''+x.k+'\')"><span>'+esc(x.nombre)+'</span>'+(x.unread?'<span class="b">'+x.unread+'</span>':'')+'</div>';}).join('')||'<div style="font-size:11.5px;color:#64748b;padding:6px">Sin directos aún.</div>';
 side+='<div style="margin-top:10px"><select id="newDm" style="width:100%;padding:6px;border:1px solid #e2e8f0;border-radius:7px;font-size:12px"><option value="">➕ Nuevo directo…</option>'+users().filter(function(u){return u.id!==id;}).map(function(u){return '<option value="dm:'+u.id+'">'+esc(u.nombre)+'</option>';}).join('')+'</select></div>';
 side+=puedeCanal(me)?'<button class="bd mini" style="width:100%;margin-top:8px" onclick="nuevoCanal()">➕ Crear canal</button>':'<div style="font-size:10.5px;color:#94a3b8;margin-top:8px">Solo directivos/Help Desk crean canales (Art. IV).</div>';
 var main=CUR?thread(CUR):'<div class="empty">Selecciona una conversación o inicia un directo.</div>';
 el('panel').innerHTML='<div class="chatwrap"><div class="side">'+side+'</div><div class="thread">'+main+'</div></div>';
 var nd=el('newDm');if(nd)nd.onchange=function(){if(nd.value)openConv(nd.value);};
 var mb=el('msgs');if(mb)mb.scrollTop=mb.scrollHeight;
}
function openConv(k){CUR=k;
 // marcar leídos
 var id=meId();var M=L('sigej_mensajes');var any=false;M.forEach(function(m){if(m.borrado)return;var belong=(k.indexOf('canal:')===0&&m.canal===k.slice(6))||(k.indexOf('dm:')===0&&m.tipo==='dm'&&((m.from===id&&(m.to||[])[0]===k.slice(3))||(m.from===k.slice(3)&&(m.to||[]).indexOf(id)>=0)));if(belong&&m.from!==id&&(m.leidoPor||[]).indexOf(id)<0){m.leidoPor=m.leidoPor||[];m.leidoPor.push(id);any=true;}});
 if(any){S('sigej_mensajes',M);msgAudit('Lectura de mensajes',k);}
 render();
}
function convMsgs(k){var id=meId();return msgs().filter(function(m){if(k.indexOf('canal:')===0)return m.canal===k.slice(6);var o=k.slice(3);return m.tipo==='dm'&&((m.from===id&&(m.to||[])[0]===o)||(m.from===o&&(m.to||[]).indexOf(id)>=0));});}
function thread(k){var id=meId();var titulo,sub='';
 if(k.indexOf('canal:')===0){var c=canales().filter(function(x){return x.id===k.slice(6);})[0];if(!c)return '<div class="empty">Canal no disponible.</div>';if((c.miembros||[]).indexOf(id)<0)return '<div class="empty">🔒 No tienes acceso a este canal (necesidad de conocer).</div>';titulo=c.nombre;sub=(c.miembros||[]).length+' integrantes · '+c.confid;}
 else{var o=userById(k.slice(3));titulo='💬 '+o.nombre;sub=o.rol+' · '+o.coord;}
 var ms=convMsgs(k);
 var body=ms.length?ms.map(function(m){var mine=m.from===id;var ad=(m.adjuntos||[]).map(function(a,j){return '<div style="font-size:11px;margin-top:3px">📎 <a href="'+a.data+'" download="'+esc(a.nombre)+'" onclick="regDescarga(\''+m.id+'\',\''+esc(a.nombre)+'\')">'+esc(a.nombre)+'</a></div>';}).join('');
  var extra=(m.exp?'<span class="chip">📁 '+esc(m.exp)+'</span>':'')+(m.modulo?'<span class="chip">'+esc(m.modulo)+'</span>':'')+(m.prio&&m.prio!=='Normal'?'<span class="chip">⚠ '+esc(m.prio)+'</span>':'');
  var leido=mine?(' · '+((m.leidoPor||[]).length)+' leído(s)'):'';
  return '<div class="msg '+(mine?'mine':'other')+'">'+(mine?'':'<div class="who">'+esc(userById(m.from).nombre)+'</div>')+esc(m.texto).replace(/\n/g,'<br>')+ad+(extra?'<div style="margin-top:4px">'+extra+'</div>':'')+'<div class="meta">'+m.ts+leido+(mine?' <span class="lk" style="cursor:pointer;color:#c0392b" onclick="delMsg(\''+m.id+'\')">eliminar</span>':'')+'</div></div>';}).join(''):'<div class="empty">Sin mensajes. Escribe el primero.</div>';
 var comp='<div class="compose"><div class="row"><input id="c_exp" placeholder="📁 Expediente (opcional)" style="flex:1"><input id="c_mod" placeholder="Módulo (opcional)" style="flex:1"><select id="c_prio"><option>Normal</option><option>Alta</option><option>Urgente</option></select></div><div class="row"><textarea id="c_txt" placeholder="Escribe un mensaje…"></textarea><button class="bd" onclick="adj()">📎</button><button class="b3" onclick="enviar(\''+k+'\')">Enviar ▶</button></div><div id="c_adj" style="font-size:11px;color:#64748b"></div></div>';
 return '<div class="thead"><div>'+esc(titulo)+'<div style="font-size:11px;color:#64748b;font-weight:400">'+esc(sub)+'</div></div></div><div class="msgs" id="msgs">'+body+'</div>'+comp;
}
var _adj=[];
function adj(){_adj=[];el('fileIn').value='';el('fileIn').onchange=function(){var f=this.files[0];if(!f)return;if(f.size>2e6){alert('Máx 2 MB.');return;}var r=new FileReader();r.onload=function(){_adj.push({nombre:f.name,tipo:f.type,data:r.result});el('c_adj').textContent='📎 '+_adj.map(function(a){return a.nombre;}).join(', ');};r.readAsDataURL(f);};el('fileIn').click();}
function enviar(k){var id=meId();var txt=(el('c_txt').value||'').trim();if(!txt&&!_adj.length){return;}
 var m={id:uid(),tipo:k.indexOf('canal:')===0?'canal':'dm',canal:k.indexOf('canal:')===0?k.slice(6):null,to:k.indexOf('dm:')===0?[k.slice(3)]:[],from:id,texto:txt,ts:now(),exp:(el('c_exp').value||'').trim(),modulo:(el('c_mod').value||'').trim(),prio:el('c_prio').value,adjuntos:_adj.slice(),leidoPor:[id],borrado:false};
 var M=L('sigej_mensajes');M.push(m);S('sigej_mensajes',M);_adj=[];
 msgAudit('Mensaje enviado',(m.canal?('canal '+m.canal):'directo')+(m.exp?' · exp '+m.exp:''));
 if(m.exp){var Bk=L('sigej_bitacora');Bk.push({ts:now(),perfil:ME().nombre,modulo:'Mensajería',tipo:'Vínculo a expediente',accion:'Mensaje vinculado al expediente '+m.exp});S('sigej_bitacora',Bk);}
 render();
}
function regDescarga(mid,nombre){msgAudit('Descarga de adjunto',nombre);}
function delMsg(mid){if(!confirm('¿Eliminar (baja lógica)? Se conserva la trazabilidad.'))return;var M=L('sigej_mensajes');var m=M.filter(function(x){return x.id===mid;})[0];if(m){m.borrado=true;m.texto='(mensaje eliminado)';S('sigej_mensajes',M);msgAudit('Eliminación lógica de mensaje',mid);}render();}
function nuevoCanal(){if(!puedeCanal(ME())){alert('No autorizado para crear canales (Art. IV).');return;}var n=prompt('Nombre del canal:','');if(!n)return;var C=canales();C.push({id:'c'+uid(),nombre:n,desc:prompt('Descripción:','')||'',confid:'Restringido',modulo:'',admin:ME().nombre,miembros:[meId()]});S('sigej_canales',C);msgAudit('Creación de canal',n);render();}

/* ---------- Avisos institucionales (Art. VII/VIII) ---------- */
var AUDIENCIAS=[['todos','Todos los usuarios'],['abogados','Solo abogados'],['administrativo','Personal administrativo'],['directivos','Directores/Coordinadores/Jefes'],['nuevoingreso','Personal de nuevo ingreso'],['personal','Área de Personal → todo el personal']];
function avisoVisible(a,u){if(a.aud==='todos')return true;if(a.aud==='abogados')return /Abogado/.test(u.rol||'')||/Abogado/.test(u.tipo||'');if(a.aud==='administrativo')return /Administrativo|Asistente|Secretaría|Oficialía|Mensajería|Chofer/.test((u.rol||'')+(u.tipo||''));if(a.aud==='directivos')return /Director|Coordinador|Jefe|Abogado General|Secretaría/.test(u.rol||'');if(a.aud==='nuevoingreso')return /Becario|Servicio social|Temporal/.test(u.tipo||'');if(a.aud==='personal')return true;return false;}
function vAvisos(){var me=ME();var A=L('sigej_avisos');var vis=A.filter(function(a){return avisoVisible(a,me);});
 var form=puedeAviso(me)?'<div class="card"><b style="color:#0a4d8c">📢 Publicar aviso institucional</b><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px;margin-top:8px"><select id="a_aud">'+AUDIENCIAS.map(function(x){return '<option value="'+x[0]+'">'+x[1]+'</option>';}).join('')+'</select><input id="a_tit" placeholder="Título / asunto"><select id="a_prio"><option>Informativo</option><option>Importante</option><option>Urgente</option></select><input id="a_vig" type="date" title="Vigencia"><label style="font-size:12px;display:flex;align-items:center;gap:5px"><input type="checkbox" id="a_obl"> Acuse obligatorio</label></div><textarea id="a_txt" placeholder="Contenido del aviso" style="width:100%;margin-top:6px;border:1px solid #e2e8f0;border-radius:8px;padding:8px;min-height:50px"></textarea><div style="margin-top:6px"><button class="b3" onclick="pubAviso()">Publicar aviso</button> <span style="font-size:11px;color:#64748b">Emisor: '+esc(me.nombre)+' ('+esc(me.rol)+')</span></div></div>':'<div class="note">Solo el Administrador General, Help Desk, Área de Personal, directores y coordinadores pueden publicar avisos (Art. III).</div>';
 var lista=vis.length?vis.slice().reverse().map(function(a){var id=meId();var leido=(a.leidoPor||[]).indexOf(id)>=0;var venc=a.vig&&a.vig<hoy();var cls=a.prio==='Urgente'?' urg':(a.obl?' obl':'');
  var pill=(a.prio==='Urgente'?'<span class="pill r">Urgente</span>':a.prio==='Importante'?'<span class="pill y">Importante</span>':'<span class="pill g">Info</span>')+(a.obl?' <span class="pill y">Acuse obligatorio</span>':'')+(venc?' <span class="pill r">Vencido</span>':'');
  var ack=leido?'<span style="color:#15803d;font-size:11.5px">✔ Leído</span>':'<button class="b1 mini" onclick="acuse(\''+a.id+'\')">Confirmar lectura</button>';
  return '<div class="aviso'+cls+'"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px"><b>'+esc(a.tit)+'</b><span>'+pill+'</span></div><div style="margin:4px 0;font-size:12.5px">'+esc(a.txt).replace(/\n/g,'<br>')+'</div><div style="font-size:11px;color:#64748b">'+esc(a.emisor)+' · '+esc(a.area)+' · '+esc(a.fecha)+(a.vig?' · vigencia '+esc(a.vig):'')+' · '+AUDIENCIAS.filter(function(x){return x[0]===a.aud;}).map(function(x){return x[1];})[0]+' · '+((a.leidoPor||[]).length)+' lectura(s)</div><div style="margin-top:6px">'+ack+'</div></div>';}).join(''):'<div class="empty">No hay avisos para tu perfil.</div>';
 el('panel').innerHTML=form+'<div style="padding:0 0 10px">'+lista+'</div>';
}
function pubAviso(){var me=ME();if(!puedeAviso(me))return;var tit=(el('a_tit').value||'').trim();var txt=(el('a_txt').value||'').trim();if(!tit||!txt){alert('Indica título y contenido.');return;}
 var A=L('sigej_avisos');A.push({id:uid(),tit:tit,txt:txt,aud:el('a_aud').value,prio:el('a_prio').value,obl:el('a_obl').checked,vig:el('a_vig').value,emisor:me.nombre,area:me.coord||me.area||'OAG',fecha:hoy(),leidoPor:[]});S('sigej_avisos',A);
 msgAudit('Aviso institucional publicado',tit+' → '+el('a_aud').value);
 // también a Notificaciones
 var N=L('sigej_notificaciones');N.push({ts:now(),area:'Aviso institucional',texto:tit,folio:'',modulo:'Mensajería',leida:false});S('sigej_notificaciones',N);
 alert('📢 Aviso publicado y enviado al Centro de Notificaciones.');render();}
function acuse(id){var A=L('sigej_avisos');var a=A.filter(function(x){return x.id===id;})[0];if(!a)return;var mid=meId();if((a.leidoPor||[]).indexOf(mid)<0){a.leidoPor=a.leidoPor||[];a.leidoPor.push(mid);S('sigej_avisos',A);msgAudit('Acuse de lectura de aviso',a.tit);}render();}

/* ---------- Búsqueda (Art. X) ---------- */
function vBuscar(){el('panel').innerHTML='<div class="card"><b style="color:#0a4d8c">🔎 Búsqueda de mensajes y avisos</b><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin-top:8px"><input id="s_q" placeholder="Palabra clave" oninput="doBuscar()"><input id="s_exp" placeholder="Expediente" oninput="doBuscar()"><input id="s_mod" placeholder="Módulo" oninput="doBuscar()"><select id="s_prio" onchange="doBuscar()"><option value="">Toda prioridad</option><option>Alta</option><option>Urgente</option></select></div><div class="note" style="margin:8px 0 0">Búsqueda por reglas sobre lo que puedes ver (confidencialidad). La búsqueda semántica y el OCR de adjuntos son fase backend.</div><div id="s_res" style="margin-top:10px"></div></div>';doBuscar();}
function doBuscar(){var id=meId();var q=norm(el('s_q').value),ex=norm(el('s_exp').value),mo=norm(el('s_mod').value),pr=el('s_prio').value;
 var vis=msgs().filter(function(m){if(m.tipo==='canal'){var c=canales().filter(function(x){return x.id===m.canal;})[0];return c&&(c.miembros||[]).indexOf(id)>=0;}return m.from===id||(m.to||[]).indexOf(id)>=0;});
 var r=vis.filter(function(m){return (!q||norm(m.texto).indexOf(q)>=0)&&(!ex||norm(m.exp).indexOf(ex)>=0)&&(!mo||norm(m.modulo).indexOf(mo)>=0)&&(!pr||m.prio===pr);});
 el('s_res').innerHTML=r.length?'<table style="width:100%;font-size:12px;border-collapse:collapse"><tr style="text-align:left;color:#64748b"><th style="padding:5px">Fecha</th><th>De</th><th>Mensaje</th><th>Exp/Módulo</th></tr>'+r.slice().reverse().slice(0,100).map(function(m){return '<tr style="border-top:1px solid #eef2f7"><td style="padding:5px;white-space:nowrap">'+m.ts+'</td><td>'+esc(userById(m.from).nombre)+'</td><td>'+esc(m.texto.slice(0,70))+'</td><td>'+esc(m.exp||'')+' '+esc(m.modulo||'')+'</td></tr>';}).join('')+'</table>':'<div class="empty">Sin coincidencias.</div>';
}

/* ---------- Tablero (Art. XIII) ---------- */
function vTablero(){var id=meId();var M=msgs();var A=L('sigej_avisos');var C=canales();
 var enviados=M.filter(function(m){return m.from===id;}).length;
 var avActivos=A.filter(function(a){return !a.vig||a.vig>=hoy();}).length;
 var avVenc=A.filter(function(a){return a.vig&&a.vig<hoy();}).length;
 var oblig=A.filter(function(a){return a.obl&&(!a.vig||a.vig>=hoy());});
 var pendConf=oblig.reduce(function(acc,a){var aud=users().filter(function(u){return avisoVisible(a,u);});return acc+aud.filter(function(u){return (a.leidoPor||[]).indexOf(u.id)<0;}).length;},0);
 var sinLeer=oblig.filter(function(a){var aud=users().filter(function(u){return avisoVisible(a,u);});return aud.some(function(u){return (a.leidoPor||[]).indexOf(u.id)<0;});}).length;
 var porMod={};M.forEach(function(m){if(m.modulo)porMod[m.modulo]=(porMod[m.modulo]||0)+1;});
 var kp='<div class="kpis"><div class="kpi"><div class="n">'+M.length+'</div><div class="l">Mensajes (tú enviaste '+enviados+')</div></div><div class="kpi g"><div class="n">'+avActivos+'</div><div class="l">Avisos activos</div></div><div class="kpi y"><div class="n">'+avVenc+'</div><div class="l">Avisos vencidos</div></div><div class="kpi r"><div class="n">'+pendConf+'</div><div class="l">Confirmaciones pendientes</div></div><div class="kpi"><div class="n">'+sinLeer+'</div><div class="l">Avisos con lectura pendiente</div></div><div class="kpi"><div class="n">'+C.length+'</div><div class="l">Canales activos</div></div></div>';
 var pm=Object.keys(porMod).length?'<div class="card"><b style="color:#0a4d8c">Chats por módulo</b><div style="margin-top:6px">'+Object.keys(porMod).map(function(k){return '<span class="chip">'+esc(k)+': '+porMod[k]+'</span>';}).join('')+'</div></div>':'';
 var per=A.filter(function(a){return a.aud==='personal'||/Personal/.test(a.area||'');}).length;
 el('panel').innerHTML=kp+pm+'<div class="card"><b style="color:#0a4d8c">Comunicados del Área de Personal:</b> '+per+' · <b>Incidencias de comunicación:</b> 0 (demo)</div><div class="note">La entrega por correo/Teams/push, la confirmación push y la búsqueda semántica/OCR se ejecutan en el backend.</div>';
}
buildTabs();render();
</script>
__SNIP__
</body></html>"""
out=TPL.replace("__NAV__",NAV).replace("__SNIP__",SNIP)
open(B+"mensajeria_SIGEJ.html","w",encoding="utf-8").write(out)
print("mensajeria_SIGEJ.html OK -",len(out),"bytes")
