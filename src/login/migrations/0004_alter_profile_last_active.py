# Generated by Django 3.2.8 on 2021-11-10 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_profile_last_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_active',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 4, 17, 37, 559940)),
        ),
    ]