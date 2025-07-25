from django.urls import path
from base.views import UploadVideoApi,LatestVideoApi,stream_video,generate_token_view

urlpatterns = [
    path('video-upload/', UploadVideoApi.as_view()),
    path('latest-video/', LatestVideoApi.as_view()),
    path('generate-token/<str:uid>/', generate_token_view),
    path('stream-video/<str:token>/<str:filename>', stream_video,name='stream-video'),
]