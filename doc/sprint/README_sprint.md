<br id="topo">

# 2ª Sprint

## [Ir para a tela de início](./../../../README.md)

## :mag_right: Índice

<p style="text-align: center">
    <a href="#descrição">Descrição</a> |
    <a href="#comoUsar">Como Usar</a> |
    <a href="#MVP">MVP</a> |
    <a href="#backlog">BackLog</a> |
    <a href="#apresentação-do-projeto">Apresentação do projeto</a>
</p>

# Descrição
Nesta segunda entrega, foi combinado juntamente do cliente, a priorização da interface do projeto.

<span id="comoUsar"></span>

# :wrench: Como Usar
<h3>Para garantir o sucesso na utilização de nosso sistema, aqui vai uma listinha das tecnologias necessárias para realizar os próximos passos:</h3>
<h4>
  <details>
  <summary><b>O que será necessário:</b></summary>
  <h4>  1. <a href="https://git-scm.com/downloads">Git</a> Precisaremos do git para realizarmos a clonagem do nosso repositório do github
  </h4>
  <h4>  2. <a href="https://www.python.org/downloads">Python</a> Recomendamos que você instale uma versão superior à 3.6, nós particularmente utilizamos a 3.11, mas qualquer uma a partir do 3.7 irá funcionar, não esqueça de na hora da instalação, marcar a opção da instalação do pip, pois precisaremos dele para o ambiente virtual
  </h4>
  </details>
</h4>
<h4>
  <details>
  <summary><b>Clonando o repositório:</b></summary>
  <h4>  1. Clone o repositório atual através do git no seu cmd, utilize o comando:

  ```
  git clone https://github.com/equipedevo/API_1
  ```
  </h4>
  <h4>  2. Ainda no cmd vá para a pasta src:

  ```
  cd API_1/
  cd src/
  ```
  </h4>

  </details>
</h4>
<h4>
  <details>
  <summary><b>Rodando o projeto:</b></summary>
  <h4>  1. Após entrar na pasta src, digite os seguintes comandos:

    ```
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    flask run
    ```
  </h4>
  <h4>  2. Após realizar o comando flask run, clique no link que ele te dá no cmd, ou então simplesmente acesse este: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>
  </h4>
  <h4> 3. Após finalizar o uso do nosso site, para sair do ambiente virtual, execute o seguinte comando:

  ```
  deactivate
  ```
  </h4>

  </details>
</h4>

→ [Voltar ao topo](#topo)

<span id="MVP"></span>

# :triangular_flag_on_post: Minimum Viable Product (MVP)

O mínimo produto viável desta sprint é um site já navegável, porém com priorização apenas na programação das telas, sem necessariamente o uso das raspagens de dados, dos gráficos e  filtros que futuramente serão colocados.<br> 
A base para o MVP é a coerência entre o site programado e o nosso [Protótipo](./../prototipo/Prot%C3%B3tipo.gif), realizado na Sprint 1.

# Backlog

[Clique aqui](./Backlog_sprint.md) para acessar o backlog da segunda sprint.

→ [Voltar ao topo](#topo)

# Apresentação do Projeto

<h4>
<details>
  <summary><b><u>Vídeo:</u></b></summary>
  <img>
</details>
</h4>
<h4>
<details>
  <summary><b><u>Explicação das Tecnologias:</u></b></summary>
  <br>
  1. <a href="https://www.w3schools.com/html/">HTML</a>: Utilizado para toda a estruturação das páginas do nosso site<br>
  2. <a href="https://www.w3schools.com/css/">CSS</a>: Utilizado para toda a estilização das páginas do nosso site<br>
  3. <a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a>: Utilizado para fazer as rotas do nosso site e facilitar manutenção do mesmo, já que fazemos o uso do "base.html", onde está incluído tudo que será equivalente em todas as páginas do site<br>
  4. <a href="https://www.w3schools.com/js/default.asp">JavaScript</a>: Utilizado para a funcionalidade dos pop-ups<br>
  5. <a href="https://www.w3schools.com/python/default.asp">Python</a>: Utilizado para fazer a construção dos gráficos através de arquivos .csv já criados
</details>
</h4>

→ [Voltar ao topo](#topo)

## [Ir para a tela de início](./../../../README.md)
