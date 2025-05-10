from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('departments/biology', views.biology, name='biology'),
    path('departments/departments', views.departments, name='departments'),
    path('departments/cs', views.cs, name='cs'),
    path('departments/history', views.history, name='history'),
    path('departments/home', views.home, name='home'),
    path('home/departments', views.departments, name='departments'),
]
