# Generated by Django 3.2.18 on 2023-03-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_useractivity_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.CharField(blank=True, choices=[('UAE', 'UAE'), ('INDIA', 'INDIA'), ('USA', 'USA'), ('ENGLAND', 'ENGLAND')], max_length=50, null=True),
        ),
    ]