from django.urls import path
from .views import incomes_view, add_income,delete_income, edit_income

urlpatterns = [
    path("", incomes_view, name="income-list"),
    path("add/", add_income, name="add-income"),
    path("edit/<int:pk>/", edit_income, name="edit-income"),
    path("delete/<int:pk>/", delete_income, name="delete-income"),

]
