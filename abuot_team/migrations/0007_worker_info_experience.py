# Generated by Django 3.0.1 on 2022-03-21 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abuot_team', '0006_auto_20220321_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker_info',
            name='Experience',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
