# Generated by Django 4.2 on 2023-04-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
