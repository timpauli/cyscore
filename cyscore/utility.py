def str_format(value: str) -> str:
    return '\"' + value + '\"'


def number_format(value: str) -> str:
    return '{0:f}'.format(round(value, 6)).rstrip('0').rstrip('.')
