# Projeto flightdashboard

Este projeto tem como objetivo a criação de um sistema integrado de controle de voos para um aeroporto. Tem como principais features o CRUD, que permite o cadastro, leitura, deleção e atualização de voos no sistema e a geração de relatório de voos. 

A linguagem de promação usada é o Python, com a framework Django.

## Nome do Grupo: BCJ

**Integrantes:** 

Breno Suguru Costa Tominaga - NUSP: 11804320

Caio Amaral Gurgel Xavier - NUSP: 11804293

Johan Su Kwok - NUSP: 10770176

## Pré-requisitos:
[Python 3.6+](https://www.python.org/downloads/)


## Roteiro de Execução do Projeto

1. Clone o repositório a alguma pasta local.

    ```
    C:\...\MinhaPastaLocal> git clone https://github.com/Brenovyski/flightdashboard.git
    ```

2. É recomendado criar um ambiente virtual usando `venv` utilizando o python (a depender do seu sistema operacional). Para isso, use o comando:

    ```
    C:\...\MinhaPastaLocal>python -m venv env
    ```

3. Depois, e ative o ambiente usando o comando no Powershell do Windows:

    ```
    C:\...\MinhaPastaLocal>.\env\bin\Activate.ps1
    ```

4. Instale os requerimentos do projeto:

    ```
    C:\...\MinhaPastaLocal> cd flightdashboard
    C:\...\MinhaPastaLocal\flightdashboard>pip install -r requirements.txt
    ```

5. Para rodar o projeto, use os comandos:

    ```
    C:\...\MinhaPastaLocal\flightdashboard> cd flightdashboard
    C:\...\MinhaPastaLocal\flightdashboard\flightdashboard>python manage.py runserver
    ```

6. Finalmente, para realizar o teste da aplicação voo, acessamos o link:

    http://localhost:8000/voos


Diagrama de Entidade e Relacionamento:



![This is an image](https://i.imgur.com/kcgnGWB.png)

