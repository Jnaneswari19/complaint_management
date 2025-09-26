from django.db import models
from django.utils import timezone

# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    Quantity = models.IntegerField()
    address = models.TextField()
    donation_count = models.IntegerField(default=1)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class MoneyDonation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    donation_count = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Ashram(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    is_approved = models.BooleanField(default=False)

class Functionhall(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    is_approved = models.BooleanField(default=False)


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    is_approved = models.BooleanField(default=False)





class Complaint(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    complaint_type = models.CharField(max_length=50)
    complaint_text = models.TextField()
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.complaint_type
    

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    complaint_text = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return self.name