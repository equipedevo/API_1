periodos = ["2019", "2020", "2021", "2022"]

cidades = [
    { "name": "sjc", "value": "São José dos Campos" },
    { "name": "jacarei", "value": "Jacareí" },
    { "name": "taubate", "value": "Taubaté" }]

tipovalor = [
    { "name": "gastos", "value": "Gastos" },
    { "name": "quantidade", "value": "Quantidade" }
]

tipos = [
    { "name": "consultas", "value": "Consultas" },
    { "name": "internacoes", "value": "Internações" },
    { "name": "procedimentos", "value": "Procedimentos" },
    { "name": "tratamentos", "value": "Tratamentos" },
    { "name": "medicamentos", "value": "Medicamentos" }]

subtipos = [
    [
        { "name": "consultas", "value": "Total" },
        { "name": "consultas", "value": "Serviços hospitalares" },
        { "name": "consultas", "value": "Serviços profissionais" }
    ],

    [
        # As linhas codadas, são subtipos das CID, filtros para sprints futuras. Favor não apagar. 

        { "name": "internacoes", "value": "CID I: Algumas doenças infecciosas e parasitárias" },
        # { "name": "internacoes", "value": "CID I Doenças infecciosas e parasitárias - HIV" },
        # { "name": "internacoes", "value": "CID I Doenças infecciosas e parasitárias - Tuberculose" },
        # { "name": "internacoes", "value": "CID I Doenças infecciosas e parasitárias - Septicemia" },

        { "name": "internacoes", "value": "CID II: Neoplasias (tumores)" },
        # { "name": "internacoes", "value": "CID II Neoplasias (tumores) - Leucemia" },
        # { "name": "internacoes", "value": "CID II Neoplasias (tumores) - Neoplasias da pele" },
        # { "name": "internacoes", "value": "CID II Neoplasias (tumores) - Neoplasias e doenças do fígado" },

        { "name": "internacoes", "value": "CID III: Doenças do sangue e dos órgãos hematopoiéticos e alguns transtornos" },
        # { "name": "internacoes", "value": "CID III Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários - Anemias por deficiência de ferro e outras anemias" },
        # { "name": "internacoes", "value": "CID III Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários - Afecções hemorrágicas e outras doenças do sangue e dos orgãos hematopoiéticos" },
        # { "name": "internacoes", "value": "CID III Doenças do sangue e dos órgãos hematopoéticos e alguns transtornos imunitários - Transtornos envolvendo mecanismo imunitário" },

        { "name": "internacoes", "value": "CID IV: Doenças endócrinas, nutricionais e metabólicas" },
        # { "name": "internacoes", "value": "CID IV Doenças endócrinas, nutricionais e metabólicas - Diabetes mellitus" },
        # { "name": "internacoes", "value": "CID IV Doenças endócrinas, nutricionais e metabólicas - Transtornos nutricionais metabólicos e sequelas nutricionais" },
        # { "name": "internacoes", "value": "CID IV Doenças endócrinas, nutricionais e metabólicas - Obesidade" },

        { "name": "internacoes", "value": "CID VI: Doenças do sistema nervoso" },
        # { "name": "internacoes", "value": "CID VI Doenças do sistema nervoso - Meningítes bacterianas, infecciosas, parasitórias e outras" },
        # { "name": "internacoes", "value": "CID VI Doenças do sistema nervoso - Doenças de parkinson, alzheimer e epilepsia" },
        # { "name": "internacoes", "value": "CID VI Doenças do sistema nervoso - Doenças do sistema nervoso" },

        { "name": "internacoes", "value": "CID IX: Doenças do aparelho circulatório" },
        # { "name": "internacoes", "value": "CID IX Doenças do aparelho circulatório - Infarto agúdo do miocárdio" },
        # { "name": "internacoes", "value": "CID IX Doenças do aparelho circulatório - Infarto cerebral" },
        # { "name": "internacoes", "value": "CID IX Doenças do aparelho circulatório - Insuficiência cardíaca" },

        { "name": "internacoes", "value": "CID X: Doenças do aparelho respiratório" },
        # { "name": "internacoes", "value": "CID X Doenças do aparelho respiratório - Pneumonia" },
        # { "name": "internacoes", "value": "CID X Doenças do aparelho respiratório - Bronquite e bronqueolíte agúda, doenças pulmonares crônicas e bronquequiectasia" },
        # { "name": "internacoes", "value": "CID X Doenças do aparelho respiratório - Asma" },

        { "name": "internacoes", "value": "CID XI: Doenças do aparelho digestivo" }
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
    ]]

def GetSubtipo(tipoIndex, subtipoIndex):
    pad = 0
    for i in range(0, tipoIndex):
        pad += len(subtipos[i])
    return subtipos[tipoIndex][subtipoIndex-pad]