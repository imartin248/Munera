from django.db import models
from django.conf import settings

# Create your models here.
class Gift(models.Model):
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )

        selected = models.BooleanField(default=False)

        name = models.CharField(max_length=30)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        link = models.CharField(max_length=2083)

        def __str__(self):
                return self.name

class ShoppingList(models.Model):
        gift = models.ForeignKey(Gift,
                on_delete=models.CASCADE
        )
        buyer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )



class UserGroup(models.Model):
    admin = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )

    group_name = models.CharField(max_length=30)

    def __str__(self):
        		return self.group_name

class GroupMember(models.Model):
    member = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    class Meta:
            unique_together = ('member', 'group')

class GroupMemberRequest(models.Model):
    to_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='to_group')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_group')
    timestamp = models.DateTimeField(auto_now_add=True) 

    class Meta:
            unique_together = ('to_group', 'from_user')

    def __str__(self):
	    return "From {}, to {}".format(self.from_user.username, self.to_group.group_name)

    
