# Generated by Django 3.2.18 on 2023-03-09 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllHolidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('date', models.DateField()),
                ('occasion', models.CharField(max_length=100)),
                ('region', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.region')),
            ],
        ),
    ]
