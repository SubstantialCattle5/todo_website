from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from core.models import Post


def index(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            task = request.POST['task']
            print(task)

    return render(request, 'index.html')
