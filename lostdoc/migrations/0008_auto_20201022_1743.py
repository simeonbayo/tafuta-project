# Generated by Django 3.1.1 on 2020-10-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostdoc', '0007_document_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docrequest',
            name='doc_request_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], max_length=10, null=True, verbose_name='Status'),
        ),
    ]