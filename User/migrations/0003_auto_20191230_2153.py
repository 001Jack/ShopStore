# Generated by Django 2.2.1 on 2019-12-30 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_payorder_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorder',
            name='pay_price',
            field=models.FloatField(default=0),
        ),
    ]
