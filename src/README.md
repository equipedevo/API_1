# Como rodar
> _Os códigos e processos presentes neste readme possuem versão para WINDOWS e LINUX, dentro de comentários como este, para melhor aproveitamento e abrangência de nosso projeto_
## O que será necessário

Para garantir o sucesso na utilização de nosso sistema, aqui vai uma listinha das tecnologias necessárias para realizar os próximos passos:

1. [Git](https://git-scm.com/downloads): Precisaremos do git para realizarmos a clonagem do nosso repositório do github.

2. [Python](https://www.python.org/downloads/): Recomendamos que você instale a versão do python 3.11, não esqueça de na hora da instalação, marcar a opção da instalação do pip, pois precisaremos dele para a criação e configuração do ambiente virtual.

## Clonando o repositório:

<details>
  <summary><b>Clique aqui</b></summary>

 Para clonar o projeto e utilizá-lo em seu computador, siga os seguintes passos:

 1. Crie uma pasta onde deseja armazenar nosso projeto, e então abra-a e clique na url da pasta ou então utiliza o comando ```Ctrl+L``` para selecionar a url <br> Como demonstrado no exemplo abaixo 👇<br> <img src="https://media.discordapp.net/attachments/733064358694748303/1113832068032507954/image.png">

 > _Obs.: Caso você esteja no LINUX, o cmd não vai funcionar, então clique com o botão direito na pasta que você criou e clique em "Abrir no terminal"_

 Um prompt de comando irá abrir, e então execute o comando abaixo
 ```
 git clone https://github.com/equipedevo/API_1
 ``` 

 2. Ainda no cmd, execute os seguintes comandos para entrar no diretório da aplicação:
 ```
 cd API_1/
 cd src/
 ```
</details>

## Iniciando o ambiente virtual

<details>
<summary><b>Clique aqui</b></summary> 

 1. Estando na pasta ```src```, execute os seguintes comandos:
 ```
 python -m venv venv
 venv\Scripts\activate
 pip install -r requirements.txt
 flask run
 ```
 > _Caso você esteja em LINUX, digite os comandos desta maneira:_ <br>```python3 -m venv venv```<br>
 ```source venv/bin/activate```<br>
 ```pip install -r requirements.txt```<br>
 ```flask run ```

 2. Após isto, entre no link que aparecerá no cmd copiando e colando ele no seu navegador de preferência, ou então simplesmente clique aqui: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

 3. Após finalizar o uso do nosso site, para sair do ambiente virtual, no cmd, execute o atalho ```Ctrl+C``` para finalizar o serviço do Flask, e então execute o seguinte comando:
 ```
 deactivate
 ```

</details>

→ [Voltar ao topo](#topo)
