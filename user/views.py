from django.shortcuts import render
from .models import FoodIteams,ChefDetails
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    context={}
    data=FoodIteams.objects.all()
    chefs=ChefDetails.objects.all()
    context['data']=data
    context['chefs']=chefs
    return render(request,'index.html',context)

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password_confirm=request.POST['password_confirm']
        if password==password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
                return redirect('/registration/')
            elif User.objects.filter(first_name=first_name).exists():
                messages.error(request,'first_name already exist')
                return redirect('/registration/')
            elif User.objects.filter(last_name=last_name).exists():
                messages.error(request,'last_name already exist')
                return redirect('/registration/')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exist')
                return redirect('/registration/')
            else:
                user=User.objects.create_user(password=password,username=username,first_name=first_name,last_name=last_name,email=email)
                user.save
                print("User Registered")
        else:
            print("Wrong Password")
            messages.error(request,"Wrong Password")
            return redirect('/registration/')
        return redirect('/')
    return render(request,"registration.html",{})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/homepage/')
        else:
            messages.error(request,'Invalid Credential')
            return redirect('/')
    return render(request,"login.html",{})

def logout(request):
    auth.logout(request)
    return redirect("/")