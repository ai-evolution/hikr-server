# Generated by Django 2.2.2 on 2019-06-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='tag',
        ),
    ]
