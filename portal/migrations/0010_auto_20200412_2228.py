# Generated by Django 3.0.5 on 2020-04-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20200412_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal_user',
            name='otp_generated',
            field=models.TextField(default='2020-04-12 22:28:31'),
        ),
    ]
