from django import template

register = template.Library()


# 创建过滤器
@register.filter
def id_filter(obj):
    if obj <= 3:
        return str(obj).zfill(4)
    else:
        return str(obj).zfill(5)

@register.filter()
def cut_obj(obj):
    return obj[:4]
