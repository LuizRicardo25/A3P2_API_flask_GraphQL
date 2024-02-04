# Importa a biblioteca Graphene para criar esquemas GraphQL
import graphene

# Define a classe User como um tipo de objeto GraphQL com dois campos: id e nome
class User(graphene.ObjectType):
    id = graphene.ID()  # Define um campo ID, usualmente usado para identificadores únicos
    name = graphene.String()  # Define um campo String para o nome do usuário

# Define a classe Query que permite realizar consultas GraphQL
class Query(graphene.ObjectType):
    # Cria um campo 'user' na consulta que retorna um objeto User, aceitando um argumento 'id' do tipo Int
    user = graphene.Field(User, id=graphene.Int())

    # Define como os dados para a consulta 'user' são resolvidos, dado um 'id'
    def resolve_user(self, info, id):
        # Em uma aplicação real, aqui você buscaria os dados do usuário no banco de dados
        # Por enquanto, retorna um usuário de exemplo com o id e nome fornecidos
        return User(id=id, name="Usuário Exemplo")

# Cria um esquema GraphQL com a classe Query definida como a raiz da consulta
schema = graphene.Schema(query=Query)

