from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
    def fancy_name(self):
        return self.name+"!!!"

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + "_" + self.role.name