# Generated by Django 3.1.2 on 2021-01-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0086_auto_20201222_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='displaycolor',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issuetype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='licensetype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notetype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='priority',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicecallstatus',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subissuetype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasktypelink',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usetype',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
