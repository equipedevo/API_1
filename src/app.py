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
    TableToGraph.TableToGraph("./tables/Procedimentos/quantidade Jacarei.csv", "Quantidade de procedimentos em Jacareí", 4, range(1, 13, 1), "Mês", "Quantidade", "./static/img/grafico.svg")
    
    return consulta()
    #render_template("consulta.html",
    #    periodos = FilterData.periodos,
    #    cidades = FilterData.cidades,
    #    tipos = FilterData.tipos,
    #    subtipos = FilterData.subtipos)