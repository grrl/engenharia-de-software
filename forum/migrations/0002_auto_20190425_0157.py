# Generated by Django 2.2 on 2019-04-25 01:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='last_modification_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='last_modification_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='Title', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(),
        ),
    ]
