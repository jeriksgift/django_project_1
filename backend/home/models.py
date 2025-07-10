from django.db import models

# Create your models here.
class Members(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone = models.BigIntegerField(null=True)
    dob = models.DateField(null=True)
    occupation = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name}"