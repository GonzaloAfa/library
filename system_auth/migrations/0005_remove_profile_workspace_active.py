# Generated by Django 2.0.2 on 2018-08-26 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_auth', '0004_workspace_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='workspace_active',
        ),
    ]