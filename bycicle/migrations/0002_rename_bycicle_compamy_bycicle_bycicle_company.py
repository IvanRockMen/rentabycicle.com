# Generated by Django 3.2.8 on 2021-10-27 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bycicle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bycicle',
            old_name='bycicle_compamy',
            new_name='bycicle_company',
        ),
    ]