# Generated by Django 3.0.5 on 2020-04-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_official', '0002_official_user_contact_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='official_user',
            name='is_admin',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
