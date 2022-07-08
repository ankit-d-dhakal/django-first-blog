from msilib.schema import Class
from secrets import choice
from tabnanny import verbose

from django.db import models

CAT_CHOICES = (
    ('sport', 'Sport News'),
    ('news', 'News'),
    ('pol', 'Politics'),
)

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='post title')
    thumbnail = models.ImageField('post thumbnail', upload_to='posts/', blank=True, null=True)
    summary = models.CharField(max_length=400, null=True, blank=True, verbose_name='post summary')
    content = models.TextField(verbose_name='post content', null=True, blank=True)
    views = models.IntegerField('post views', default=0)
    is_published = models.BooleanField('post is published', default=False)
    category = models.CharField("post category", max_length= 30, choices= CAT_CHOICES)
    date_posted = models.DateField(verbose_name='created at', auto_now_add=True)



    def __str__(self):
        return f'{self.title} - {self.date_posted}'

