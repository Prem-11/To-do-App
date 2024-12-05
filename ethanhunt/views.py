from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserProfile
from rest_framework import viewsets
from .serializers import UserProfileSerializer


# Create your views here.
# from django.http import HttpResponse
def home(request):
    p1=request.user
    todo=UserProfile.objects.all()
    if(request.method=="POST"):
        aid=request.POST.get("agent_id")
        todotitle=request.POST.get("todotitle")
        TODODesc=request.POST.get("TODODesc")
        category=request.POST.get("category")
        date=request.POST.get("date")
        reg=UserProfile(agent_id=aid,TodoTitle=todotitle,TodoDesc=TODODesc,Category=category,DueDate=date)
        reg.save()
        todo=UserProfile.objects.order_by('DueDate').reverse()
        print (todo)
        messages.info(request,"successfully added todo item")
        return render(request,"home.html",{'todo1':todo})
    return render(request,"home.html",{'todo1':todo})

def signup(request):
    if(request.method=="POST"):
        username=request.POST.get("agent_id")
        password=request.POST.get("password")
        password1=request.POST.get("password1")
        def password_check(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 6') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 8') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            if val == False: 
                val=True
                return val
        if (password_check(password)): 
            print("y")
        else: 
            print("x")
        #print(password)                    
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif (password_check(password)):
                    messages.info(request,'password is not valid')
                    print("pooja")
                    return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request,"'Status':'account Created'\n 'status_code':'200'")
        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('login')
    return render(request,"signup.html")

def login(request):
    if(request.method=="POST"):
        aid=request.POST.get("agent_id")
        pswd=request.POST.get("password")
        user=auth.authenticate(username=aid,password=pswd)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"'Status':'Success'\n 'status_code':'200' \n 'Agent_id':" + aid)
            return redirect("/")   
        else:
            messages.info(request,"'Status':'Failure'\n 'status_code':'401'")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return render(request,"home.html")

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all().order_by('DueDate').reverse()
    serializer_class=UserProfileSerializer