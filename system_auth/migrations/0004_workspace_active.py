# Generated by Django 2.0.2 on 2018-08-26 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_auth', '0003_auto_20180826_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
