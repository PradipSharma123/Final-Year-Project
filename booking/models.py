from django.db import models
import enum
from django.contrib.auth.models import User
# Create your models here.
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="booking")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="maharashtra")
    country = models.CharField(max_length=50,default="india")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    METHOD = (
    ("Cash On Checkout", "Cash On Checkout"),
    ("Khalti", "Khalti"),
    
    )

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    payment_method = models.CharField(
        max_length=50, choices = METHOD)
    
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    booking_id = models.CharField(max_length=100,default="null")
    payment_status = models.IntegerField(default=1)
    guest_count = models.IntegerField(default=1)

    def __str__(self):
        return self.guest.username

    def date_dif(self):
        return (self.check_out - self.check_in).days

    def booking_amount(self):
        return self.date_dif() * self.room.price

    def is_payment_pending(self):
        return self.payment_status == PaymentStatus.Pending

    def get_payment_status(self):
        return PaymentStatus(self.payment_status).name


class PaymentStatus(enum.IntEnum):
   Pending = 1
   Paid = 2
   