# Generated by Django 3.2.23 on 2023-12-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(max_length=20),
        ),
    ]
