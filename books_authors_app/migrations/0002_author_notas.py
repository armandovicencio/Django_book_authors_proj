# Generated by Django 4.0.2 on 2022-02-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notas',
            field=models.TextField(default='notas'),
        ),
    ]
