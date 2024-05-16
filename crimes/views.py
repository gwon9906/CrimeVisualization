from django.shortcuts import render
from .models import Crime
from collections import Counter


def crime_chart(request):
    data = Crime.objects.all()
    categories = Counter([crime.category for crime in data])
    categories = sorted(categories.items())
    return render(request, 'crimes/chart.html', {'categories': categories})
