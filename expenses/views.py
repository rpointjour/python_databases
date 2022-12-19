from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def idealbudget(request):
    template = loader.get_template('ideal.html')
    return HttpResponse(template.render())
