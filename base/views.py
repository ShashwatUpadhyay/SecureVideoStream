from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializer import VideoSerializer
# Create your views here.

class UploadVideoApi(APIView):
    def post(self, request):
        data = request.data
        serializer = VideoSerializer(data = data)
        if serializer.is_valid():
            serializer.create(data)
            return Response({
            "status" : True,
            "message" : "Video Uploaded sucessfully!",
            "data" : serializer.validated_data.get('title')
        })
        else:
            return Response({
            "status" : False,
            "message" : "something went wrong",
            "data" : {}
        })
            
        
        
class LatestVideoApi(APIView):
    def get(self, reqeust):
        video = Video.objects.latest()
        video = VideoSerializer(video)
        return Response({
            "status" : True,
            "message" : "Video Fetched!",
            "data" : video.data
        })