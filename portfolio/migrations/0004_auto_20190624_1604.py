# Generated by Django 2.2.2 on 2019-06-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20190624_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/img'),
        ),
    ]
