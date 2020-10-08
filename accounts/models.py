from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #The relationship must be OneToOne (one user have only one profile)
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.user)
