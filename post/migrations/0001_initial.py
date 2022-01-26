# Generated by Django 3.1.14 on 2022-01-25 12:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default=None, max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('register_date', models.DateTimeField()),
                ('solved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default=None, max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('register_date', models.DateTimeField()),
                ('choice', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]