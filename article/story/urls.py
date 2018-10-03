from django.conf.urls import url
from story import apis


urlpatterns = [
    url(r'^story/$', apis.StoryAPI.as_view()),
    url(r'^vote/(?P<pk>[0-9]+)', apis.VoteAPI.as_view()),
    ]


    