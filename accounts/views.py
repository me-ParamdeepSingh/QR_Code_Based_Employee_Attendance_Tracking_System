from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def login_page(request):
    return render(request,'accounts/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_data = User.objects.get(username==username)

        if user_data:
            if user_data.username == username:
                if user_data.password == password:
                    return render(request, 'index.html',{"user": user_data})
                else:
                    return redirect
        
def logout(request):
    logout(request)
    return redirect('login')
        
