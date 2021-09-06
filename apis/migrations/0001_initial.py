# Generated by Django 3.2 on 2021-09-06 02:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BidData',
            fields=[
                ('user_pk', models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.id'))),
                ('timestamp', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('number_of_tokens', models.IntegerField(default=0)),
                ('bid_status', models.CharField(max_length=15)),
                ('share_code', models.CharField(max_length=30)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30)),
                ('no_of_shares', models.IntegerField()),
                ('bidding_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('share_quantity', models.IntegerField(default=0)),
                ('share_name', models.CharField(max_length=30)),
                ('share_code', models.CharField(max_length=30)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bid_start_time', models.DateTimeField()),
                ('bid_end_time', models.DateTimeField()),
                ('share_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30)),
            ],
        ),
    ]