# Generated by Django 4.1.7 on 2023-03-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.TextField()),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_mobile', models.TextField()),
            ],
        ),
    ]
