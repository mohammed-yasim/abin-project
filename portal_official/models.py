from django.db import models
# Create your models here.
class official_user(models.Model):
    email = models.EmailField(primary_key=True)
    passwd = models.CharField(max_length=64)
    designation = models.CharField(max_length=32)
    contact_no = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=32)
    localbody_name = models.CharField(max_length=40)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.email+" - "+self.localbody_name
    
class official_athorities_list(models.Model):
    localbody_state = models.CharField(max_length=32)
    localbody_district = models.CharField(max_length=32)
    localbody_type = models.CharField(max_length=32)
    localbody_name = models.CharField(max_length=40)
    localbody_admin = models.ForeignKey(official_user,on_delete=models.CASCADE)
    def __str__(self):
        return self.localbody_name


