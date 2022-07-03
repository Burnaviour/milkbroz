
import mailbox
from pyexpat import model
from typing import Text
from django.db import models
from django.forms import CharField

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  desc = models.TextField()
  date = models.DateField()
  
  def __str__(self) -> str:
    return self.name +'  '+ self.email
class item(models.Model):
    title = models.CharField(max_length=122)
    
    def __str__(self):
       return self.title
class orderitem(models.Model):
    def __str__(self):
       return self.title
class orderitem(models.Model):
    def __str__(self):
       return self.title