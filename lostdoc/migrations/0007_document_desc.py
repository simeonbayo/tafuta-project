# Generated by Django 3.1.1 on 2020-10-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostdoc', '0006_auto_20201019_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='desc',
            field=models.TextField(default='', verbose_name='Description'),
        ),
    ]