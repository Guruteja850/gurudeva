# Generated by Django 4.1.3 on 2023-02-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(blank=True, choices=[('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Admin', 'Admin')], max_length=100, null=True),
        ),
    ]
