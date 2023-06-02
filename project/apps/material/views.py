from audioop import reverse

from django.shortcuts import redirect, render

from .form import DimensionForm, MaterialForm, ProveedorForm
from .models import Dimension, Material, Proveedor

# Create your views here.


def index(request):
    material_registros = Material.objects.all()
    contexto = {"materiales": material_registros}
    return render(request, "material/index.html", contexto)


# def crear_materiales_predeterminados(request):
#     # Crea instancias de materiales
#     m1 = Material.objects.create(nombre="Cobre")
#     m2 = Material.objects.create(nombre="Aluminio")
#     m3 = Material.objects.create(nombre="Latón")

#     # Crear instancias de dimensiones
#     Dimension.objects.create(largo=3000, ancho=1500, espesor=2, material_id=m2)
#     Dimension.objects.create(largo=2000, ancho=1000, espesor=1, material_id=m2)
#     Dimension.objects.create(largo=2000, ancho=600, espesor=3, material_id=m3)
#     Dimension.objects.create(largo=2000, ancho=600, espesor=1.5, material_id=m1)

#     # Crear instancias de proveedores

#     Proveedor.objects.create(nombre="Aluar", pais="Argentina", material_id=m2)
#     Proveedor.objects.create(nombre="Termo", pais="Brasil", material_id=m3)

#     # url = reverse("material:index")
#     return redirect("material:index")


def crear_material(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:index")
    else:  # method == "GET"
        form = MaterialForm()
    return render(request, "material/crear.html", {"form": form})


def crear_dimension(request):
    if request.method == "POST":
        form = DimensionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:index")
    else:  # method == "GET"
        form = DimensionForm()
    return render(request, "material/dimensiones.html", {"form": form})


def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:index")
    else:  # method == "GET"
        form = ProveedorForm()
    return render(request, "material/pais.html", {"form": form})
