from django.urls import path
from . import views

urlpatterns = [
    path('404-error/', views.error, name='error'),
]