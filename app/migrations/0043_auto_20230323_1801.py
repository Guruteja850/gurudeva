# Generated by Django 3.2.18 on 2023-03-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_leaves_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='allholidays',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='Leave_type',
            field=models.CharField(choices=[('Casual', 'Casual'), ('Paternity', 'Paternity')], max_length=100),
        ),
    ]
