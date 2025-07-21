from django.urls import path
from base.views import UploadVideoApi,LatestVideoApi

urlpatterns = [
    path('video-upload/', UploadVideoApi.as_view()),
    path('latest-video/', LatestVideoApi.as_view()),
]