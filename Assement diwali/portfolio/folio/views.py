from django.shortcuts import render
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Portfolio

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Exists")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already Exists")
                return redirect('signup')
            else:
                User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name).save()
                return redirect('signin')
        else:
            messages.info(request,"Password should match")
            return redirect('signup')
            
    return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect("signin")
            
    return render(request,"signin.html")

def logout(request):
    auth.logout(request)
    return redirect('home')


def create_profile(request):
    user = request.user
 
    if user is None:
        return redirect('signin')
    
    if Portfolio.objects.filter(user=user).exists():
        return redirect('profile')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        profile= request.FILES.get('profile')
        resume= request.POST.get('resume')
        location= request.POST.get('location')
        linkedin= request.POST.get('linkedin')
        github= request.POST.get('github')
        bio= request.POST.get('bio')
        age= request.POST.get('age')
        degree= request.POST.get('degree')
        college= request.POST.get('college')
        graduation_year= request.POST.get('grad_year')
        company= request.POST.get('company')
        position= request.POST.get('role')
        responsibilities= request.POST.get('experience_desc')
        projects_title= request.POST.get('project_title')
        project_desc= request.POST.get('project_desc')
        skills= request.POST.get('skills')
        project_link= request.POST.get('project_link')
     
        portfolio = Portfolio(
            user=user,
            name=name,
            email=email,
            phone=phone,
            profile=profile,
            resume=resume,
            location=location,
            linkedin=linkedin,
            github=github,
            bio=bio,
            age=age,
            degree=degree,
            college=college,
            graduation_year=graduation_year,
            company=company,
            position=position,
            responsibilities=responsibilities,
            projects_title=projects_title,
            project_desc=project_desc,
            project_link=project_link,
            skills=skills
        )
        portfolio.save()
        return redirect('profile')

    return render(request, 'profile_form.html')

# @login_required
def profile(request):
    portfolio = Portfolio.objects.all()
    print(portfolio,'===================')
    
    

    # print(name,'+++++++++++++++')


    return render(request, 'profile.html', {'user': portfolio})