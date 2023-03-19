import string

from django.conf import settings
from django.utils.crypto import get_random_string


class RandomCodeGenerator:
    BASE_STR = string.ascii_letters + string.digits

    def generate(self, length=settings.SHORT_URL_CODE_LENGTH) -> str:
        return get_random_string(length=length, allowed_chars=self.BASE_STR)


code_generator = RandomCodeGenerator()
