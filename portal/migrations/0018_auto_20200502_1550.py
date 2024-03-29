# Generated by Django 3.0.5 on 2020-05-02 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal_official', '0004_auto_20200429_1506'),
        ('portal', '0017_auto_20200502_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.TextField(null=True)),
                ('total_price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='food_order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_qty', models.IntegerField()),
                ('item_date', models.TextField(null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Portal_user_profile')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.food_item')),
            ],
        ),
        migrations.RemoveField(
            model_name='food_orders_list',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='food_orders_list',
            name='item_id',
        ),
        migrations.DeleteModel(
            name='food_orders',
        ),
        migrations.DeleteModel(
            name='food_orders_list',
        ),
        migrations.AddField(
            model_name='food_order',
            name='items_ordered',
            field=models.ManyToManyField(to='portal.food_order_list'),
        ),
        migrations.AddField(
            model_name='food_order',
            name='localbody',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal_official.official_athorities_list'),
        ),
        migrations.AddField(
            model_name='food_order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Portal_user_profile'),
        ),
    ]
