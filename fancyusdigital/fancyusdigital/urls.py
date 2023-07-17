"""fancyusdigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from general import views
from django.conf  import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('c162b4871x7F16vAc6cN1b7C4b6Y18U724S61D8cI7bG41IcbT-AdminL/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('blog.urls')),
    path('', include('erors.urls')),
    path('', include('faq.urls')),
    path('', include('portfolio.urls')),
    path('', include('pricing.urls')),
    path('', include('service.urls')),
    path('', include('team.urls')),
    path('', include('general.urls')),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
