<br id="topo">

# 3ª Sprint

## [Ir para a tela de início](./../../../README.md)

## :mag_right: Índice

* [Sobre a Sprint](#SobreASprint)
* [Como Usar](#comoUsar)
* [Backlog](#backlog)
* [MVP](#MVP)
* [Tag](#tag)

<span id="SobreASprint"></span>

# Sobre a Sprint
Nesta terceira entrega, foi combinado juntamente do cliente, a priorização da análise de dados e criação de gráficos através do filtro.
<img src="https://github.com/equipedevo/API_1/blob/main/doc/sprint/Site_sprint3.gif?raw=true"></br>

→ [Voltar ao topo](#topo)</br>

<span id="comoUsar"></span>

# :wrench: Como Usar
<h3>Para garantir o sucesso na utilização de nosso sistema, aqui vai uma lista das tecnologias necessárias para realizar os próximos passos:</h3>

<details>
  <summary><b>O que será necessário:</b></summary>

  1. <a href="https://git-scm.com/downloads">Git</a> Precisaremos do git para realizarmos a clonagem do nosso repositório do github.

  2. <a href="https://www.python.org/downloads">Python</a> Recomendamos que você instale uma versão superior à 3.6, nós particularmente utilizamos a 3.11, mas qualquer uma a partir do 3.7 irá funcionar, não esqueça de na hora da instalação, marcar a opção da instalação do pip, pois precisaremos dele para o ambiente virtual.
</details>

<details>
  <summary><b>Clonando o repositório:</b></summary>

1. Para clonar (baixar) o projeto e utiliza-lo no seu computador, siga os seguintes passos:

```
Crie uma pasta onde deseja clonar o projeto e abra-a
Clique no link do diretório ou utilize o comando "CTRL+L" no seu teclado
Digite "cmd" (sem aspas) e pressione "Enter"

Um prompt de comando (cmd) irá abrir, copie o comando todo abaixo e de "Enter"
git clone https://github.com/equipedevo/API_1
``` 

2. Ainda no cmd, você precisará ir para a pasta src, para isso, execute os seguintes comandos, linha por linha:
```
cd API_1/
cd src/
```
</details>


<details>
<summary><b>Iniciando o ambiente virtual para poder usar o projeto através do navegador:</b></summary> 

 1. Após entrar na pasta src, digite os seguintes comandos:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
  flask run
  ```

 2. Após realizar o comando "flask run", clique no link que aparece no cmd segurando o botão "CTRL" no seu teclado, ou então simplesmente acesse este link: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

 3. Após finalizar o uso do nosso site, para sair do ambiente virtual, execute o seguinte comando:
  ```
  CTRL+C (teclado)
  (digite) deactivate
  ```

</details>

→ [Voltar ao topo](#topo)

<span id="backlog"></span>

# Backlog

| Código |            Descrição das Tarefas            | Início | Término |
| :----: | :-----------------------------------------: | :----: | :-----: |
| US#15  | Protótipo dos Dropdowns                       | 03/abr | 03/mai  |
| US#16  | Coleta de Dados de Quantidade de Consultas    | 13/mar | 11/mai  |
| US#17  | Coleta de Dados de Quantidade de Medicamentos | 13/mar | 05/mai  |
| US#18  | Coleta de Dados de Quantidade de Tratamentos  | 13/mar | 09/mai  |
| US#19  | Coleta de Dados de Custo Consultas            | 05/abr | 11/mai  |
| US#20  | Coleta de Dados de Custo Medicamentos         | 05/abr | 05/mai  |
| US#21  | Coleta de Dados de Custo Tratamentos          | 05/abr | 09/mai  |
| US#22  | Checkbox de porcentagem                       | 06/mai | 06/mai  |
| US#23  | Funcão Porcentagem                            | 05/mai | 05/mai  |
| US#24  | Arrumar Pop-up em JavaScript                  | 10/mai | 11/mai  |
| US#25  | Arrumar os gráficos                           | 04/mai | 14/mai  |
| US#26  | Carrossel dos Gráficos                        | 06/mai | 06/mai  |
| US#27  | Erro dos campos inexistente                   | 05/mai | 05/mai  |
| US#28  | Arrumar Manual                                | 13/mai | 13/mai  |
| US#29  | README da sprint 3                            | 30/abr | 14/mai  |

→ [Voltar ao topo](#topo)

<span id="MVP"></span>

# :triangular_flag_on_post: Minimum Viable Product (MVP)

O mínimo produto viável desta sprint é um filtro funcional que mostre os dados de maneira clara e objetiva.

<details>
  <summary><b>Explicação das Tecnologias:</b></summary>
  <br>
  1. <a href="https://www.w3schools.com/html/">HTML</a>: Utilizado para toda a estruturação das páginas do nosso site<br>
  2. <a href="https://www.w3schools.com/css/">CSS</a>: Utilizado para toda a estilização das páginas do nosso site<br>
  3. <a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a>: Utilizado para fazer as rotas do nosso site e facilitar manutenção do mesmo, já que fazemos o uso do "base.html", onde está incluído tudo que será equivalente em todas as páginas do site<br>
  4. <a href="https://www.w3schools.com/js/default.asp">JavaScript</a>: Utilizado para as funcionalidades do filtro da página de consultas<br>
  5. <a href="https://www.w3schools.com/python/default.asp">Python</a>: Utilizado para fazer a construção dos gráficos através de arquivos .csv já criados
</details>

<span id="tag"></span>

# Tag

A última versão da 3ªSprint foi a [V3](https://github.com/equipedevo/API_1/releases/tag/V3.0).

→ [Voltar ao topo](#topo)

## [Ir para a tela de início](https://github.com/equipedevo/API_1/)
