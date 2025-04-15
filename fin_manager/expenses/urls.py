from django.urls import path
from .views import expense_list, add_expense

urlpatterns = [
    path('', expense_list, name='expense-list'),
    path('add/', add_expense, name='add-expense')
]
