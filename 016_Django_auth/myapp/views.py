from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    if request.user.id is None:
        return render(request,"index.html")
    else : 

        return redirect("home")

def reg(request):
    return render(request,"reg.html")

def adduser(request):

    try :
        if request.method=='POST':
            data = request.POST
            fname = data.get('fname')
            lname = data.get('lname')
            uname = data.get('uname')
            password = data.get("pass")

            if User.objects.filter(username=uname).exists():
                messages.add_message(request, messages.ERROR, "Username Already Exist !!!!")
                return render(request,'reg.html')

            user = User(first_name=fname,last_name=lname,username=uname)
            user.set_password(password)
            user.save()

            messages.add_message(request, messages.SUCCESS, "Registration successfully")
            return render(request,'reg.html')

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something Went Wrong !!!")
        return render(request,'reg.html')

def loginuser(request):
     try :
        if request.method=='POST':
                data = request.POST
                uname = data.get('uname')
                password = data.get("pass")

                user = authenticate(username=uname,password=password)

                if user is not None:
                    login(request,user)
                    return redirect("home")
                else:
                    messages.add_message(request, messages.ERROR, "Invalid credentals !!!")
                    return render(request,'index.html')
     except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR, "Something Went Wrong !!!")
        return render(request,'index.html')

@login_required(login_url="index")
def home(request):

    return render(request,"home.html")


@login_required
def userlogout(request):
    logout(request)
    return render(request,"index.html")