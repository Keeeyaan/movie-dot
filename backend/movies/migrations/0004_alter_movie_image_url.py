# Generated by Django 5.0.6 on 2024-06-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_alter_movie_genre_alter_movie_image_url_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]