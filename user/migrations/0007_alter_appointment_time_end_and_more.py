# Generated by Django 4.1.1 on 2022-09-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_myuser_username_myuser_email_myuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_end',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_start',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
