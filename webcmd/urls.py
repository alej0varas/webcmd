from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from webcmd import views

urlpatterns = [
    url(r'^webcmd/$', views.webcmd),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),
    # url(r'^admin/', admin.site.urls),
]
