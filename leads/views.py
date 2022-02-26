from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    #return HttpResponse("Hello, CRM")
    return render(request, "second_page.html")