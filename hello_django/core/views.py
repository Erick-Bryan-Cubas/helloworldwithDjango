from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    #return HttpResponse('<h1>Hello, World!</h1>')
    #return HttpResponse(f'<h1>Hello, {nome}!</h1>')
    return HttpResponse(f'<h1>Hello, {nome} de {idade} anos!')