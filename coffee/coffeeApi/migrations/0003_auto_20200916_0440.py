# Generated by Django 3.0.5 on 2020-09-16 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeApi', '0002_auto_20200916_0311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='water_line_compaitable',
            new_name='water_line_compatible',
        ),
    ]
