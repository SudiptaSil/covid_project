# Generated by Django 3.2.9 on 2021-11-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_age_ethnicity_id_income_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='covid_deaths',
            fields=[
                ('id', models.BigIntegerField(default=0, primary_key='true', serialize=False)),
                ('report_date', models.CharField(default=0, max_length=100)),
                ('county', models.CharField(default=0, max_length=100)),
                ('total_deaths', models.IntegerField(default=0)),
                ('population', models.IntegerField(default=0)),
                ('deaths_percent', models.FloatField(default=0)),
                ('deaths_per100', models.FloatField(default=0)),
            ],
        ),
    ]