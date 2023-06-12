# Generated by Django 3.2.18 on 2023-04-13 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_auto_20230413_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailvalidation',
            name='Leaves',
            field=models.IntegerField(default=21),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='address',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='blood_group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='contact',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='date_joined',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='emergency_contact',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='emergency_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='hr',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='manager',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.region'),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.role'),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='updated_by',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='emailvalidation',
            name='updated_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]