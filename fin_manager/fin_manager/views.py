
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from expenses import models as expense_models
from income import models as income_models
from income.models import Income
from expenses.models import Expense
from django.db.models import Sum

@login_required
def category_list(request):
    return HttpResponse("Category list placeholder")


def main(request):

  total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
  total_income = Income.objects.aggregate(total=Sum('amount'))['total'] or 0
  saves = total_income - total_expenses

  context = {
        'total_expenses': total_expenses,
        'total_income': total_income,
        'saving': saves
    }

  return render(request, 'dashboard.html', context)

