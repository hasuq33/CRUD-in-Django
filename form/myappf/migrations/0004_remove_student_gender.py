# Generated by Django 4.1.6 on 2023-03-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappf', '0003_alter_student_address_alter_student_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
    ]
