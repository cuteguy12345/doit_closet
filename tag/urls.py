from django.urls import path, include
from . import views

best_patterns = [
    path('<int:pk>/', views.BestDetail.as_view()),
    path('main/', views.BestList.as_view())
]

urlpatterns = [
    path('best/', include(best_patterns))
]
