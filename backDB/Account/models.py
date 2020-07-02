from django.db import models
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField

class College(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False, unique=True, validators=[validate_email])
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100, blank=False)
    enrollment = models.CharField(max_length=50,blank=False, unique=True)
    email = models.EmailField(max_length=254, blank=False, unique=True, validators=[validate_email])
    semester = models.IntegerField(blank=False)
    department = models.CharField(max_length=100, blank=False)
    college = models.ForeignKey('College', related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Professors(models.Model):
    Professors_ROLE = (
        ("HOD", "HOD"),
        ("Professor", "Professor"),
    )
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False, unique=True, validators=[validate_email])
    department = models.CharField(max_length=100, blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    role = models.CharField(max_length=20, choices=Professors_ROLE, default='Professor')
    college = models.ForeignKey('College', related_name='professor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name