# Generated by Django 3.0.3 on 2020-05-05 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_itemvariation_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvariation',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Item'),
        ),
    ]
