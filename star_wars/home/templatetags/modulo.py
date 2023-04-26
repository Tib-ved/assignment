from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    """
    Generates number for 'num' in the range of 'val'
    Use-case: To show 'val' set of images randomly

    Example:
    {% for id in ids %}
        <img src="{% static 'images/planets/planet'%}{{ id|modulo:4 }}.jpg">
    {% endfor %}

    Generates following code:
        <img src="images/planets/planet1.jpg">
        <img src="images/planets/planet2.jpg">
        <img src="images/planets/planet3.jpg">
        <img src="images/planets/planet0.jpg">
    """
    return num % val
