# Generated by Django 5.0.6 on 2024-07-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0009_rename_id_employmentequity_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmentequity',
            name='Table_Name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
