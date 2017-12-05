from django.conf.urls import url
from . import views

urlpatterns = [
    #/home/#
    url(r'^$', views.index, name='index'),

    #/home/71/
    url(r'^(?P<car_id>[A-Za-z0-9]{17})/$', views.detail, name='detail'),
]