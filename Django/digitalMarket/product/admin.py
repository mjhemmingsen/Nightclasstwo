from django.contrib import admin
from .models import Product # IMPORT PRODUCT FROM MODELS
# Register your models here.


# This will register the model to our admin panel
admin.site.register(Product)