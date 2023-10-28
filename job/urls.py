from django.contrib import admin
from django.urls import path
from job import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applicant/create/', views.create_applicant, name='create_applicant'),
    path('applicant/update/<int:pk>/', views.update_applicant, name='update_applicant'),
    path('applicant/delete/<int:pk>/', views.delete_applicant, name='delete_applicant'),
    path('reset-database/', views.reset_database, name='reset_database'),
]
