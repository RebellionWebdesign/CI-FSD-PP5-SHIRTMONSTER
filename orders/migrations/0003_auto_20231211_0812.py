# Generated by Django 3.2.23 on 2023-12-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20231208_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cancelledorders',
            options={'ordering': ('-requested_on',)},
        ),
        migrations.AlterField(
            model_name='cancelledorders',
            name='order_number',
            field=models.OneToOneField(max_length=32, on_delete=django.db.models.deletion.PROTECT, related_name='order_id', to='orders.order'),
        ),
    ]
