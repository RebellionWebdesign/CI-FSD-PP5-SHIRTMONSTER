# Generated by Django 3.2.23 on 2023-12-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customshirt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customshirt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='custom_shirts'),
        ),
    ]
