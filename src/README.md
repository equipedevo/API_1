# Como rodar
> _Os códigos e processos presentes neste readme possuem versão para WINDOWS e LINUX, dentro de comentários como este, para melhor aproveitamento e abrangência de nosso projeto_
## O que será necessário

Para garantir o sucesso na utilização de nosso sistema, aqui vai uma listinha das tecnologias necessárias para realizar os próximos passos:

1. [Git](https://git-scm.com/downloads): Precisaremos do git para realizarmos a clonagem do nosso repositório do github.

2. [Python](https://www.python.org/downloads/): Precisaremos do python, para isso, recomendamos que você instale a versão 3.11, não se esqueça de na hora da instalação, marcar a opção da instalação do pip, pois precisaremos dele para a criação e configuração do ambiente virtual.

3. [MySQL](https://dev.mysql.com/downloads/): Precisaremos também do MySQL para obter a funcionalidade de estatísticas das opções mais utilizadas no filtro.

## 1º Passo: Clonando o repositório

<details>
  <summary><b>Clique aqui</b></summary>

  Para clonar o projeto e utilizá-lo em seu computador, siga os seguintes passos:
  
  1. Crie uma pasta onde deseja armazenar nosso projeto, e então abra-a e clique na url da pasta, ou então utilize o atalho `Ctrl+L` para selecionar a url, como demonstrado no exemplo abaixo 👇<br> <img src="https://media.discordapp.net/attachments/733064358694748303/1113832068032507954/image.png">
  
  > _Obs.: Caso você esteja no LINUX, a parte de escrever "cmd" não irá funcionar, então clique com o botão direito na pasta que você criou e selecione a opção "Abrir no terminal"_

  Um prompt de comando irá se abrir, e então execute o comando abaixo:
  
  ```
  git clone https://github.com/equipedevo/API_1
  ``` 

  2. Ainda no cmd, execute os seguintes comandos para entrar no diretório da aplicação:

  ```
  cd API_1/
  cd src/
  ```

</details>
<br>

## 2º Passo: Iniciando o ambiente virtual

<details>
  <summary><b>Clique aqui</b></summary>

  1. Estando na pasta `src`, execute os seguintes comandos:

  ```
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

  > _Caso você esteja em LINUX, digite os comandos desta maneira:_<br>
  `python3 -m venv venv`<br>
  `source venv/bin/activate`<br>
  `pip install -r requirements.txt`

</details>
<br>

## 3º Passo: Preparando o banco de dados

<details>
  <summary><b>Clique aqui</b></summary>

  1. Com o banco de dados MySQL devidamente instalado e configurado, execute os comandos do arquivo `BancoCICOVALE.sql` que se encontra na pasta `src/database/`.

  2. Edite o arquivo app.py da seguinte maneira:
  ```
  app.config["MYSQL_HOST"] = "127.0.0.1"
  app.config["MYSQL_USER"] = "PREENCHA AQUI COM SEU USUARIO NO MYSQL"
  app.config["MYSQL_PASSWORD"] = "PREENCHA AQUI COM A SENHA DO SEU USUARIO NO MYSQL"
  app.config["MYSQL_DB"] = "BancoCICOVALE"
  ```

  3. Edite também o arquivo databaseAutoInsert.py, dessa forma:
  ```
    conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "PREENCHA AQUI COM SEU USUARIO NO MYSQL"
    password = "PREENCHA AQUI COM A SENHA DO SEU USUARIO NO MYSQL"
    db = "BancoCICOVALE")
  ```

  4. Ainda com o ambiente virtual aberto, execute o comando:
  ```
  python databaseAutoInsert.py
  ```

  5. Caso algum erro ocorra, certifique-se de ter seguido todos os passos e instalado o MySQL corretamente.
  > _Também pode dar algum erro caso você não tenha iniciado o serviço do MySQL em seu computador, para isso, pesquise pelo aplicativo "Serviços", ache o serviço do MySQL e clique em "Iniciar"._

</details>
<br>

## 4º Passo: Abrindo a aplicação web

<details>
  <summary><b>Clique aqui</b></summary>

  1. Ainda dentro do ambiente virtual, execute o seguinte comando:
  ```
  flask run
  ```

  2. Por fim, entre no link que aparecerá no cmd copiando e colando ele no seu navegador de preferência, ou então simplesmente clique aqui: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

  3. Após finalizar o uso do nosso site, para sair do ambiente virtual, no cmd, execute o atalho `Ctrl+C` para finalizar o serviço do Flask, e então execute o seguinte comando:
  ```
  deactivate
  ```

</details>

→ [Voltar ao topo](#topo)
