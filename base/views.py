from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from .serializer import VideoSerializer
from django.http import FileResponse, HttpResponseForbidden,JsonResponse
from utils.signed_url import verify_signed_token,generate_signed_token
import os
from lms import settings
# Create your views here.


@api_view(['GET'])
def generate_token_view(request, uid):
    token = generate_signed_token(uid)
    return Response({"token": token})

class UploadVideoApi(APIView):
    def post(self, request):
        data = request.data
        serializer = VideoSerializer(data = data)
        if serializer.is_valid():
            serializer.create(data)
            return Response({
            "status" : True,
            "message" : "Video Uploaded successfully!",
            "data" : serializer.validated_data.get('title')
        })
        else:
            return Response({
            "status" : False,
            "message" : "something went wrong",
            "data" : {}
        })
            
        
        
class LatestVideoApi(APIView):
    def get(self, request):
        video = Video.objects.latest()
        video = VideoSerializer(video)
        return Response({
            "status" : True,
            "message" : "Video Fetched!",
            "data" : video.data
        })
    
from django.conf import settings
from django.utils.encoding import smart_str

@api_view(['GET'])
def stream_video(request, filename, token):
    # Verify token and get video UID
    video_uid = verify_signed_token(token)
    if not video_uid:
        return HttpResponseForbidden("Invalid or expired token")

    # Expected path
    path = os.path.join(settings.MEDIA_ROOT, 'hls_video', video_uid, filename)

    if not os.path.exists(path):
        return HttpResponseForbidden("File not found")

    return FileResponse(open(path, 'rb'), content_type='application/octet-stream')
