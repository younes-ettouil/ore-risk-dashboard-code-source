# Generated by Django 3.2.6 on 2021-08-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvApp', '0016_alter_xpv_nettingset_allocatedcva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xpv_nettingset',
            name='COLVA',
            field=models.CharField(max_length=150),
        ),
    ]
