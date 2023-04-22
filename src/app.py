from flask import Flask, render_template, request, url_for
import FilterData
import TableToGraph

app = Flask(__name__)

Gastos2019Jacarei = "./static/img/Gastos2019Jacarei.jpg"
Gastos2020Jacarei = "./static/img/Gastos2020Jacarei.jpg"
Internacoes2019Jacarei = "./static/img/Internacoes_CIDX_JCR19.jpg"
Internacoes2020Jacarei = "./static/img/Internacoes_CIDX_JCR20.jpg"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/consulta", methods=["GET", "POST"])
def consulta(grafico = "./static/img/grafico.svg"):
    return render_template("consulta.html",
        periodos = FilterData.periodos,
        cidades = FilterData.cidades,
        tipovalor = FilterData.tipovalor,
        tipos = FilterData.tipos,
        subtipos = FilterData.subtipos,
        imgpath = grafico) #"./static/img/Gastos2019Jacarei.jpg")

@app.route("/atualizarConsulta", methods=["GET"])
def atualizarConsulta():
    selecPeriodos = request.args.get("periodo")
    selecCidades = request.args.get("cidade")
    selecTipovalor = request.args.get("tipovalor")
    selecTipo = request.args.get("tipo")
    selecSubtipos = request.args.get("subtipo")
    #selecPeriodos = request.form.getlist("periodo")
    #selecCidades = request.form.getlist("cidade")
    #selecTipovalor = request.form.get("tipovalor")
    #selecTipo = request.form.get("tipo")
    #selecSubtipos = request.form.getlist("subtipo")
    
    #if FilterData.tipos[int(selecTipo)] == "internacoes" and FilterData.subtipos[int(selecSubtipos)] == "internacoes": # "CID X: Doenças do aparelho respiratório - Gastos e quantidade":
    #print(FilterData.subtipos[int(selecTipo)][int(selecSubtipos)])
    if FilterData.periodos[int(selecPeriodos)] == "2019":
        #if FilterData.subtipos[int(selecTipo)][int(selecSubtipos)]["value"] == "CID X: Doenças do aparelho respiratório":
            if FilterData.tipovalor[int(selecTipovalor)]["name"] == "gastos":
                return consulta(Gastos2019Jacarei)
            elif FilterData.tipovalor[int(selecTipovalor)]["name"] == "quantidade":
                return consulta(Internacoes2019Jacarei)
    if FilterData.periodos[int(selecPeriodos)] == "2020":
        #if FilterData.subtipos[int(selecSubtipos)]["value"] == "CID X: Doenças do aparelho respiratório":
            if FilterData.tipovalor[int(selecTipovalor)]["name"] == "gastos":
                return consulta(Gastos2020Jacarei)
            elif FilterData.tipovalor[int(selecTipovalor)]["name"] == "quantidade":
                return consulta(Internacoes2020Jacarei)

    # TableToGraph.TableToGraph("./tables/Procedimentos/quantidade Jacarei.csv", "Quantidade de procedimentos em Jacareí", 4, range(1, 13, 1), "Mês", "Quantidade", "./static/img/grafico.svg")
    
    return consulta()