# Generated by Django 3.1.2 on 2020-12-05 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_auth_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
