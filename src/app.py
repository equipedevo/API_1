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
    checkboxPorcent = request.args.get("porcentagem")

    periodos = FilterData.GetPeriodos(selecPeriodos)
    cidades = FilterData.GetCidades(selecCidades)
    tipoValor = FilterData.GetTipoValor(selecTipovalor)["value"]
    tipo = FilterData.GetTipo(selecTipo)["value"]
    porcentagem = True if checkboxPorcent == "true" else False

    graficos = []

    for cidade in cidades:
        paths = []
        for periodo in periodos:
            cidadeValue = cidade["value"]
            periodoName = periodo["name"]
            periodoRange = periodo["range"]

            path = f"./static/graficos/grafico_{cidadeValue}_{periodoName}.svg"

            csvDir = f"./tables/{tipo}/{tipoValor} {cidadeValue}.csv"
            title = f"{tipoValor} de {tipo} em {cidadeValue} durante {periodoName}{(' em porcentagem' if porcentagem else '')}"
            barRange = selecSubTipos
            lineRange = periodoRange
            xLabel = periodoName
            yLabel = f"{tipoValor} de {tipo}{(' em porcentagem' if porcentagem else '')}"
            figDir = path

            try:
                if porcentagem:
                    TableToGraph.PercentageLineGraph(
                        csvDir = csvDir,
                        title = title,
                        barRange = barRange,
                        lineRange = lineRange,
                        xLabel = xLabel,
                        yLabel = yLabel,
                        figDir = figDir,
                        divisor = 1)
                else:
                    TableToGraph.GroupedBarGraph(
                        csvDir = csvDir,
                        title = title,
                        barRange = barRange,
                        lineRange = lineRange,
                        xLabel = xLabel,
                        yLabel = yLabel,
                        figDir = figDir,
                        divisor = 1)
                paths.append(path)
            except:
                paths.append("static/img/erroGrafico.png")
        
        graficos.append({ "name": cidade["name"], "paths": paths })
        
    return render_template("consulta.html", title = title,
        periodos = FilterData.periodos,
        cidades = FilterData.cidades,
        tipoValor = FilterData.tipoValor,
        tipos = FilterData.tipos,
        subTipos = FilterData.subTipos,
        graficos = graficos)
