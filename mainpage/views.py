from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .phantom import main
from django.shortcuts import render_to_response
from django.template import RequestContext

# query,page=1
def search(request):
    if request.GET.get('search'):
        page=request.GET.get('page')
        #print(request.GET)

        if page==None:
            page = 1
            acadict = main(request.GET.get('search'), 1, gs1=request.GET.get('gs'),
                       ma1=request.GET.get('ma'), scopus1=request.GET.get('scopus'),
                       ss1=request.GET.get('ss'))
        else:
            acadict = main(request.GET.get('search'), int(page), gs1=request.GET.get('gs'),
                       ma1=request.GET.get('ma'), scopus1=request.GET.get('scopus'),
                       ss1=request.GET.get('ss'))
            page=int(page)

        #print(acadict['gs'][0].title)
        context={'request':request,'user':request.user,
            'query': request.GET.get('search'),'scopus':acadict['scopus'],
                 'gs':acadict['gs'],'semantic':acadict['semantic'],'ma':acadict['ma'],
            'range':range(page,page+6,1)}
         
            #          'ss':all[1],'scopus':all[2],
            #          }
        return render(request,"mainpage/details.html",context)
    else:
        context = RequestContext(request,
                                 {'request': request,
                                  'user': request.user})
        return render_to_response("mainpage/home.html",
                                  context_instance=context)
def home(request):
   context = RequestContext(request,

                            {'request':request,
                             'page': '1',
                           'user': request.user})
   # a=request.user
   # print(a.get_full_name)
   #print('**************************')
   return render_to_response("mainpage/home.html",
                             context_instance=context)