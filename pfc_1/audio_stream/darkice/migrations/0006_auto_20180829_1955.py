# Generated by Django 2.0.5 on 2018-08-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darkice', '0005_auto_20180826_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='server',
            field=models.CharField(help_text='URL o IP del servidor Icecast, sin http / https', max_length=20),
        ),
    ]
