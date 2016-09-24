from django.contrib import admin
from .models import ReporteVial
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ReporteVialAdmin(ImportExportModelAdmin):
    list_display =("numdeticket","tiempo_evento","motivo","latitud","longitud",)
    list_filter=("motivo",)
    model = ReporteVial


admin.site.register(ReporteVial, ReporteVialAdmin)