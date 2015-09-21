from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',

    url(r'^$', 'app.views.get'),
    url(r'^register/$', views.Register.as_view(), name='register'), 
    url(r'^login', views.Login.as_view(), name = 'login'), 
    url(r'^get_last_login', views.GetLastLogin.as_view(), name = 'get_last_login'),
    url(r'^admin/', include(admin.site.urls)),
)
