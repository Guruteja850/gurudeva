# Generated by Django 3.2.18 on 2023-03-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20230328_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Leaves',
            field=models.IntegerField(default=21),
        ),
    ]