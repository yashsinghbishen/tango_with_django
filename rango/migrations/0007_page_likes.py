# Generated by Django 2.1.5 on 2019-01-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
