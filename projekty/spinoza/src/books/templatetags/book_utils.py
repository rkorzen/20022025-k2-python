from django import template
import markdown
from django.utils.html import mark_safe

register = template.Library()

@register.filter(name="markdown_filter")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.filter(name="remove_newlines")
def remove_newlines(text):
    """
    Zamienia wszystkie wystąpienia old na new w tekście.
    Przykład:
    {{ "Ala\nma\nkota" | remove_newlines }}
    Wynik:
    Alamakota
    """
    return text.replace("\\n","")

@register.filter(name="first_words")
def first_words(text, num):
    return " ".join(text.split()[:num]) + "..."

@register.simple_tag
def markdown_tag(text):
    return mark_safe(markdown.markdown(text.replace("\\n","")))