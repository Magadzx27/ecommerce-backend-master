# Generated by Django 3.1.4 on 2020-12-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_item', '0002_auto_20201203_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_item',
            name='comment',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
