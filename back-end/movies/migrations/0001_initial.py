# Generated by Django 3.2.13 on 2022-11-16 01:47

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('adult', models.BooleanField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.TextField()),
                ('video', models.BooleanField()),
                ('release_date', models.DateField()),
                ('vote_average', models.IntegerField()),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('overview', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('content', models.TextField()),
                ('rank', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
