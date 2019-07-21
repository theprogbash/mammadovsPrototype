from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = latin_slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    content = HTMLField()
    # image_url = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='static/img')
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
    str = str.replace(",", "-")
    str = str.replace("ə", "e")
    str = str.replace("ö", "o")
    str = str.replace("ç", "ch")
    str = str.replace("ş", "sh")
    str = str.replace("ı", "i")
    str = str.replace("ü", "u")
    str = str.replace("ğ", "gh")
    return str.lower()




