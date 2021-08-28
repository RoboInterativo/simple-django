from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template


# Create your views here.
def index (request):


    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(context={}, request=None)
    return HttpResponse(html)

# def index (request):
#     p = Vitrina.objects.all()
#     #a = p.values()
#
#     t = get_template('front/build/index.html')
#     html = t.render(context={'bd':bd,'items':p,'date_now':str(datetime.datetime.now() )}, request=None)
#     return HttpResponse(html)
