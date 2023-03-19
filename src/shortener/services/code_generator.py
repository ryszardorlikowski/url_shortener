import string

from django.conf import settings
from django.utils.crypto import get_random_string


class RandomCodeGenerator:
    BASE_STR = string.ascii_letters + string.digits

    @classmethod
    def generate(cls, length=None) -> str:
        if length is None:
            length = settings.SHORT_URL_CODE_LENGTH
        return get_random_string(length=length, allowed_chars=cls.BASE_STR)


code_generator = RandomCodeGenerator
