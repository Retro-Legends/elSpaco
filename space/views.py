from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Cladire, Office, Desk, Employee, Remote
from .forms import CladireForm, OfficeForm, DeskForm, EmployeeForm, RemoteForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import *


def index(request):

    num_cladiri = Cladire.objects.all().count()
    num_offices = Office.objects.all().count()
    num_desks = Desk.objects.all().count()
    num_employees = Employee.objects.all().count()
    num_remotes = Remote.objects.all().count()

    context = {
        'num_cladiri': num_cladiri,
        'num_offices': num_offices,
        'num_desks': num_desks,
        'num_employees': num_employees,
        'num_remotes': num_remotes,
    }
    return render(request, 'index.html', context=context)


# ~~~ Cladiri ~~~#
#

def cladiri(request):
    cladiri = Cladire.objects.all()
    context = {'cladiri': cladiri}
    return render(request, 'space/cladiri.html', context)


def cladire(request, pk):
    cladireObj = Cladire.objects.get(codCladire=pk)
    # tags = cladireObj.tags.all()
    return render(request, 'space/cladire.html', {'cladire': cladireObj})


def createCladire(request):
    form = CladireForm()

    if request.method == 'POST':
        form = CladireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cladiri')

    context = {'form': form}
    return render(request, "space/cladire_form.html", context)


def updateCladire(request, pk):
    cladire = Cladire.objects.get(codCladire=pk)
    form = CladireForm(instance=cladire)

    if request.method == 'POST':
        form = CladireForm(request.POST, instance=cladire)
        if form.is_valid():
            form.save()
            return redirect('cladiri')

    context = {'form': form}
    return render(request, "space/cladire_form.html", context)


def deleteCladire(request, pk):
    cladire = Cladire.objects.get(codCladire=pk)
    if request.method == 'POST':
        cladire.delete()
        return redirect('cladiri')
    context = {'object': cladire}
    return render(request, 'space/sterge_cladire.html', context)

# ---
# END
# ---

# ~~~ Birouri ~~~#
#


def birouri(request):
    birouri = Office.objects.all()
    context = {'birouri': birouri}
    return render(request, 'space/birouri.html', context)


def birou(request, pk):
    birouObj = Office.objects.get(idOffice=pk)
    return render(request, 'space/birou.html', {'birou': birouObj})


def createBirou(request):
    form = OfficeForm()

    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('birouri')

    context = {'form': form}
    return render(request, "space/birou_form.html", context)


def updateBirou(request, pk):
    birou = Office.objects.get(idOffice=pk)
    form = OfficeForm(instance=birou)

    if request.method == 'POST':
        form = OfficeForm(request.POST, instance=birou)
        if form.is_valid():
            form.save()
            return redirect('birouri')

    context = {'form': form}
    return render(request, "space/birou_form.html", context)


def deleteBirou(request, pk):
    birou = Office.objects.get(idOffice=pk)
    if request.method == 'POST':
        birou.delete()
        return redirect('birouri')
    context = {'object': birou}
    return render(request, 'space/sterge_birou.html', context)

# ---
# END
# ---

# ~~~ Desks ~~~#
#


def desks(request):
    desks = Desk.objects.all()
    context = {'desks': desks}
    return render(request, 'space/desks.html', context)


def desk(request, pk):
    deskObj = Desk.objects.get(idDesk=pk)
    return render(request, 'space/desk.html', {'desk': deskObj})


def createDesk(request):
    form = DeskForm()

    if request.method == 'POST':
        form = DeskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desks')

    context = {'form': form}
    return render(request, "space/desk_form.html", context)


def updateDesk(request, pk):
    desk = Desk.objects.get(idDesk=pk)
    form = DeskForm(instance=desk)

    if request.method == 'POST':
        form = DeskForm(request.POST, instance=desk)
        if form.is_valid():
            form.save()
            return redirect('desks')

    context = {'form': form}
    return render(request, "space/desk_form.html", context)


def deleteDesk(request, pk):
    desk = Desk.objects.get(idDesk=pk)
    if request.method == 'POST':
        desk.delete()
        return redirect('desks')
    context = {'object': desk}
    return render(request, 'space/sterge_desk.html', context)

# ---
# END
# ---

# ~~~ Employees ~~~#
#


def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'space/employees.html', context)


def employee(request, pk):
    employeeObj = Employee.objects.get(idEmployee=pk)
    return render(request, 'space/employee.html', {'employee': employeeObj})


def createEmployee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {'form': form}
    return render(request, "space/employee_form.html", context)


