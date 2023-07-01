from django.contrib import admin

# Register your models here.
from .models import FoodIteams,ChefDetails

admin.site.register(FoodIteams)
admin.site.register(ChefDetails)