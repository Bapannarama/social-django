from django.db import models

class Profile(models.Model):
	text = models.CharField(max_length=4096)

	def __str__(self):
		if self.member:
			return self.member.username + ": " + self.text
		return self.text

class Member(models.Model):
	username = models.CharField(max_length=16,primary_key=True)
	password = models.CharField(max_length=16)
	profile = models.OneToOneField(Profile, null=True)
	following = models.ManyToManyField("self", symmetrical=False)

	def __str__(self):
		return self.username

<<<<<<< HEAD
#
=======

>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
class Message(models.Model):
	# class attributes have been mirrored from original PHP code with slight
	# modification to types

<<<<<<< HEAD
=======
	# django automatically adds a primary key under attribute name 'id'
>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
	id = models.IntegerField(primary_key=True)
	user = models.CharField(max_length=16)
	auth = models.CharField(max_length=16)
	recip = models.CharField(max_length=16)
	pm = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now=True)
	message = models.CharField(max_length=4096)

	def __str__(self):
		return "\'{}\', posted at {}, private={}".format(self.message, str(self.time), str(self.pm))