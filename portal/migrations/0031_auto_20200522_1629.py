# Generated by Django 2.2.6 on 2020-05-22 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal_official', '0004_auto_20200429_1506'),
        ('portal', '0030_medicine_list_quantity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicare_order',
            fields=[
                ('med_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_qty', models.IntegerField()),
                ('order_date', models.TextField(null=True)),
                ('total_price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('uid', models.TextField(default='0')),
                ('localbody', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal_official.official_athorities_list')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Medicine_list')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Portal_user_profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='medicine_order',
            name='localbody',
        ),
        migrations.RemoveField(
            model_name='medicine_order',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='medicine_item_list_in_orders',
        ),
        migrations.DeleteModel(
            name='Medicine_order',
        ),
    ]