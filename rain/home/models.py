from django.db import models

# Create your models here.
#  Feedback Model
#  Stats Work
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100,blank = False)
    message =  models.TextField(max_length=2000)
    mail = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=10)
    
    def _str_(self):
        return self.name