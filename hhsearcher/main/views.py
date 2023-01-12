from django.shortcuts import render
from django.contrib import messages

from .models import *
from .scripts.last_vacancies import hh_parser
from django.http import HttpResponse


def index(request):
    introCards = IntroCards.objects.all()
    introFacts = IntroFacts.objects.all()
    context = {
        'aboutPage': AboutPage.objects.get(page="ГЛАВНАЯ"),
        'introCards': introCards,
        "introFacts": introFacts,
    }
    return render(request, 'main/intro.html', context=context)

def demand(request):
    demand = Demand.objects.all()
    context = {
        'aboutPage': AboutPage.objects.get(page="ВОСТРЕБОВАННОСТЬ"),
        'demand': demand
    }
    return render(request, 'main/demand.html', context=context)

def geography(request):
    geography = Geography.objects.all()
    context = {
        'aboutPage': AboutPage.objects.get(page="ГЕОГРАФИЯ"),
        'geography': geography
    }
    return render(request, 'main/geography.html', context=context)

def skills(request):
    skills = Skills.objects.all()
    context = {
        'aboutPage': AboutPage.objects.get(page="НАВЫКИ"),
        'skills': skills
    }
    return render(request, 'main/skills.html', context=context)

def last_vacancies(request):
    main_context = {'aboutPage': AboutPage.objects.get(page="ПОСЛЕДНИЕ ВАКАНСИИ")}
    if request.method == 'POST':
        day = request.POST.get('day')
        data = hh_parser(day).fetch_data()
        if data is not None:
            context = {"data": data, **main_context}
            return render(request, 'main/last_vacancies.html', context= context)
        return render(request, 'main/last_vacancies.html', context= main_context)
    return render(request, 'main/last_vacancies.html', context= main_context)