# Generated by Django 2.2.6 on 2020-05-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0029_auto_20200521_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine_list',
            name='quantity_type',
            field=models.CharField(default='Strip', max_length=32),
        ),
    ]
