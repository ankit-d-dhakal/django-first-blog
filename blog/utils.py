import uuid

from django.utils.text import slugify


def generate_new_slug(model, title):
    original = slugify(title)
    unique = original
    num = 1
    while model.objects.filter(slug=unique).exists():
        unique = "%s-%d" % (original, num)
        num += 1
    return unique