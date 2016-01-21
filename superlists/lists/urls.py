from django.conf.urls import url
from lists import views

 
urlpatterns = [    
    url(r'(?P<listID>[0-9]+)/addItem/', views.addItem, name='addItem'),    
    url(r'^(?P<listID>[0-9]+)/$', views.viewList, name='viewList'),
    url(r'^new/$', views.newList, name='newList'),
    url(r'^$', views.homePage, name='homePage'),
    
]