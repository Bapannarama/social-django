from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from social.models import Member, Profile, Message

appname = 'Facemagazine'

<<<<<<< HEAD
# this function deals with the redirect to the index page if a
=======

>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
def index_redirect(request):
	appname = 'Facemagazine'
	index_redirect = loader.get_template('social/index.html')
	index_context = RequestContext(request, {
		'appname': appname,
		'loggedin': False,
		})

	return HttpResponse(index_redirect.render(index_context))


def index(request):
	template = loader.get_template('social/index.html')
	context = RequestContext(request, {
			'appname': appname,
		})
	return HttpResponse(template.render(context))


def messages(request):
	if 'username' in request.session:
		username = request.session['username']
		messages_table = Message.objects.all() # declaring messages table in views
		template = loader.get_template('social/messages.html')
		context = RequestContext(request, {
				'appname': appname,
				'username': username,
				'loggedin': True,
<<<<<<< HEAD
				'messages_database': messages_table, # namespace clash took 3 hours to solve :(
			})

		if 'text' in request.POST:
			# this code block tries to get the recipient of the message from the URL
			referer = request.META['HTTP_REFERER'].split("?")
			recip = username
			try:
				recip = referer[1]
			except IndexError:
				pass

			message = request.POST['text']
			user = username
			auth = username
			pm = request.POST['pm']
			text = Message(user=user, auth=auth, recip=recip, pm=pm, message=message)
			text.save()

		# HttpResponse contains the data which is passed to the template manager
=======
				'messages': messages_table,
			})

		if 'text' in request.POST:
			message = request.POST['text']
			user = username
			auth = username
			recip = username # needs to be corrected
			pm = request.POST['pm']

			member = Message(user=user, auth=auth, recip=recip, pm=pm, message=message)
			member.save()

>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
		return HttpResponse(template.render(context))
	else:
		return index_redirect(request)


def signup(request):
	template = loader.get_template('social/signup.html')
	context = RequestContext(request, {
			'appname': appname,
		})
	return HttpResponse(template.render(context))


def register(request):
	u = request.POST['user']
	p = request.POST['pass']
	user = Member(username=u, password=p)
	user.save()
	template = loader.get_template('social/user-registered.html')
	context = RequestContext(request, {
		'appname': appname,
		'username' : u
		})
	return HttpResponse(template.render(context))


def login(request):
	if 'username' not in request.POST:
		template = loader.get_template('social/login.html')
		context = RequestContext(request, {
				'appname': appname,
			})
		return HttpResponse(template.render(context))
	else:
		u = request.POST['username']
		p = request.POST['password']
		try:
			member = Member.objects.get(pk=u)
		except Member.DoesNotExist:
			raise Http404("User does not exist")
		if member.password == p:
			request.session['username'] = u;
			request.session['password'] = p;
			return render(request, 'social/login.html', {
				'appname': appname,
				'username': u,
				'loggedin': True}
				)
		else:
			raise Http404("Incorrect password")


def logout(request):
	if 'username' in request.session:
		u = request.session['username']
		request.session.flush()
		template = loader.get_template('social/logout.html')
		context = RequestContext(request, {
				'appname': appname,
				'username': u
			})
		return HttpResponse(template.render(context))
	else:
		raise Http404("Can't logout, you are not logged in")


def member(request, view_user):
	if 'username' in request.session:
		username = request.session['username']
		member = Member.objects.get(pk=view_user)

		if view_user == username:
			greeting = "Your"
		else:
			greeting = view_user + "'s"

		if member.profile:
			text = member.profile.text
		else:
			text = ""
		return render(request, 'social/member.html', {
			'appname': appname,
			'username': username,
			'greeting': greeting,
			'profile': text,
<<<<<<< HEAD
			'loggedin': True,
			'member': member.username} # member field sent in order to be able to include username in URL
=======
			'loggedin': True}
>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
			)
	else:
		return index_redirect(request)


def friends(request):
	if 'username' in request.session:
		username = request.session['username']
		member_obj = Member.objects.get(pk=username)
		# list of people I'm following
		following = member_obj.following.all()
		# list of people that are following me
		followers = Member.objects.filter(following__username=username)
		# render reponse
		return render(request, 'social/friends.html', {
			'appname': appname,
			'username': username,
			'members': members,
			'following': following,
			'followers': followers,
			'loggedin': True}
			)
	else:
		return index_redirect(request)


def members(request):
	if 'username' in request.session:
		username = request.session['username']
		member_obj = Member.objects.get(pk=username)
		# follow new friend
		if 'add' in request.GET:
			friend = request.GET['add']
			friend_obj = Member.objects.get(pk=friend)
			member_obj.following.add(friend_obj)
			member_obj.save()
		# unfollow a friend
		if 'remove' in request.GET:
			friend = request.GET['remove']
			friend_obj = Member.objects.get(pk=friend)
			member_obj.following.remove(friend_obj)
			member_obj.save()
		# view user profile
		if 'view' in request.GET:
			return member(request, request.GET['view'])
		else:
			# list of all other members
			members = Member.objects.exclude(pk=username)
			# list of people I'm following
			following = member_obj.following.all()
			# list of people that are following me
			followers = Member.objects.filter(following__username=username)
			# render reponse
			return render(request, 'social/members.html', {
				'appname': appname,
				'username': username,
				'members': members,
				'following': following,
				'followers': followers,
				'loggedin': True}
				)
	else:
		return index_redirect(request)


def profile(request):
	if 'username' in request.session:
		u = request.session['username']
		member = Member.objects.get(pk=u)
		if 'text' in request.POST:
			text = request.POST['text']
			if member.profile:
				member.profile.text = text
				member.profile.save()
			else:
				profile = Profile(text=text)
				profile.save()
				member.profile = profile
			member.save()
		else:
			if member.profile:
				text = member.profile.text
			else:
				text = ""
		return render(request, 'social/profile.html', {
			'appname': appname,
			'username': u,
			'text' : text,
			'loggedin': True}
			)
	else:
		return index_redirect(request)


def checkuser(request):
	if 'user' in request.POST:
		u = request.POST['user']
		try:
			member = Member.objects.get(pk=u)
		except Member.DoesNotExist:
			member = None
		if member is not None:
			return HttpResponse("<span class='taken'>&nbsp;&#x2718; This username is taken</span>")
		else:
<<<<<<< HEAD
			return HttpResponse("<span class='available'>&nbsp;&#x2714; This username is available</span>")


def api(request):
	messages_table = Message.objects.all()
	template = loader.get_template('social/api.html')
	context = RequestContext(request, {'messages_database': messages_table,})
	return HttpResponse(template.render(context))
=======
			return HttpResponse("<span class='available'>&nbsp;&#x2714; This username is available</span>")
>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
