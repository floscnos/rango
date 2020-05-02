from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, Creamy, Cookie, Candy, Cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'body': 'A lot of boring information is said here.'}
    return render(request, 'rango/about.html', context=context_dict)