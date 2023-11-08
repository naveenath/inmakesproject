from django.db import models

# Create your models here.
from django.db import models
from department.models import Department, Course


# Create your models here.
class Purpose(models.Model):
    purpose = models.CharField(max_length=250)

    def __str__(self):
        return self.purpose


class Materials(models.Model):
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.material


class Order(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    options=(
        ('male','male'),
        ('female','female')
    )
    gender = models.CharField(max_length=200,choices=options,default='male')
    phonenumber = models.CharField(max_length=10)
    mailid = models.EmailField(max_length=100)
    address = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Materials)
    


    def __str__(self):
        return self.name
    

