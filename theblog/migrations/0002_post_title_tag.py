# Generated by Django 3.2.3 on 2021-05-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='kpop blog', max_length=255),
        ),
    ]
