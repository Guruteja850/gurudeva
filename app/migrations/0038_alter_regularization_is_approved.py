# Generated by Django 3.2.18 on 2023-03-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20230316_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularization',
            name='is_approved',
            field=models.BooleanField(blank=True, default=10, null=True),
        ),
    ]