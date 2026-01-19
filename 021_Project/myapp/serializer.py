from rest_framework import serializers
from myapp.models import *
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    class Meta:
        model = User
        fields ='__all__'
        

    def create(self, validated_data):
        """
        Create a new user instance with the provided validated data.
        """
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
         # Automatically set the is_active field to True for new users
        return user
    



class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = '__all__'
        # Make category read-only to prevent modification through this serializer

    def to_representation(self, instance):
        """
        Customize the representation of the Product model to include category details.
        """
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation
    
class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.
    """
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize the representation of the Cart model to include product details.
        """
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        
        return representation

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'created_at']

    def to_representation(self, instance):
        """
        Customize the representation of the Order model to include product details.
        """
        representation = super().to_representation(instance)
        representation['user'] = UserRegistrationSerializer(instance.user).data
        return representation
    
class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.
    """
    class Meta:
        model = OrderItem
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize the representation of the OrderItem model to include product details.
        """
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        representation['order'] = OrderSerializer(instance.order).data
        return representation