from secrets import choice
from django.db import models
from django.forms import CharField, DateTimeField
import uuid


class Cladire(models.Model):
    codCladire = models.AutoField(primary_key=True)
    denCladire = models.CharField(max_length=30, null=False, blank=False)
    # verbose_name=('Denumire') - pentru denumire
    adresaCladire = models.CharField(max_length=200, null=False, blank=False)
    nrEtaje = models.IntegerField(null=False, blank=False)
    # nrBirouri = models.IntegerField()

    def __str__(self) -> str:
        return self.denCladire


class Office(models.Model):
    idOffice = models.AutoField(primary_key=True)
    nameOffice = models.CharField(max_length=30)
    floor = models.IntegerField(null=False, blank=False)
    building = models.ForeignKey(
        'Cladire', on_delete=models.CASCADE, null=False, blank=False)
    deskCount = models.IntegerField(null=False, blank=False)
    usedDesks = models.IntegerField(null=True, blank=True)
    adminOffice = models.CharField(max_length=30, null=True, blank=True)
    lengthOffice = models.IntegerField(null=False, blank=False)
    widthOffice = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return self.nameOffice


class Desk(models.Model):
    ROLES = [
        ('admin', 'admin'),
        ('officeadmin', 'oficeadmin'),
    ]
    idDesk = models.AutoField(primary_key=True)
    office = models.ForeignKey(
        'Office', on_delete=models.CASCADE, null=False, blank=False)
    deskCount = models.IntegerField(null=False, blank=False)
    usedDesks = models.IntegerField(null=True, blank=True)
    adminOffice = models.CharField(
        max_length=30, null=False, blank=False, choices=ROLES)
    lengthDesk = models.IntegerField(null=False, blank=False)
    widthDesk = models.IntegerField(null=False, blank=False)
    isOccupied = models.BooleanField(null=False, blank=False)


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
        max_length=50, choices=ROLES, null=False, blank=False)
    gender = models.CharField(
        max_length=20, choices=STATUS, null=False, blank=False)
    desk = models.ForeignKey(
        'Desk', on_delete=models.CASCADE, null=False, blank=False)
    birthDate = models.DateField(null=False, blank=False)
    nationality = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    isActive = models.BooleanField(null=False, blank=False)
    id = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName


class Remote(models.Model):
    idRemote = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        'Employee', on_delete=models.CASCADE, null=False, blank=False)
    startDate = models.DateField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    isApproved = models.BooleanField()
    approvedBy = models.CharField(
        max_length=30, choices=Employee.ROLES, null=False, blank=False)
