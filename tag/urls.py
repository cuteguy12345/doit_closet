from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.best_detail),
    path('main/', views.best_list),
    
]