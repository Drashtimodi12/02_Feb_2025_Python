from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from myapp.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import razorpay
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    """
    Render the home page.
    """
    
    return render(request, "index.html")

def accounts(request):
    """
    Render the accounts page.
    """
    if request.user.is_authenticated:
        user = request.user
        orders = Order.objects.filter(user=user)

    return render(request, "accounts.html",{"orders":orders})

@login_required(login_url="login-register")
def cart(request):
    """
    Render the cart page.
    """
    cart = Cart.objects.filter(user=request.user)

    total=0
    for i in cart:
        total += i.product.price*i.quantity


    return render(request, "cart.html",{"carts":cart,"total":total})



def checkout(request):
    """
    Render the checkout page.
    """
    return render(request, "checkout.html")
def details(request):
    """Render the details page.
    """
    return render(request, "details.html")

def login_register(request):
    """
    Render the login/register page.
    """ 
    return render(request, "login-register.html")

def shop(request):
    """
    Render the shop page.
    """
    return render(request, "shop.html")


def register_user(request):
    """
    Handle user registration.
    """
    try :
        if request.method == "POST":
            # Handle registration logic here
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if username and email and password:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return render(request, "login-register.html", {"msg": "Registration successfully completed. You can now log in."})
            else:
                return render(request, "login-register.html", {"msg": "All fields are required."})
    except Exception as e:
        return render(request, "login-register.html", {"msg": f"An error occurred: {str(e)}"})
    

def login_user(request):
    """
    Handle user login.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login-register.html", {"msg": "Invalid credentials. Please try again."})
    return render(request, "login-register.html")


def logout_user(request):
    """
    Handle user logout.
    """
    logout(request)
    return render(request, "login-register.html", {"msg": "You have been logged out successfully."})



def categories(request):
    """
    Render the categories page.
    """
    # You can fetch categories from the database if needed
    categories = Category.objects.all()
    
    return JsonResponse({'categories': list(categories.values())},)


def products(request):
    """
    Render the products page.
    """
    # You can fetch products from the database if needed
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())},)


def addtocart(request):
        
        try :
            pid = request.GET['pid']
            user = request.user
            

            if user.is_anonymous:
                return HttpResponse(user)
            else : 
                
                product = Product.objects.get(pk=pid)

                isExist =   Cart.objects.filter(user=user,product=product).exists()

                if not isExist:
                    cart =  Cart.objects.create(user=user,product=product)
                    if cart:
                        return HttpResponse("Product added into the cart !")
                else:
                    return HttpResponse("Product already exist !!!")

        except Exception as e :
            print(e)

def deletecart(request):
    cid = request.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Item removed from cart")

def changeqty(request):
    qty = request.GET['qty']
    cid = request.GET['cid']

    cart = Cart.objects.get(pk=cid)
    cart.quantity=qty
    cart.save()
    return HttpResponse("Qty changed...")


def payment(request):

    # Initialize Razorpay client with your API key and secret
    amount = float(request.GET.get('amount') ) # Default amount is 500 if not provided
    client = razorpay.Client(auth=("rzp_test_oox9ZKsz6Uu09W", "1umN06wc9ZHC2blBvuR41bN9"))
    data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
   
    return JsonResponse(payment)  # This will return the payment order details as a response


def order(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    
    if not cart_items:
        return HttpResponse("Your cart is empty.")

    total_price = sum(item.total_price() for item in cart_items)
    
    order = Order.objects.create(user=user, total_price=total_price)
    
    msg="<table border='1'>"
    msg+="<tr><th>Product</th><th>Quantity</th><th>Price</th></tr>"
    for item in cart_items:
        msg += f"<tr><td>{item.product.name}</td><td>{item.quantity}</td><td>{item.total_price()}</td></tr>"
    
    msg += f"<tr><td colspan='2'>Total Price</td><td>{total_price}</td></tr></table>"

    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        item.delete()  # Remove the item from the cart after creating the order


    send_mail(
    subject='Order Confirmation',
    message='Order placed successfully',  # Plain text version
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=['chintan.tops@gmail.com'],
    html_message=msg,  # HTML version
    fail_silently=False,
)


    return HttpResponse(f"Order placed successfully! Total price: {total_price}")