# Generated by Django 4.2.5 on 2023-09-10 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_rename_number_of_guests_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='no_of_guests',
            new_name='number_of_guests',
        ),
    ]