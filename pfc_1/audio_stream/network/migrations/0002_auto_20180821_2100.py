# Generated by Django 2.0.5 on 2018-08-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wifi',
            name='SSID',
            field=models.CharField(max_length=20),
        ),
    ]
