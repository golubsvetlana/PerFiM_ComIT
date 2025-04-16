from django.urls import path
from .views import income_list, add_income,delete_income, edit_income

urlpatterns = [
    path("", income_list, name="income-list"),
    path("add/", add_income, name="add-income"),
    path("edit/<int:pk>/", edit_income, name="edit-income"),
    path("delete/<int:pk>/", delete_income, name="delete-income"),

]
