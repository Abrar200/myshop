# Generated by Django 3.0.3 on 2020-05-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200429_1610'),
        ('orders2', '0007_order_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='variation',
            field=models.ManyToManyField(to='products.Variation'),
        ),
    ]
