# Generated by Django 4.2.5 on 2023-09-13 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_rename_no_of_guests_booking_number_of_guests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='number_of_guests',
            new_name='no_of_guests',
        ),
    ]
