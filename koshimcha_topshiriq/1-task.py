from django.db import models
from django.conf import settings


class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    everything = models.Manager()
    objects = NonDeleted()

    def soft_deleted(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


# Create your models here.
class Color(SoftDelete):
    name = models.CharField(max_length=16)
    hex_code = models.CharField(max_length=16)

    def __str__(self):
        return self.name
