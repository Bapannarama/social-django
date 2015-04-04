from django.contrib import admin

# Register your models here.

from social.models import Profile, Member, Message

admin.site.register(Profile)
admin.site.register(Member)
<<<<<<< HEAD
admin.site.register(Message) # this line was added in order to register the messaging module
=======
admin.site.register(Message)
>>>>>>> 52506c1fd0f346afe15e81538ee2893deee90683
