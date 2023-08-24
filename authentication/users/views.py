from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def Homepage(request):
    return render(request, 'home.html')


def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'login.html')


def SignUppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Both the passwords are different")
        else:
            my_user = User.objects.create_user(uname, email, password1)
            my_user.save()
        # return HttpResponse("User has been created successfully")
            return redirect('login')

        print(uname, email, password1, password2)
    return render(request, 'signup.html')


def Logoutpage(request):
    logout(request)
    return redirect('login')
