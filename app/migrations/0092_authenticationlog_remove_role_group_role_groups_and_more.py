# Generated by Django 4.2 on 2023-05-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0091_leavebalance_times_applied'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('action', models.CharField(blank=True, max_length=20, null=True)),
                ('ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='group',
        ),
        migrations.AddField(
            model_name='role',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.permission'),
        ),
    ]
