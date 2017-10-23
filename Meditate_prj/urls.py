"""Meditate_prj URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
#from .settings import MEDIA_ROOT
from timer import views as timer_views
from hello import views as hello_views
from accounts import views as accounts_views
from useruploads import views as useruploads_views
from diary import views as diary_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^guide/$', hello_views.get_guide, name='guide'),
    url(r'^timer/$', timer_views.get_timer, name='timer'),
    url(r'^mytimer/$', useruploads_views.get_mytimer, name='mytimer'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^myimages/$', useruploads_views.ImageCreate, name='myimages'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^diaryentries/$', diary_views.entry_list, name='diaryentries'),
    url(r'^diaryentries/(?P<id>\d+)/$', diary_views.entry_detail, name='entrydetail'),
    url(r'^diary/new/$', diary_views.new_entry, name='new_entry'),
   # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns