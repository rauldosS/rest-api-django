# Rest API Django

Criando uma rest api com django

Application Programming Interface

"É um conjunto de funções estabelecidos por um software para 
a utilização das suas funcionalidades por aplicativos que não 
pretendem envolver-se em detalhes de implementação de software, 
mas apenas usar seus serviços"

## Esquemas

Programa 1 contém lógica de negócio e comunicação com banco
![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/01.png?raw=true)

Programa 1 pode ser acessível em vários dispositivos (lógica de negócio e comunicação com banco)
![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/02.png?raw=true)

Programa 1 é consumido por outras empresas
![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/03.png?raw=true)

## API == Serviço

Para utilizar esse serviço, você precisa entender como ele funciona

- Criar documentação

## O quê tem a ver com a economia?

- API é um produto
- Fácil de integrar
- Viabilização de parcerias

"As APIs do Twitter têm facilmente dez vezes mais tráfego do que o site do Twitter"


🔗 [APIs THE BUILDING BLOCKS OF THE APP ECONOMY - NEW YORK TIMES](https://www.nytimes.com/paidpost/ca-technologies/apis-the-building-blocks-of-the-app-economy.html)

## Exemplos

🔗 [Twitter](https://developer.twitter.com/en/docs/twitter-api)
🔗 [Facebook]()
🔗 [Youtube](https://developers.google.com/youtube/v3)
    🔗 [Youtube Examples](https://github.com/youtube/api-samples)

🔗 [Github examples](https://github.com/public-apis/public-apis)
🔗 [Rapidapi examples](https://rapidapi.com/blog/most-popular-apis-2018/)

# API
## Métodos HTTP

- GET: Retorna recursos do servidor. Não altera o servidor
- POST/PUT: Criar e editar recursos no servidor
- DELETE: Deletar recursos do servidor

## REST APIs

- Design de APIs para web
- É um estilo de arquitetura
- Série de padrões/restrições para construir uma API

🔗 [Sua API não é RESTful: Entenda por quê](https://blog.geekhunter.com.br/sua-api-nao-e-restful-entenda-por-que/)
🔗 [10 Best Practices for Better RESTful API](https://medium.com/@mwaysolutions/10-best-practices-for-better-restful-api-cbe81b06f291)

## Representação dos Dados

- JSON
- XML
- ...

### JSON
- JavaScript Object Notation
- Formato utilizado pelo padrão REST
- Modelo de dados
- O formato JSON é sinteticamente idêntico ao código para criar objetos JavaScript

🔗 [JSON](https://www.json.org/json-en.html)
🔗 [JSON em Python](https://docs.python.org/pt-br/3/library/json.html)

# DJANGO REST FRAMEWORK

Django: Web Framework para Python

DRF permite que uma aplicação Django se comporte com uma REST API

Django REST Framework é um kit de ferramentas poderoso e flexível para criar Web APIS

### Por que Django/DRF?

- Rápido de fazer uma aplicação
- Possui várias ferramentas
- Versátil
- Escalável

### Links

🔗 [Quick Start]()
🔗 [Tutorial]()
🔗 [Web browsable API](https://restframework.herokuapp.com/)

# Criando um Projeto (School)

### Criar e ativar ambiente virtual

```bash
$ python -m venv env
```
```bash
$ .\env\Scripts\activate
```

### Instalar dependências

Python

```bash
\$ pip install django
```
```bash
\$ pip install --upgrade pip
```
```bash
\$ pip install djangorestframework
```

### Criando projeto

```bash
\$ django-admin startproject school .
```

### Criando apps 

```bash
\$ py .manage.py 
```

### Sincronização inicial do banco de dados

```bash
\$ py .\manage.py migrate
```

### Configuração

-Em .\school\settings.py adicione manualmente em INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework'
    'grades.apps.GradesConfig'
]
```

🔗 [Configurações](https://www.django-rest-framework.org/api-guide/settings/)

### Arquitetura

Arquitetura: Model, Serializar e View (MSC?)

View: Descreve qual dado será apresentado
Serializar: Descreve como o dado será apresentado (JSON)
Model: Descreve as entidades da lógica do seu problema

### Django's architecture
![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/04.png?raw=true)

### DRF's architecture
![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/05.png?raw=true)


🔗 []()
🔗 []()
🔗 []()

![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/02.png?raw=true)