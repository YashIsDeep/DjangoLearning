# Generated by Django 2.0.5 on 2018-06-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]