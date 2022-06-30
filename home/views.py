from django.shortcuts import render
from django.views.generic import ListView, View
# from services.models import Services,DataCertificate,BillingData



def HomeListView(request):
    return render(request, 'principal/index.html')
