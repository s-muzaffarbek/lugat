from django.shortcuts import render
from .models import Lugat

def home(request):
    soz = request.GET.get('text', '')
    if soz in soz!= '':
        natija = Lugat.objects.filter(inglizcha__contains=soz).all()[:3]
    else:
        natija = None
    context = {
        'text': soz,
        'natija': natija,
    }
    return render(request, 'index.html', context)