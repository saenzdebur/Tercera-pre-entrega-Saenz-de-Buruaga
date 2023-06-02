from audioop import reverse

from django.shortcuts import redirect, render

from .models import Dimension, Material, Proveedor

from .form import MaterialForm

# Create your views here.


def index(request):
    material_registros = Material.objects.all()
    contexto = {"materiales": material_registros}
    return render(request, "material/index.html", contexto)


def crear_materiales_predeterminados(request):
    # Crea instancias de materiales
    m1 = Material.objects.create(nombre="Cobre", proveedor_id=1)
    m2 = Material.objects.create(nombre="Aluminio", proveedor_id=2)
    m3 = Material.objects.create(nombre="Latón", proveedor_id=3)

    # Crear instancias de dimensiones
    Material.objects.create(largo=3000, ancho=1500, espesor=2, material_id=m2)
    Material.objects.create(largo=2000, ancho=1000, espesor=1, material_id=m2)
    Material.objects.create(largo=2000, ancho=600, espesor=3, material_id=m3)
    Material.objects.create(largo=2000, ancho=600, espesor=1.5, material_id=m1)

    # Crear instancias de proveedores

    Material.objects.create(nombre="Aluar", pais="Argentina", material_id=m2)
    Material.objects.create(nombre="Termo", pais="Brasil", material_id=m)

    # url = reverse("material:index")
    return redirect("material:index")


def crear_material(request):
    # from .forms import MaterialForm

    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("cliente:index"))
    else:  # method == "GET"
        form = MaterialForm()
    return render(request, "cliente/crear.html", {"form": form})
