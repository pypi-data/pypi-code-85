# Generated by Django 2.1 on 2019-07-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0101_agreement_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='agreement_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='cancelled_flag',
            field=models.BooleanField(default=False),
        ),
    ]
