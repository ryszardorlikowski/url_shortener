from django.db import models, IntegrityError

from .services.code_generator import code_generator


class ShortLink(models.Model):
    code = models.CharField(max_length=10, unique=True)
    url = models.URLField()

    def save(self, *args, **kwargs):
        if not self.code:
            while True:
                try:
                    self.code = code_generator.generate()
                    super().save(*args, **kwargs)
                except IntegrityError:
                    continue
                break
            return

        super().save(*args, **kwargs)
