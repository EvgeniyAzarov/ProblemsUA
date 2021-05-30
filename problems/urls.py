from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('problem/<int:problem_id>', views.problem, name="problem"),
    path('problems/', views.problems_list, name="problems_list"),
    path('compile-paper/', views.compile_paper, name="compile paper"),
]
