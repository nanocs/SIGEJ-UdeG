# -*- coding: utf-8 prueba -*-
import json, datetime, collections
OUT="/Users/edithroque/Documents/CLAUDE/"
E=json.load(open(OUT+"expedientes_data.json",encoding="utf-8"))["expedientes"]
cu=json.load(open(OUT+"cuellos_data.json",encoding="utf-8"))
nlp=json.load(open(OUT+"nlp_expedientes.json",encoding="utf-8"))
ator_idx={a["num"]:a for a in cu["atorados"]}
# última actuación por expediente (del NLP)
def ult(num):return nlp.get(num,{}).get("ult_actuacion")
def meses_idle(num):
    u=ult(num)
    if not u:return None
    try:return round((datetime.date(2026,6,18)-datetime.date.fromisoformat(u)).days/30.4)
    except:return None
def riesgo_fin(m):
    return "Crítico" if m>500000 else "Alto" if m>100000 else "Medio" if m>0 else "Indeterminado"
# Caducidad: activos con inactividad (>=12 meses) — score y prob
cad=[]
for e in E:
    if not e["activo"]:continue
    mi=meses_idle(e["num"])
    if mi is None or mi<12:continue
    monto=e["nlp_monto_texto"] or e["monto"] or 0
    sc=min(100,round(40+mi*0.7+(15 if monto>0 else 0)))
    prob=min(100,round(50+mi))  # prob de consumación de caducidad
    cad.append({"num":e["num"],"materia":e["materia_fina"],"meses":mi,"ultimo":ult(e["num"]),
      "resp":e["responsable"],"dep":e["dependencia"],"pasivo":round(monto),"score":sc,
      "prob_perdida":min(95,round(40+sc*0.5)),"prob_caducidad":prob,"riesgo_fin":riesgo_fin(monto)})
cad.sort(key=lambda x:(-x["score"],-x["pasivo"]))
# Matriz de riesgo institucional por dependencia
depc=collections.Counter();depalto=collections.Counter();deppas=collections.Counter()
for e in E:
    if not e["dependencia"]:continue
    depc[e["dependencia"]]+=1
    if e["nivel_riesgo"] in("Alto","Crítico"):depalto[e["dependencia"]]+=1
    deppas[e["dependencia"]]+=(e["nlp_monto_texto"] or e["monto"] or 0)
matriz=[]
for d,n in depc.most_common(15):
    alto=depalto[d];dens=alto/n if n else 0
    riesgo="Crítico" if (alto>=4 or deppas[d]>1e6) else "Alto" if (alto>=2 or dens>0.1) else "Medio" if alto>=1 else "Bajo"
    matriz.append({"dep":d,"n":n,"alto":alto,"pasivo":round(deppas[d]),"riesgo":riesgo})
# Estratégico (Abogado General)
act=[e for e in E if e["activo"]]
pasivo_act=sum((e["nlp_monto_texto"] or e["monto"] or 0) for e in act)
criticos=sum(1 for e in E if e["nivel_riesgo"] in("Alto","Crítico"))
prob_global=round(sum(min(95,e["score"]) for e in act)/len(act)) if act else 0
data={"corte":"2026-06-18","atora24":cu["idle_counts"]["a24"],
 "estrategico":{"pasivo_contingente":round(pasivo_act),"criticos":criticos,"atorados":len(cad),
   "prob_global":prob_global,"riesgo_total":round(pasivo_act*prob_global/100)},
 "caducidad":cad[:60],"matriz":matriz,
 "fund_caducidad":"LFT arts. 772 (inactividad 45 días → requerimiento) y 773 (caducidad por falta de promoción en 4 meses)."}
json.dump(data,open(OUT+"alertas_centro_data.json","w",encoding="utf-8"),ensure_ascii=False)
print("caducidad:",len(cad),"| matriz deps:",len(matriz))
print("estratégico:",data["estrategico"])
print("top atorado:",cad[0]["num"],cad[0]["meses"],"meses score",cad[0]["score"],"pasivo",cad[0]["pasivo"])
