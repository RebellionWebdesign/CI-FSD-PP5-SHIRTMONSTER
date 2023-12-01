# Generated by Django 3.2.23 on 2023-12-01 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_line_1', models.CharField(max_length=35)),
                ('adress_line_2', models.CharField(max_length=35)),
                ('city', models.CharField(max_length=35)),
                ('zip_code', models.CharField(max_length=35)),
                ('country', models.CharField(max_length=35)),
                ('telephone', models.CharField(max_length=35)),
                ('mobile_phone', models.CharField(max_length=35)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]