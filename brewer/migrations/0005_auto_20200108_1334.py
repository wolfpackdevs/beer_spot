# Generated by Django 3.0.1 on 2020-01-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewer', '0004_auto_20200108_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='beer',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
