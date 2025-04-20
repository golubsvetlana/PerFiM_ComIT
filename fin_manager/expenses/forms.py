from django import forms
from expenses.models import Expense  # Make sure you also import your model

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date', 'description']
        widgets = {
            "description": forms.Textarea(attrs={"rows": 1, "class": 'form-control'}),
            "category": forms.Select(attrs={"class": 'form-select'}),
            "amount":forms.NumberInput(attrs={"class": 'form-control'})
            # "date": forms.DateInput(attrs={"class": 'form-control'})
        }

