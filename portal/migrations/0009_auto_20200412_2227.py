# Generated by Django 3.0.5 on 2020-04-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20200412_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal_user',
            name='otp_generated',
            field=models.TextField(default='2020-04-12 22:27:34'),
        ),
    ]
