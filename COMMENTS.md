# Teste para vaga de desenvolvedor na W Technology

O projeto consistem em criar um API Rest para cadastrar e obter informações de empresas, ofertas e lances.
Os dados foram armazenados em um banco de dados Postgres, para isso foi usado a ferramenta docker. Para a construção do projeto será usado Django bem como Django Rest Framework.

Todo o projeto foi realizado usado Test Driven Development (TDD), bem como ferramentas de linter como pylava. Assim o código final fica mais limpo e com melhor manutenção.

Para automatizar o processo de testes será usado o [tox](https://tox.wiki/en/latest/index.html). Também será usado github actions para realização dos testes após cada push para o servidor do github. Será usado o [coverage]() para proporcionar um feedback visual do código testado e não testado.

## Criação do projeto

Inicialmente deve-se iniciar o projeto usando um gerenciador de pacotes, para isolar as dependências. Para esse projeto será usado o pipenv.

```
pipenv shell
```

Agora temos que instalar o djando. Instalaremos os demais pacotes a medida que formos necessitando.

```
pipenv install django
```

Para criar o projeto podemos usar o comando no terminal.

```
django-admin startproject w_technology
```

Logo depois, deve-se criar uma app. Essa app centralizará os modelos, bem como as regras de negócio.

```
django-admin startapp core
```

Agora já poderíamos partir para criação dos modelos, mas para melhor gerenciamento do projeto, vamos criar as configurações do tox.

## Configurando o ambiente de testes

### Configurando o tox

inicialmente precisamos instalar o tox, e depois criar o arquivo de configuração `tox.ini` e `setup.py` na raiz do projeto. Para a instalação usaremos o comando:

```
pipenv install tox -d
```

A flag `-d` foi usada para declarar o pacote como dependência de desenvolvimento.

Depois do ambiente configurado, basta rodar `tox` no terminal, e todos os testes serão executados.

### Criar a configurar o repositório no GITHUB

Inicialmente temos que criar o repositório local usando o comando:

```
git init
```

Em seguida, adicionamos um arquivo `.gitignore`. Dentre várias opções, usaremos o site [gitignore.io](https://gitignore.io). Agora podemos criar um repositório remoto no github. logo em seguida, podemos linkar o nosso repositório local com o remoto usando o comando:

```
git remote add origin https://github.com/danilodcn/teste_W_Technology.git
```

Para finalizar essa primeira parte vamos fazer o primeiro commit. Para isso, vamos juntar todos os arquivos criados até aqui em um único commit. E em seguida subir para o servidor:

```
$ git add .
$ git commit -m "criação do projeto + configuração do tox"
$ git push
```

### Configurando o git actions

Agora temos que configurar o git actions para realização dos testes sempre que subirmos o código.

obs: nao sei explicar o motivo, mas os testes falham no github actions. Da um erro no report do coverage. Vou tentar remover algumas linhas da configuração e ver se o teste passa.
Ainda nao passou!!! O erro é o seguinte:

```
 No data to report.
  ERROR: InvocationError for command /home/runner/work/teste_W_Technology/teste_W_Technology/.tox/stats/bin/coverage report (exited with code 1)
```

Ao finalizar o projeto eu volto nessa tema e tento novamente.

## Configuração do Postgres usando Docker

Existem várias maneiras de subir o serviço do Postgres por meio do docker. Uma delas é usando docker compose. Essa ferramenta usa um arquivo de configuração com extensão `.yaml`. Essa ferramenta facilita a orquestração de múltiplos containers. Poderíamos apenas rodar um simples `docker run` no terminal, mas como precisamos passar várias variáveis de ambiente, é mais simples usar o docker compose.

Depois do arquivo de configuração criado, podemos rodar o seguinte comando:

```
docker-compose up -d
```

Usando a flag -d, o docker sobe o container em background.

No arquivo de configuração criamos três variáveis de ambiente que serão usadas na configuração do banco no arquivo `settings.py` do django. São elas: POSTGRES_PASSWORD, POSTGRES_DB e POSTGRES_USER.


## configurando o Banco de Dados do django

Inicialmente vamos configurar o django para usar banco de dados Postgres, cuja configuração foi apresentada na seção anterior. Para isso vamos criar um arquivo `.env` na raiz do projeto. Nesse arquivo vamos adicionar todas as variáveis de ambiente necessárias. Já vamos aproveitar e criar uma variável de ambiente para a `SECRET_KEY`. Para carregar as variáveis de ambiente, vamos usar o módulo `python-dotenv`.

Para instalar o pacote `python-dotenv` usamos o comando:

```
pipenv install python-dotenv
```

## Criação dos modelos no Banco de Dados

Todos os modelos serão criados na app core, para que facilite as posteriores mudanças na aplicação. Esses modelos serão criados no arquivo `models.py` do app core.

Para aplicar as mudanças no banco de dados temos adicionar a app `core` na lista `INSTALLED_APPS` no arquivo `settings.py` e depois que realizar as migrações usando os comandos:

```
$ python manage.py makemigrations
$ python manage.py migrate 
```

## Usando o Django Admin

Para gerenciar nossa aplicação de maneira fácil e simples podemos usar o django admin. Esse aplicativo de administração do django pode usar os modelos criados para criar automaticamente uma área para criar, atualizar, visualizar, editar e excluir registros no banco de dados. Ele também será usado para gerenciar os usuário da aplicação.

Por padrão o django expõe essa aplicação na rota `/admin`, mas é possível alterá-la no arquivo `admin.py`  

Para criar o usuário e senha de administração podemos usar o comando:

```
$ python manage.py createsuperuser
```

Ao fazer login podemos ver toda o ambiente administrativo do django. Agora temos que adicionar os modelos no arquivo `core/admin.py`. Isso é feito usando a função `admin.site.register`. O argumento dessa função deve ser uma lista contendo as classes de modelos criados.

## Criação da API

Até agora não havia necessidade de realização de testes já que os testes de modelos são feitos pelo django. Mas a partir de agora temos que garantir a qualidade do código.

Nessa aplicação será usado o django rest framework para facilitar a criação da API. Inicialmente temos que instalá-lo usando o comando.

 ```
$ pipenv install djangorestframework
```

Para usá-lo temos que adicionar o app `'rest_framework'` a lista `INSTALLED_APPS` do arquivo `settings.py`. Agora temos que criar os serializers, que são classes do django rest framework para que serializam os dados do banco de dados. Ou seja, essas classes são responsáveis em converter o objetos da classe `Model` em objetos `JSON`.

Foram criados 4 serializers, um para cada classe criada no arquivo `models.py`.

Agora, no arquivo `views.py`, vamos criar as views da API. Para isso vamos usar a classe ModelViewSet, disponível no pacote django rest framework.
