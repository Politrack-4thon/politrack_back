# Generated by Django 4.2.7 on 2023-11-06 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politician', '0006_alter_board_community_alter_community_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 16, 53, 5, 471778, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]