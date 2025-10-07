from django.shortcuts import render
from django.shortcuts import redirect

from .models import User

def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile= request.POST.get('mobile')
        age= request.POST.get('age')
       
        user = User(name=name, email=email, mobile=mobile, age=age)
        user.save()
        print('user',user)

        # return render(request, 'create_user.html', {'message': 'User created successfully!'})
        return redirect('list_users')
    return render(request, 'create_user.html')

def list_users(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def edit_user(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.mobile = request.POST.get('mobile')
        user.age = request.POST.get('age')
        user.save()
        print('user',user)
        # return render(request, 'edit_user.html', {'user': user, 'message': 'User updated successfully!'})
        return redirect('list_users')
    print('uservsdf',user.email)
    print(request.method,'request.method')
    return render(request, 'edit_user.html', {'user': user})


def delete_user(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        user.delete()
        print('useer deleted')
        return redirect('list_users')
    return render(request, 'confirm.html', {'user': user})

def view_user(request, id):
    user = User.objects.get(pk=id)
    return render(request, 'view_user.html', {'user': user})