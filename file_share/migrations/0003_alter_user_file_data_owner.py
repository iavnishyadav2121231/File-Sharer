# Generated by Django 3.2.16 on 2023-12-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_share', '0002_user_file_data_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_file_data',
            name='owner',
            field=models.CharField(default='self', max_length=40),
        ),
    ]
