from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.HomeView),
    url(r'^add-tag/$', views.AddTagName),
    url(r'^add-channel/$', views.AddChannel),
    url(r'^join-channel/(?P<id>\d+)/$', views.JoinChannel),
    url(r'^joined-channel/$', views.JoinedChannels),
    url(r'^all-channel/$', views.AllChannels),
    url(r'^message-panel/(?P<id>\d+)/$', views.MessagePanel),
    url(r'^post-message/(?P<id>\d+)/$', views.PostMessage)
]