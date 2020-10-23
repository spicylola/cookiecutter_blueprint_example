# Typically Schema such as Mutation, Connection fields will go here
# Adding Example of what Graphql schema would look like

# import graphene
# from graphene import Connection
# from graphene_sqlalchemy import SQLAlchemyObjectType
# from graphene_sqlalchemy_filter import FilterSet
#
# from {{cookiecutter.repo_name}}.models.example import Example as ExampleModel
# from {{cookiecutter.repo_name}}.schemas.base import CustomNode
#
#
# class Example(SQLAlchemyObjectType):
#     class Meta:
#         model = ExampleModel
#         interfaces = (CustomNode,)
#
#
# class ExampleFilterConnection(Connection):
#     total_count = graphene.Int()
#
#     def resolve_total_count(self, info):
#         return info.variable_values["total_count"]
#
#     class Meta:
#         node = Example
#         total_count = graphene.Int()
#
#
# class ExampleFilter(FilterSet):
#     class Meta:
#         model = ExampleModel
#         fields = {
#             "id": ["eq", "ne", "like", "in"],
#             "description": ["eq", "ne", "like", "in"]
#         }
