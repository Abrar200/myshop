# Generated by Django 3.0.3 on 2020-05-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200429_1610'),
        ('orders2', '0002_order_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='variation',
            field=models.ManyToManyField(blank=True, null=True, to='products.Variation'),
        ),
    ]
