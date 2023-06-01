from django.shortcuts import render

# Create your views here.

from .models import Material


def index(request):
    material = Material.objects.all()
    contexto = {"material": material}
    return render(request, "material/index.html", contexto)
