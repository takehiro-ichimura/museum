# Generated by Django 3.1 on 2020-09-01 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0007_auto_20200901_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='aythor',
            new_name='author',
        ),
    ]
