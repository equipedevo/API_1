from flask import Flask, render_template
# import TableToGraph

app = Flask(__name__)

# procedimentos = TableToGraph.Table("Procedimentos SJC", "ano", "quantidade", "./tables/Procedimentos/Sao Jose dos Campos.csv", 4, 13)
# procedimentos.SaveFig("./static/img/", "grafico procedimentos sjc.svg")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consulta")
def consulta():
    return render_template("consulta.html",
    anos=["2019", "2020", "2021", "2022"],
    cidades=[
        { "name": "sjc", "value": "São José dos Campos" },
        { "name": "jacarei", "value": "Jacareí" },
        { "name": "taubate", "value": "Taubaté" }],
    tipos=[
        { "name": "consultas", "value": "Consultas" },
        { "name": "internacoes", "value": "Internações" },
        { "name": "procedimentos", "value": "Procedimentos" },
        { "name": "tratamentos", "value": "Tratamentos" }],
    subtipos=["subtipo 1", "subtipo 2", "subtipo 3"])