from django.db import models
from django.utils.text import slugify

# Create your models here.
# save a shortend links - name , url , slug , clicks 

class Link(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True , blank=True)
    email = models.EmailField(max_length=100 , default="")
    clicks = models.PositiveIntegerField(default=0)
    
    #define a human-readable string representation of an object
    def __str__(self): 
        return f"{self.name} | {self.clicks} | {self.email}"
    
<<<<<<< HEAD
    
=======
 
>>>>>>> style
    def click(self):
        self.clicks += 1 
        self.save() # save that row in the table (instance)

    # set up the "SlugField" so that it works automatically (auto-generated from "name") 
    # overwriting the "save()" method.
    def save(self , *args , **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args , **kwargs)     
