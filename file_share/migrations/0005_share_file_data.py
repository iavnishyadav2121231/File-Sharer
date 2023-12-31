# Generated by Django 3.2.16 on 2023-12-10 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file_share', '0004_remove_user_file_data_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='share_file_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_Ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_share.user_file_data')),
                ('share_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
