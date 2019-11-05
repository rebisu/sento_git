from django import forms
from .models import SentoData

class SentoDataForm(forms.ModelForm): 

    class Meta:
        model = SentoData
        fields = '__all__' #('title','text','date')
        

        