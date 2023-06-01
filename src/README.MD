# Como rodar

## O que será necessário

Para garantir o sucesso na utilização de nosso sistema, aqui vai uma listinha das tecnologias necessárias para realizar os próximos passos:

1. [Git](https://git-scm.com/downloads): Precisaremos do git para realizarmos a clonagem do nosso repositório do github

2. [Python](https://www.python.org/downloads/): Recomendamos que você instale uma versão superior à 3.6, nós particularmente utilizamos a 3.11, mas qualquer uma a partir do 3.7 irá funcionar, não esqueça de na hora da instalação, marcar a opção da instalação do pip, pois precisaremos dele para o ambiente virtual

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
<summary><b>Iniciando o ambiente virtual para poder usar o projeto através do navegador:<b></summary> 

 1. Após entrar na pasta src, digite os seguintes comandos:
 ```
 python -m venv venv
 .\venv\Scripts\activate
 pip install -r requirements.txt
 flask run
 ```

 2. Após realizar o comando "flask run", clique no link que aparece no cmd segurando o botão "CTRL" no seu teclado, ou então simplesmente acesse este link: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

 3. Após finalizar o uso do nosso site, para sair do ambiente virtual, execute os seguintes comando:
 ```
 CTRL+C (teclado)
 (digite) deactivate
 ```

</details>

→ [Voltar ao topo](#topo)
