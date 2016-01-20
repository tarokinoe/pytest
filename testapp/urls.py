# -*- encoding: utf-8 -*-


from django.conf.urls import patterns, url

from testapp.views import ThanksPage, AboutPage, IndexPage

urlpatterns = patterns(
        '',
        url(r'^thanks$', ThanksPage.as_view(), name='thanks'),
        url(r'^about$', AboutPage.as_view(), name='about'),
        url(r'^$', IndexPage.as_view(), name="home"),

)
