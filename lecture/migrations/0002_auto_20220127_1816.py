# Generated by Django 3.1.14 on 2022-01-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Memo',
        ),
        migrations.AddField(
            model_name='memolecture',
            name='user',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='memolecture',
            name='text',
            field=models.TextField(blank='True'),
        ),
    ]
