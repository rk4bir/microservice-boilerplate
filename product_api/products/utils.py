import string
from django.utils.text import slugify
import random


def generate_random_string(size=1):
    numbers = string.digits
    return "".join(random.choice(numbers) for _ in range(size))


def get_unique_slug(instance, slug=None):
    # get model class of the given instance
    klass = instance.__class__
    # set slug if not have any
    if slug is None:
        slug = slugify(instance.title)
        slug = slug.lower()
    # check if slug exists, if exists generate new
    # one recursively
    if klass.objects.filter(slug=slug).exists():
        slug += '-' + generate_random_string(size=1)
        return get_unique_slug(instance, slug=slug)
    return slug
