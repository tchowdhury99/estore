# Generated by Django 2.1.5 on 2019-01-26 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('order_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 27, 1, 42, 37, 95617))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]