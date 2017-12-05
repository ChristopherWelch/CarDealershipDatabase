from django.conf.urls import url
from . import views

urlpatterns = [
    #/home/#
    url(r'^$', views.index, name='index'),

    #/home/71/
    #[A-Za-z0-9]{1)
    url(r'^(?P<brand_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<car_id>[A-Za-z0-9]{17})/$', views.carDetail, name='carDetail'),
]