from django.db import models

# Create your models here.

from django.db import connections
from django.db import models

# Create your models here.

from django.db import models
# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=100,default="")
    cl=models.CharField(max_length=10,db_column='class',default="")
    mark =models.IntegerField(default="")
    gender  =models.CharField(max_length=6,default="")
    class Meta:
        db_table='users'

    def Get_data(self):
        return {"n_usr_id":"Vishwanath","c_usr_eml":"vishwanath@gmail.com","n_usr_rl_id":"Admin"}

