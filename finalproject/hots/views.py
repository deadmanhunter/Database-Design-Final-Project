from django.shortcuts import render
from django.http import HttpResponse
from .models import Heroes, Universe, Abilities, Ultimate
from django.template import loader

# Create your views here.

def index(request):
    heroes = Heroes.objects.order_by("hero_name")
    template = loader.get_template('hots/index.html')
    context = {'hero_list': heroes,}

    return HttpResponse(template.render(context, request))

def detail(request, hero_id):
    hero = Heroes.objects.get(id=hero_id)
    abilities = Abilities.objects.filter(hero_id=hero_id)
    ultimates = Ultimate.objects.filter(hero_id=hero_id)
    template = loader.get_template('hots/heroes.html')
    context = {'hero': hero,
               'abilities': abilities,
               'ultimates': ultimates}


    return HttpResponse(template.render(context, request))

def ability(request, hero_id):
    response = "Hero: %s"
    return HttpResponse(response % hero_id)

def update(request, hero_id):
    response = "Hero: %s"
    return HttpResponse(response % hero_id)