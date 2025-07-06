from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_dashboard),  # redirection par défaut
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('utilisateurs/', views.utilisateur_view, name='utilisateurs'),
]