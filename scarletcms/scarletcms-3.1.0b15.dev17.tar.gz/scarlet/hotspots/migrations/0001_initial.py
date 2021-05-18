# Generated by Django 1.11 on 2017-07-28 18:10
import django.db.models.deletion
from django.db import migrations, models

import scarlet.assets.fields
import scarlet.assets.utils
import scarlet.cms.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_cord', models.IntegerField()),
                ('y_cord', models.IntegerField()),
                ('overlay_size_x', models.IntegerField()),
                ('overlay_size_y', models.IntegerField()),
                ('order', scarlet.cms.fields.OrderField(db_index=True, default=0, verbose_name=b'Pin number')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name=b'Pin title')),
                ('text', scarlet.cms.fields.HTMLTextField(blank=True)),
                ('video_json', models.TextField(blank=True)),
                ('image_cache', scarlet.assets.fields.AssetRealFileField(blank=True, editable=False, max_length=255, upload_to=scarlet.assets.utils.assets_dir)),
                ('icon_cache', scarlet.assets.fields.AssetRealFileField(blank=True, editable=False, max_length=255, upload_to=scarlet.assets.utils.assets_dir)),
                ('icon', scarlet.assets.fields.AssetsFileField(blank=True, denormalize=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='assets.Asset', verbose_name=b'Icon')),
                ('image', scarlet.assets.fields.AssetsFileField(blank=True, denormalize=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='assets.Asset')),
            ],
            options={
                'verbose_name': 'Hotspot',
                'verbose_name_plural': 'Hotspots',
            },
        ),
        migrations.CreateModel(
            name='HotSpotModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('intro_copy', models.TextField(blank=True)),
                ('image_cache', scarlet.assets.fields.AssetRealFileField(editable=False, max_length=255, upload_to=scarlet.assets.utils.assets_dir)),
                ('image', scarlet.assets.fields.AssetsFileField(denormalize=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='assets.Asset')),
            ],
            options={
                'verbose_name': 'Hotspot module',
                'verbose_name_plural': 'Hotspot modules',
            },
        ),
        migrations.AddField(
            model_name='hotspot',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotspots', to='hotspots.HotSpotModule'),
        ),
    ]
