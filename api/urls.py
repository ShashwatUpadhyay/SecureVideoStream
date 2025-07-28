from django.urls import path
from base.views import UploadVideoApi,LatestVideoApi,stream_video,generate_token_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('video-upload/', UploadVideoApi.as_view()),
    path('latest-video/', LatestVideoApi.as_view()),
    path('generate-token/<str:uid>/', generate_token_view),
    path('stream-video/<str:token>/<str:filename>', stream_video,name='stream-video'),
]