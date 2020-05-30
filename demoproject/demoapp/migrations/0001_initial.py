# Generated by Django 3.0.5 on 2020-04-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_loc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
