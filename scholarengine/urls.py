
from django.conf.urls import url,include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('mainpage.urls')),
    url('',include('social.apps.django_app.urls',namespace='social')),
    url('',include('django.contrib.auth.urls',namespace='auth')),


]
