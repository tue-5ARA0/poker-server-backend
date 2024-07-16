from django.db import models

class Announcement(models.Model):
    title      = models.TextField()
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    is_hidden  = models.BooleanField()
