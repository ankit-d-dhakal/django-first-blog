from audioop import reverse
from msilib.schema import Class
from secrets import choice
from tabnanny import verbose

from django.db import models
from django.urls import reverse

from .utils import generate_new_slug


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='post title')
    slug = models.SlugField(unique=True, null=False, blank=False, editable=False)
    thumbnail = models.ImageField('post thumbnail', upload_to='posts/', blank=True, null=True)
    summary = models.CharField(max_length=400, null=True, blank=True, verbose_name='post summary')
    content = models.TextField(verbose_name='post content', null=True, blank=True)
    views = models.IntegerField('post views', default=0)
    is_published = models.BooleanField('post is published', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_posted = models.DateField(verbose_name='created at', auto_now_add=True)



    def __str__(self):
        return f'{self.title} - {self.date_posted}'
    
    def save(self, *args, **kwargs):
        self.slug = generate_new_slug(Post, self.title)
        return super().save(*args, *kwargs)
    
    def get_absolute_url(self):
        return reverse('single_blog_page', args=[self.slug])

