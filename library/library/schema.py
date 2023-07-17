import graphene
import catelog.schema
import users.gql.schema


class Query(catelog.schema.Query, users.gql.schema.Query, graphene.ObjectType):
    pass


class Mutation(catelog.schema.Muation, users.gql.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
