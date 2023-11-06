from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': "Username already exists"}, status = 400)
        else:
            user = User.objects.create_user(username, email, password)
            return JsonResponse({'message': 'User created sucessfully'})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'logged in sucessfully'})
        else:
            return JsonResponse({'message':'login failed'}, status=400)
        
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message':'logout successfull'})
# Create your views here.
