# Generated by Django 3.2.5 on 2021-08-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='servico',
            field=models.CharField(max_length=50, verbose_name='Serviço'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='opiniao',
            field=models.TextField(max_length=350, verbose_name='Opinião'),
        ),
    ]
