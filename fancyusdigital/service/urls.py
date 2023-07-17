from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('service-detail/<int:pk>/', views.services_detail, name='service-detail'),

]