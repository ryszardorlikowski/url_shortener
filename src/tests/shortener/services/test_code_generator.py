from django.test import override_settings

from shortener.services.code_generator import RandomCodeGenerator


@override_settings(SHORT_URL_CODE_LENGTH=12)
def test_random_code_generator():
    """
    Test checking the generation of a unique character string
    """
    code = RandomCodeGenerator.generate()
    code2 = RandomCodeGenerator.generate()
    assert code != code2
    assert len(code) == 12
