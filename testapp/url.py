from django.conf.urls import patterns, include, url

urlpatterns = patterns('', url('testapp/', 'testapp.views.test', name = 'hello'),)