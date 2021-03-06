# Generated by Django 3.2.2 on 2021-11-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_company_event_jobvacancies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='jobvacancies',
            name='job_type',
            field=models.CharField(choices=[('part_time', 'part_time'), ('full_time', 'full_time')], default='full_time', max_length=50),
        ),
    ]
