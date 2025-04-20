from django import forms
from income.models import Income



class IncomeForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Income
        fields = ['category', 'amount', 'date','source']  
        widgets = {
            "source": forms.Textarea(attrs={"rows": 1, "class": 'form-control'}),
            "category": forms.Select(attrs={"class": 'form-select'}),
            "amount":forms.NumberInput(attrs={"class": 'form-control'})      
        }