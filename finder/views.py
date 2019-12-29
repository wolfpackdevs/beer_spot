from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Brewer, Viewer



# Create your views here.


@login_required()
def dashbord(request):

    print(Viewer.objects.get(user=request.user))
    return render(request, 'finder/dashbord.html')


@login_required()
def brewer_dashbord(request):
    # brewer = Brewer.objects.get(id=request.user.id)

    return render(request, 'finder/brewer.html')

