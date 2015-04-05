from django import template

register = template.Library()

@register.assignment_tag(name='range')
def range_tag(start=None, stop=None, step=None):
    """
    {% range [start,] stop[, step] as context_name %}
    """
    if start is not None and stop is None:
        # {% range 5 as r %} => range(start=0, stop=5, step=1)
        stop = start
        start = 0
    return range(start if start is not None else 0, stop, step if step is not None else 1)


@register.filter()
def times(value):
    return range(value)
