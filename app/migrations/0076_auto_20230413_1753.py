# Generated by Django 3.2.18 on 2023-04-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0075_emailvalidation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailvalidation',
            name='user',
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission'),
        ),
    ]
