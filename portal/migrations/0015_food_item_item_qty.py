# Generated by Django 3.0.5 on 2020-04-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20200430_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_item',
            name='item_qty',
            field=models.IntegerField(default=0),
        ),
    ]
