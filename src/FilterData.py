periodos = [
    { "name": "2019", "range": range(1, 13) },
    { "name": "2020", "range": range(14, 26) },
    { "name": "2021", "range": range(27, 39) },
    { "name": "2022", "range": range(40, 52) }
]

cidades = [
    { "name": "sjc", "value": "São José dos Campos" },
    { "name": "jacarei", "value": "Jacareí" },
    { "name": "taubate", "value": "Taubaté" }
]

tipoValor = [
    { "name": "gastos", "value": "Gastos" },
    { "name": "quantidade", "value": "Quantidade" }
]

tipos = [
    { "name": "consultas", "value": "Consultas" },
    { "name": "internacoes", "value": "Internações" },
    { "name": "procedimentos", "value": "Procedimentos" },
    { "name": "tratamentos", "value": "Tratamentos" },
    { "name": "medicamentos", "value": "Medicamentos" }
]

subTipos = [
    [
        { "name": "consultas", "value": "Consultas médicas/outros profissionaisde nivel superior"},
        { "name": "consultas", "value": "Consulta/Atendimento ás urgências (em geral)"},
    ],
    [
        # { "name": "internacoes", "value": "CID I - HIV" },
        # { "name": "internacoes", "value": "CID I - Tuberculose" },
        # { "name": "internacoes", "value": "CID I - Septicemia" },

        # { "name": "internacoes", "value": "CID II - Leucemia" },
        # { "name": "internacoes", "value": "CID II - Neoplasias da pele" },
        # { "name": "internacoes", "value": "CID II - Neoplasias e doenças do fígado" },

        { "name": "internacoes", "value": "CID III - Anemias por deficiência de ferro e outras anemias" },
        { "name": "internacoes", "value": "CID III - Afecções hemorrágicas e outras doenças do sangue e dos orgãos hematopoiéticos" },
        # { "name": "internacoes", "value": "CID III - Transtornos envolvendo mecanismo imunitário" },

        { "name": "internacoes", "value": "CID IV - Diabetes mellitus" },
        { "name": "internacoes", "value": "CID IV - Transtornos nutricionais metabólicos e sequelas nutricionais" },
        # { "name": "internacoes", "value": "CID IV - Obesidade" },

        { "name": "internacoes", "value": "CID VI - Meningites bacterianas, infecciosas, parasitórias e outras causas" },
        { "name": "internacoes", "value": "CID VI - Doenças de parkinson, alzheimer e epilepsia" },
        { "name": "internacoes", "value": "CID VI - Doenças Relacionadas ao sistema Nervoso" },

        { "name": "internacoes", "value": "CID IX - Infarto agúdo do miocárdio" },
        { "name": "internacoes", "value": "CID IX - Infarto cerebral" },
        { "name": "internacoes", "value": "CID IX - Insuficiência cardíaca" },

        { "name": "internacoes", "value": "CID X - Pneumonia" },
        { "name": "internacoes", "value": "CID X - Bronquite e bronqueolíte agúda, doenças pulmonares crônicas e bronquequiectasia" },
        { "name": "internacoes", "value": "CID X - Asma" },

        # { "name": "internacoes", "value": "CID XI - Pancreatite aguda e doenças do pâncreas" },
        # { "name": "internacoes", "value": "CID XI - Doença de crohn, úlcera gástrica e duodenal" },
    ],
    [
        { "name": "procedimentos", "value": "Procedimentos com finalidade diagnóstica" },
        { "name": "procedimentos", "value": "Procedimentos clínicos" },
        { "name": "procedimentos", "value": "Procedimentos cirúrgicos" }
    ],
    [
        { "name": "tratamentos", "value": "Aparelho respiratório"},
        { "name": "tratamentos", "value": "Tratamento de doenças infecciosas e parasitárias"},
        { "name": "tratamentos", "value": "Traqueia e brônquios"},
        { "name": "tratamentos", "value": "Pulmão"},
    ],
    [
        { "name": "medicamentos", "value": "IMUNOGLOBULINA ANTI-RHO (D) (FRASCO AMPOLA DE 2 ML E 1.250 UI)" },
        { "name": "medicamentos", "value": "IMUNOGLOBULINA HUMANA 1,0 G INJETAVEL (POR FRASCO)" },
        { "name": "medicamentos", "value": "SURFACTANTE FRASCO-AMPOLA" },
        { "name": "medicamentos", "value": "ALBUMINA HUMANA 20 POR CENTO (FRASCO-AMPOLA DE 50 ML)" }
    ]
]

def GetPeriodos(periodosIndexes):
    retPeriodos = []
    for index in periodosIndexes:
        retPeriodos.append(periodos[int(index)])
    return retPeriodos

def GetCidades(cidadesIndexes):
    retCidades = []
    for index in cidadesIndexes:
        retCidades.append(cidades[int(index)])
    return retCidades

def GetTipoValor(tipoValorIndex):
    return tipoValor[int(tipoValorIndex)]

def GetTipo(tipoIndex):
    return tipos[int(tipoIndex)]

def GetSubtipos(tipoIndex, subTipoIndexes):
    retSubTipos = []
    pad = 0
    for i in range(0, int(tipoIndex)):
        pad += len(subTipos[i])
    for index in subTipoIndexes:
        retSubTipos.append(subTipos[tipoIndex][int(index)-pad])
    return retSubTipos

def GetSubtiposRange(tipoIndex, subTipoIndexes):
    retSubTipos = []
    pad = 0
    for i in range(0, int(tipoIndex)):
        pad += len(subTipos[i])
    for index in subTipoIndexes:
        retSubTipos.append(int(index)-pad)
    return retSubTipos