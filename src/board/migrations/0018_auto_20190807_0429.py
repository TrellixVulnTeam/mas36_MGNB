# Generated by Django 2.2.3 on 2019-08-07 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_auto_20190805_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='active',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='active',
        ),
    ]
