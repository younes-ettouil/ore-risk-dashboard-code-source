# Generated by Django 3.2.6 on 2021-08-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvApp', '0012_limits_counterparty_limits_creditrating_limits_nettingset_limits_total_limits_trade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limits_total',
            name='CVA',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='limits_total',
            name='DVA',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='limits_total',
            name='FBA',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='limits_total',
            name='FCA',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='limits_total',
            name='FVA',
            field=models.CharField(max_length=150),
        ),
    ]
