# Generated by Django 3.2.18 on 2023-03-22 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_date', models.DateField()),
                ('Reason', models.CharField(max_length=300)),
                ('Leave_type', models.TextField()),
                ('Is_approved', models.BooleanField(blank=True, default=None, null=True)),
                ('Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]