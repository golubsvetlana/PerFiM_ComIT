from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('expenses/', include('expenses.urls')),
    path('income/', include('income.urls')),
]
