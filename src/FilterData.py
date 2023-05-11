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
        { "name": "consultas", "value": "Total" },
        { "name": "consultas", "value": "Serviços hospitalares" },
        { "name": "consultas", "value": "Serviços profissionais" }
    ],
    [
        # As linhas codadas, são subtipos das CID, filtros para sprints futuras. Favor não apagar. 

        # { "name": "internacoes", "value": "CID I: Algumas doenças infecciosas e parasitárias" },
        # { "name": "internacoes", "value": "CID I Doenças infecciosas e parasitárias - HIV" },
        # { "name": "internacoes", "value": "CID I Doenças infecciosas e parasitárias - Tuberculose" },
        # { "name": "internacoes", "value": "CID I Doenças infecciosas e parasitárias - Septicemia" },

        # { "name": "internacoes", "value": "CID II: Neoplasias (tumores)" },
        # { "name": "internacoes", "value": "CID II Neoplasias (tumores) - Leucemia" },
        # { "name": "internacoes", "value": "CID II Neoplasias (tumores) - Neoplasias da pele" },
        # { "name": "internacoes", "value": "CID II Neoplasias (tumores) - Neoplasias e doenças do fígado" },

        # { "name": "internacoes", "value": "CID III: Doenças do sangue e dos órgãos hematopoiéticos e alguns transtornos" },
        # { "name": "internacoes", "value": "CID III Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários - Anemias por deficiência de ferro e outras anemias" },
        # { "name": "internacoes", "value": "CID III Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários - Afecções hemorrágicas e outras doenças do sangue e dos orgãos hematopoiéticos" },
        # { "name": "internacoes", "value": "CID III Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários - Transtornos envolvendo mecanismo imunitário" },

        # { "name": "internacoes", "value": "CID IV: Doenças endócrinas, nutricionais e metabólicas" },
        # { "name": "internacoes", "value": "CID IV Doenças endócrinas, nutricionais e metabólicas - Diabetes mellitus" },
        # { "name": "internacoes", "value": "CID IV Doenças endócrinas, nutricionais e metabólicas - Transtornos nutricionais metabólicos e sequelas nutricionais" },
        # { "name": "internacoes", "value": "CID IV Doenças endócrinas, nutricionais e metabólicas - Obesidade" },

        { "name": "internacoes", "value": "CID VI - Meningítes" },
        { "name": "internacoes", "value": "CID VI - Doenças de parkinson, alzheimer e epilepsia" },
        { "name": "internacoes", "value": "CID VI - Doenças Relacionadas ao sistema Nervoso" },

        # { "name": "internacoes", "value": "CID IX: Doenças do aparelho circulatório" },
        # { "name": "internacoes", "value": "CID IX Doenças do aparelho circulatório - Infarto agúdo do miocárdio" },
        # { "name": "internacoes", "value": "CID IX Doenças do aparelho circulatório - Infarto cerebral" },
        # { "name": "internacoes", "value": "CID IX Doenças do aparelho circulatório - Insuficiência cardíaca" },

        { "name": "internacoes", "value": "CID X - Pneumonia" },
        { "name": "internacoes", "value": "CID X - Bronquite e bronqueolíte agúda, doenças pulmonares crônicas e bronquequiectasia" },
        { "name": "internacoes", "value": "CID X - Asma" },

        # { "name": "internacoes", "value": "CID XI: Doenças do aparelho digestivo" }
        # { "name": "internacoes", "value": "CID XI Doenças do aparelho digestivo - Pancreatite aguda e doenças do pâncreas" },
        # { "name": "internacoes", "value": "CID XI Doenças do aparelho digestivo - Doença de crohn, úlcera gástrica e duodenal" },
    ],
    [
        { "name": "procedimentos", "value": "Procedimentos com finalidade diagnóstica" },
        { "name": "procedimentos", "value": "Procedimentos clínicos" },
        { "name": "procedimentos", "value": "Procedimentos cirúrgicos" }
    ],
    [
        { "name": "tratamentos", "value": "INFORMAÇÃO NÃO DISPONIVEL" },
        { "name": "tratamentos", "value": "INFORMAÇÃO NÃO DISPONIVEL" },
        { "name": "tratamentos", "value": "INFORMAÇÃO NÃO DISPONIVEL" }
    ],
    [
        { "name": "medicamentos", "value": "INFORMAÇÃO NÃO DISPONIVEL" },
        { "name": "medicamentos", "value": "INFORMAÇÃO NÃO DISPONIVEL" },
        { "name": "medicamentos", "value": "INFORMAÇÃO NÃO DISPONIVEL" }
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
    for i in range(0, tipoIndex):
        pad += len(subTipos[i])
    for index in subTipoIndexes:
        retSubTipos.append(subTipos[tipoIndex][int(index)-pad])
    return retSubTipos