# Generated by Django 3.0.3 on 2020-03-05 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200302_1249'),
    ]

    operations = [
        migrations.RunSQL(
            "UPDATE auth_group SET name='Mgr' WHERE name='Manager';"
        )
    ]
