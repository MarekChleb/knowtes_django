from django.urls import path

from . import views

urlpatterns = [
    path('', views.knowte, name='knowte'),
    path('<int:=id>/', views.knowte, name='knowte_element'),
]