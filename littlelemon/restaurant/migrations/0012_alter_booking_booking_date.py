# Generated by Django 4.2.5 on 2023-09-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
    ]
