from django.contrib import admin
from .models import UserOfGroup, GroupOfUser, GroupAndUser

admin.site.register(UserOfGroup)
admin.site.register(GroupAndUser)
admin.site.register(GroupOfUser)