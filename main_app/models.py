from django.db import models
from datetime import date

# Create your models here.
my_email = 'vasiliy.moscvin@yandex.ru'

class Works(models.Model):
    name = models.CharField(max_length=64)
    logo = models.CharField(max_length=64)
    logo_alt = models.CharField(max_length=32)
    e_address = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    post = models.CharField(max_length=32)
    work_from = models.DateField(auto_now=False,  default=date.today)
    work_to = models.DateField(auto_now=False,  default=date.today)

    def __str__(self):
        return self.name

class Studies(models.Model):
    name = models.CharField(max_length=32)
    logo = models.CharField(max_length=64)
    logo_alt = models.CharField(max_length=32)
    e_address = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    place_sturies = models.ForeignKey(Studies, on_delete=models.CASCADE)
    course = models.CharField(max_length=64)
    certif = models.CharField(max_length=64)

    def __str__(self):
        return self.course


class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    logo = models.CharField(max_length=64)
    logo_alt = models.CharField(max_length=32)
    birth_day = models.CharField(max_length=32)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    my_email = models.CharField(max_length=32)

    def __str__(self):
        return self.name


    # name = models.CharField(max_length=32, unique=True)
    # surname = models.CharField(max_length=32)
    # age = models.PositiveIntegerField()
    # time = models.DateField(blank=True)
    # text = models.TextField()
    # img = models.ImageField()
    # file = models.FileField()
    # bol = models.BooleanField()