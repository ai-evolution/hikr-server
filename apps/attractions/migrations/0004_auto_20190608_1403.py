# Generated by Django 2.2.2 on 2019-06-08 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0003_auto_20190608_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attractions.Category'),
        ),
    ]
