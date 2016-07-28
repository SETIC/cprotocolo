from django.conf.urls import url
from django.contrib import admin
from cprotocolo.core.views import new_search, search

urlpatterns = [
    url(r'^$', new_search, name='new_search'),
    url(r'^search/', search, name='search'),
    url(r'^admin/', admin.site.urls),
]
