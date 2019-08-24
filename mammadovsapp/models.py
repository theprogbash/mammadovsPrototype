from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = HTMLField()
    image = models.CharField(max_length=2000)
    # image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.title)
        super(Article, self).save(*args, **kwargs)


def latin_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace("?", "-")
    str = str.replace(",", "-")
    str = str.replace("ə", "e")
    str = str.replace("ö", "o")
    str = str.replace("ç", "ch")
    str = str.replace("ş", "sh")
    str = str.replace("ı", "i")
    str = str.replace("ü", "u")
    str = str.replace("ğ", "gh")
    str = str.replace("İ", "i")
    str = str.replace("Ə", "e")
    str = str.replace("Ö", "o")
    str = str.replace("Ü", "u")
    return str.lower()




