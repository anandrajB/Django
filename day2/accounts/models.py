from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    country = models.CharField(max_length=155)


class Principal(models.Model):
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    salary = models.CharField(max_length=155)
    joined_date = models.DateTimeField(auto_now_add=True)
    


class Staff(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    classroom_id = models.IntegerField()
    is_class_councellor = models.BooleanField(default=False)
    subject = models.CharField(max_length=155)


class student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_class_leader = models.BooleanField(default=False)
    standard = models.CharField(max_length=255)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
