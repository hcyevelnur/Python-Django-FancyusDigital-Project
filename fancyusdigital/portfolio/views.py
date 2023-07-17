from django.shortcuts import render, get_object_or_404
from .models import Portifolio

# Create your views here.

def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portifolio, pk=pk)
    title = portfolio.title

    return render(request, 'portfolio-detail.html', {'portfolio': portfolio, 'title': title})


def portfolio(request):
    portfolios = Portifolio.objects.all()
    context = {
        'title': 'Portfolio',
        'portfolios': portfolios

    }
    return render(request, 'portfolio.html', context=context)