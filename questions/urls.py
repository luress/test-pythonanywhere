from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.question_list, name='qlist'),
    path('question/<slug:slug>', views.question_details, name='qdetails'),
    path('register/', views.register, name='register'),
    path('add/', views.create_question, name='create_question'),
    path('update/<slug:slug>', views.update_question, name='update_question'),
    path('delete/<slug:slug>', views.delete_question, name='delete_question'),
    path('answer/update/<int:id>', views.update_answer, name='update_answer'),
    path('answer/delete/<int:id>', views.delete_answer, name='delete_answer'),
    path('profile/', views.change_profile, name='profile'),
    path('list/', views.list_info, name='list')
]
