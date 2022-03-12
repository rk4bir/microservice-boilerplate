import re


def validate_email(email):
    """Checks pattern check at least: usr@pm.me"""
    pattern = r'^[a-z\.0-9]{3,}@[a-z]{2,}\.[a-z\.]{2,}$'
    if not re.compile(pattern).match(email):
        return False
    return True


def has_numeric_character(password):
    pattern = r'\d'
    return bool(re.search(pattern, password))


def has_letter_character(password):
    pattern = r'[a-zA-Z]'
    return bool(re.search(pattern, password))
