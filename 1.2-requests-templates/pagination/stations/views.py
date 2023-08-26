from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv
from pprint import pprint

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    CONTENT = []
    with open(BUS_STATION_CSV, encoding= 'utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            CONTENT += [{'Name':row['Name'],'Street': row['Street'], 'District':row['District']}]

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    #Единственный момент это то что в контекст нужно передавать список станций на странице который хранится в
    #page.object_list.
    context = {

            'bus_stations': CONTENT[(page_number - 1) * 10:(page_number - 1) * 10 + 9],
            'page': page,
    }

    return render(request, 'stations/.html', context)
