# Generated by Django 4.1.3 on 2022-11-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_residencias_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residencias',
            name='id',
        ),
        migrations.AlterField(
            model_name='residencias',
            name='numero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
