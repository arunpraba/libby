import graphene
import catelog.schema
import users.gql.schema
import reviews.gql.schema


class Query(catelog.schema.Query, users.gql.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    catelog.schema.Mutation,
    users.gql.schema.Mutation,
    reviews.gql.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
