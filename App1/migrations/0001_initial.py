# Generated by Django 4.2.3 on 2023-07-25 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('No_of_Employees', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AddDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Parent_department', models.CharField(choices=[('Main Department', 'Main Department'), ('Admin $ HR', 'Admin $ HR'), ('Account', 'Account'), ('Development', 'Development'), ('Software', 'Software'), ('Ui&Ux', 'Ui&Ux')], max_length=150)),
                ('Location', models.CharField(max_length=100)),
                ('Work_Shift', models.CharField(choices=[('Regular work shift', 'Regular work shift'), ('demo working shift regular', 'demo working shift regular'), ('demo working shift scheduled', 'demo working shift scheduled')], max_length=150)),
                ('Description', models.TextField(max_length=150)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.manager')),
            ],
        ),
    ]
