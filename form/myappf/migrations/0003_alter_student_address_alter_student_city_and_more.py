# Generated by Django 4.1.6 on 2023-03-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappf', '0002_alter_student_date_of_birth_alter_student_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
    ]
