# Generated by Django 4.2.3 on 2023-07-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=24)),
                ('Last_name', models.CharField(max_length=30)),
                ('Email_address', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Password_comfirmation', models.CharField(max_length=30)),
            ],
        ),
    ]
