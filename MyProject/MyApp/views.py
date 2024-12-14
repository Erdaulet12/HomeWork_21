from django.shortcuts import render, redirect
from .forms import IceCreamForm

# Create your views here.


def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = IceCreamForm()
    return render(request, 'ice_cream/create_ice_cream.html', {'form': form})
