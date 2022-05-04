from django.shortcuts import render
from .models import Fads, Decades

# Create your views here.
def fad_list(request):
    fads = Fads.objects.all()
    return render(request, 'nostald/fad_list.html', {'fads': fads})

def decade_list(request):
    decades = Decades.objects.all()
    return render(request, 'nostald/decades_list.html', {'decades': decades})

def fad_detail(request, pk):
    fad = Fads.objects.get(id=pk)
    return render(request, 'nostald/fad_detail.html', {'fad': fad})

def decade_detail(request, pk):
    decade = Decades.objects.get(id=pk)
    return render(request, 'nostald/decade_detail.html', {'decade': decade})