# Generated by Django 3.2 on 2022-07-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='', verbose_name='post thumbnail'),
            preserve_default=False,
        ),
    ]