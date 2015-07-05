from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<ques_id>[0-9]+)/',include([
        url(r'^$',views.details,name='details'),
        url(r'^result/$',views.result,name='result'),
        url(r'^vote/$',views.vote,name='vote')]))
]
