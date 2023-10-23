# Generated by Django 4.2.5 on 2023-10-23 12:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_movielist_cast'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streamplatform',
            options={'verbose_name': 'Stream Platform', 'verbose_name_plural': 'Stream Platforms'},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxLengthValidator(5)], verbose_name='rating')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movielist')),
            ],
        ),
    ]