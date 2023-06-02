from django import forms

from .models import Dimension, Material, Proveedor


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = "__all__"


class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = "__all__"


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"
