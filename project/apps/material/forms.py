from django import forms

from .models import Dimension, Material, Proveedor


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = {"nombre"}


class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = {"largo", "ancho", "espesor"}


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = {"nombre", "pais"}
