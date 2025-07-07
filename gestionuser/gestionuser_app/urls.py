from django.urls import path
from . import views
from .views import login_view
from .views import logout_view

urlpatterns = [
    path('', views.redirect_to_dashboard),  # redirection par défaut
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('utilisateurs/', views.utilisateur_view, name='utilisateurs'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]