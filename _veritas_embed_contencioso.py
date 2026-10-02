# -*- coding: utf-8 -*-
# Inyecta el script de "modo embebido" (?embed=1) en los 9 módulos que se unifican en Asuntos Contenciosos.
# En modo embebido: oculta header/navbar/badge propios y elimina overlays de acceso (el padre ya gatea).
import subprocess
B="/Users/edithroque/Documents/CLAUDE/"
EMBED=('<script>(function(){if(!/[?&]embed=1/.test(location.search))return;'
 'var st=document.createElement("style");st.textContent="header,.navbar{display:none!important}body{padding-top:0!important;margin-top:0!important}";document.head.appendChild(st);'
 'function clean(){try{var c=document.getElementById("__chg");if(c&&c.parentNode)c.parentNode.style.display="none";'
 'document.querySelectorAll("div[style*=\\"99999\\"]").forEach(function(o){o.remove();});}catch(e){}}'
 'clean();setTimeout(clean,150);setTimeout(clean,500);setTimeout(clean,1200);})();</script>')

mods=['masc','resp','alertas','abogados','documental','captura','modulo','asesoria','proyectos']
TERM='</body></html>"""'
for name in mods:
    f=B+"_veritas_build_"+name+".py"
    s=open(f,encoding="utf-8").read()
    if 'embed=1' in s:
        print(f"{name:10s} ya tiene embed");continue
    if TERM in s:
        s=s.replace(TERM,EMBED+TERM,1);open(f,"w",encoding="utf-8").write(s)
        out=subprocess.run(["python3",f],capture_output=True,text=True)
        print(f"{name:10s} inyectado · run:{'OK' if out.returncode==0 else 'ERR'} {out.stdout.strip()[:40]}{out.stderr.strip()[:120]}")
    else:
        print(f"{name:10s} ⚠ no se halló el terminador del TPL")
