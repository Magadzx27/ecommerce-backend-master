# Generated by Django 3.1.2 on 2020-12-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_method', '0002_auto_20201112_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping_method',
            old_name='shipping_method_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='shipping_method',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shipping_method',
            name='info_message',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='shipping_method',
            name='price',
            field=models.FloatField(default=None, null=True),
        ),
    ]
