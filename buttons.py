from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum

class Characters(Enum):
    btn_lower = ascii_lowercase
    btn_upper = ascii_uppercase
    btn_digits = digits
    btn_simbols = punctuation