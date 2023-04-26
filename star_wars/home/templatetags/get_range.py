from django import template

register = template.Library()

@register.filter
def get_range(value):
    """
    Returns a list containing range made from given 'value' - starting with 1, till (value - 1)
    Example:
        <ul>
            {% for i in 2|get_range %}
                <li>{{ i }} - Some list item</li>
            {% endfor %}
        </ul>

    Generates following code:
        <ul>
            <li>1 - Some list item</li>
            <li>2 - Some list item</li>
        </ul>
    """
    return range(1, value)
