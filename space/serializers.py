from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cladire, Office, Desk, Employee, Remote


class CladireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cladire
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class DeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desk
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('idEmployee', 'firstName', 'lastName', 'role', 'gender',
                  'birthDate', 'nationality', 'address', 'isActive', 'desk')


class RemoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remote
        fields = '__all__'
