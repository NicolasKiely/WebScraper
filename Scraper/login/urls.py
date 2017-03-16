from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.user_account, name='account'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout')
]
