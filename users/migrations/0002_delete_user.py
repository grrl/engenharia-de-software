# Generated by Django 2.2 on 2019-04-26 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20190426_0207'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
