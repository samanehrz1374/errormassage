# Generated by Django 4.0.1 on 2022-02-06 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0008_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='timestamp',
        ),
    ]