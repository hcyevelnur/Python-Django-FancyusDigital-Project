from django.shortcuts import render, render,get_object_or_404
from .models import ServicePost

# Create your views here.


def services(request):
    services = ServicePost.objects.all()
    context = {
        'title': 'Services',
        'services': services

    }
    return render(request, 'services.html', context=context)


def services_detail(request, pk):
    service = get_object_or_404(ServicePost, pk=pk)
    title = service.title
    return render(request, 'service-detail.html', {'service': service, 'title': title})