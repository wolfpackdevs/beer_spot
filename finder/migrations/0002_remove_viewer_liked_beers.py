# Generated by Django 3.0.1 on 2020-01-08 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewer',
            name='liked_beers',
        ),
    ]
