from django.conf.urls import url

from app import views

urlpatterns = [	
	url(r'^$', views.index1, name='index1.html'),
]
