# Generated by Django 4.1.5 on 2023-04-24 05:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0088_leavetype_leavebalance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leaves",
            name="Leave_type",
        ),
    ]
