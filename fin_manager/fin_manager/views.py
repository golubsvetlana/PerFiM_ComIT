
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
# from expenses import models as expense_models
# from income import models as income_models
from income.models import Income
from expenses.models import Expense
from django.db.models import Sum
from datetime import datetime

# @login_required
def category_list(request):
    return HttpResponse("Category list placeholder")

def main(request):

    selected_year = request.GET.get('year')
    current_year = datetime.now().year

    # Start with all expenses and all incomes
    expenses = Expense.objects.all()
    incomes = Income.objects.all()

    if selected_year:
        expenses = expenses.filter(date__year=int(selected_year))
        incomes = incomes.filter(date__year=int(selected_year))
    
    # Total after filters
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'total_expenses': round(total_expenses, 2),
        'total_income': round(total_income,2),
        'saving': round(total_income-total_expenses,2),
        'expenses': expenses,
        'selected_year': selected_year,
        'years': [
            (current_year-2, current_year-2),
            (current_year-1, current_year-1), 
            (current_year, current_year)
        ]
    }

    return render(request, 'dashboard.html', context)
