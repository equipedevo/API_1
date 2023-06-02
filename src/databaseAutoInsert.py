import FilterData

import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root", # "***PREENCHA OS DADOS AQUI***"
    password = "admin", # "***PREENCHA OS DADOS AQUI***"
    db = "BancoCICOVALE")
cursor = conn.cursor()

for i in range(len(FilterData.periodos)):
    cursor.execute(f"insert into Periodo values ({i+1}, '{FilterData.periodos[i]['name']}', 0);")

for i in range(len(FilterData.cidades)):
    cursor.execute(f"insert into Cidade values ({i+1}, '{FilterData.cidades[i]['value']}', 0);")

for i in range(len(FilterData.tipoValor)):
    cursor.execute(f"insert into Valor values ({i+1}, '{FilterData.tipoValor[i]['value']}', 0);")

for i in range(len(FilterData.tipos)):
    cursor.execute(f"insert into Tipo values ({i+1}, '{FilterData.tipos[i]['value']}', 0);")

subtipoIndex = 0
for subtipoArr in FilterData.subTipos:
    for subtipo in subtipoArr:
        cursor.execute(f"insert into Subtipo values ({subtipoIndex+1}, '{subtipo['value']}', 0);")
        subtipoIndex += 1

conn.commit()
conn.close()
