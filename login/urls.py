from django.conf.urls import *

urlpatterns = patterns('login',
    url(r'^$','views.index'),
)
