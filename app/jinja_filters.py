from datetime import datetime

"""
In order to pass custom functions through jinja2 templates,
they are defined here and set in __init__.py
"""

def datetime_format(value, format="%B %d %Y"):
    return value.strftime(format)

