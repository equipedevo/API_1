# Como rodar

## O que será necessário

Para garantir o sucesso na utilização de nosso sistema, aqui vai uma listinha das tecnologias necessárias para realizar os próximos passos:

1. [Git](https://git-scm.com/downloads): Precisaremos do git para realizarmos a clonagem do nosso repositório do github

2. [Python](https://www.python.org/downloads/): Recomendamos que você instale uma versão superior à 3.6, nós particularmente utilizamos a 3.11, mas qualquer uma a partir do 3.7 irá funcionar, não esqueça de na hora da instalação, marcar a opção da instalação do pip, pois precisaremos dele para o ambiente virtual

## Clonando o repositório

1. Clone o repositório atual através do git no seu cmd, utilize o comando:

```
git clone https://github.com/equipedevo/API_1
``` 

2. Ainda no cmd vá para a pasta src:
```
cd API_1/
cd src/
```

## Startando o ambiente virtual

1. Após entrar na pasta src, digite os seguintes comandos:
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask run
```

2. Após realizar o comando flask run, clique no link que ele te dá no cmd, ou então simplesmente acesse este: http://127.0.0.1:5000

3. Após finalizar o uso do nosso site, para sair do ambiente virtual, execute o seguinte comando:
```
deactivate
```