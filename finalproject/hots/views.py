from django.shortcuts import render
from django.http import HttpResponse
from .models import Heroes, Universe, Abilities, Ultimate
from django.template import loader

# Create your views here.

def index(request):
    heroes = Heroes.objects.order_by("-hero_name")
    output = ""
    template = loader.get_template('hots/index.html')
    context = {'hero_list': heroes,}


    for h in heroes:
        for a in Abilities.objects.filter(hero_id=h.id):
            output += h.hero_name + ": " + a.ability_name + ",\n\n"

    return HttpResponse(template.render(context, request))

def detail(request, hero_id):
    response = "Hero: %s"
    return HttpResponse(response % hero_id)

def ability(request, hero_id):
    response = "Hero: %s"
    return HttpResponse(response % hero_id)

def update(request, hero_id):
    response = "Hero: %s"
    return HttpResponse(response % hero_id)