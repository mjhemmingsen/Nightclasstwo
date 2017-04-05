from django.db import models

# Create your models here.

'''
This is where you define your model it's important to
remember not to forget to register this model in your
admin.py file as well as add the product app to the installed apps array
in the settings.py
'''
class Product(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)


    def __str__(self):
        return self.title

