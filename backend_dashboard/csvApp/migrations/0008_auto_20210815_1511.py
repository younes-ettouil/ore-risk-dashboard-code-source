# Generated by Django 3.2.6 on 2021-08-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvApp', '0007_alter_dates_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npv_counterparty',
            name='id_date',
        ),
        migrations.RemoveField(
            model_name='npv_creditrating',
            name='id_date',
        ),
        migrations.RemoveField(
            model_name='npv_nettingset',
            name='id_date',
        ),
        migrations.RemoveField(
            model_name='npv_total',
            name='id_date',
        ),
        migrations.RemoveField(
            model_name='npv_trade',
            name='id_date',
        ),
        migrations.AddField(
            model_name='npv_counterparty',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='npv_creditrating',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='npv_nettingset',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='npv_total',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='npv_trade',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
