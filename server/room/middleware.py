from django.http import HttpRequest
import json

class ParseJSON:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        data = None
        if request.POST:
            data = json.loads(request.body.decode('utf-8'))

        response = self.get_response(request)

        return response

    # def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
    #     data = json.loads(request.body.decode('utf-8'))

    #     view_func()
