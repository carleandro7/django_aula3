# Generated by Django 5.1 on 2024-10-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='data_compra',
            field=models.CharField(max_length=100),
        ),
    ]
