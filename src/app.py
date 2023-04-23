from flask import Flask, render_template, request, url_for
import FilterData
import TableToGraph

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/consulta", methods=["GET", "POST"])
def consulta(grafico2019 = "", grafico2020 = "", grafico2021 = "", grafico2022 = ""):
    return render_template("consulta.html",
        periodos = FilterData.periodos,
        cidades = FilterData.cidades,
        tipovalor = FilterData.tipovalor,
        tipos = FilterData.tipos,
        subtipos = FilterData.subtipos,
        graph2019path = grafico2019,
        graph2020path = grafico2020,
        graph2021path = grafico2021,
        graph2022path = grafico2022)

@app.route("/atualizarConsulta", methods=["GET"])
def atualizarConsulta():
    selecPeriodos = request.args.get("periodo").split(",")
    selecCidades = request.args.get("cidade").split(",")
    selecTipovalor = request.args.get("tipovalor")
    selecTipo = request.args.get("tipo")
    selecSubtipos = request.args.get("subtipo").split(",")

    """ return f"{selecPeriodos}<br>{selecCidades}<br>{selecTipovalor}<br>{selecTipo}<br>{selecSubtipos}"
    print(selecPeriodos)
    for periodo in selecPeriodos:
        print(FilterData.periodos[int(periodo)])
    for cidade in selecCidades:
        print(FilterData.cidades[int(cidade)]["value"])
    print(FilterData.tipovalor[int(selecTipovalor)])
    print(FilterData.tipos[int(selecTipo)])
    for subtipo in selecSubtipos:
        print(FilterData.GetSubtipo(int(selecTipo), int(subtipo))["value"])
    """

    """
    #if FilterData.tipos[int(selecTipo)] == "internacoes" and FilterData.subtipos[int(selecSubtipos)] == "internacoes": # "CID X: Doenças do aparelho respiratório - Gastos e quantidade":
    #print(FilterData.subtipos[int(selecTipo)][int(selecSubtipos)])
    if FilterData.periodos[int(selecPeriodos[0])] == "2019":
        if FilterData.GetSubtipo(int(selecTipo), int(selecSubtipos[0]))["value"] == "CID X: Doenças do aparelho respiratório":
            if FilterData.tipovalor[int(selecTipovalor)]["name"] == "gastos":
                return consulta(Gastos2019Jacarei)
            elif FilterData.tipovalor[int(selecTipovalor)]["name"] == "quantidade":
                return consulta(Internacoes2019Jacarei)
    if FilterData.periodos[int(selecPeriodos[0])] == "2020":
        if FilterData.GetSubtipo(int(selecTipo), int(selecSubtipos[0]))["value"] == "CID X: Doenças do aparelho respiratório":
            if FilterData.tipovalor[int(selecTipovalor)]["name"] == "gastos":
                return consulta(Gastos2020Jacarei)
            elif FilterData.tipovalor[int(selecTipovalor)]["name"] == "quantidade":
                return consulta(Internacoes2020Jacarei)
    """

    """
    TableToGraph.BarGraph(
        csvDir = "./tables/procedimentos/quantidade jacarei.csv",
        title = "Quantidade de procedimentos em Jacareí",
        barCount = 12,
        lineRange = range(1, 13, 1),
        xLabel = "2019",
        yLabel = "Quantidade",
        figDir = "./static/img/grafico.svg")

    TableToGraph.GroupedBarGraph(
        csvDir = "./tables/procedimentos/quantidade jacarei.csv",
        title = "Quantidade de procedimentos em Jacareí",
        barRange = [1, 3],
        lineRange = range(1, 13, 1),
        xLabel = "2019",
        yLabel = "Quantidade",
        figDir = "./static/img/grafico.svg",
        divisor = 1)
    #"""
    
    for cidade in selecCidades:
        print(FilterData.cidades[int(cidade)]["value"])
    print(FilterData.tipovalor[int(selecTipovalor)])
    print(FilterData.tipos[int(selecTipo)])
    for subtipo in selecSubtipos:
        print(FilterData.GetSubtipo(int(selecTipo), int(subtipo))["value"])

    for i in selecPeriodos:
        periodo = FilterData.periodos[int(i)]

        TableToGraph.GroupedBarGraph(
            csvDir = f"./tables/{FilterData.tipos[int(selecTipo)]["value"]}/{FilterData.tipovalor[int(selecTipovalor)]["value"]} {}.csv",# "./tables/procedimentos/quantidade jacarei.csv",
            title = "Quantidade de procedimentos em Jacareí",
            barRange = [1, 3],
            lineRange = range(1, 13, 1),
            xLabel = periodo,
            yLabel = "Quantidade",
            figDir = f"./static/img/grafico{periodo}.svg",
            divisor = 1)
        FilterData.periodos[int(periodo)]
    for cidade in selecCidades:
        print(FilterData.cidades[int(cidade)]["value"])
    print(FilterData.tipovalor[int(selecTipovalor)])
    print(FilterData.tipos[int(selecTipo)])
    for subtipo in selecSubtipos:
        print(FilterData.GetSubtipo(int(selecTipo), int(subtipo))["value"])

    return consulta()