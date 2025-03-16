# Generated by Django 4.2.6 on 2023-10-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_passes_passnumber_alter_passes_mobilenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('aboutus', models.TextField()),
                ('email', models.EmailField(max_length=200)),
                ('mobilenumber', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
