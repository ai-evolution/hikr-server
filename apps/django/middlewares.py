from django.contrib.auth.models import User
from django.contrib import auth

from django.utils.deprecation import MiddlewareMixin
from threading import local


_thread_locals = local()


def get_current_request():

    """
    returns the request object for this thread
    """

    return getattr(_thread_locals, "request", None)


def get_current_user():

    return getattr(get_current_request(), "user", None)


class ThreadLocalMiddleware(MiddlewareMixin):

    """
    Simple middleware that adds the request object in thread local storage.
    """

    def process_request(self, request):
        _thread_locals.request = request

    def process_response(self, request, response):
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request
        return response