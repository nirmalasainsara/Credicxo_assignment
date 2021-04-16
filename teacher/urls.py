
from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApi, TeacherApi, StudentApi, AdminApi

urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('api/student/',TeacherApi.as_view(), name='student'),
    path('api/student/<int:stu_id>/',StudentApi.as_view(), name='students'),
    path('api/admindata/',AdminApi.as_view(), name='admindata'),
]