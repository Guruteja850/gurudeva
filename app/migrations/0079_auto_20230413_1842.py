# Generated by Django 3.2.18 on 2023-04-13 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_remove_emailvalidation_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailvalidation',
            name='Leaves',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='address',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='emergency_contact',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='emergency_email',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='hr',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='region',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='emailvalidation',
            name='updated_on',
        ),
    ]
