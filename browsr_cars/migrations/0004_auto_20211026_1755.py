# Generated by Django 2.2.12 on 2021-10-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browsr_cars', '0003_cars_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='images_2',
            field=models.ImageField(default=1, upload_to='cars_imges'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='images_3',
            field=models.ImageField(default=1, upload_to='cars_imges'),
            preserve_default=False,
        ),
    ]
