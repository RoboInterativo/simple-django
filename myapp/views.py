from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):

    html="HHH"
    now = datetime.datetime.now()
    return HttpResponse(html)
