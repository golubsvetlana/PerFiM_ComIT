from django import forms
from expenses.models import Expense  # Make sure you also import your model

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date', 'description']
