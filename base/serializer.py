from rest_framework import serializers
from .models import Video
from utils.utility import convert_to_hls
from lms.settings import BASE_DIR

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    
    def create(self, data):
        title = data.get('title') if data.get('title') else ''
        video = data.get('video') 
        video = Video.objects.create(title = title, video=video)
        video.playlist = convert_to_hls(video)
        video.save()