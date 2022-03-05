from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cladire
from .forms import CladireForm

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
