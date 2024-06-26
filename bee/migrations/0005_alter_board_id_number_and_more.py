# Generated by Django 5.0.6 on 2024-06-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0004_board_id_employmentequity_id_alter_board_job_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employmentequity',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='procurement',
            name='reg_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='skillsdevelopment',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
