# Generated by Django 3.0.3 on 2020-04-26 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
