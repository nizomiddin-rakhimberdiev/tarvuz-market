from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

# Create your views here.
def create_or_login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = "1234567890"
        user = authenticate(username=phone_number, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            user = CustomUser.objects.create_user(username=phone_number, phone_number=phone_number, password=password)
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return