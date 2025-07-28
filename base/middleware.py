from lms.settings import CSRF_TRUSTED_ORIGINS
from django.http import HttpResponseForbidden

class VideoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.META.get('HTTP_REFERER') in CSRF_TRUSTED_ORIGINS:
            print('Thrown out')
            return HttpResponseForbidden('You not allowed')
        response = self.get_response(request)
        return response
