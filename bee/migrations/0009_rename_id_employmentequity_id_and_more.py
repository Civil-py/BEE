# Generated by Django 5.0.6 on 2024-07-03 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0008_alter_employmentequity_ingest_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employmentequity',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='ingest_date',
            new_name='Ingest_date',
        ),
    ]