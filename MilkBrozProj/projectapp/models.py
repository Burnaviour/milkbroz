

from pyexpat import model
from typing import Text
import uuid
from django.db import models
from django.forms import CharField

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=122)
 
  address = models.TextField()
  payment=models.CharField(max_length=120,default='none')
  phone_number=models.CharField( default=None,max_length=120)
  date = models.DateField()
  
  trans_id = models.UUIDField(unique=True, null=True, default=None)
  def __str__(self) -> str:
    return self.name

