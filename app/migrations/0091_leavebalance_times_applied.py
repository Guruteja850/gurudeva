# Generated by Django 4.1.5 on 2023-04-24 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0090_leaves_leave_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="leavebalance",
            name="times_applied",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
