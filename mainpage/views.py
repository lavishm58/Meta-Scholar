from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from django.shortcuts import render
from .scholar import main
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    context={}
    return render(request,"mainpage/index.html",context)


def querypage(request,query):
    context={}
    html="<h2>this is querypage for"+str(query)+"</h2>"
    return HttpResponse(html)

def search(request):
    if request.GET['entry'] is not "":
        all=main(request.GET["entry"])

        context={"query": request.GET['entry'],'gs':all[0],
                 'ss':all[1],'scopus':all[2],
                 }
        return render(request,"mainpage/details.html",context)
    else:
        message='no value typed'
        return HttpResponse(message)

def gsandss(request):
    html='<h2>sjdbch</h2>'
    return HttpResponse(html)

def gsandscopus(request):
    html='<h2>sjdbch</h2>'
    return HttpResponse(html)

def ssandscopus(request):
    html='<h2>sjdbch</h2>'
    return HttpResponse(html)

def all(request):
    html='<h2>sjdbch</h2>'
    return HttpResponse(html)

def home(request):
   context = RequestContext(request,
                            {'request':request,
                           'user': request.user})
   return render_to_response("mainpage/home.html",
                             context_instance=context)