from django.db import models

from base62_uuid.utils import uuid_to_base62


class Base62UUIDMixin(models.Model):
    id = models.CharField(max_length=32, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pk = uuid_to_base62()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
