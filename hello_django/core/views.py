from django.shortcuts import render, HttpResponse

# Create your views here.

#def hello(request, nome, idade):
    #return HttpResponse('<h1>Hello, World!</h1>')
    #return HttpResponse(f'<h1>Hello, {nome}!</h1>')
    #return HttpResponse(f'<h1>Hello, {nome} de {idade} anos!')
def sum(request, algarism1, algarism2):
    sum_result = algarism1 + algarism2
    return HttpResponse(f'<h1> The sum of {algarism1} and {algarism2} results in {sum_result}</h1>')
def multiplication(request, algarism1, algarism2):
    multi_result = algarism1 * algarism2
    return HttpResponse(f'<h1> The Multiplication between {algarism1} and {algarism2} results in {multi_result}</h1>')


def dividing(request, algarism1, algarism2):
    div_result = algarism1 / algarism2
    return HttpResponse(f'<h1>Dividing between {algarism1} and {algarism2} results in {div_result}</h1>')

def subtraction(request, algarism1, algarism2):
    sub_result = algarism1 - algarism2
    return HttpResponse(f'<h1>Subtraction between {algarism1} and {algarism2} results in {sub_result}</h1>')