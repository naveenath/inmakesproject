from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250)
    deptimg = models.ImageField(upload_to='pics')
    deptdesc = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=250)
    cimg = models.ImageField(upload_to='pic')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cdesc = models.TextField()

    def __str__(self):
        return self.name
