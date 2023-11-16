# forms.py
from django import forms
from .models import Bezeroa, Platerra

class BezeroaForm(forms.ModelForm):
    class Meta:
        model = Bezeroa
        fields = '__all__'

class PlaterraForm(forms.ModelForm):
    class Meta:
        model = Platerra
        fields = '__all__'