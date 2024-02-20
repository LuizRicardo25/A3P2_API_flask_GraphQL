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
pip install Flask graphene Flask-GraphQL
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


## Configuração no GitHub Codespace

Para iniciar o serviço no GitHub Codespace, siga os passos abaixo:

1. Crie um novo Codespace a partir do repositório do projeto.
2. Uma vez dentro do Codespace, abra o terminal integrado.
3. Ative o ambiente virtual (se aplicável):

   ```bash
   source .venv/bin/activate
   ```

Defina a variável de ambiente FLASK_APP:

```bash
export FLASK_APP=app.py
```

Inicie o servidor Flask:

```bash
flask run --host=0.0.0.0
```
Isso iniciará o servidor Flask e o tornará acessível através do encaminhamento de porta do Codespace.

Testando a API GraphQL
Para testar a API GraphQL, você pode utilizar o seguinte exemplo de consulta GraphQL:

```bash
query {
  user(id: 1) {
    id
    name
  }
}
```
## Para executar esta consulta:

Acesse o GraphiQL navegando para http://localhost:5000/graphql no seu navegador (substitua localhost pelo URL do Codespace, se necessário).
Insira a consulta no painel esquerdo do GraphiQL.
Pressione o botão "Play" ou "Execute Query" para rodar a consulta.
O resultado será exibido no painel direito do GraphiQL.
Documentação da API
Para mais informações sobre os tipos e consultas disponíveis na API, consulte a documentação gerada pelo GraphiQL acessando a URL da API no seu navegador e clicando em "Docs" no canto superior direito da interface do GraphiQL.
