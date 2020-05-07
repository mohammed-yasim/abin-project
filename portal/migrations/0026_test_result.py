# Generated by Django 3.0.5 on 2020-05-07 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal_official', '0004_auto_20200429_1506'),
        ('portal', '0025_food_item_list_in_orders_localbody'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.TextField(null=True)),
                ('fever', models.IntegerField(default=0)),
                ('pain', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('nose', models.IntegerField(default=0)),
                ('breath', models.IntegerField(default=0)),
                ('travel', models.IntegerField(default=0)),
                ('other', models.IntegerField(default=0)),
                ('disease', models.TextField(max_length=32)),
                ('localbody', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal_official.official_athorities_list')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Portal_user_profile')),
            ],
        ),
    ]
