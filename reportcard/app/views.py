from django.shortcuts import render,redirect
from app.models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def index(request):
    allStudent = Student.objects.all()
    paginator = Paginator(allStudent, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_obj})

def marksheet(request):
    id = int(request.GET['id'])
    allstudents =  Marks.objects.filter(student_id=id)
   
    sum =  allstudents.aggregate(total = Sum("marks"))

    # for st in allstudents:
    #     sum+=st.marks
    
    rankstduents = Student.objects.annotate(total=Sum("marks__marks")).order_by("-total")
    count = 0
    for ranks in rankstduents:
        count+=1
        if ranks.id==id : 
            break;
            

    return render(request,"marksheet.html",{"students":allstudents,"sum":sum,"count":count})

def sendmail(request):
    id = int(request.GET['id'])

    allstudents =  Marks.objects.filter(student_id=id)
    

    sum =  allstudents.aggregate(total = Sum("marks"))

    # for st in allstudents:
    #     sum+=st.marks
    
    rankstduents = Student.objects.annotate(total=Sum("marks__marks")).order_by("-total")
    count = 0
    for ranks in rankstduents:
        count+=1
        if ranks.id==id : 
            break;
    

    subject = "Marskheet Details"
    from_email = settings.EMAIL_HOST_USER
    to_email = [allstudents[0].student.email]

    
    html_content = render_to_string("marksheet.html",{"students":allstudents,"sum":sum,"count":count})

    email = EmailMultiAlternatives(subject, '', from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return redirect("index")

