from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Portfolio
# Create your views here.
@login_required
def create_portfolio(request):
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
        return redirect('portfolio_preview')

    return render(request, 'create_portfolio.html')

@login_required
def preview(request):
    
    portfolio = Portfolio.objects.all()
    print(portfolio,'portfolio')

    return render(request, 'portfolio_preview.html', {'portfolio': portfolio})