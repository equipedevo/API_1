<br id="topo">

# 2ª Sprint

## [Ir para a tela de início](./../../../README.md)

## :mag_right: Índice

* [Sobre a Sprint](#SobreASprint)
* [Como Usar](#comoUsar)
* [Backlog](#backlog)
* [MVP](#MVP)
* [Tag](#tag)

<p style="text-align: center">
<span id="SobreASprint"></span>

# Sobre a Sprint
Nesta segunda entrega, foi combinado juntamente do cliente, a priorização da interface do projeto.
<img src="https://github.com/equipedevo/API_1/blob/main/doc/sprint/Site_sprint2.gif?raw=true"></br>

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

 1. Clone o repositório atual através do git no seu cmd, utilize o comando:
  ```
  git clone https://github.com/equipedevo/API_1
  ```

 2. Ainda no cmd vá para a pasta src:
  ```
  cd API_1/src/
  ```
</details>


<details>
<summary><b>Rodando o projeto:</b></summary> 

 1. Após entrar na pasta src, digite os seguintes comandos:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
  flask run
  ```

 2. Após realizar o comando flask run, clique no link que ele te dá no cmd, ou então simplesmente acesse este: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

 3. Após finalizar o uso do nosso site, para sair do ambiente virtual, execute o seguinte comando:
  ```
  deactivate
  ```

</details>

→ [Voltar ao topo](#topo)

<span id="backlog"></span>

# Backlog

| Código |      Backlog     |     Quem      |                                                                 Quer                                                                 |                       Para                        |
| :----: | :--------------: | :-----------: | :----------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------: |
| US#05  | Página Home      | Cliente       | Ver uma introdução de onde ir no site quando eu abri-lo o site pela primeira vez.                                                    | Me direcionar nele.                               |
| US#06  | Página Sobre     | Cliente       | Saber sobre a importância e utilidade do site.                                                                                        | Saber mais sobre o site.                          |
| US#07  | Página Consulta  | Cliente       | Ver os gráficos e poder alterar a visualizaçãos deles através de filtros.                                                            | Saber os dados da covid longa.                    |
| US#08  | Pop-up Fontes    | Usuário Leigo | Saber como visualizar os gráficos e os filtros.                                                                                      | Poder visualizar os gráficos que prefiro.         |
| US#09  | Pop-up Ajuda     | Jornalista    | Saber as fontes que foram utilizadas para fazer o site.                                                                              | Saber a verossimilidade do site.                  |
| US#10  | NavBar           | Usuário       | Um modo de navegar por todas as páginas e pop-ups do sites facilmente.                                                               | Ver tudo que o projeto tem a oferecer.            |
| US#11  | Filtro de cidade | Jornalista    | Poder filtrar as informações que desejo visualizar entre as cidades de SJC, Jacareí e Taubaté.                                       | Poder facilitar na montagem de uma matéria.       |
| US#12  | Filtro de ano    | Jornalista    | Poder filtrar as informações que desejo visualizar entre as anos de 2019 a 2022.                                                     | Poder facilitar na montagem de uma matéria.       |
| US#13  | Filtro de Tipo   | Jornalista    | Poder filtrar as informações que desejo visualizar entre tipos de consultas, tratamentos, procedimentos, internações e medicamentos. | Poder facilitar na montagem de uma matéria.       |
| US#14  | Botão Troca      | Jornalista    | Alterar a visualização dos dados entre número e porcentagem.                                                                         | Facilitar o entendimento da diferença entre eles. |

→ [Voltar ao topo](#topo)

<span id="MVP"></span>

# :triangular_flag_on_post: Minimum Viable Product (MVP)

O mínimo produto viável desta sprint é um site já navegável, porém com priorização apenas na programação das telas, sem necessariamente o uso das raspagens de dados, dos gráficos e  filtros que futuramente serão colocados.<br> A base para o MVP é a coerência entre o site programado e o nosso [Protótipo](./../../prototipo/Prot%C3%B3tipo.gif), realizado na Sprint 1.

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

A última versão da 2ªSprint foi [V2.3](https://github.com/equipedevo/API_1/releases/tag/V2.3)

→ [Voltar ao topo](#topo)

## [Ir para a tela de início](https://github.com/equipedevo/API_1/)