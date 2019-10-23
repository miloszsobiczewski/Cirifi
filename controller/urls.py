from django.conf.urls import url

from . import views

app_name = "controller"

urlpatterns = [
    url(r'^$', views.play, name='play'),
]
