# Projeto flightdashboard

Este projeto tem como objetivo a criação de um sistema integrado de controle de voos para um aeroporto. Tem como principais features o CRUD, que permite o cadastro, leitura, deleção e atualização de voos no sistema e a geração de relatório de voos. 

A linguagem de promação usada é o Python, com a framework Django.

**Diagrama de Entidade e Relacionamento:**

![This is an image](https://i.imgur.com/kcgnGWB.png)[

**Diagrama de Navegação no Sistema:**

![This is an image](https://i.imgur.com/UH5zzUy.png)

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
    C:\...\MinhaPastaLocal> git clone https://github.com/Brenovyski/projeto_PCS3643_FD
    ```

2. É recomendado criar um ambiente virtual usando `venv` utilizando o python (a depender do seu sistema operacional). Para isso, use o comando:

    ```
    C:\...\MinhaPastaLocal> cd projeto_PCS3643_FD
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> python -m venv env
    ```

3. Depois, e ative o ambiente usando o comando no Powershell do Windows:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> .\env\bin\Activate.ps1
    ```
    se não funcionar, tente trocar a pasta `bin` por `Scripts`:
    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> .\env\Scripts\Activate.ps1
    ```


4. Instale os requerimentos do projeto:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> pip install -r requirements.txt
    ```

5. Faça as migrações do Django:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD> cd flightdashboard
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py makemigrations
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py makemigrations sys_voos
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py migrate
    ```
6. Execute os testes:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py test
    ```

7. Crie os usuários padrão para o uso do sistema (logins pré-definidos):

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard> python manage.py createsuperuser
    ```

    Rode esse comando 3 vezes para criar 3 credenciais diferentes conforme o seguinte padrão:

    | Username      | Email address             | Password    |
    |---------------|---------------------------|-------------|
    | Administrador | admin@flightdashboard.com | admin       |
    | Funcionario   | func@flightdashboard.com  | func        |
    | Gerente       | geren@flightdashboard.com | geren       |

8. Para rodar o projeto, use os comandos:

    ```
    C:\...\MinhaPastaLocal\projeto_PCS3643_FD\flightdashboard>python manage.py runserver
    ```


9. Finalmente, para executar os sistema, acessamos o link:

    http://localhost:8000/
