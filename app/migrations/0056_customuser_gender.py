# Generated by Django 3.2.18 on 2023-03-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_auto_20230331_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default='M', max_length=10),
        ),
    ]