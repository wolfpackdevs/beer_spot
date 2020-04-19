from functools import wraps
from django.shortcuts import redirect

from finder.models import Viewer


def brewers_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if Viewer.objects.filter(user=request.user).exists():
            return redirect('dashbord')
        else:
            return function(request, *args, **kwargs)

    return wrap