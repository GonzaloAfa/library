# Generated by Django 2.0.2 on 2018-08-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20180826_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
