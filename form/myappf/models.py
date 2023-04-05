from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200,default="")
    father_name = models.CharField(max_length= 200,default="")
    mother_name = models.CharField(max_length= 200,default="")
    address = models.CharField(max_length= 2000,default="")
    gender = models.CharField(max_length= 200,default="")
    state = models.CharField(max_length= 200,default="")
    city = models.CharField(max_length= 200,default="")
    date_of_birth = models.CharField(max_length=50 ,default="")
    enrollment = models.IntegerField(default=0)
    course = models.CharField(max_length= 200,default="")
    email = models.CharField(max_length= 200,default="")

    

    def __str__(self):
        return self.first_name

class Image(models.Model):
    image = models.ImageField(upload_to='myappf/images')    
    

