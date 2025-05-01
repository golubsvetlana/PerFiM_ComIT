from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from datetime import datetime
# from django.contrib.auth.decorators import login_required

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, "expenses/expense_list.html", {"expenses": expenses})
# @login_required
def expenses_view(request):
    selected_category = request.GET.get('category')
    selected_month = request.GET.get('month')
    selected_year = request.GET.get('year')
    current_year = datetime.now().year

    # Start with all expenses
    expenses = Expense.objects.all()

    # Apply filters one by one
    if selected_category:
        expenses = expenses.filter(category=selected_category)

    if selected_month:
        expenses = expenses.filter(date__month=int(selected_month))

    if selected_year:
        expenses = expenses.filter(date__year=int(selected_year))

    # Total after filters
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'total_expenses': round(total_expenses, 2),
        'expenses': expenses,
        'category_choices': Expense.CATEGORY_CHOICES,
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

    return render(request, 'expenses/expense_list.html', context)

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense-list")
    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})


def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("expense-list")
    return render(request, "expenses/delete_expense.html", {"expense": expense})


def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expense-list")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "expenses/edit_expense.html", {"form": form})
