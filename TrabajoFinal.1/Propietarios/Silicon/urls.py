from django.urls import path
from . import views

urlpatterns = [
    path('avances/', views.avance_list, name='avance_list'),
    path('avances/<int:pk>/', views.avance_detail, name='avance_detail'),
    path('avances/new/', views.avance_create, name='avance_create'),
    path('avances/<int:pk>/delete/', views.avance_delete, name='avance_delete'),
    path('avances/', views.avance_list, name='avance_list'),

]