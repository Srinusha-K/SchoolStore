from django.db import models
from django.core.validators import RegexValidator

class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Courses(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class St_data(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(
        'Date Of Birth'
    )
    age = models.IntegerField()
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    phone = models.CharField(unique=True, max_length=10, validators=[
        RegexValidator(regex='\w{10}$', message='Mobile number should be strictly of 10 digits. ')])
    email = models.EmailField(max_length=40)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    PURPOSE_CHOICES = {
        ('Place Order', 'Place Order'),
        ('Enquiry', 'Enquiry'),
        ('Return', 'Return')
    }
    purpose = models.CharField(choices=PURPOSE_CHOICES, max_length=50)
    materials = models.CharField(max_length=50)


    def __str__(self):
        return self.name