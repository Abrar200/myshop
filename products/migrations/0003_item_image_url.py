# Generated by Django 3.0.3 on 2020-04-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]
