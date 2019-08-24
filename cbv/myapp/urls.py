from django.conf.urls import url
from . import views
app_name='goto'
urlpatterns=[
url(r'^lol/$',views.lol.as_view(),name='lol'),
url(r'^$',views.index.as_view(),name='index'),
url(r'^school',views.school.as_view(),name='school'),
url(r'^(?P<pk>\d+)/$',views.student.as_view(),name='students'),
url(r'^create/$',views.create.as_view(),name='create'),
url(r'^update/(?P<pk>\d+)/$',views.update.as_view(),name='update'),
url(r'^delete/(?P<pk>\d+)/$',views.delete.as_view(),name='delete'),]
