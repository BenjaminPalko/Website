# Generated by Django 2.2.5 on 2019-10-07 00:20

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191006_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_body',
            field=martor.models.MartorField(),
        ),
    ]
