from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import get_unique_slug


class Product(models.Model):
    slug = models.SlugField(blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField()
    price = models.FloatField(default=0.00)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title", "-created_at"]


def product_pre_save_action(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance, slug=slugify(instance.title))


pre_save.connect(product_pre_save_action, sender=Product, weak=False)
