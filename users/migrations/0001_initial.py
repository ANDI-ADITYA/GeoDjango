# Generated by Django 2.2.9 on 2020-07-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='raster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=150)),
                ('geotiff', models.FileField(upload_to='files/raster/')),
            ],
        ),
        migrations.CreateModel(
            name='shapefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=150)),
                ('shp', models.FileField(upload_to='files/shapefile/')),
            ],
        ),
    ]