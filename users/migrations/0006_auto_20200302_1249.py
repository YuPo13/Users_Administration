# Generated by Django 3.0.3 on 2020-03-02 10:49

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200302_1235'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('user_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
