from django.shortcuts import render
from  first_app.forms import LoginForm
from first_app.models import MyModel

# Create your views here.
# def home(request):
#     return render(request,'first_app/home.html')

# def login(request):
#     contract=LoginForm()
#     return render(request,'first_app/home.html',{'form':contract})


def login(request):
    contract=MyModel
    return render(request,'first_app/home.html',{'form':contract})
