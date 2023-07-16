import graphene
import catelog.schema


class Query(catelog.schema.Query, graphene.ObjectType):
    pass


class Mutation(catelog.schema.Muation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
