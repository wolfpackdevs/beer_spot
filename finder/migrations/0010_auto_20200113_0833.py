# Generated by Django 3.0.1 on 2020-01-13 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewer', '0005_auto_20200108_1334'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finder', '0009_auto_20200109_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='beer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beer_liked', to='brewer.Beer'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
