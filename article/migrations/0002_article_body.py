# Generated by Django 3.0.7 on 2020-06-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default='I am the body'),
        ),
    ]