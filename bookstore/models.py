from __future__ import unicode_literals

 

from django.db import models

 

# Create your models here.

class Genre(models.Model):

  text = models.CharField(max_length=200)

  def __str__(self):

        return self.text

 

class Book(models.Model):

   book_id = models.CharField(max_length=100)

   title = models.CharField(max_length=200)

   author = models.CharField(max_length=100)

   genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default="")

   price = models.DecimalField(default=0,max_digits=10, decimal_places=2)

   def __str__(self):

        return self.title
