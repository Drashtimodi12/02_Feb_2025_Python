from django.shortcuts import render
from library.models import *
from library.serializer import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class AuthorAPI(APIView):
    
    def get(self, request):
        try:
            allAuthors = Author.objects.all()
            ser = AuthorSerializer(allAuthors,many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
    
    def post(self,request):
        try:
            ser = AuthorSerializer(data = request.data)
            if not ser.is_valid():
                return Response({"Errors":ser.errors})
            ser.save()
            return Response({"data":ser.data,"message":"Author inserted successfully"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})


class AuthorAPIById(APIView):
    
    def get(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            ser = AuthorSerializer(author)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})

    def patch(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            ser = AuthorSerializer(author,request.data,partial=True)
            if not ser.is_valid():
                return Response({"errors":ser.errors})
            ser.save()
            return Response({"data":ser.data,"message":"Autor updated successfully !!!"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
        
    def delete(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
            return Response({"message":"author deleted successfully !!!"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
        
class PublicationAPI(APIView):
    
    def get(self, request):
        try:
            allPublications = Publication.objects.all()
            ser = PublicationSerializer(allPublications,many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
    
    def post(self,request):
        try:
            ser = PublicationSerializer(data = request.data)
            if not ser.is_valid():
                return Response({"Errors":ser.errors})
            ser.save()
            return Response({"data":ser.data,"message":"Publication inserted successfully"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
 
class PublicationAPIById(APIView):
    
    def get(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            ser = PublicationSerializer(publication)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})

    def patch(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            ser = PublicationSerializer(publication,request.data,partial=True)
            if not ser.is_valid():
                return Response({"errors":ser.errors})
            ser.save()
            return Response({"data":ser.data,"message":"Publication updated successfully !!!"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
        
    def delete(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            publication.delete()
            return Response({"message":"Publication deleted successfully !!!"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
        

@api_view(['GET'])
def bookList(request):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    try:
        allBooks = Book.objects.all()
        ser = BookSerializer(allBooks,many=True)
        return Response({"books":ser.data})
    except Exception as e:
        print(e)
        return Response({"message":"Something went wrong !!!"})
    
@api_view(['POST'])
def bookCreate(request,aid,pid):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    try:
        author = Author.objects.get(pk=aid)
        publication = Publication.objects.get(pk=pid)
        data = request.data
        data['author'] = author.id
        data['publication'] = publication.id
        ser = BookSerializer(data=data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        ser.save()
        return Response({"data":ser.data,"message":"Book created successfully !!!"})
    except Exception as e:
        print(e)
        return Response({"message":"Something went wrong !!!"})
    

@api_view(['PATCH'])
def bookUpdate(request,aid,pid,id):
    try:
        author = Author.objects.get(pk=aid)
        publication = Publication.objects.get(pk=pid)
        book = Book.objects.get(pk=id)
        data = request.data
        data['author'] = author.id
        data['publication'] = publication.id
        ser = BookSerializer(book,data=data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        ser.save()
        return Response({"data":ser.data,"message":"Book updated successfully !!!"})
    except Exception as e:
        print(e)
        return Response({"message":"Something went wrong !!!"})
    
class BookAPIById(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            ser = BookSerializer(book)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
        
    def delete(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return Response({"message":"Book deleted successfully !!!"})
        except Exception as e:
            return Response({"message":"Something went wrong !!!"})
        
@api_view(['GET'])
def bookByAuthor(request,aid):
    try:
        author = Author.objects.get(pk=aid)
        books = Book.objects.filter(author=author)
        ser = BookSerializer(books,many=True)
        return Response({"data":ser.data})
    except Exception as e:
        return Response({"message":"Something went wrong !!!"})
    
@api_view(['GET'])
def bookByPublication(request,pid):
    try:
        publication = Publication.objects.get(pk=pid)
        books = Book.objects.filter(publication=publication)
        ser = BookSerializer(books,many=True)
        return Response({"data":ser.data})
    except Exception as e:
        return Response({"message":"Something went wrong !!!"})
    

