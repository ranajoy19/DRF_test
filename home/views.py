from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Student ,Book
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.




# Class base  APIView

class Register(APIView):


    def post(self,request):
        data=request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response({"status": 403, "errors": serializer.errors, "message": "something went wrong"})
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])

        token_obj, created = Token.objects.get_or_create(user=user)

        return Response({"status": 200, "payload": serializer.data,
                         'Token':str(token_obj),
                         "massage": "your User has been created successfully"})


class StudentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({"status": 200, "message": "This my Django Rest Api", "payload": serializer.data})


    def post(self,request):
        # to get the post data
        data = request.data
        # create a new records
        serializer = StudentSerializer(data=data)
        if not serializer.is_valid():
            return Response({"status": 403, "errors": serializer.errors, "message": "something went wrong"})
        serializer.save()

        return Response({"status": 200, "payload": serializer.data,
                         "massage": "your record has been created successfully"})



    def patch(self,request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            data = request.data

            serializer = StudentSerializer(student_obj, data=data, partial=True)
            if not serializer.is_valid():
                return Response({"status": 403, "errors": serializer.errors, "message": "something went wrong"})
            serializer.save()

            return Response({"status": 200, "payload": serializer.data,
                             "massage": "your record has been Updated successfully"})

        except Exception as e:
            print(e)
            return Response({'status': 404, 'message': 'invalid id'})

    def delete(self,request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({'status': 200, 'message': 'your record has been deleted successfully'})

        except Exception as e:
            print(e)
            return Response({'status': 404, 'message': 'invalid id'})



# Decorator base api_view

@api_view(['Get'])
def home(request):
    student_obj = Student.objects.all()

    serializer = StudentSerializer(student_obj, many=True)
    return Response({"status":200 ,"message":"This my Django Rest Api", "payload":serializer.data})


@api_view(['POST'])
def student_post(request):
    # to get the post data
    data=request.data
    # create a new records
    serializer=StudentSerializer(data=data)
    if not serializer.is_valid():
        return Response({"status": 403, "errors":serializer.errors,"message": "something went wrong"})
    serializer.save()

    return Response({"status":200 , "payload":serializer.data,
                     "massage":"your record has been created successfully"})

@api_view(['PATCH'])
def student_update(request,pk):

    try:
        student_obj=Student.objects.get(id=pk)
        data = request.data

        serializer = StudentSerializer(student_obj,data=data, partial=True)
        if not serializer.is_valid():
            return Response({"status": 403, "errors": serializer.errors, "message": "something went wrong"})
        serializer.save()

        return Response({"status": 200, "payload": serializer.data,
                         "massage": "your record has been Updated successfully"})

    except Exception as e:
        print(e)
        return Response({'status':404,'message':'invalid id'})


@api_view(['DELETE'])
def student_delete(request,pk):
    try:
        student_obj=Student.objects.get(id=pk)
        student_obj.delete()
        return Response({'status':200,'message':'your record has been  deleted successfully'})

    except Exception as e:
        print(e)
        return Response({'status':404,'message':'invalid id'})





@api_view(['GET'])
def Get_Book(request):
    try:
        book_obj = Book.objects.all()
        serializer = BookSerializer(book_obj, many=True)
        return Response({'status': '403', 'payload': serializer.data, 'message': 'This are all the book records'})

    except Exception as e:
        print(e)
        return Response({'status': 404, 'message': 'Something went wrong'})











