# Generated by Django 3.1 on 2020-10-20 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_commnet_restaurant'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commnet',
            new_name='Comment',
        ),
    ]
