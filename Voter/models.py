from django.db import models

# Create your models here.
# this is model for Voter 
class Voter(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(default="ps.jpg",upload_to="pics")
    aadhar=models.BigIntegerField(max_length=12)
    city = models.CharField(max_length=20 )
    ward = models.CharField(max_length=20)
    contact=models.BigIntegerField(max_length=10)
    dob=models.DateField()
    
    def __str__(self):
        return self.name

class Group(models.Model):
    symbol=models.ImageField(default="ps.jpg",upload_to="pics")
    name = models.CharField(max_length=40)
    party = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    ward = models.CharField(max_length=20)

    def __str__(self):
        return self.party