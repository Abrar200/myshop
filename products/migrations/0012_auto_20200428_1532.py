# Generated by Django 3.0.3 on 2020-04-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_variation_variation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_type',
            field=models.CharField(blank=True, choices=[('size', 'size'), ('color', 'color')], max_length=120, null=True),
        ),
    ]