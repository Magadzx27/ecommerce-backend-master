# Generated by Django 3.1.2 on 2020-11-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imageslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=1000, null=True)),
                ('title', models.TextField(blank=True, max_length=100, null=True)),
                ('subtitle', models.TextField(blank=True, max_length=100, null=True)),
                ('display_order', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
