import graphene
from graphene_federation import build_schema


class Query(graphene.ObjectType):
    # Insert Queries here
    pass

class Mutation(graphene.ObjectType):
    # Insert Mutation Fields Here
    pass

schema = build_schema(query=Query, mutation=Mutation)