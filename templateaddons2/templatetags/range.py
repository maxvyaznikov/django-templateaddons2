from django import template

register = template.Library()

@register.assignment_tag(name='range')
def range_tag(start=None, stop=None, step=1):
    """
    {% range [start,] stop[, step] as context_name %}
    """
    if start is not None and stop is None:
        # {% range 5 as r %} => range(start=0, stop=5, step=1)
        stop = start
        start = 0
    if stop is not None:
        return range(start if start is not None else 0, stop, step)
    else:
        return ''

@register.filter()
def times(value):
    return range(int(value))
