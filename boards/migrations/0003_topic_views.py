# Generated by Django 5.0.6 on 2024-07-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_rename_last_update_topic_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
