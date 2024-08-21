from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=12,blank=True)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=125,blank=True)
#to show in admiin name of username in admin page
    def __str__(self):
        return f'{self.user.username}\'s Profile'


    """ class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames' """ 