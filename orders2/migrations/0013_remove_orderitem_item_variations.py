# Generated by Django 3.0.3 on 2020-05-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders2', '0012_orderitem_item_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item_variations',
        ),
    ]
