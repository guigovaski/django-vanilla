# Generated by Django 3.2.5 on 2021-09-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210808_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Preço'),
        ),
    ]
