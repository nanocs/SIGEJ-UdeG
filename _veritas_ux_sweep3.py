# -*- coding: utf-8 -*-
# Pendiente #3 (Del sistema.docx 2019): DEDUP de personas/dependencias en listas de autocompletado.
# Quita opciones <datalist> con el mismo nombre (normalizado). NO toca <select> (catálogos) ni datos guardados.
import glob

DEDUP = r"""<script>(function(){
 function norm(s){return (s||'').trim().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/\s+/g,' ');}
 function dedup(dl){var seen={};[].slice.call(dl.querySelectorAll('option')).forEach(function(o){var k=norm(o.value||o.textContent);if(!k){return;}if(seen[k]){o.remove();}else{seen[k]=1;}});}
 function run(){[].slice.call(document.querySelectorAll('datalist')).forEach(dedup);}
 if(document.readyState!=='loading'){run();}else{document.addEventListener('DOMContentLoaded',run);}
 setTimeout(run,800);
 try{var t;function sched(){clearTimeout(t);t=setTimeout(run,250);}
  var mo=new MutationObserver(function(muts){for(var i=0;i<muts.length;i++){var n=muts[i].target;while(n&&n.tagName!=='DATALIST'){n=n.parentElement;}if(n){sched();break;}}});
  mo.observe(document.documentElement,{childList:true,subtree:true});}catch(e){}
})();</script>"""

BUILDERS = sorted(set(glob.glob("/Users/edithroque/Documents/CLAUDE/_veritas_build_*.py")))
done=[];skip=[];nosel=[]
for f in BUILDERS:
    s=open(f,encoding="utf-8").read()
    if "var opt=" not in s or "__G=[" not in s:
        nosel.append(f.split("/")[-1]);continue
    if "function dedup(dl)" in s:
        skip.append(f.split("/")[-1]);continue
    idx=s.find("window.__bitlog")
    j=s.find("</script>",idx)
    s=s[:j+len("</script>")]+DEDUP+s[j+len("</script>"):]
    open(f,"w",encoding="utf-8").write(s)
    done.append(f.split("/")[-1])
print("MODIFICADOS:",len(done))
print("OMITIDOS (sin UX/SNIP):",nosel)
print("YA tenían dedup:",skip)
