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