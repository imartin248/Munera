from django.contrib import admin
from . import models

# Register your models here
admin.site.register(models.Gift)
admin.site.register(models.UserGroup)
admin.site.register(models.GroupMember)
admin.site.register(models.GroupMemberRequest)
admin.site.register(models.ShoppingList)
