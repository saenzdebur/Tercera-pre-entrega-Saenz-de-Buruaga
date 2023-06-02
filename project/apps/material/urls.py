from django.urls import path

from .views import crear_material, crear_materiales_predeterminados, index

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'cliente:index' %}
app_name = "material"

urlpatterns = [
    path("", index, name="index"),
    path("crear-materiales-predeterminados/", crear_materiales_predeterminados, name="crear-materiales"),
    path("crear/", crear_material, name="crear"),
]
