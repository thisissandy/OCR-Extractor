# Generated by Django 3.2.4 on 2021-07-17 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0003_auto_20210709_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload_time',
            field=models.TimeField(default=datetime.time(19, 59, 16, 744628)),
        ),
    ]