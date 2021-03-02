from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Specialization(models.Model):

    name = models.CharField('Имя специлизаций', max_length=255)

    def __str__(self):

        return self.name


class Profile(models.Model):

    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE,related_name="profile")
    photo = models.ImageField('Фото профиля',upload_to="ProfileImg/",blank=True,null=True)
    specialization = models.ForeignKey(Specialization,blank=True,null=True,on_delete=models.CASCADE,default=None)
