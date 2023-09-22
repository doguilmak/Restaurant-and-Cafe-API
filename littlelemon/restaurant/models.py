from django.db import models
# from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    # booking_date = models.DateField(default=timezone.now)
    booking_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)
    phone_number = models.CharField(max_length=13, default='+90')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self) -> str:
        return f'{self.name} for {self.no_of_guests} guests on {self.booking_date} using table {self.reservation_slot}.'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'