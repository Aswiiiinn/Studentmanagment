from django.db import models
from studentapp.models import Teacher


class announcment(models.Model):
    Headings = models.CharField(max_length =25,null=False, blank=False)
    announcement_details = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateField()
    def __str__(self):
        return self.Headings
class notifications(models.Model):
    teacher_name = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length = 255)
    notification_details = models.TextField(max_length=255)
    document = models.FileField(upload_to='notification/',null=True, blank=True)
    posted_date = models.DateField()
    expire_date  = models.DateField()
    def __str__(self):
        return self.title
    
