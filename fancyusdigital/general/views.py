from django.shortcuts import render ,get_object_or_404
from service.models import ServicePost
from portfolio.models import Portifolio
from team.models import TeamPost
from general.models import TeslimationPost
from django.shortcuts import render, redirect
from .models import ContactFormEntry
from .forms import ContactForm, EmailForm
 

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index') 
    else:
        form = ContactForm()

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index') 
    else:
        form = EmailForm()

    teams = TeamPost.objects.all()
    portfolios = Portifolio.objects.all()
    services = ServicePost.objects.all()
    teslimation = TeslimationPost.objects.all()

    context = {
        'title': 'Welcome to Fancyus Digital!',
        'services': services,
        'portfolios': portfolios,
        'teams': teams,
        'teslimation': teslimation,
        'form':form,
    }
    return render(request, 'index.html', context=context)


def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portifolio, pk=pk)
    title = portfolio.title

    return render(request, 'portfolio-detail.html', {'portfolio': portfolio, 'title': title})


def about_us(request):
    context = {
        'title': 'About Us',

    }
    return render(request, 'about-us.html', context=context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    
    title = 'Contact Us'
    
    return render(request, 'contact-us.html', {'form': form, 'title': title})



def services_detail(request, pk):
    service = get_object_or_404(ServicePost, pk=pk)
    title = service.title
    return render(request, 'service-detail.html', {'service': service, 'title': title})


def team_detail(request, pk):
    team = get_object_or_404(TeamPost, pk=pk)
    name = team.name
    return render(request, 'team-detail.html', {'team': team, 'name': name})
