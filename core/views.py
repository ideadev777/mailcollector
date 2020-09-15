from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

from .models import Person

# Create your views here.

######################################################################################
@csrf_exempt
def AjaxTest(request):
    val = request.POST.get('val',None)
    val = val+val 
    print(val)
    data = {
        'ajaxdata':val
    }
    return JsonResponse(data)
######################################################################################
def index(request):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    step = 0
    for i in range(5,5):
        fileName = ("codeforce%s.txt" % i) 
        text_file = open(fileName, "w")
        url = 'https://codeforces.com/ratings'
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        for tag in tags:
            val = str(tag.get('href', None))
            if val.find("profile") == -1:
                continue
            print(val)
#            user = Person(userid=val[9:],nation='Brazil')
#            user.save()
    template = loader.get_template('index.html')
    bgimglist = [ 
        ['img/slide-1.jpg','active'],
        ['img/slide-2.jpg','']
    ]
    context = {
        'nav':'Home',
        'bgimglist':bgimglist,
    }
    return HttpResponse(template.render(context, request))

class Search(generic.View):
    template = loader.get_template('search.html')
    def get(self, *args, **kwargs):
        bgimglist = [ 
            ['img/slide-4.jpg','active'],
        ]
        context = {
            'nav':'Scrape',
            'bgimglist':bgimglist,
            'isSearch':True,
        }
        return HttpResponse(self.template.render(context, self.request))

class Result(generic.View):
    template = loader.get_template('result.html')
    def get(self, *args, **kwargs):
        context = {
            'nav':'Result',
        }
        return HttpResponse(self.template.render(context, self.request))
