from django.shortcuts import render, redirect
from general.models import TeslimationPost, EmailAdressFrom
from faq.models import FaqPost, FaqFormEntry
from faq.forms import FaqForm
from general.forms import EmailForm
# Create your views here.

def faq(request):
    faqpost = FaqPost.objects.all()
    teslimation = TeslimationPost.objects.all()
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('faq') 
            
    else:
        form = FaqForm()

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('faq') 
    else:
        form = EmailForm()
    context = {
        'title': 'F.A.Q',
        'teslimation': teslimation,
        'faqpost': faqpost,
        'form': form,
        'form': form,

    }
    return render(request, 'faq.html', context=context)