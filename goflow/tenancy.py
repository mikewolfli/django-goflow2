from django.conf import settings


def get_tenant_context(request=None, user=None):
    resolver = getattr(settings, 'GOFLOW_TENANT_RESOLVER', None)
    if callable(resolver):
        return resolver(request=request, user=user) or {}
    return {}


def apply_tenant_filter(queryset, request=None, user=None):
    filter_func = getattr(settings, 'GOFLOW_TENANT_FILTER', None)
    if callable(filter_func):
        return filter_func(queryset, request=request, user=user)
    return queryset
