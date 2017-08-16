# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=155)),
                ('slug', models.SlugField(unique=True)),
                ('imagen', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('contenido', models.TextField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('actualizado', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp', '-actualizado'],
            },
        ),
    ]
