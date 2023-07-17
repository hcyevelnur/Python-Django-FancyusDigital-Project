from django.shortcuts import render

# Create your views here.

def blog(request):
    context = {
        'title': 'Blog',

    }
    return render(request, 'blog-grid.html', context=context)

def blog_details(request):
    context = {
        'title': 'Blog Details',

    }
    return render(request, 'blog-detail.html', context=context)