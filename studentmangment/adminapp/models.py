from django.db import models


class announcment(models.Model):
    Headings = models.CharField(max_length =25,null=False, blank=False)
    announcement_details = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateField()
    def __str__(self):
        return self.Headings
