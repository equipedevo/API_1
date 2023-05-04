from flask import Flask, render_template, request, url_for
import FilterData
import TableToGraph

app = Flask(__name__)

@app.route("/")
def index():
    title = "Home"
    return render_template("index.html", title = title)

@app.route("/sobre")
def sobre():
    title = "Sobre o CICOVALE"
    return render_template("sobre.html", title = title)

@app.route("/consulta", methods=["GET"])
def consulta():
    title = "Consultar"
    if request.method != "GET" or not request.args.get("periodo") or not request.args.get("cidade") or not request.args.get("tipoValor") or not request.args.get("tipo") or not request.args.get("subTipo"):
        return render_template("consulta.html",
            periodos = FilterData.periodos,
            cidades = FilterData.cidades,
            tipoValor = FilterData.tipoValor,
            tipos = FilterData.tipos,
            subTipos = FilterData.subTipos)
    
    selecPeriodos = request.args.get("periodo").split(",")
    selecCidades = request.args.get("cidade").split(",")
    selecTipovalor = request.args.get("tipoValor")
    selecTipo = request.args.get("tipo")
    selecSubTipos = request.args.get("subTipo").split(",")

    periodos = FilterData.GetPeriodos(selecPeriodos)
    cidades = FilterData.GetCidades(selecCidades)
    tipoValor = FilterData.GetTipoValor(selecTipovalor)["value"]
    tipo = FilterData.GetTipo(selecTipo)["value"]
    subTipos = FilterData.GetSubtipos(int(selecTipo), selecSubTipos)

    graficos = []

    for cidade in cidades:
        paths = []
        for periodo in periodos:
            cidadeValue = cidade["value"]
            path = f"./static/img/grafico_{cidadeValue}_{periodo}.svg"
            TableToGraph.GroupedBarGraph(
                csvDir = f"./tables/{tipo}/{tipoValor} {cidadeValue}.csv",
                title = f"{tipoValor} de {tipo} em {cidadeValue}",
                barRange = selecSubTipos,
                lineRange = range(1, 13, 1),
                xLabel = periodo,
                yLabel = f"{tipoValor} de {tipo}",
                figDir = path,
                divisor = 1)
            paths.append(path)
        graficos.append({ "cidade": cidade["name"], "paths": paths })
        
    return render_template("consulta.html", title = title,
        periodos = FilterData.periodos,
        cidades = FilterData.cidades,
        tipoValor = FilterData.tipoValor,
        tipos = FilterData.tipos,
        subTipos = FilterData.subTipos,
        graficos = graficos)
