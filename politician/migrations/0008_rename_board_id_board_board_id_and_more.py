# Generated by Django 4.2.7 on 2023-11-06 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politician', '0007_alter_community_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='Board_id',
            new_name='board_id',
        ),
        migrations.AlterField(
            model_name='community',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 17, 0, 53, 707140, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
