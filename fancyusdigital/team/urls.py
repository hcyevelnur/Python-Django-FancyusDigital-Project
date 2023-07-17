from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team, name='team'),
    path('team-detail/<int:pk>/', views.team_detail, name='team-detail'),

]