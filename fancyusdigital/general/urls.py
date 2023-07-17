from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact'),
    path('service-detail/<int:pk>/', views.services_detail, name='service-detail'),
    path('portfolio-detail/<int:pk>/', views.portfolio_detail, name='portfolio-detail'),
    path('team-detail/<int:pk>/', views.team_detail, name='team-detail'),
]