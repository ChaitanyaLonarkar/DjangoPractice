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
    if request.user.is_authenticated:
        return redirect("profile")
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

@login_required
def signin(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("profile")
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect("signin")
            
    return render(request,"signin.html")

@login_required
def logout(request):
    
    auth.logout(request)
    return redirect('home')

@login_required
def create_profile(request):
    user = request.user
 
    # if user is None:
    #     return redirect('signin')
    
    # if Portfolio.objects.filter(user=user).exists():
    #     return redirect('profile')

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

@login_required
def profile(request):
    # portfolio = Portfolio.objects.filter(user=request.user)
    #  this is working fine to get the data
    # portfolio =Portfolio.objects.all().first()

    # portfolio = Portfolio(user=request.user)
    # for obj in portfolio:
    #     print(obj)

    portfolio = Portfolio.objects.get(user=request.user)

    # print(portfolio.user.name,'===================')
    # print(portfolio,'+++++++++++++++')

    return render(request, 'profile.html', {'user': portfolio})


@login_required
def update_profile(request):
    portfolio = Portfolio.objects.get(user=request.user)
    # print(portfolio,'+++++++++++++++')
    if request.method == 'POST':
        if request.FILES.get('profile'):
            portfolio.profile = request.FILES.get('profile')
        if request.POST.get('name'):
            portfolio.name = request.POST.get('name')
        if request.POST.get('email'):
            portfolio.email = request.POST.get('email')
        if request.POST.get('phone'):
            portfolio.phone = request.POST.get('phone')
        if request.POST.get('resume'):
            portfolio.resume = request.POST.get('resume')
        if request.POST.get('location'):
            portfolio.location = request.POST.get('location')
        if request.POST.get('linkedin'):
            portfolio.linkedin = request.POST.get('linkedin')
        if request.POST.get('github'):
            portfolio.github = request.POST.get('github')    
        if request.POST.get('bio'):
            portfolio.bio = request.POST.get('bio')
        if request.POST.get('age'):
            portfolio.age = request.POST.get('age')
        if request.POST.get('degree'):
            portfolio.degree = request.POST.get('degree')
        if request.POST.get('college'):
            portfolio.college = request.POST.get('college')
        if request.POST.get('grad_year'):
            portfolio.graduation_year = request.POST.get('grad_year')
        if request.POST.get('company'):
            portfolio.company = request.POST.get('company')
        if request.POST.get('role'):
            portfolio.position = request.POST.get('role')
        if request.POST.get('experience_desc'):
            portfolio.responsibilities = request.POST.get('experience_desc')
        if request.POST.get('project_title'):
            portfolio.projects_title = request.POST.get('project_title')
        if request.POST.get('project_desc'):
            portfolio.project_desc = request.POST.get('project_desc')
        if request.POST.get('skills'):
            portfolio.skills = request.POST.get('skills')
        if request.POST.get('project_link'):
            portfolio.project_link = request.POST.get('project_link')
        portfolio.save()
        return redirect('profile')
    return render(request, 'profile_form.html', {'user': portfolio})


@login_required

def resume(request):
    portfolio = Portfolio.objects.get(user=request.user)
    return render(request, 'resume.html', {'user': portfolio})