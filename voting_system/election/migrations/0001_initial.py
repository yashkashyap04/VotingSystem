# Generated by Django 3.2.15 on 2022-09-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('regno', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
