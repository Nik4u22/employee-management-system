# Generated by Django 4.1 on 2023-02-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
