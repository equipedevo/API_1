from flask import Flask, render_template, request, url_for
import FilterData
import TableToGraph

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "devoapi"
app.config["MYSQL_PASSWORD"] = "dsmdevoapi2023"
app.config["MYSQL_DB"] = "BancoCICOVALE"

mysql = MySQL(app)

@app.route("/")
def index():
    title = "Home"
    graficos = [
        "./static/graficos/grafico_pesquisa_periodo.svg",
        "./static/graficos/grafico_pesquisa_cidade.svg",
        "./static/graficos/grafico_pesquisa_valor.svg",
        "./static/graficos/grafico_pesquisa_tipo.svg",
        "./static/graficos/grafico_pesquisa_subtipo.svg"
    ]
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(f"select per_nome, per_quant from Periodo order by per_quant desc;")
        periodos = cursor.fetchall()

        cursor.execute(f"select cid_nome, cid_quant from Cidade order by cid_quant desc;")
        cidades = cursor.fetchall()

        cursor.execute(f"select val_nome, val_quant from Valor order by val_quant desc;")
        valores = cursor.fetchall()

        cursor.execute(f"select tip_nome, tip_quant from Tipo order by tip_quant desc;")
        tipos = cursor.fetchall()

        cursor.execute(f"select sub_nome, sub_quant from Subtipo order by sub_quant desc;")
        subtipos = cursor.fetchall()
        conn.commit()
        cursor.close()

        TableToGraph.BarGraphFromDB(
            select = periodos,
            title = "Periodos mais selecionados na filtragem",
            xLabel = "Opção de periodo",
            yLabel = "Quantidade de pesquisas",
            figDir = graficos[0])
        
        TableToGraph.BarGraphFromDB(
            select = cidades,
            title = "Cidades mais selecionados na filtragem",
            xLabel = "Opção de cidade",
            yLabel = "Quantidade de pesquisas",
            figDir = graficos[1])
        
        TableToGraph.BarGraphFromDB(
            select = valores,
            title = "Valores mais selecionados na filtragem",
            xLabel = "Opção de valor",
            yLabel = "Quantidade de pesquisas",
            figDir = graficos[2])
        
        TableToGraph.BarGraphFromDB(
            select = tipos,
            title = "Tipos mais selecionados na filtragem",
            xLabel = "Opção de tipo",
            yLabel = "Quantidade de pesquisas",
            figDir = graficos[3])
        
        TableToGraph.BarGraphFromDB(
            select = subtipos[:4],
            title = "Subtipos mais selecionados na filtragem",
            xLabel = "Opção de subtipo",
            yLabel = "Quantidade de pesquisas",
            figDir = graficos[4])
    except:
        render_template("index.html", title = title)
    return render_template("index.html", title = title, graficos = graficos)

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
    subtipos = FilterData.GetSubtiposRange(selecTipo, selecSubTipos)
    porcentagem = True if checkboxPorcent == "true" else False

    graficos = []

    registrar = False

    for cidade in cidades:
        paths = []
        for periodo in periodos:
            cidadeValue = cidade["value"]
            periodoName = periodo["name"]
            periodoRange = periodo["range"]

            path = f"./static/graficos/grafico_{cidadeValue}_{periodoName}.svg"

            csvDir = f"./tables/{tipo}/{tipoValor} {cidadeValue}.csv"
            title = f"{tipoValor} de {tipo} em {cidadeValue} durante {periodoName}{(' em porcentagem' if porcentagem else '')}"
            barRange = subtipos
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
                        figDir = figDir)
                else:
                    TableToGraph.GroupedBarGraph(
                        csvDir = csvDir,
                        title = title,
                        barRange = barRange,
                        lineRange = lineRange,
                        xLabel = xLabel,
                        yLabel = yLabel,
                        figDir = figDir,
                        autoDivide = True)
                paths.append(path)
                registrar = True
            except:
                paths.append("static/img/erroGrafico.png")
        
        graficos.append({ "name": cidade["name"], "paths": paths })
    
    if registrar:
        conn = mysql.connection
        cursor = conn.cursor()
        for periodo in periodos:
            cursor.execute(f"update Periodo set per_quant = per_quant + 1 where per_cod = '{FilterData.periodos.index(periodo)+1}';")
        for cidade in cidades:
            cursor.execute(f"update Cidade set cid_quant = cid_quant + 1 where cid_cod = '{FilterData.cidades.index(cidade)+1}';")
        cursor.execute(f"update Valor set val_quant = val_quant + 1 where val_cod = '{int(selecTipovalor)+1}';")
        cursor.execute(f"update Tipo set tip_quant = tip_quant + 1 where tip_cod = '{int(selecTipo)+1}';")
        for subtipo in selecSubTipos:
            cursor.execute(f"update Subtipo set sub_quant = sub_quant + 1 where sub_cod = '{int(subtipo)+1}';")
        conn.commit()
        cursor.close()
        
    return render_template("consulta.html", title = title,
        periodos = FilterData.periodos,
        cidades = FilterData.cidades,
        tipoValor = FilterData.tipoValor,
        tipos = FilterData.tipos,
        subTipos = FilterData.subTipos,
        graficos = graficos)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "5000", debug = False)
