# Generated by Django 3.1.1 on 2020-09-23 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lostdoc', '0003_auto_20200922_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.DateTimeField(auto_now_add=True, verbose_name='Requested Date')),
                ('doc_request_status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], max_length=10, verbose_name='Status')),
                ('doc_clearance_date', models.DateTimeField(auto_now_add=True, verbose_name='Clearance Date')),
                ('doc_requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('requested_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lostdoc.docupload', verbose_name='Requested Document')),
            ],
        ),
    ]