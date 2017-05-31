from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^mainpage/$', views.index, name='index'),
url(r'^search/$',views.search ,name='search'),
url(r'^gsandss/$',views.gsandss,name='gsandss'),
url(r'^ssandscopus/$',views.ssandscopus,name='ssandscopus'),
url(r'^gsandscopus/$',views.gsandscopus,name='gsandscopus'),
url(r'^all/$',views.all,name='all'),
]

