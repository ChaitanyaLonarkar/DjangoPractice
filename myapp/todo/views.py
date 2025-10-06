from django.shortcuts import render, redirect
from . import views
# Create your views here.

def index(request):    
    sum_value = 0
    print(request.method)
    if request.method == "POST":
        num_1 = request.POST.get("num1")
        num_2 = request.POST.get("num2")
        sum_value = int(num_1) + int(num_2)
        return render(request, 'result.html',{'result':sum_value})
    print("this os",sum_value)
    return render(request,'index.html',{'result':sum_value})
def result(request):
    return render(request,'index.html',)