from django.shortcuts import render

# Create your views here.


def pricing(request):
    context = {
        'title': 'Pricing',

    }
    return render(request, 'pricing.html', context=context)