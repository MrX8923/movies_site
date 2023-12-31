# Generated by Django 4.2.5 on 2023-10-08 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_poster_alter_movie_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='actor',
            old_name='surname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='agerating',
            old_name='rating',
            new_name='rate',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='surname',
            new_name='lastname',
        ),
    ]
