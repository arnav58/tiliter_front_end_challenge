from django import template

register = template.Library()


def format_name(value):
    """Converts a string into all lowercase and joins spaced out words with underscore"""
    return "_".join(value.lower().split(" "))

register.filter('format_name', format_name)
