# Generated by Django 4.2.7 on 2023-11-06 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politician', '0013_alter_community_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='comment',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='community',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 17, 59, 36, 905524, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
