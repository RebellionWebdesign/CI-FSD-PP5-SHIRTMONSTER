# Generated by Django 3.2.23 on 2023-12-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelledorders',
            name='cancel_reason',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('Defective', 'Defective'), ('Ordered wrong item', 'Ordered wrong item'), ('Unauthorized Purchase', 'Unauthorized purchase'), ('Just return', 'I just want to return the item')], default='Choose...', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=7),
        ),
    ]
