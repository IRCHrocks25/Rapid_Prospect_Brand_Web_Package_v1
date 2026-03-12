from django.shortcuts import render
from myApp.data import PACKAGE_SERVICES

def home(request):
    return render(request, 'cheat_sheet.html', {'package_services': PACKAGE_SERVICES})

def sales_pitch(request):
    return render(request, 'sales_pitch.html', {'package_services': PACKAGE_SERVICES})
