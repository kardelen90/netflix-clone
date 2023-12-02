from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=11)

    def profil_counter(self):
        return self.profile_set.all().count()


class Profile(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile_pic')
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
