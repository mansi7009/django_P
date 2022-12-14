# Generated by Django 4.1.2 on 2022-10-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='AVAILABLE', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='AVAILABLE', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='AVAILABLE', max_length=10),
        ),
    ]
