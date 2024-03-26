# Generated by Django 3.1.2 on 2020-12-13 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='cart_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='carts',
            old_name='product_qty',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='carts',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
