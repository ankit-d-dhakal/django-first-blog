from msilib.schema import Class
from tabnanny import verbose

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='post title')
    thumbnail = models.ImageField('post thumbnail')
    summary = models.CharField(max_length=400, null=False, blank=False, verbose_name='post summary')
    content = models.TextField(verbose_name='post content', null=False, blank=False)
    views = models.IntegerField('post views', default=0)
    is_published = models.BooleanField('post is published', default=False)
    date_posted = models.DateField(verbose_name='created at', auto_now_add=True)



    def __str__(self):
        return f'{self.title} - {self.date_posted}'

