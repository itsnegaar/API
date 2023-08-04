from django.db import models

# Create your models here.


class Location(models.Model):
    LocationName = models.CharField(max_length=200 , unique=True)

    def __str__(self):
        return self.LocationName

class Item(models.Model):
    ItemName = models.CharField(max_length=100)
    DateAdded = models.DateField(auto_now_add=True)
    ItemLocation = models.ForeignKey(Location , on_delete=models.CASCADE)

    def __str__(self):
        return self.ItemName