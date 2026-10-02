# -*- coding: utf-8 -*-
# Pendiente #1 (Del sistema.docx 2019): AVISO DE CAMBIOS SIN GUARDAR.
# Inyecta una guarda universal en los 33 builders con SNIP estándar, tras el script de bitácora.
import glob

GUARD = r"""<script>(function(){
 var CONSULT=['buscador_SIGEJ','transparencia_general_SIGEJ','chat_SIGEJ','notificaciones_SIGEJ','SIGEJ_inicio','dashboard_SIGEJ','centro_ejecutivo_SIGEJ','bitacora_SIGEJ','reportes_SIGEJ','comando_SIGEJ','seguimiento_SIGEJ'];
 var pk=(location.pathname.split('/').pop()||'').replace('.html','');
 if(CONSULT.indexOf(pk)>=0)return;
 var dirty=false;
 function isSearch(el){if(el.id&&el.id.indexOf('__')===0)return true;var s=((el.id||'')+' '+(el.name||'')+' '+(el.placeholder||'')+' '+(el.className||'')).toLowerCase();return /buscar|search|filtro|filtrar|query|consulta/.test(s);}
 document.addEventListener('input',function(e){var el=e.target;if(!el||!/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName))return;if((el.type||'')==='search'||isSearch(el))return;if(((el.value||'')+'').length>0)dirty=true;},true);
 function clean(){dirty=false;}
 document.addEventListener('click',function(e){var t=e.target;if(!t)return;var n=t;for(var k=0;k<3&&n;k++){var x=((n.textContent||'')+' '+(n.title||'')).toLowerCase();if(/guardar|registrar|dar de alta|\bcrear\b|aceptar|\benviar\b|turnar|recibir|actualizar|aplicar/.test(x)){setTimeout(clean,60);break;}n=n.parentElement;}},true);
 document.addEventListener('submit',clean,true);
 window.addEventListener('beforeunload',function(e){if(dirty){e.preventDefault();e.returnValue='Tienes cambios de captura sin guardar. Si sales de la página se perderán.';return e.returnValue;}});
})();</script>"""

BUILDERS = sorted(set(glob.glob("/Users/edithroque/Documents/CLAUDE/_veritas_build_*.py")))
done=[];skip=[];nosel=[]
for f in BUILDERS:
    s=open(f,encoding="utf-8").read()
    if "var opt=" not in s or "__G=[" not in s:   # solo los que ya tienen el SNIP+UX estándar
        nosel.append(f.split("/")[-1]);continue
    if "sigej dirty guard" in s or "cambios de captura sin guardar" in s:
        skip.append(f.split("/")[-1]);continue
    idx=s.find("window.__bitlog")
    j=s.find("</script>",idx)
    s=s[:j+len("</script>")]+GUARD+s[j+len("</script>"):]
    open(f,"w",encoding="utf-8").write(s)
    done.append(f.split("/")[-1])
print("MODIFICADOS:",len(done))
print("OMITIDOS (sin UX/SNIP):",nosel)
print("YA tenían guarda:",skip)
