# Generated by Django 2.2.3 on 2019-07-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_slide_advertising_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide_advertising',
            name='Slide_img_upload',
            field=models.ImageField(default=True, upload_to='images'),
        ),
    ]
