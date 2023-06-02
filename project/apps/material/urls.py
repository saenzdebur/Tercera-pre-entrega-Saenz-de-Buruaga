from django.urls import path

from .views import (
    crear_dimension,
    crear_material,
    # crear_materiales_predeterminados,
    crear_proveedor,
    index,
)

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'cliente:index' %}
app_name = "material"

urlpatterns = [
    path("", index, name="index"),
    # path("crear-materiales-predeterminados/", crear_materiales_predeterminados, name="crear-materiales"),
    path("crear/", crear_material, name="crear"),
    path("crear-dimension/", crear_dimension, name="crear-dimension"),
    path("crear-proveedor/", crear_proveedor, name="crear-proveedor"),
]
