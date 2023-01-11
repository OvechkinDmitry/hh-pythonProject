from django.shortcuts import render
from django.contrib import messages

from .models import *
from .scripts.last_vacancies import hh_parser
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def demand(request):
    demand = Demand.objects.all()
    context = {
        'demand': demand
    }
    return render(request, 'main/demand.html', context)

def geography(request):
    return render(request, 'main/geography.html')

def skills(request):
    return render(request, 'main/skills.html')

def last_vacancies(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        data = hh_parser(day).fetch_data()
        if data is not None:
            context = {"data": data}
            return render(request, 'main/last_vacancies.html', context=context)
        return render(request, 'main/last_vacancies.html')
    return render(request, 'main/last_vacancies.html')