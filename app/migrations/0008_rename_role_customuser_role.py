# Generated by Django 4.1.3 on 2023-02-22 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_status_customuser_role_alter_customuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Role',
            new_name='role',
        ),
    ]
