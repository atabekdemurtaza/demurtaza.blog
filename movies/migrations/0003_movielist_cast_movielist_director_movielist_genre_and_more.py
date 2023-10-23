# Generated by Django 4.2.5 on 2023-10-18 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movielist_streamplatform_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='cast',
            field=models.ManyToManyField(blank=True, null=True, related_name='acted_in_movies', to=settings.AUTH_USER_MODEL, verbose_name='cast'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directed_movies', to=settings.AUTH_USER_MODEL, verbose_name='director'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='genre',
            field=models.CharField(blank=True, choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama')], max_length=20, null=True, verbose_name='genre'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movie_posters/', verbose_name='poster'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='release date'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='trailer_url',
            field=models.URLField(blank=True, null=True, verbose_name='trailer URL'),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='storyline',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='title',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='name'),
        ),
    ]