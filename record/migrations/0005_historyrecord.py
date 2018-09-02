# Generated by Django 2.0.2 on 2018-09-01 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_auth', '0006_auto_20180901_2313'),
        ('book', '0006_auto_20180827_0023'),
        ('record', '0004_auto_20180901_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('workspace', models.CharField(max_length=120)),
                ('ref_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.Book')),
                ('ref_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='system_auth.Profile')),
            ],
        ),
    ]