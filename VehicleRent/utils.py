import os
import random
import string
from django.core.files.storage import default_storage
from django.db.models import ImageField

ALPHANUMERICAL_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERICAL_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))
