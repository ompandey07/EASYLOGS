# Generated by Django 4.2.11 on 2024-09-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crm_Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(max_length=50)),
                ('note_content', models.CharField(max_length=50)),
            ],
        ),
    ]