# Generated by Django 3.2.18 on 2023-03-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_useractivity_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
    ]