# Generated by Django 3.1 on 2020-08-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='artist',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
