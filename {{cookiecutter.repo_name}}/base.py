import graphene
from graphene import relay
from graphene_sqlalchemy_filter import FilterableConnectionField
from werkzeug.exceptions import BadRequest


class CustomField(FilterableConnectionField):
    filter_arg = "where"
    limit = graphene.Int()

    @classmethod
    def get_query(cls, model, info: "ResolveInfo", sort=None, **args):  # noqa: F821
        """Standard get_query with filtering."""

        # If Page comes in as 0, to get around the boolean of Page #0
        # being treated as false
        page = int(args.get("page")) + 1 if args.get("page") is not None else None
        limit = args.get("limit")

        # Conditionals are up here to avoid generating a bad requested query
        if limit or page:
            if (
                args.get("first")
                or args.get("last")
                or args.get("before")
                or args.get("after")
            ):
                raise BadRequest(
                    "Can not use page or limit with after, before, first, or last arguments."  # noqa: E501
                )

            if limit is None:
                raise BadRequest(
                    "You must also provide limit, if you provide a page argument. "
                )

            if page and page <= 0:
                raise BadRequest("The page number must be an integer above 0.")

            if limit and limit <= 0:
                raise BadRequest("The limit must be an integer above 0.")

        query = super().get_query(model, info, sort, **args)

        request_filters = args.get(cls.filter_arg)
        if request_filters:
            filter_set = cls.get_filter_set(info)
            query = filter_set.filter(info, query, request_filters)

        # Hacky solution to work around Page/Limit
        info.variable_values["total_count"] = query.count()

        if limit:
            if page:
                # To get page back to correct number, if its done in
                # the query, PEMDAS will cause issues
                page = page - 1
                query = query.offset(int(page) * int(limit))
            query = query.limit(limit)
        return query


class CustomNode(relay.Node):
    class Meta:
        name = "CustomNode"

    # These two methods were to override the Base 64 encoding that comes with
    @classmethod
    def from_global_id(cls, global_id):
        return global_id

    @staticmethod
    def to_global_id(type, id):
        return id
