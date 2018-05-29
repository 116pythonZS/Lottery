"""MarkSix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

app_name = "ssq"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cj/$', views.collector, name='collector'),
    url(r'^tj/$', views.tjdefault),
    url(r'^tj/(?P<serialno>[0-9]{7})/$', views.tj),
]

# urlpatterns = [
#     url(r'^articles/2003/$', views.special_case_2003),
#     url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
#     url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
#     url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
# ]
