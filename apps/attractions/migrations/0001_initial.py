# Generated by Django 2.2.2 on 2019-06-08 21:50

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('node_id', models.BigIntegerField(unique=True, verbose_name='OSM ID')),
                ('name', models.CharField(max_length=2048)),
                ('address', models.CharField(max_length=2048, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAttraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('visited', models.BooleanField(default=False)),
                ('liked', models.BooleanField(default=False)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='attractions.Attraction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'attraction')},
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='attraction',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='attractions.Category'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='tags',
            field=models.ManyToManyField(to='attractions.Tag'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='user',
            field=models.ManyToManyField(through='attractions.UserAttraction', to=settings.AUTH_USER_MODEL),
        ),
    ]
