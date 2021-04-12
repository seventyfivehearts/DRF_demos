import json

from django.utils.deprecation import MiddlewareMixin


class JsonMiddle(MiddlewareMixin):
    def process_request(self, request):
        try:
            request.data = json.loads(request.body)
        except Exception as e:
            request.data = request.POST
