from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
def test(request):
    return HttpResponse("This is Req")


def contact(request):
    return HttpResponse("Contact page")