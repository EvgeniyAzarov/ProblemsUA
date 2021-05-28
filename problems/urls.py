from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('problems/', views.problems_list, name="problems_list"),
]
