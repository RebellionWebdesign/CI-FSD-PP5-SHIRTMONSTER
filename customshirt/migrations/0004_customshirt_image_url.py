# Generated by Django 3.2.23 on 2023-12-18 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customshirt', '0003_auto_20231218_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='customshirt',
            name='image_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]