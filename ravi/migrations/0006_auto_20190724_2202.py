# Generated by Django 2.2.3 on 2019-07-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravi', '0005_auto_20190724_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
