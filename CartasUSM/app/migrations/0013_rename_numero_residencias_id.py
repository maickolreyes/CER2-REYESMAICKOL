# Generated by Django 4.1.3 on 2022-11-13 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_residencias_id_alter_residencias_numero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='residencias',
            old_name='numero',
            new_name='id',
        ),
    ]
