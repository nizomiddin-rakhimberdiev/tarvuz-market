from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser

# Create your views here.
def create_or_login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        user = authenticate(username=phone_number)
        if user:
            login(request, user)
            return redirect('home')
        else:
            user = CustomUser.objects.create_user(username=phone_number, phone_number=phone_number)
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')