from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True, unique=True)
    username = models.CharField(max_length=500, blank=True, null=True, unique=True)
    email = models.CharField(max_length=500, blank=True, null=True, unique=True)
    emp_id = models.BigIntegerField(unique=True, blank=True, null=True)
    designation = models.ForeignKey('Designation', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name