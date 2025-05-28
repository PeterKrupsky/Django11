from django import forms
from django.forms import ModelForm
from .models import Program_model


class MeForm(forms.Form):
    widget=forms.TextInput(attrs={'class': 'form-control'})
    task = forms.CharField(initial = "Впишите нужную фразу")
    a = forms.CharField(initial='Обо мне')


class ProgramForm(ModelForm):
    class Meta:
        model = Program_model
        fields = '__all__'

