from django.db import models
import uuid
# Create your models here.
class Video(models.Model):
    uid = models.CharField(max_length=100, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    video = models.FileField(upload_to='video')
    playlist = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        get_latest_by = 'created_at'