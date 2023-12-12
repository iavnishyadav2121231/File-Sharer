from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_file_data(models.Model):
    user_ref = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to="files")

   
class share_file_data(models.Model):
    share_ref = models.ForeignKey(User,on_delete=models.CASCADE)
    file_Ref = models.ForeignKey(user_file_data,on_delete=models.CASCADE)