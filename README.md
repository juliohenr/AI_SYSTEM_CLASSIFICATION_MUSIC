# AI_SYSTEM_CLASSIFICATION_MUSIC

## Resumo

Este projeto consiste em uma inteligência artificial, a qual foi desenvolvida utilizando técnicas de redes neurais, para classificação de gênero musicais. Esta Inteligência Artificial classifica apenas 4 gêneros musicais os quais são: BOSSA NOVA, FUNK, SERTANEJO e GOSPEL.

## Tecnologias Utilizadas

<ul>
<li>Django</li>
<li>Jquery</li>
<li>Docker</li>
<li>Python 3.7</li>
</ul>  


## Interface

A interface desenvolvida é responsiva e contém 6 elementos, os quais são: text box, probabilidades das classes, índice de confiança da classe com maior proba, relatório com o comparativo da quantidade de tokens com a quantidade média de tokens das bases de cada classe, relatório com o comparativo da quantidade de tokens diferentes com a quantidade média de tokens diferentes das bases de cada classe e o relatório com as palavras mais frequentes. Abaixo será exibido cada elemento.

### Interface Completa

![interface_completa](https://user-images.githubusercontent.com/40969977/93151669-eb54f500-f6d2-11ea-9c98-842247d1c186.png)


### Elemento Text Box

Este elemento contém o input para o usuário inserir o texto e enviar para Inteligência Artificial

![text_box](https://user-images.githubusercontent.com/40969977/93150437-7fbd5880-f6cf-11ea-8d38-7248cb154bca.png)

### Probabilidades das Classes

Este elemento contém um gráfico de barras com o proba calculado pela Inteligência Artificial de cada classe 
![probabilidades](https://user-images.githubusercontent.com/40969977/93153071-bcd91900-f6d6-11ea-96a6-a622a06a94a1.png)


### Índice de confiança da classe com maior proba

Este elemento exibe o valor do índice de confiança da classe que obteve a maior probabilidade 
![indice](https://user-images.githubusercontent.com/40969977/93152984-87ccc680-f6d6-11ea-9af6-54f637cc0201.png)

### Relatório com o comparativo da quantidade de tokens com a quantidade média de tokens da base de cada classe em percentual

No exemplo abaixo a amostra (letra de música) tem aproximadamente 80% a menos de tokens comparado com as bases de desenvolvimento utilizadas para cada classe
![diferents_words](https://user-images.githubusercontent.com/40969977/93152870-37556900-f6d6-11ea-93a3-41cb1dc11872.png)

### Relatório com o comparativo da quantidade de tokens diferentes com a quantidade média de tokens diferentes da base de cada classe em percentual

No exemplo abaixo a amostra (letra de música) tem aproximadamente 70% a menos de tokens diferentes comparado com as bases de desenvolvimento para cada classe
![diferents](https://user-images.githubusercontent.com/40969977/93153097-d2e6d980-f6d6-11ea-883a-636d20c3b8a3.png)

### Relatório com as palavras mais frequentes em percentual

No exemplo abaixo a amostra (letra de música) tem como a palavra mais frequente "dançar", e a mesma representa aproximadamente 18% da amostra

![frequents_words](https://user-images.githubusercontent.com/40969977/93152961-72579c80-f6d6-11ea-945b-11853143c274.png)


## Execução 

É necessário a instalação das dependências através do comando "pip install -r requirements.txt". Após a instalação das dependências o usuário pode iniciar a aplicação através do comando "python manage.py runserver 0.0.0.0:8000" 

## Execução pelo docker

É possível iniciar a aplicação pelo docker também. Na pasta dockers contém um dockerfile e na raiz um docker-compose para buildar a aplicação, logo o usuário pode rodar o "docker-compose build" e em seguida o "docker-compose up"


## Desenvolvimento do modelo

Na pasta MODEL contém o jupyter notebook com todas as etapas de desenvolvimento do modelo, e as bases utilizadas. No jupyter é realizado uma análise exploratória com o intuito de entender os detalhes das bases utilizadas de cada classe, no mesmo é feito diversas visualizações como por exemplo as palavras diferentes entre as classes e mais frequentes em cada uma, como pode ser visto na figura abaixo: 


![exploratory](https://user-images.githubusercontent.com/40969977/93154761-d4b29c00-f6da-11ea-9b6b-bea34e817bae.png)

Foi realizado também neste jupyter notebook alguns testes com diferentes configurações de redes neurais, para mais detalhes da etapa 



