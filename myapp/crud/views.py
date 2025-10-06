from django.shortcuts import render

from .models import User
# Create your views here.
def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile= request.POST.get('mobile')
        age= request.POST.get('age')
        # Here, you would typically save the user to the database
        # For simplicity, we'll just render a success message

        # Create a new User object
        user = User(name=name, email=email, mobile=mobile, age=age)
        user.save()

        return render(request, 'create_user.html', {'message': 'User created successfully!'})
    return render(request, 'create_user.html')

def list_users(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def edit_user(request, user_index):
    user = User.objects.get(index=user_index)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.mobile = request.POST.get('mobile')
        user.age = request.POST.get('age')
        user.save()
        return render(request, 'edit_user.html', {'user': user, 'message': 'User updated successfully!'})
    return render(request, 'edit_user.html', {'user': user})


def delete_user(request, user_email):
    user = User.objects.get(email=user_email)
    user.delete()
    return redirect('list_users')