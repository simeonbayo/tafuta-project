# Generated by Django 3.1.1 on 2020-10-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostdoc', '0008_auto_20201022_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='docimage',
            field=models.ImageField(null=True, upload_to='documents/'),
        ),
    ]
