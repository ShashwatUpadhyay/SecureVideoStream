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
from django.conf import settings
from django.utils.encoding import smart_str
from lms.settings import CSRF_TRUSTED_ORIGINS
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]
    def get(self, request):
        video = Video.objects.latest()
        video = VideoSerializer(video)
        print(request.user)
        return Response({
            "status" : True,
            "message" : "Video Fetched!",
            "data" : video.data
        })
    

@api_view(['GET'])
def stream_video(request, filename, token):
    # Verify token and get video UID
    if not request.META.get('HTTP_REFERER') in CSRF_TRUSTED_ORIGINS:
            print('Thrown out')
            return HttpResponseForbidden('Request Forbidden')
        
    video_uid = verify_signed_token(token)
    
    print("Accessed Video UID: ", video_uid)
    
    if not video_uid:
        return HttpResponseForbidden("Invalid or expired token")

    # Expected path
    path = os.path.join(settings.MEDIA_ROOT, 'hls_videos', video_uid, filename)
    
    print(not os.path.exists(path))
    
    if not os.path.exists(path):
        return HttpResponseForbidden("File not found")

    return FileResponse(open(path, 'rb'), content_type='application/octet-stream')
