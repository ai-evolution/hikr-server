# Generated by Django 2.2.2 on 2019-06-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0005_auto_20190608_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='coor_x',
            field=models.FloatField(null=True, verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='coor_y',
            field=models.FloatField(null=True, verbose_name='Y'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
