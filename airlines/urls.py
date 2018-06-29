from django.urls import path, re_path
from django.conf.urls.static import static

from airlines.views import index, arrival_count
from airlines.views import AirportList, AirlinerList

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^api/v1/airports/$', AirportList.as_view(), name='airports'),
    re_path(r'^api/v1/airliners/$', AirlinerList.as_view(), name='airliners'),
    re_path(r'^api/v1/arrival_count', arrival_count, name='arrival_count'),
]
