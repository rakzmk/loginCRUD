from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request,'login.html')

def login(request):
    if request.user.is_authenticated:
         return redirect(home)
    else:
        if request.method == 'POST':
            username2=request.POST['name2']
            password3=request.POST['password2']
            print("hello")
            #if User.objects.filter(username=username2).exists():
            user = auth.authenticate(username=username2,password=password3)
            if user is not None:
                auth.login(request,user)
                print("hellopu")
                return JsonResponse('true', safe=False)
            else:
                print("hellopi")
                return JsonResponse('false', safe=False)
        else:
            return render(request,"login.html")
        

def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect(login)


def register(request):
    if request.user.is_authenticated:
       return redirect(home)
    else:
        if request.method == 'POST':
            first_name=request.POST['name3']
            #last_name=request.POST['lname3']
            email=request.POST['email3']
            username1=request.POST['username3']
            password1=request.POST['pwd3']
            password2=request.POST['cpwd3']
            if User.objects.filter(username=username1).exists():
                print("username taken")
                return JsonResponse('false', safe=False)
            elif User.objects.filter(email=email).exists():
                print("email taken")
                return JsonResponse('false1', safe=False)

            else:    
                User.objects.create_user(username=username1, password=password1,email=email,first_name=first_name)
                print('user created')
                return JsonResponse('true', safe=False)
        
        else:
            return render(request,'register.html')
    


def logout(request):
    auth.logout(request)
    #if request.session.has_key("setkey"):
        #request.session.flush()
    return redirect(login)
    #return render(request,'login.html')