# Generated by Django 5.1 on 2024-09-13 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0015_cheque_pending_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='is_completed',
        ),
    ]