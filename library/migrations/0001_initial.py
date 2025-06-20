# Generated by Django 6.0.dev20250115212837 on 2025-06-12 06:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, default='logos/logo_default.png', null=True, upload_to='logos/')),
                ('preview', models.ImageField(blank=True, default='previews/preview_default.png', null=True, upload_to='previews/')),
                ('thumbnail', models.ImageField(blank=True, default='thumbnails/thumbnail_default.png', null=True, upload_to='thumbnails/')),
                ('descript', models.TextField(blank=True, null=True)),
                ('needs_login', models.BooleanField(default=False)),
                ('authors', models.ManyToManyField(to='library.author')),
                ('favorited_by', models.ManyToManyField(blank=True, related_name='favorite_games', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(to='library.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='library.game')),
            ],
        ),
    ]
