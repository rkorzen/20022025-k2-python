import logging
from django.utils import timezone
import time
"""

Nowy request:
datetime: 2025-03-20 12:00:00
Path: /
Method: GET
User: Anonymous
IP: 127.0.0.1

Request zakończony:
Path: /
Status code: 200
Czas wykonania: 0.001 sekund

"""

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start_time = time.time()
        logger.info(f"""Nowy request:
                    datetime: {timezone.now()}
                    Path: {request.path}
                    Method: {request.method}
                    User: {request.user if request.user.is_authenticated else 'Anonymous'}
                    IP: {request.META.get('REMOTE_ADDR')}
        """)

        response = self.get_response(request)
        response["XXXXXX"] = "yyyyyy"
        logger.info(f"""Request zakończony:
                    Path: {request.path}
                    Status code: {response.status_code}
                    Czas wykonania: {time.time() - start_time:.2f} sekund
        """)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    

def process_time(get_response):
# One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start_time = time.time()
        
        response = get_response(request)
        
        response["X-Process-Time"] = time.time() - start_time

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware