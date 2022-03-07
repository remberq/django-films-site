from django import template

from main.models import Category, Films

register = template.Library()


@register.simple_tag()
def get_categories():
    """
    Send all categories to html template
    register this tag on header.html to avoid double code
    """
    return Category.objects.all()


@register.inclusion_tag('main/tags/last_films.html')
def get_last_films(count=5):
    """
    Same as get_categories function
    Add to sidebar.html this tag and render template --> last_films.html on sidebar template
    """
    films = Films.objects.order_by('-pk')[:count]
    return {'last_films': films}
