from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^keyboard/', 'pytoon.views.keyboard'),
    url(r'^message' , 'pytoon.views.answer'),
]
