# Generated by Django 4.1.6 on 2023-03-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappf', '0004_remove_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
    ]