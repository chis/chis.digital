from datetime import datetime

def datetime_format(value, format="%d-%m-%y"):
    return value.strftime(format)

