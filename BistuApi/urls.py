from django.conf.urls import patterns, include, url
urlpatterns = patterns('BistuApi.views',
    url(r'^bistuapi/me/$','student_me')
    )