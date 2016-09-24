from django.shortcuts import render
from .models import ReporteVial
# Create your views here.
def reportevial(request):
    reportes = ReporteVial.objects.all()
    return render(request, "reporte/lista_reporte.html", {"reportes": reportes })

def grafica(request):
    return render(request,"reporte/grafica.html",{})