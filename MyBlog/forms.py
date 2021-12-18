from django import forms
from .models import newPost

class CrearPost(forms.ModelForm):
    class Meta:
        models = newPost
        fields = '__all__'
        