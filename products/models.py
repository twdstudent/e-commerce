from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

# will create the database for our product. 
# So this is where we specify the columns that will be within tables in our database.
# need to do 'sudo pip3 install Pillow' to be able to install images.