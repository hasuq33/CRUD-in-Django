# Generated by Django 4.1.6 on 2023-03-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappf', '0011_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='myappf/images'),
        ),
    ]
