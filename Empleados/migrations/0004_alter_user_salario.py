# Generated by Django 3.2.7 on 2021-09-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0003_auto_20210930_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salario',
            field=models.FloatField(null=True, verbose_name='Salario'),
        ),
    ]
