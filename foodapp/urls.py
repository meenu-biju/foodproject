from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^starter$', views.starter),
    url(r'^menu$', views.menu),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^drinks$', views.drinks),
    url(r'^meals$', views.meals),
    url(r'^combo$', views.combo),
    url(r'^snack$', views.snack),
    url(r'^cartsave$', views.cartsave),
    url(r'^yourcartnew$',views.yourcartnew),
    url(r'^yourcart$', views.yourcart),
    url(r'^update1$', views.update1),
    url(r'^order$', views.order),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^edit$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),


]
