from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse
import requests
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')


def payment(request):

    # Initialize Razorpay client with your API key and secret
    amount = int(request.GET.get('amount') ) # Default amount is 500 if not provided
    client = razorpay.Client(auth=("rzp_test_oox9ZKsz6Uu09W", "1umN06wc9ZHC2blBvuR41bN9"))
    data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    print(payment)
    return JsonResponse(payment)  # This will return the payment order details as a response

def message(request):
   
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"WXfAe5cjnlMG0thTkdLD9IsgRyZbS7w41UzP3H8mKiqQNVEova9vDJtywEXpMNoUieOfPlq1r8HhdnTL","variables_values":"5599","route":"otp","numbers":"9979492057"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def send_mail_page(request):
        context = {}
   
        address = request.GET.get('address')
        subject = request.GET.get('subject')
        message = request.GET.get('message')

       
        # address = "chintan.tops@gmail.com",
        # subject = "Test Email from Django"
        # message = "This is a test email sent from Django application."
 
        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
        return HttpResponse(context['result'])