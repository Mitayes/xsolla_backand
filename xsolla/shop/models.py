import uuid
from django.db import models


class Product(models.Model):
    article = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=255, blank=False)
    price = models.IntegerField(default=0, blank=False)
    count = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.name, self.type
