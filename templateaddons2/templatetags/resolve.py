from django import template
from django.template import Variable, VariableDoesNotExist

register = template.Library()


@register.assignment_tag()
def resolve(context, path):
    """
    From http://stackoverflow.com/a/13771503/2261861
    {% resolve some_list some_index as value %}
    {% resolve some_dict some_dict_key as value %}
    """
    try:
        return Variable(path).resolve(context)
    except VariableDoesNotExist:
        return None


@register.assignment_tag(takes_context=True)
def call(context, fn_path, *arg, **kwargs):
    """
    {% call context.fn arg1 arg2 as value %}
    """
    if '.' in fn_path:
        fn_ctx, fn_name = fn_path.rsplit('.', 1)
        fn_ctx = Variable(fn_ctx).resolve(context)
        fn = getattr(fn_ctx, fn_name)
        if callable(fn):
            return fn(*arg, **kwargs)


