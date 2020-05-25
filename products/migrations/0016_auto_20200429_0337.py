# Generated by Django 3.0.3 on 2020-04-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_delete_variationmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_type',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], default='Size', max_length=120),
        ),
    ]
