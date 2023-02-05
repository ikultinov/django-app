import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings




def read_csv():
    name_list = []
    street_list = []
    district_list = []
    bus_stations = {}
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            name_list.append(row['Name'])
            street_list.append(row['Street'])
            district_list.append(row['District'])

        bus_stations.update(Name=name_list)
        bus_stations.update(Street=street_list)
        bus_stations.update(District=district_list)
    return bus_stations


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    read_csv()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 30)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'bus_stations': bus_stations
    }
    return render(request, 'stations/index.html', context)
