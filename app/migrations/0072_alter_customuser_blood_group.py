# Generated by Django 3.2.18 on 2023-04-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_alter_customuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]