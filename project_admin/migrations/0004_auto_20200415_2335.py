# Generated by Django 3.0.5 on 2020-04-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0003_auto_20200415_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global_variable',
            name='var_key',
            field=models.CharField(default='*', max_length=50),
        ),
    ]
