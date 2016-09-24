from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def hola (request):
	return HttpResponse("hola mundo")

def saludo(request, name):
	if name:
		saludo = "Hola " + name
	elif request.user:
		saludo = "Hola " + request.user.username
	else:
		saludo = "Hola Mundo"
	return HttpResponse(saludo)

@login_required(login_url="/avisoauth")
def protegida(request):
	return HttpResponse("vista protegida")

def avisoauth(request):
	return HttpResponse("Requieres autentificarte")