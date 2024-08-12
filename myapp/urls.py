from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/update/<uuid:pk>/', views.subject_update, name='subject_update'),
    path('subjects/delete/<uuid:pk>/', views.subject_delete, name='subject_delete'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<uuid:pk>/', views.student_update, name='student_update'),
    path('students/delete/<uuid:pk>/', views.student_delete, name='student_delete'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<uuid:pk>/', views.teacher_update, name='teacher_update'),
    path('teachers/delete/<uuid:pk>/', views.teacher_delete, name='teacher_delete'),
    
]