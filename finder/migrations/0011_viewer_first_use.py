# Generated by Django 3.0.1 on 2020-01-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0010_auto_20200113_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewer',
            name='first_use',
            field=models.BooleanField(default=True),
        ),
    ]
