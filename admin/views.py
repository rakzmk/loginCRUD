from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth



# Create your views here.

def adlogin(request):
    if request.session.has_key("setkey"):
        return redirect (adhome)
        
    else:
        if request.method == 'POST':
            usernamead=request.POST['name2']
            passwordad=request.POST['password2']
            print("heeeelo")
            if  usernamead == "admin" and passwordad =="password":
                request.session ['setkey'] = passwordad
                #return redirect(homepage)
                return JsonResponse('true', safe=False)
            else:
                #return render(request,"index.html")
                return JsonResponse('false', safe=False)
        else:
            return render(request, 'adminlogin.html')
    

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('adminhome')   


def updata_data(request, id):
    if request.session.has_key("setkey"):  
        if request.method == 'POST':
            user = User.objects.get(pk=id)
            user.first_name = request.POST ['name3']
            user.email = request.POST ['email3']
            user.username = request.POST ['username3']
            print ("hello")
            if User.objects.filter(username=user.username).exclude(id=id).exists():
                return JsonResponse('false', safe=False)
            elif User.objects.filter(email=user.email).exclude(id=id).exists():
                return JsonResponse('false1', safe=False)
            else:
                user.save()
                return JsonResponse('true', safe=False) 
        else:
            pi = User.objects.get(pk=id)
            context = {'user':pi}
            return render(request, 'adminedit.html',context)
    else:
        return redirect (adlogin)

def adduser(request):
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
        return render(request,'adminadd.html')

def adhome(request):
    if request.session.has_key("setkey"):
         if 'q' in request.GET:     
            q=request.GET['q']
            if q is not None:
                user = (User.objects.filter(username__icontains=q)) or (User.objects.filter(email__icontains=q)) or (User.objects.filter(first_name__icontains=q))
            else:
                user=User.objects.all()
            return render(request, 'adminhome.html', {'users': user})
         else:
            user = User.objects.all()
            return render(request, 'adminhome.html', {'users': user})

    else:
        return redirect (adlogin)
        #return render(request,"index.html")


def adlogout(request):
    #return render(request, 'adminlogin.html')
    if request.session.has_key("setkey"):
        request.session.flush()
        return redirect(adlogin)