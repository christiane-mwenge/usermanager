from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    return render(request, 'gestionuser_app/base.html')
@login_required(login_url='/login/')
def dashboard_view(request):
    return render(request, 'gestionuser_app/dashboard.html')

@login_required(login_url='/login/')
def utilisateur_view(request):
    return render(request, 'gestionuser_app/utilisateur.html')
def redirect_to_dashboard(request):
    return redirect('dashboard')  # 'dashboard' = nom donné à ta route

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # ou une autre vue
        else:
            return render(request, 'gestionuser_app/login.html', {'error': 'Identifiants invalides'})
    return render(request, 'gestionuser_app/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')