from django.db import models

# Create your models here.
class Global_variable(models.Model):
    var_data = models.CharField(max_length=50)
    var_name = models.CharField(max_length=50,choices=(
        ('district','District'),
        ('state','State'),
        ('localbody_type','Localbody Type'),
        ) )
    var_key = models.CharField(max_length=50,default="*")
    def __str__(self):
        return ("%s - (%s, %s)")%(self.var_name.capitalize(),self.var_data.capitalize(),self.var_key.capitalize())
    