from secrets import choice
from django.db import models
from django.forms import CharField, DateTimeField
import uuid


class Cladire(models.Model):
    codCladire = models.AutoField(primary_key=True)
    denCladire = models.CharField(max_length=30)
    # verbose_name=('Denumire') - pentru denumire
    adresaCladire = models.CharField(max_length=200)
    nrEtaje = models.IntegerField()
    # nrBirouri = models.IntegerField()

    def __str__(self) -> str:
        return self.denCladire


class Office(models.Model):
    idOffice = models.AutoField(primary_key=True)
    nameOffice = models.CharField(max_length=30)
    floor = models.IntegerField(null=True, blank=True)
    building = models.ForeignKey('Cladire', on_delete=models.CASCADE)
    deskCount = models.IntegerField(null=True, blank=True)
    usedDesks = models.IntegerField(null=True, blank=True)
    adminOffice = models.CharField(max_length=30, null=True, blank=True)
    lengthOffice = models.IntegerField(null=True, blank=True)
    widthOffice = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nameOffice


class Desk(models.Model):
    idDesk = models.AutoField(primary_key=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE)
    deskCount = models.IntegerField(null=True, blank=True)
    usedDesks = models.IntegerField(null=True, blank=True)
    adminOffice = models.CharField(max_length=30, null=True, blank=True)
    lengthDesk = models.IntegerField(null=True, blank=True)
    widthDesk = models.IntegerField(null=True, blank=True)
    isOccupied = models.BooleanField()


class Employee(models.Model):
    STATUS = [
        ('male', 'male'),
        ('female', 'female'),
        ('nonbinary', 'nonbinary'),
    ]

    ROLES = [
        ('admin', 'admin'),
        ('officeadmin', 'oficeadmin'),
        ('user', 'user'),
    ]
    idEmployee = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(
        max_length=50, choices=ROLES, null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=STATUS, null=True, blank=True)
    desk = models.ForeignKey('Desk', on_delete=models.CASCADE)
    birthDate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    isActive = models.BooleanField()

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName


class Remote(models.Model):
    idRemote = models.AutoField(primary_key=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    startDate = models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    isApproved = models.BooleanField()
    approvedBy = models.CharField(max_length=30, choices=Employee.ROLES)
