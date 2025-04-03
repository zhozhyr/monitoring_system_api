from drf_spectacular.utils import extend_schema_view, extend_schema


def schema_view(tag):
    def decorator(view):
        if hasattr(view, 'get') or hasattr(view, 'post'):
            return extend_schema(tags=[tag])(view)
        else:
            return extend_schema_view(
                list=extend_schema(tags=[tag]),
                create=extend_schema(tags=[tag]),
                retrieve=extend_schema(tags=[tag]),
                update=extend_schema(tags=[tag]),
                partial_update=extend_schema(tags=[tag]),
                destroy=extend_schema(tags=[tag]),
            )(view)

    return decorator
