# Generated by Django 5.0.6 on 2024-06-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.URLField(),
        ),
    ]