# Generated by Django 3.1 on 2020-09-01 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0005_dbs_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbs',
            old_name='aythor',
            new_name='author',
        ),
    ]