def updateEmployee(request, pk):
    employee = Employee.objects.get(idEmployee=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {'form': form}
    return render(request, "space/employee_form.html", context)


def deleteEmployee(request, pk):
    employee = Employee.objects.get(idEmployee=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')
    context = {'object': employee}
    return render(request, 'space/sterge_employee.html', context)

# ---
# END
# ---

# ~~~ Remotes ~~~#
#


def remotes(request):
    remotes = Remote.objects.all()
    context = {'remotes': remotes}
    return render(request, 'space/remotes.html', context)


def remote(request, pk):
    remoteObj = Remote.objects.get(idRemote=pk)
    return render(request, 'space/remote.html', {'remote': remoteObj})


def createRemote(request):
    form = RemoteForm()

    if request.method == 'POST':
        form = RemoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remotes')

    context = {'form': form}
    return render(request, "space/remote_form.html", context)


def updateRemote(request, pk):
    remote = Remote.objects.get(idRemote=pk)
    form = RemoteForm(instance=remote)

    if request.method == 'POST':
        form = RemoteForm(request.POST, instance=remote)
        if form.is_valid():
            form.save()
            return redirect('remotes')

    context = {'form': form}
    return render(request, "space/remote_form.html", context)


def deleteRemote(request, pk):
    remote = Remote.objects.get(idRemote=pk)
    if request.method == 'POST':
        remote.delete()
        return redirect('remotes')
    context = {'object': remote}
    return render(request, 'space/sterge_remote.html', context)

# ---
# END
# ---

# ~~
# ~~ API
# ~~


@api_view(['GET'])
def apiCladiri(request):
    cladiri = Cladire.objects.all()
    serializer = CladireSerializer(cladiri, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiOffices(request):
    offices = Office.objects.all()
    serializer = OfficeSerializer(offices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiDesks(request):
    desks = Desk.objects.all()
    serializer = DeskSerializer(desks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiRemotes(request):
    remotes = Remote.objects.all()
    serializer = RemoteSerializer(remotes, many=True)
    return Response(serializer.data)

# ~~
# ~~ API SELECTIV
# ~~


@api_view(['GET', 'POST', 'DELETE'])
def apiCladire(request, pk):
    try:
        cladire = Cladire.objects.get(codCladire=pk)
    except Cladire.DoesNotExist:
        return JsonResponse({'message': 'The cladire does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CladireSerializer(cladire, many=False)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        cladire_data = JSONParser().parse(request)
        serializer = CladireSerializer(cladire, data=cladire_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cladire.delete()
        return JsonResponse({'message': 'Cladire was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def apiOffice(request, pk):
    try:
        office = Office.objects.get(idOffice=pk)
    except Office.DoesNotExist:
        return JsonResponse({'message': 'The office does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OfficeSerializer(office, many=False)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        office_data = JSONParser().parse(request)
        serializer = OfficeSerializer(office, data=office_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        office.delete()
        return JsonResponse({'message': 'Office was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def apiDesk(request, pk):
    try:
        desk = Desk.objects.get(idDesk=pk)
    except Desk.DoesNotExist:
        return JsonResponse({'message': 'The desk does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeskSerializer(desk, many=False)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        desk_data = JSONParser().parse(request)
        serializer = DeskSerializer(desk, data=desk_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        desk.delete()
        return JsonResponse({'message': 'Desk was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def apiEmployee(request, pk):
    try:
        employee = Employee.objects.get(idEmployee=pk)
    except Employee.DoesNotExist:
        return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee, many=False)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=employee_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def apiRemote(request, pk):
    try:
        remote = Remote.objects.get(idRemote=pk)
    except Remote.DoesNotExist:
        return JsonResponse({'message': 'The remote does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RemoteSerializer(remote, many=False)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        remote_data = JSONParser().parse(request)
        serializer = RemoteSerializer(remote, data=remote_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        remote.delete()
        return JsonResponse({'message': 'Remote was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def apiEmployee(request, pk):
#     employee = Employee.objects.get(idEmployee=pk)
#     serializer = EmployeeSerializer(employee, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def apiRemote(request, pk):
#     remote = Remote.objects.get(idRemote=pk)
#     serializer = RemoteSerializer(remote, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def apiDesk(request, pk):
#     desk = Desk.objects.get(idDesk=pk)
#     serializer = DeskSerializer(desk, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def apiOffice(request, pk):
#     office = Office.objects.get(idOffice=pk)
#     serializer = OfficeSerializer(office, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def apiCladire(request, pk):
#     cladire = Cladire.objects.get(codCladire=pk)
#     serializer = CladireSerializer(cladire, many=False)
#     return Response(serializer.data)
