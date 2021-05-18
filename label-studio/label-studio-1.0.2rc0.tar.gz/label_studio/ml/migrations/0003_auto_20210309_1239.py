# Generated by Django 3.1.4 on 2021-03-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_auto_20210308_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlbackend',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Description for the machine learning backend', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='mlbackend',
            name='model_version',
            field=models.TextField(blank=True, default='', help_text='Current model version associated with this machine learning backend', null=True, verbose_name='model version'),
        ),
        migrations.AlterField(
            model_name='mlbackend',
            name='title',
            field=models.TextField(blank=True, default='default', help_text='Name of the machine learning backend', null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='mlbackend',
            name='url',
            field=models.TextField(help_text='URL for the machine learning model server', verbose_name='url'),
        ),
    ]
