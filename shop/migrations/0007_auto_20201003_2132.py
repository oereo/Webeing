# Generated by Django 3.1 on 2020-10-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200917_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['name'], 'verbose_name': 'restaurant', 'verbose_name_plural': 'restauranxts'},
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available_display', models.BooleanField(default=True, verbose_name='Display')),
                ('available_order', models.BooleanField(default=True, verbose_name='Order')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Register', to='shop.restaurant')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
