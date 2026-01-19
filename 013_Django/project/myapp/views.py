from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    return render(request,"index.html",{'title':"tops | Index"})

def about(request):
    return render(request,"about.html",{'title':"tops | About"})

def contact(request):
    return render(request,"contact.html",{'title':"tops | Contact"})