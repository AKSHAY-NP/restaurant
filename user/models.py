from django.db import models

# Create your models here.
class FoodIteams(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='food_pic',max_length=500)
    description=models.TextField()