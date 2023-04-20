from flask import Flask, render_template, request, url_for
import FilterData
# import TableToGraph

app = Flask(__name__)

# procedimentos = TableToGraph.Table("Procedimentos SJC", "ano", "quantidade", "./tables/Procedimentos/Sao Jose dos Campos.csv", 4, 13)
# procedimentos.SaveFig("./static/img/", "grafico procedimentos sjc.svg")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/consulta")
def consulta():
    return render_template("consulta.html",
        periodos = FilterData.periodos,
        cidades = FilterData.cidades,
        tipos = FilterData.tipos,
        subtipos = FilterData.subtipos)

@app.route("/atualizarConsulta", methods=["GET", "POST"])
def atualizarConsulta():
    selecPeriodos = request.form.getlist("periodo")
    selecCidades = request.form.getlist("cidade")
    selecTipo = request.form.get("tipo")
    selecSubtipos = request.form.getlist("subtipo")
    return str(selecPeriodos) + "\n" + str(selecCidades) + "\n" + str(selecTipo) + "\n" + str(selecSubtipos)