# Generated by Django 3.2.18 on 2023-04-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Admin', 'Admin')], max_length=100, null=True),
        ),
    ]
