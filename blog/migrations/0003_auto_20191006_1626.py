# Generated by Django 2.2.5 on 2019-10-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191006_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_body',
            field=models.TextField(),
        ),
    ]
