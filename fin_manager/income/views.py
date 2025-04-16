from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'income/income_list.html', {'incomes': incomes})

def add_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income-list')
    else:
        form = IncomeForm()
    return render(request, 'income/add_income.html', {'form': form})

def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        income.delete()
        return redirect("income-list")
    return render(request, "income/delete_income.html", {'income': income})


def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect("income-list")
    else:
        form = IncomeForm(instance=income)
    return render(request, "income/edit_income.html", {"form": form})
