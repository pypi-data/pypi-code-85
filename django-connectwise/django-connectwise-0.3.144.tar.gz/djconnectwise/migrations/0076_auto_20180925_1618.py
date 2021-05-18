# Generated by Django 2.0 on 2018-09-25 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0075_auto_20180910_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('all_day_flag', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HolidayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='holiday',
            name='holiday_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djconnectwise.HolidayList'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='holiday_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djconnectwise.HolidayList'),
        ),
    ]
