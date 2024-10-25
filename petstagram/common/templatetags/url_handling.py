from django import template

register = template.Library()

@register.simple_tag
def url_handling(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()