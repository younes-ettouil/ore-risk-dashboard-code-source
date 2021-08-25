# Generated by Django 3.2.5 on 2021-08-12 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvApp', '0002_auto_20210813_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='npv_Counterparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Counterparty', models.CharField(max_length=150)),
                ('TradeType', models.CharField(max_length=150)),
                ('Maturity', models.CharField(max_length=150)),
                ('MaturityTime', models.CharField(max_length=150)),
                ('NPV', models.CharField(max_length=150)),
                ('NpvCurrency', models.CharField(max_length=150)),
                ('NPV_Base', models.FloatField()),
                ('BaseCurrency', models.CharField(max_length=150)),
                ('CE_Base', models.FloatField()),
            ],
        ),
    ]