from flask import Flask, render_template

app = Flask(__name__)

# import testeGrafico
import TableToGraph

# procedimentos = TableToGraph.Table("Procedimentos SJC", "ano", "quantidade", "./tables/Procedimentos/Sao Jose dos Campos.csv", 4, 13)
# procedimentos.SaveFig("./static/img/", "grafico procedimentos sjc.svg")

@app.route("/")
def index():
    return render_template("index.html")