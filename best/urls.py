from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.BestDetail.as_view()),
    path('', views.BestList.as_view()),
]

