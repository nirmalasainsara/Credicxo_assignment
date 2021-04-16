
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import UserSerializer, RegisterSerializer, TeacherSerializer, StudentSerializer,  AdminSerializer
from rest_framework import status
from .models import Student, Teacher
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view
from django.contrib.admin.views.decorators import staff_member_required



# user signup view
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


    def post(self, request, *args,  **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "message": "User Created Successfully.",
        })


# Admin added users and create list every user in the database
class AdminApi(generics.GenericAPIView):
    def get_serializer_class(self):
        if self.request.query_params.get("type") == "student":
            return TeacherSerializer
        return AdminSerializer

    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        t_serializer = AdminSerializer(teachers, many=True)
        students = Student.objects.all()
        s_serializer = TeacherSerializer(students, many=True)
        response = {
            "teachers": t_serializer.data,
            "students": s_serializer.data,
        }
        return Response(response)


    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object = serializer.save()
        return Response({
            "object":self.get_serializer(object).data,
            "message": "object added Successfully.",
        })




# Teacher added students and create list of students.
class TeacherApi(generics.GenericAPIView):
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = TeacherSerializer(students, many=True)
        return Response(serializer.data)


    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response({
            "student": TeacherSerializer(student).data,
            "message": "student added Successfully.",
        })


# Students see his information 
class StudentApi(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    lookup_url_kwarg="stu_id"
    queryset = Student.objects.all()



