from rest_framework import serializers
from library.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        # depth = 1  # This allows nested serialization for related fields

    def validate(self, attrs):
        if attrs['qty'] < 0:
            raise serializers.ValidationError("Quantity cannot be negtive.")
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = AuthorSerializer(instance.author).data
        representation['publication'] = PublicationSerializer(instance.publication).data
        return representation