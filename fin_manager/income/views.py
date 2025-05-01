from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm
from django.db.models import Sum
from datetime import datetime



# from django.contrib.auth.decorators import login_required

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'income/income_list.html', {'incomes': incomes})

# @login_required
def incomes_view(request):
    selected_category = request.GET.get('category')
    selected_month = request.GET.get('month')
    selected_year = request.GET.get('year')
    current_year = datetime.now().year

    # Start with all incomes
    incomes = Income.objects.all()

    # Apply filters one by one
    if selected_category:
        incomes = incomes.filter(category=selected_category)

    if selected_month:
        incomes = incomes.filter(date__month=int(selected_month))

    if selected_year:
        incomes = incomes.filter(date__year=int(selected_year))

    # Total after filters
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'total_income': round(total_income, 2),
        'incomes': incomes,
        'category_choices': Income.CATEGORY_CHOICES,
        'selected_category': selected_category,
        'selected_month': selected_month,
        'selected_year': selected_year,
        'months': [
            ('01', 'January'), ('02', 'February'), ('03', 'March'),
            ('04', 'April'), ('05', 'May'), ('06', 'June'),
            ('07', 'July'), ('08', 'August'), ('09', 'September'),
            ('10', 'October'), ('11', 'November'), ('12', 'December')
        ],
        'years': [
            (current_year-2, current_year-2),
            (current_year-1, current_year-1), 
            (current_year, current_year)
        ]
    }

    return render(request, 'income/income_list.html', context)

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
