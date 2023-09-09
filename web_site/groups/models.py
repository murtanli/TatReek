from django.db import models
from django.contrib.auth.models import User

class lobbys(models.Model):
    lobby_name = models.CharField(max_length=30)
    ueser1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lobby_user1')
    ueser2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lobby_user2', null=True)
    status = models.BooleanField(default=0)


class search_lobby(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

