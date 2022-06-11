from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'