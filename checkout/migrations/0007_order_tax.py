# Generated by Django 3.2.23 on 2024-01-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20231220_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
