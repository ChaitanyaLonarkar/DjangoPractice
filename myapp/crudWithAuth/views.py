from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.
def Register(request):
    # print(form,'form')

    if request.method == 'POST':
        form = UserCreationForm( request.POST)  
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username,password,'username,password')
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm( request.POST)  

    return render(request,'register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, f'Welcome {username}!')
        return redirect('home')
    return render(request,'login.html')

def Home(request):
    return render(request,'home.html')

def Logout(request):
   
    logout(request)
    return redirect('login')

