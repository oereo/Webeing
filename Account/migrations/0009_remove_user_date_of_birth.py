# Generated by Django 3.1 on 2020-10-17 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20201015_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]