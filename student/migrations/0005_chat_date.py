# Generated by Django 3.2.6 on 2022-01-04 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_chat_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]