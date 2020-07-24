from django.db import models



class Blood(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Donors(models.Model):
    GENRE_CHOICES= [
    ('M', 'Male'),
    ('F', 'Female'),
    ]

    name = models.CharField(max_length=30)
    blood_type = models.ForeignKey(Blood, null=True, on_delete= models.SET_NULL)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENRE_CHOICES)
    
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Hospital(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Order (models.Model):
    partner = models.ForeignKey(Hospital, null=True, on_delete= models.SET_NULL)
    phone = models.CharField(max_length=20);
    address = models.TextField()
    delivery_date = models.DateField(blank=True);
    product =  models.ForeignKey(Blood, null=True, on_delete= models.SET_NULL)
    quantity = models.IntegerField()
    payment_option = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
    	return self.partner.name

    @property
    def amount(self):
        return self.price * self.quantity
