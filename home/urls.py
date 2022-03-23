from django.urls import path
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
   path('student_view/',StudentView.as_view(),name='student_view'),
   path('register/', Register.as_view(), name='register'),

   path('',home,name='home'),
   path('student_post/', student_post, name='student_post'),
   path('student_update/<str:pk>/', student_update, name='student_update'),
   path('student_delete/<str:pk>/', student_delete, name='student_delete'),
   path ('get_book/',Get_Book,name='get_book'),
   path('api-token-auth/', views.obtain_auth_token),

]

