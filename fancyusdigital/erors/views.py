from django.shortcuts import render

# Create your views here.

def error(request):
    context = {
        'title': '404 Not Found',

    }
    return render(request, '404-error.html', context=context)