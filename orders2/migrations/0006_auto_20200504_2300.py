# Generated by Django 3.0.3 on 2020-05-04 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders2', '0005_auto_20200504_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='variation',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='variation',
        ),
    ]