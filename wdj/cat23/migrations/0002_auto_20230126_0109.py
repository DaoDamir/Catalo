# Generated by Django 3.1.1 on 2023-01-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat23', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора книги', to='cat23.Author', verbose_name='Автор книги'),
        ),
    ]