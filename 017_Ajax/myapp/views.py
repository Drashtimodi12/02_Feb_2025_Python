from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


def search(request):
    data =  request.GET['data']
    # rows = ""
    # if data=="sports":
    #     rows+="<ul><li>BAT</li><li>Ball</li><li>VollyBall</li></ul>"
    # elif data=="electric":
    #     rows+="<ul><li>Fan</li><li>TV</li><li>Laptop</li></ul>"

    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"data":list(products.values())})


def countries(request):
    allcountries = Country.objects.all()
    return JsonResponse({"data":list(allcountries.values())})

def states(request):
    cid = request.GET['cid']
    allstates = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(allstates.values())})

def cities(request):
    sid = request.GET['sid']
    allCity = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(allCity.values())})