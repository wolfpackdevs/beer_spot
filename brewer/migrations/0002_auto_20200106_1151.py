# Generated by Django 3.0.1 on 2020-01-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
