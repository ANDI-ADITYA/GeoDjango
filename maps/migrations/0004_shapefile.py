# Generated by Django 2.2.9 on 2020-03-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_delete_provinsi'),
    ]

    operations = [
        migrations.CreateModel(
            name='shapefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('shp', models.FileField(upload_to='data/shps/')),
            ],
        ),
    ]
