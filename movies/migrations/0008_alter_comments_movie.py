# Generated by Django 4.2.5 on 2023-10-24 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='movies.movie'),
        ),
    ]
