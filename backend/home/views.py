from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def home(request):
    template = loader.get_template('home.html')
    members = Members.objects.all().values()
    context = {'members': members}
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')
    member = Members.objects.get(id = id)
    context = { 'x' : member }
    return HttpResponse(template.render(context, request))