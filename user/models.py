from django.db import models

# Create your models here.
class FoodIteams(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='food_pic',max_length=500)
    description=models.TextField()
    price=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class ChefDetails(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='chef_details', max_length=500)
    designation=models.CharField( max_length=50)
    
    def __str__(self) :
        return self.name