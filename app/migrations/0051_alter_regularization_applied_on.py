# Generated by Django 3.2.18 on 2023-03-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_regularization_applied_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularization',
            name='applied_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
