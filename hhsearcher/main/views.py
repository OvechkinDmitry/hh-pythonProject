from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def demand(request):
    return render(request, 'main/demand.html')

def geography(request):
    return render(request, 'main/geography.html')

def skills(request):
    return render(request, 'main/skills.html')

def last_vacancies(request):
    return render(request, 'main/last_vacancies.html')