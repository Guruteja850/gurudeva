# Generated by Django 3.2.18 on 2023-03-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_useractivity_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularization',
            name='approved_by',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regularization',
            name='approved_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regularization',
            name='updated_by',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regularization',
            name='updated_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
