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

```bash
$ pip freeze > requirements.txt
```

```bash
$ pip install django
$ pip install djandorestframework
$ pip install markdown
$ pip install django-filter
```
```bash
$ pip install --upgrade pip
```

```bash
$ pip install djangorestframework
```

### Criando projeto

```bash
$ django-admin startproject school .
```

### Criando apps 

```bash
$ py .manage.py 
```

### Sincronização inicial do banco de dados

```bash
$ py .\manage.py migrate
```

### Configuração

-Em .\school\settings.py adicione manualmente em INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework'
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

## Roteamento das URl

- Rotas do Programa
- Arquivos urls.py

### View

Descreve qual dados são apresentados.

Uma View é simplesmente uma função Python que recebe uma request e retorna uma response.

Uma resposta pode ser um conteúdo HTML de uma página Web, um redirecionamento, um error 404,
um documento XML, uma imagem.

A visualização em si contém qualquer lógica arbitrária para retornar essa resposta.

Como estamos trabalhando com REST APIs, o conteúdo da resposta HTTP deve ser em JSON.

### Modal

Descreve as entidades lógicas do seu problema.

Podem ou não ser uma tabela no banco de dados

![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/06.png?raw=true)

#### Migrações

- Passo 1: Mudar o seu modelo (models.py)
- Passo 2: rodar ```bash $ manage.py makemigrations ``` para gerar os arquivos de migração
- Passo 3: rodar ```bash $ manage.py migrate ``` para aplicar as mudanças no banco de dados

- Django Shell ```bash $ py manage.py shell ```

Consultar estudantes
```bash $ from grades.models import Student ```
```bash $ Student ```

```bash $ Student.objects.all() ```

Registrar estudante
```bash $ Student.objects.create(first_name="Raul", last_name="Moraes", age=10) ```

#### Serializer

![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/07.png?raw=true)

## Class Based Views (CBV)

Class Based Views fornecem uma maneira alternativa de implementar Views com objetos Python, ao invés de funções.

Não substitui as function based view

Reutilizar código através de:
- Herança
- Mixins

💡 Evita fazer um branch com if's

🔗 [Classy Django REST Framework](https://www.cdrf.co/)

IDE que possa navegar nas classes do Django e do DRF

Generics, Mixins, ViewSets...

## Ednpoint

É a URL onde seu serviço pode ser acessado por uma aplicação cliente

Cliente -> [endpoints] <- API

# Request

HTTP + URL

Além de uma requisição é uma Query string.

## URL

URL - Uniform Resource Identifier (Identificador de Recursos Universal)

- Acesso:
    - https://meusite.com.br/api/v1/produtos
    - https://meusite.com.br/api/v1/categorias

- Obs.: Estas URIs são os endpoints

### Chame os substantivos

- Sempre que falar em endpoint lembre-se:
    - pode representar uma coleção de registros;
    - ou um registro individual

- Coleção: /api/v1/produtos
- Individual: /api/v1/produtos/16

### Ações por Verbo

- RESTfull fornecem estratégias para lidar com as ações de CRUD (Create, Read, Update e Delete);
- Métodos HTTP mapeados da seguinte forma:
    
    | Método | URL | Descrição |
    | ------------------- | ------------------- | ------------------- |
    | GET    |   /api/v1/produtos    | Retorna todos os produtos |
    | GET    |   /api/v1/produtos/12 | Retorna todos o produto com ID 12 |
    | POST   |   /api/v1/produtos    | Enviar um produto |
    | POST   |   /api/v1/produtos/12 | Atualiza o produto com ID 12 |
    | PATCH  |   /api/v1/produtos/12 | Atualiza parcialmente o produto com ID 12  |
    | DELETE |   /api/v1/produtos/12 | Delete o produto com ID 12 |

## Query string

```bash
api/v1/produtos?format=xml
```
```bash
api/v1/produtos?order=desc&limite=10
```

- Tudo que está após o símbolo de interrogação (? - question mark) são:
    - Conjunto de pares chave/valor que podem ser utilizadas pela API para alterar os dados de acordo com estes parâmetros.
    - Esta forma de passar dados em uma requisição é chamada de "query string".

## Boas práticas

```bash
api/v1/produtos?format=xml
```

- Prover diretamente o formato desejado, conforme:

```bash
api/v1/produtos.xml
```

- Basta que prestemos atenção no cabeçalho da requisição HTTP, que nos foi enviado

```bash
Accept: application/xml
```

### Cabeçalhos HTTP - Accept

- Especifica o formato do arquivo que o (solicitante) quer:
    - Accept: application/xml
    - Accept: application/json
    - Accept: application/pdf

- Especifica a língua do conteúdo, por exemplo:
    - English;
    - Portuguese;
    - Spanish;

- Cabeçalhos HTTP - Accept - Cache
    - Especifica se o conteúdo pode ser consumido:
        - do cache;
        - tempo que o cache é atualizado.

- Dar atenção
    - Nem sempre precisamos prestar atenção no cabeçalho de um request;
    - Diferentes métodos HTTP enviam dados de formas diferentes;

# Response

Resposta do servidor ao cliente.

## Status Code

O servidor utiliza um código desse na resposta para indicar o que aconteceu.

![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/08.png?raw=true)

- Os códigos estão entre 100 e 500:
    - 1xx - Informativos
    - 2xx - Indicativos de sucesso
    - 3xx - Redirecionamentos
    - 4xx - Erros do cliente na hora de fazer a solicitação
    - 5xx - Erros no lado do servidor

- Códigos específicos
    - 200 - Tudo ocorreu corretamente
    - 301 - Indica redirecionamento permanente
    - 401 - Não autorizado
    - 404 - O recurso solicitado não foi encontrado no servidor
    - 403 - 405 - O URL pode ser requisitada apenas com o GET e não POST.
    - 500 - 509 - Erro do servidor


##

- 
🔗 []()
🔗 []()
🔗 []()

![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/0.png?raw=true)