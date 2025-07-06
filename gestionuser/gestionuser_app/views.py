from django.shortcuts import render
from django.shortcuts import redirect
def home(request):
    return render(request, 'gestionuser_app/base.html')
def dashboard_view(request):
    return render(request, 'gestionuser_app/dashboard.html')

def utilisateur_view(request):
    return render(request, 'gestionuser_app/utilisateur.html')
def redirect_to_dashboard(request):
    return redirect('dashboard')  # 'dashboard' = nom donné à ta route