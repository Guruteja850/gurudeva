# Generated by Django 3.2.18 on 2023-03-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20230314_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='accessed_on',
        ),
        migrations.AddField(
            model_name='useractivity',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='useractivity',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]