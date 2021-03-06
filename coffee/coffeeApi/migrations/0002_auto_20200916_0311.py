# Generated by Django 3.0.5 on 2020-09-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('LARGE', 'Large'), ('ESPRESSO', 'Espresso')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('MACHINE', 'Machine'), ('POD', 'Pod')], max_length=10),
        ),
    ]
