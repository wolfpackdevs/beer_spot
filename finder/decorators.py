from functools import wraps
from django.shortcuts import redirect

from accounts.models import Brewer


def viewers_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if Brewer.objects.filter(user=request.user).exists():
            return redirect('brewer')
        else:
            return function(request, *args, **kwargs)

    return wrap
