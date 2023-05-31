from django.shortcuts import render

# Create your views here.

from .models import Material


def index(request):
    material_registros = Material.objects.all()
    contexto = {"material": material_registros}
    return render(request, "material/index.html", contexto)
