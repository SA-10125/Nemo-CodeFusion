# Generated by Django 5.1 on 2024-10-04 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='home.idcard')),
            ],
        ),
    ]
