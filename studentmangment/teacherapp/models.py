from django.db import models

class CourseMeterial(models.Model):
    coursemeterial_name = models.CharField(max_length=45,null=True,default=None,blank=True)
    meterial = models.FileField(upload_to="meterial/",max_length=250,null = True,default=None,blank=True)
    def __str__(self):
        return self.coursemeterial_name
