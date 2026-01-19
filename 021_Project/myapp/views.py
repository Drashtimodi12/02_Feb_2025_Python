from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
import razorpay
from django.http import JsonResponse


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff

class CategoryAPIView(APIView):

    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(),IsStaffUser()]
        return [AllowAny()]

    """
    API view for handling category-related operations.
    """
    def post(self, request):
        """
        Handle POST requests to create a new category.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request, pk=0):
        """
        Handle GET requests to retrieve a specific category by ID.
        """
        print(pk)
        try:
            if pk == 0:
                categories = Category.objects.all()
                serializer = CategorySerializer(categories, many=True)
                return Response(serializer.data)
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing category.
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a category.
        """
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({'message': 'Category deleted successfully'}, status=204)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
class ProductAPIView(APIView):

    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(),IsStaffUser()]
        return [AllowAny()]

    """
    API view for handling product-related operations.
    """
    def post(self, request):
        """
        Handle POST requests to create a new product.
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request, pk=0):
        """
        Handle GET requests to retrieve a specific product by ID.
        """
        try:
            if pk == 0:
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data)
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing product.
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a product.
        """
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=204)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        
class ProductByCategoryAPIView(APIView):
    """
    API view for retrieving products by category.
    """
    def get(self, request, category_id):
        """
        Handle GET requests to retrieve products by category ID.
        """
        try:
            products = Product.objects.filter(category_id=category_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
class ProductSearchAPIView(APIView):
    """
    API view for searching products by name.
    """ 
    def get(self, request):
        """
        Handle GET requests to search products by name.
        """
        query = request.query_params.get('q', '')
        if query:
            products = Product.objects.filter(name__startswith=query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        return Response({'error': 'No search query provided'}, status=400)
    
class UserRegistrationAPIView(APIView):
    """
    API view for user registration.
    """
    def post(self, request):
        """
        Handle POST requests to register a new user.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully', 'user_id': user.id}, status=201)
        return Response(serializer.errors, status=400)
    

class CartAPIView(APIView):
    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE','GET']:
            return [IsAuthenticated()]
        

    """
    API view for handling cart-related operations.
    """
    def post(self, request):
        """
        Handle POST requests to add a product to the cart.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        # Ensure product with the given ID exists
        product_id = request.data.get('product')
        isExist = Cart.objects.filter(product_id=product_id,user_id=user.id).exists()
        if isExist:
            return Response({'error': 'Product already exists in cart'}, status=400)
        request.data['user'] = user.id
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        """
        Handle GET requests to retrieve the user's cart.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        try:
            
            cart_items = Cart.objects.filter(user=user)
            serializer = CartSerializer(cart_items, many=True)
            return Response(serializer.data)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=404)
        
    def delete(self, request, pk):
        """
        Handle DELETE requests to remove a product from the cart.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        try:
            cart_item = Cart.objects.get(pk=pk, user=user)
            cart_item.delete()
            return Response({'message': 'Cart item deleted successfully'}, status=204)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=404)
        

class ChangeQtyAPIView(APIView):
    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['PUT']:
            return [IsAuthenticated()]
        return [AllowAny()]

    """
    API view for changing the quantity of a product in the cart.
    """
    def put(self, request, pk):
        """
        Handle PUT requests to change the quantity of a cart item.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        try:
            cart_item = Cart.objects.get(pk=pk, user=user)

            request.data['quantity'] = cart_item.quantity+ request.data['quantity']   # Default to current quantity if not provided
            if request.data['quantity'] < 1:
                cart_item.delete()
                return Response({'error': 'Quantity must be at least 1'}, status=400)
           
            serializer = CartSerializer(cart_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=404)
        

def payment(request):



    authentication_classes = [JWTAuthentication]


    # Initialize Razorpay client with your API key and secret
    amount = int(request.GET.get('amount') ) # Default amount is 500 if not provided
    client = razorpay.Client(auth=("rzp_test_oox9ZKsz6Uu09W", "1umN06wc9ZHC2blBvuR41bN9"))
    data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    return JsonResponse(payment, safe=False)


class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    """
    API view for handling order-related operations.
    """
    def post(self, request):
        
        #create order from current cart cart items and current user
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        cart_items = Cart.objects.filter(user=user)
        if not cart_items.exists():
            return Response({'error': 'Cart is empty'}, status=400)
        
        total_price = sum(item.product.price * item.quantity for item in cart_items)



        request.data['user'] = user.id
        request.data['total_price'] = total_price


        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Create OrderItems for each cart item
            order = serializer.instance
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            # Clear the cart after order creation
            cart_items.delete()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    def get(self, request):
        """
        Handle GET requests to retrieve all orders for the authenticated user.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        orders = Order.objects.filter(user=user).prefetch_related("items")

        if not orders.exists():
            return Response({'message': 'No orders found'}, status=404)

        # order with orderitems

        serializer = OrderSerializer(orders , many=True)
        return Response(serializer.data)
  