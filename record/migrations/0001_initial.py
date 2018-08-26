# Generated by Django 2.0.2 on 2018-08-26 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0005_auto_20180826_0128'),
        ('system_auth', '0003_auto_20180826_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(max_length=30)),
                ('ref_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.Book')),
                ('ref_workspace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='system_auth.Workspace')),
            ],
        ),
    ]
