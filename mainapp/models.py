from django.db import models

# Create your models here.



class GroupOfUser(models.Model):
    Name = models.CharField(max_length=50, primary_key=True)
    Description = models.CharField(max_length=200)
    users = models.ManyToManyField("UserOfGroup", through="GroupAndUser")

    def __str__(self):
        return self.Name
    


class UserOfGroup(models.Model):
    username = models.EmailField(max_length=254, unique=True)
    created = models.DateField(auto_now_add=True)
    user_category = models.ManyToManyField(GroupOfUser, through="GroupAndUser")
    
    def __str__(self):
        return self.username

class GroupAndUser(models.Model):
    user  = models.ForeignKey(UserOfGroup, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupOfUser, on_delete=models.PROTECT)


    def __str__(self):
        return f"User: {self.user} with group: {self.group}"
    