from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Applicant(models.Model):
    TYPE_PERMISSIONS =(
            (1, ("disapproval")),
            (2, ("approval"))
            )

    name = models.CharField(max_length=100, default="")
    student_number = models.IntegerField(default="")
    email = models.EmailField(max_length=254,default="")
    phone_number = models.CharField(max_length=16,default="")
    usage = models.CharField(max_length=100,default="")
    username = models.CharField(max_length=100,default="")
    agreement = models.BooleanField(default=False)
    permission = models.IntegerField(choices=TYPE_PERMISSIONS, default=1)
    pwd = models.CharField(max_length=100,default="")
    apply_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def generate(self):
        return self.save()
    
