from django.conf.urls import patterns, url
from social import views

<<<<<<< HEAD
=======
# no changes need for this file

>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
urlpatterns = patterns('',
	# main page
	url(r'^$', views.index),
	# signup page
	url(r'^signup/$', views.signup),
	# register new user
	url(r'^register/$', views.register),
	# login page
	url(r'^login/$', views.login),
	# logout page
	url(r'^logout/$', views.logout),
	# members page
	url(r'^members/$', views.members),
	# friends page
	url(r'^friends/$', views.friends),
	# user profile edit page
	url(r'^profile/$', views.profile),
	# Ajax: check if user exists
	url(r'^checkuser/$', views.checkuser),
	# messages page
	url(r'^messages/$', views.messages),
<<<<<<< HEAD
	# api page
	url(r'^api/$', views.api),
=======
>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
)
