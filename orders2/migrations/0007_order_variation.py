# Generated by Django 3.0.3 on 2020-05-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200429_1610'),
        ('orders2', '0006_auto_20200504_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='variation',
            field=models.ManyToManyField(to='products.Variation'),
        ),
    ]
