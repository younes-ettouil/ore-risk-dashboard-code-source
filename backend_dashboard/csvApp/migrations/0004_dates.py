# Generated by Django 3.2.6 on 2021-08-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvApp', '0003_npv_counterparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]
