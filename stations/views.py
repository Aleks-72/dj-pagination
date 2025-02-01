from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

with open(settings.BUS_STATION_CSV, newline = '', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    TABLE = [row for row in reader]

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    try:
        page_num = int(request.GET.get('page', 1))
    except:
        page_num = 1
    paginator = Paginator(TABLE, 10)
    page = paginator.get_page(page_num)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
