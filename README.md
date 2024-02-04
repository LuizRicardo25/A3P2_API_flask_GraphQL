# Introdução à API GraphQL com Flask e Graphene

Bem-vindo ao nosso projeto de introdução à criação de APIs GraphQL usando Python, Flask e Graphene. Este guia passo a passo o ajudará a configurar seu ambiente de desenvolvimento, definir um esquema GraphQL e expor sua API através do Flask.

## Configuração do Ambiente

Antes de começarmos, é essencial preparar seu ambiente de desenvolvimento.

### Passos Iniciais:

1. **Criar Ambiente Virtual**

   Execute o comando abaixo no terminal para criar um ambiente virtual:

   ```bash
   python -m venv venv
   ```
## Ativar Ambiente Virtual

Ative o ambiente virtual usando:

- **No Windows:**

  ```cmd

  .\venv\Scripts\activate
  
  ```
  No Linux/Mac:

  
```bash

source venv/bin/activate
```
### Instalar Dependências
Com o ambiente virtual ativado, instale as dependências necessárias:

```bash
pip install Flask graphene flask-graphql
```

### Desenvolvimento da API GraphQL
Após configurar o ambiente e instalar as dependências, é hora de começar a desenvolver a API.

### Definindo o Esquema GraphQL
Crie o Arquivo schema.py

Defina seus tipos GraphQL, por exemplo, um tipo User e uma Query para buscar usuários.

python

```bash
import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())
    def resolve_user(self, info, id):
        return User(id=1, name="Usuário Exemplo")
   ```

### Configure a Aplicação Flask

Em app.py, configure o Flask para usar a API GraphQL.

python

```bash
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.add_url_rule(
    '/graphql', 
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)    
    ```
 
 ```
### Executando a Aplicação
Para executar a aplicação, use:

```bash
python app.py
``` 
### Testando a API
Acesse http://localhost:5000/graphql no navegador para usar o GraphiQL, uma interface gráfica para testar sua API GraphQL.

## Conclusão
Parabéns! Você agora tem uma API GraphQL básica rodando com Flask e Graphene. Experimente criar novos tipos e queries para expandir sua API.
